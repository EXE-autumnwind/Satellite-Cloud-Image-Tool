# 中国气象局组合云图自动爬取脚本
- 如果你没有任何基础，可通过“依赖安装.bat”自动安装环境，记得自行配置文件储存地址，默认为/Pull
- MakeVideo.py可以帮你快速把文件夹中的所有图片集合成一个视频

# 下载
- 点击code->download zip

# 生成物
- [示例视频](https://builddreams.cn/output.mp4)

# XML清单[可以通过更改XML地址(run.py第14行)以实现更改爬取的影像]
```
SAVE_MODE = 1 #1.程序根目录 2.指定目录 
MANUAL_SAVE\_PATH = "D:\\气象云图" #自定义保存路径，，上面SAVE_MODE记得改2 
MAX_THREADS = 10 #最大线程数 
INDEX_URL = "http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/SEC/xml/FY4B-china-72h.xml" #XML地址填写位置
```

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

