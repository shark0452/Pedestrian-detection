# Pedestrian-detection
本项目 主要是做 越界识别算（中等型算法应用）
街道-人体扫描

AidLUx简介 : AIdlux主打的是基于ARM架构的跨生态（Android/鸿蒙+Linux）一站式AIOT应用开发平台。

--  该项目是搭建在Aidlux（模型移植采用Python）平台上的 用到yolo5 对视频中的人踩过一条线 进行计数。

--   使用vscode远程连接 从目标检测算法的训练，Aidlux上的移植、测试等方面。目标检测后，会将目标检测和目标追踪结合，尝试完整的人体检测追踪，为后面的各类业务功能做准备。会将越界识别的业务功能也添加进来，当有人越界的时候，会通过喵提醒的方式，通知开发者及时查看手机里面的越界图片。

AI项目流程：

    1. ai需求（业务人员）：ai商机和业务需求
    
    2. 数据采集（数据工程师）： （1）数据采集和数据标注 （2） 数据分析和可视化  
    
    3. AI模型训练（算法工程师）：(1)网络模型结构设计 （2）超参调节模型训练
    
    4. AI模型部署（嵌入式软件工程师)：（1）算法芯片硬件适配 （2）视频结构化平台开发
    
    5. 系统软件工程师（系统软件工程师）：（1）业务中合开发 （2）云边端协同 （3）监控大屏数字孪生 
    
    6. 落地部署(运维工程师)：解决方案集成落地实施部署
    
1 AI项目开发及Aidlux的特点:AIdlux主打的是基于ARM架构的跨生态（Android/鸿蒙+Linux）一站式AIOT应用开发平台。用比较简单的方式理解，我们平时编写训练模型，测试模型的时候，常用的是Linux/window系统。而实际应用到现场的时候，通常会以几种形态：GPU服务器、嵌入式设备（比如Android手机、人脸识别闸机等）、边缘设备

1.1 跨平台应用的系统

1.2 安卓&Linux移植开发流程: 开发流程 pc写代码 直接迁移至Aidlux平台即可应用测试。

1.3 Aidlux算法优化 :

2 手机版本Aidlux软件安装： 手机商店直接下载Aidlux

3 电脑版Aidlux投影测试

4 Aidlux系统AI案例测试: 点击桌面下方菜单栏的examples,在桌面上下载源代码后，手机版本此应用时，也是同样下载下来了。点击Run Now

5 Aidlux软件设置默认后台运行：

（1）小米手机和平板设置教程：
https://community.aidlux.com/postDetail/832

（2）OPPO手机与平板设置教程：
https://community.aidlux.com/postDetail/834

（3）vivo手机与平板设置教程：
https://community.aidlux.com/postDetail/835

（4）华为鸿蒙/HarmonyOS 2.0设置教程：
https://community.aidlux.com/postDetail/828

（5）华为鸿蒙/HarmonyOS 3.0设置教程：
https://community.aidlux.com/postDetail/827

6 Aidlux&VScode编程调试方式

    下载vscode和aidlux

7 安装本地版的Python和Opencv

1.打开vscode安装python插件 

2.点击Vscode左上角的“File->Open Folder”，打开第二节课的Lesson2_codes文件夹。

当然Lesson2的课程中，还会用到Opencv，所以我们先安装一下Opencv库。

选择“Terminal”中的“New Terminal”。在终端页面输入：pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple，即可快速下载安装成功。

8 PC端读取图片&视频操作

    在lesson5 中video_capture_PC.py，代码里面采用了跳帧读取的操作。命令：python + 复制相对位置

9 PC端远程调试Aidlux
当PC端的python和Opencv测试成功了，我们再使用Vscode远程连接安卓版本的Aidlux，尝试在Aidlux环境下实时调试代码了。
![image](https://user-images.githubusercontent.com/73569616/200801867-d4967e37-4645-46b3-a8bc-75526498663a.png)
选择右上角的“Upload”，将Lesson5_code文件夹中的代码上传到Home文件夹下。在home文件夹下就有了一个Lesson5_code的文件夹，我们再通过远程连接的方式，使用Vscode调试其代码。

10 PC端调试Aidlux读取图片&视频

 安装Remote SSH 点击Vscode左侧的“Extensions”，输入“Remote”，针对跳出的Remote SSH，点击安装。点击"Remote Explorer"，进行远程连接的页面，点击左下角的“Open a Remote Window”，再选择“Open SSH Configuration file”。针对跳出的弹窗，再选择第一个config。输入连接信息，需要注意的是，这里的Host Name填写你自己的Aidlux里面Cloud_ip的地址。
![image](https://user-images.githubusercontent.com/73569616/200802318-04b9a15e-d7fb-45ea-83be-04c80a7642e8.png)（这里默认写9022，不写8000）保存后，在左侧会生成一个SSH服务器，鼠标放上后，会跳出一个“Connect to Host in New Window”然后会跳转到连接的页面，选择“Linux”。选择“Continue”，再输入密码，aidlux
![image](https://user-images.githubusercontent.com/73569616/200802510-72227b54-2760-48fd-beaf-56e08493ff89.png)当左下角跳出SSH Aidlux时，表示已经连接成功。
选择左上角的File，点击Open Filer，即可跳出Aidlux里面的路径。
![image](https://user-images.githubusercontent.com/73569616/200802681-03f7fce2-dace-4064-870c-c02824a88908.png)
将路径输入的信息，修改成”/home/lesson5_codes“，点击OK。跳出的窗口中，再输入密码”aidlux“，即可打开我们已经上传的Lesson5_code文件夹。

比如打开read_image_Aidlux.py文件，运行后，在手机端的Aidlux上可以看到读取的显示图片。
打开video_capture_Aidlux.py，在读取视频和显示图像的地方，采用cvs的方式，读取运行后，就可以在手机上看到显示的视频效果。
