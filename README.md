# SCIT (Satellite Cloud Image Tool)
- 用于从国家卫星气象中心采集卫星云图，并包含有将采集照片集合为视频的功能
- 默认15分钟尝试拉取一次，默认采集FY-4B中国区域
- 拥有按时间分类的目录(yyyy年\mm月\dd日)

# 快速上手
>## 注意
>在使用之前一定要将两个py文件里的输出路径更改
## 图像采集模块(run.py)
### 一、通过bat脚本控制
>如果你没有任何基础，可通过“依赖安装.bat”自动安装环境，记得自行配置文件储存地址，默认为/Pull
#### 1.运行
 双击后前台运行
#### 2.静默启动
 双击运行后自动缩小到任务栏
#### 3.下载全部
 下载当前XML链接里除了缩略图以外的全部图像
### 二、通过命令行运行
>所有命令都需要在根目录下运行
#### 1.运行
```
python run.py
```
#### 2.下载全部
```
python run.py -all
```
### 三、配置文件(脚本11到14行)
```
SAVE_MODE = 1   #1.程序根目录 2.指定目录 
MANUAL_SAVE\_PATH = "D:\\气象云图"   #自定义保存路径，上面SAVE_MODE记得改2 
MAX_THREADS = 10   #最大线程数(推荐5~10) 
INDEX_URL = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/SEC/xml/FY4B-china-72h.xml"   #XML地址填写位置
```
#### XML清单[可以通过更改XML地址(run.py第14行)以实现更改爬取的影像]
| 卫星 | 云图数据 | XML地址 |
| --- | --- | --- |
| FY-4B | 中国区域云图 | `http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/SEC/xml/FY4B-china-72h.xml` |
| FY-4B | 全圆盘云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4B/FY4B_AGRI_IMG_DISK_GCLR_NOM.xml` |
| FY-4A | 中国区域云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_REGI_MTCC_GLL.xml` |
| FY-4A | 全圆盘云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_DISK_MTCC_NOM.xml` |
| FY-4A | 闪电云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/LMI.xml` |
| FY-4A | 南海区云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_REGI_SCS_GLL_C002.xml` |
| FY-4A | 西北太平洋云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_REGI_PAC_GLL_C002.xml` |
| FY-4A | 兰勃托投影云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_REGI_PCC_LBT_C012.xml` |
| FY-4A | 麦卡托投影云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY4A/FY4A_AGRI_IMG_REGI_PCC_MCT_C012.xml` |
| FY-4A | 中国气象地理区划云图 | `http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/SEC/xml/china-72h.xml` |
| FY-3D | MERSI全球影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/GLOBAL.xml` |
| FY-3D | MERSI北极地区影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/POLAR_NORTH.xml` |
| FY-3D | MERSI南极地区影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/POLAR_SOUTH.xml` |
| FY-3D | MERSI“一带一路”区域影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/BR.xml` |
| FY-3D | MERSI中国区影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/CHINA.xml` |
| FY-3D | MERSI中亚影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/CA.xml` |
| FY-3D | MERSI非洲影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/AF.xml` |
| FY-3D | MERSI大洋洲影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/OC.xml` |
| FY-3D | MERSI北美洲影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/NA.xml` |
| FY-3D | MERSI南美洲影像 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY3D/SA.xml` |
| FY-2H | 圆盘图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/ETV_NOM.xml` |
| FY-2H | 区域云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/ETV_SEC.xml` |
| FY-2H | “丝绸之路经济带”云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/P1_IR1.xml` |
| FY-2H | “21世纪海上丝绸之路”云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/P2_IR1.xml` |
| FY-2H | 东非与西亚云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/P3_IR1.xml` |
| FY-2H | 东欧与中亚云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2H/P4_IR1.xml` |
| FY-2G | 双星动画 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2/FY2_WXCL.xml` |
| FY-2G | 中国区域云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2G/FY2G_LAN_CLC_GRA.xml` |
| FY-2G | 海区云图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2G/FY2G_SEA_CLC_GRA.xml` |
| FY-2G | 圆盘图 | `http://img.nsmc.org.cn/PORTAL/NSMC/XML/FY2G/FY2G_GLB_CLC_GRA.xml` |

## 视频整合模块(MakeVideo.py)  
>## 生成物
>[示例视频](https://builddreams.cn/output.mp4)
### 一、运行方式  
#### 1.执行bat脚本  
  双击前台运行
#### 2.通过命令行运行
```
python MakeVideo.py
```
### 二、配置文件(脚本7到11行)
```
root_folder = r'D:\气象云图' #图片文件夹
output_video = r'D:\气象云图\视频输出\output.mp4'#输出文件夹
frame_size = (825, 739) #分辨率
fps = 60 #帧率
frames_per_image = 2
```


 


