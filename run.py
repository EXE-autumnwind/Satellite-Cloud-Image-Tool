import os
import sys
import signal
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

SAVE_MODE = 1 #1.程序根目录 2.指定目录
MANUAL_SAVE_PATH = "D:\\气象云图" #自定义保存路径，，上面SAVE_MODE记得改2
MAX_THREADS = 10 #最大线程数
INDEX_URL = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/SEC/xml/FY4B-china-72h.xml"

if SAVE_MODE == 1:
    BASE_SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
elif SAVE_MODE == 2:
    BASE_SAVE_PATH = MANUAL_SAVE_PATH
else:
    print("SAVE_MODE输入错误，自动切换为程序根目录保存")
    BASE_SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

os.makedirs(BASE_SAVE_PATH, exist_ok=True)

is_running = True

def signal_handler(signum, frame):
    global is_running
    print("\n\n收到Ctrl+C信号，正在停止当前下载任务...")
    is_running = False

signal.signal(signal.SIGINT, signal_handler)

def get_images(download_all=False):
    if not is_running:
        return []
        
    try:
        response = requests.get(INDEX_URL, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        today_utc = datetime.now(timezone.utc).date()
        images = []
        
        for img in root.findall('image'):
            if not is_running:
                break
            
            url = img.get('url')
            if '-thumb' in url:
                continue
                
            time_str = img.get('time').replace(' (UTC)', '')
            try:
                img_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
                if download_all or img_time.date() == today_utc:
                    images.append((img_time, url))
            except ValueError:
                continue
        
        images.sort(key=lambda x: x[0])
        return images
        
    except Exception as e:
        if is_running:
            print(f"获取索引信息失败: {e}")
        return []

def download_single_image(img_info):
    if not is_running:
        return (False, "任务已终止")
        
    img_time, url = img_info
    try:
        year_folder = f"{img_time.year}年"
        month_folder = f"{img_time.month}月"
        day_folder = f"{img_time.day}日"
        date_path = os.path.join(BASE_SAVE_PATH, year_folder, month_folder, day_folder)
        os.makedirs(date_path, exist_ok=True)
        
        filename = os.path.join(date_path, f"{img_time.strftime('%H%M')}.JPG")
        
        if os.path.exists(filename):
            return (False, f"已存在跳过: {filename}")
        
        image_url = f"http:{url}"
        response = requests.get(image_url, timeout=15, stream=True)
        response.raise_for_status()
        
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024*1024):
                if not is_running:
                    f.close()
                    os.remove(filename)
                    return (False, "任务已终止，文件已清理")
                if chunk:
                    f.write(chunk)
            
        return (True, f"下载成功: {filename}")
        
    except Exception as e:
        if "任务已终止" not in str(e) and is_running:
            return (False, f"下载失败 {url}: {str(e)}")
        return (False, str(e))

def download_images(images):
    if not images:
        print("没有找到符合条件的图片信息")
        return
        
    print(f"找到 {len(images)} 张图片，启动多线程下载（{MAX_THREADS}线程）...")
    downloaded_count = 0
    skipped_count = 0
    failed_count = 0
    aborted_count = 0
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {}
        for img in images:
            if not is_running:
                break
            future = executor.submit(download_single_image, img)
            futures[future] = img
        
        for future in tqdm(as_completed(futures), total=len(futures), desc="下载进度"):
            if not is_running:
                executor.shutdown(wait=False)
                break
            
            success, msg = future.result()
            if "已存在跳过" in msg:
                skipped_count += 1
            elif success:
                downloaded_count += 1
                print(f"\r{msg}", end="")
            elif "任务已终止" in msg:
                aborted_count += 1
            else:
                failed_count += 1
                print(f"\r{msg}", end="")
    
    print(f"\n\n处理完成 - 新增下载: {downloaded_count} 张, 已存在跳过: {skipped_count} 张, 下载失败: {failed_count} 张")
    if aborted_count > 0:
        print(f"已终止未完成任务: {aborted_count} 个")

if __name__ == "__main__":
    download_all = '-all' in sys.argv
    
    print(f"当前保存模式：{'程序根目录' if SAVE_MODE == 1 else '指定目录'}")
    print(f"图片主目录：{BASE_SAVE_PATH}")
    print(f"下载模式：{'所有图片' if download_all else '仅当天图片'}")
    print(f"多线程配置：最大{MAX_THREADS}线程")
    
    try:
        while is_running:
            print("----- 开始获取图片列表 -----")
            images = get_images(download_all=download_all)
            if is_running and images:
                download_images(images)
            
            if is_running:
                check_interval = 900 #等待时间
                print(f"\n将在 {check_interval/60} 分钟后再次检查更新...")
                print("（按 Ctrl+C 退出）\n")
                for _ in range(check_interval):
                    if not is_running:
                        break
                    time.sleep(1)
    except Exception as e:
        if not is_running:
            print("\n程序退出")
        else:
            print(f"\n程序异常退出: {e}")
    finally:
        print("Bye")
