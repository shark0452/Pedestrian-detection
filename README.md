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

人体检测模型的训练和部署测试：

    1 Crowdhuman数据集下载及说明
    
        因为需要人体检测的模型，先训练一个检测模型，并转换成Aidlux可以部署的方式，进行推理测试。人体检测的数据集有很多，这里采用旷视开源的Crowdhuman的数据集。官网是：http://www.crowdhuman.org/ ，Crowdhuman数据集，总共包含三个方面：15000张的训练数据集，4370张的验证数据集，5000张的测试数据集。其中训练集和验证集都是有标注信息的，测试集没有标注信息。按照官网的标注信息下载之后，得到的文件是这样的。![1667996749609](https://user-images.githubusercontent.com/73569616/200830007-3ef43d6a-57a4-4bb9-b2ec-8f19f411b99d.png)，
    2 人体检测数据集标注文件转换
    
    下载LabelImg,新建一个文件夹Crowdhuman_data，并将网盘下载的Crowdhuman_val.zip和annotation_val.odgt，全都拷贝到Crowdhuman_data中。将其中的CrowdHuman_val.zip解压缩，可以得到一个Images文件夹,CrowdHuman_val.zip和annotation_val.odgt，也可以根据自己需要，后期选择是否训练集也添加进去。将Images文件夹拷贝到Crowdhuman_data路径下，并修改成JPEGImages，此外新建一个Annotations.将annotation_val.odgt中的标注信息提取出来，变成和4370张图片对应的XML格式。
    
    标注文件odgt格式转换成xml格式,在lesson3_codes/data_prepare_code文件夹中，编写了数据清洗的脚本data_code.py。使用VScode编程软件打开data_code.py的文件夹，首先修改其中的roadlabels、roadimages、fpath三个路径。![image](https://user-images.githubusercontent.com/73569616/200875003-cbe02a4c-0b66-4d66-a868-10afe6f1a5cc.png)
需要注意的是Crowdhuman中，有三种标注内容，vbox、fbox、hbox，分别对应：可看到的人体，完整人体，人脸。主要使用完整人体进行训练，因此主要用到fbox的标签。所以再修改下面的两个地方，fbox即表示提取annotation_val.odgt中完整人体的检测框信息，而person表示转换成xml后人体的标签名称信息。![image](https://user-images.githubusercontent.com/73569616/200877896-d78795be-a673-4f37-8c7a-1e5194e7bf87.png)Annotations中可以得到VOC格式的xml文件。主要采用Yolov5的算法，因此我们还要将上面VOC格式转换成Yolov5可以训练的格式。数据清理&切分的脚本，即lesson3_code/data_prepare_code/train_data_split.py。

        (1).新建train_data文件夹,并在train_data里面新建一个images_label_split/crowdhuman_val文件夹，且将前面转换好对应的JPEGImages和Annotations，拷贝到crowdhuman_val文件夹里面。
,并在train_data里面新建一个images_label_split/crowdhuman_val文件夹，且将转换好对应的JPEGImages和Annotations，拷贝到crowdhuman_val文件夹里面。

        (2) 数据集清洗:
        比如有图片，但是没有标注xml。再或者有的目标，标注的太小，比如10*10像素，针对一些标注的问题，可以进行梳理。清洗的代码，即train_data_split.py中。运行train_data_split.py代码，会进行清洗梳理，并在最后会用代码显示标注信息结果，查看是否有标错的图片，确认一下。
        
        (3) 图片和标签文件没有问题后，我们还需要划分成训练集和验证集。这里我们按照8:2的方式来切分，即80%是训练集，20%是验证集。当然我们需要注意，因为只想运行阶段二的代码，所以将阶段一的所有代码，都注释掉。一个一个 去掉注释 一个一个运行 阶段三暂不运行 
        在train_data文件夹中，我们可以看到多了train和test两个文件夹，里面是对应的image和xml文件。

    3 云服务器训练人体检测模型：
    
    （1）采用的算力平台主要是AutoDL AI算力云，官网链接是：https://www.autodl.com/。点击右上角的“注册”选项先进行注册。再进入后台的主页面，点击左上角的“算力市场”。完成后初始化一下 我的网盘。 训练&验证集图片上传： 我们再将前面的一些文件，传输到“我的网盘”里面。主要上传三个文件：将train_data文件夹中的images_label_split文件夹删除，只留下刚刚划分的train和test文件夹。为了上传方便，将train_data文件夹，压缩成一个train_data.zip。![1668010914564](https://user-images.githubusercontent.com/73569616/200884255-70aec32c-d86b-45d8-b2f8-6dae4820f2b4.png)

    将data_prepare_code文件夹，进行压缩，变成data_prepare_code.zip文件夹。
    
    （2）数据集整理代码： 将data_prepare_code文件夹，进行压缩，变成data_prepare_code.zip文件夹。
    
    （3）Yolov5训练代码 ： 将Yolov5_code训练代码，进行压缩，变成yolov5_code.zip。
    
    （4）后台上传文件 ：
    点击AutoDL后台的我的网盘，将刚刚的三个zip文件进行上传 点击“立即创建”后，就可以看到创建的实例了。
    ![image](https://user-images.githubusercontent.com/73569616/200884882-00c0cf54-0a76-4c94-b33e-31cb67339717.png)
点击右面的“JupyterLab”，可以进入控制台页面。

可以点击下面的“终端”，打开一个终端页面，就可以进行操作了。 并且在上面，我们看到autodl-nas即我们刚刚使用的网盘。
![image](https://user-images.githubusercontent.com/73569616/200885106-ae855b0a-0e9b-4b54-961d-dc05a53acdd8.png)

        操作方法与linux一致，标注文件xml格式转换txt格式 
    
    4 PC端Pytorch推理测试
        Pytorch的官网：https://pytorch.org/。显示窗口会跳出pip3 install torch torchvision torchaudio，当然在下载的时候为了网络加速，还添加了清华源。组成下载代码：pip3 install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple  Pytorch，代码中还有一系列的依赖库。
        Pandas下载：pip3 install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple

        yaml下载：pip3 install pyyaml -i https://pypi.tuna.tsinghua.edu.cn/simple

        tqdm下载：pip3 install tqdm -i https://pypi.tuna.tsinghua.edu.cn/simple

        matplotlib下载：pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

        seaborn下载：pip3 install seaborn -i https://pypi.tuna.tsinghua.edu.cn/simple

        scipy下载：pip3 install scipy -i https://pypi.tuna.tsinghua.edu.cn/simple

        ipython下载：pip3 install ipython -i https://pypi.tuna.tsinghua.edu.cn/simple
        
        yolov5的模型，对于images里面的图片进行推理，测试一下效果。

打开detect_image.py文件，这里主要修改代码中的模型、图片路径、yaml文件。![1668182432248](https://user-images.githubusercontent.com/73569616/201380736-77d31e00-947b-4745-abbd-cce6d7baeb22.png)使用Run->"Run Without Debuging"，运行后可以得到一张张推理的图片效果。

        视频处理的代码，重新进行了梳理，放在detect_video.py中。主要修改模型路径、视频路径以及yaml的路径。![1668182481303](https://user-images.githubusercontent.com/73569616/201380880-4b7a609f-0d91-424f-bd9f-5baaf54f88a8.png)运行后，可以得到视频的推理结果。

    5 Aidlux端模型推理测试
        在PC端测试完之后，我们主要是在边缘端Aidlux上进行使用，在前面我们也知道，Aidlux主要针对推理部分，在底层进行了加速优化。因此想要将pt模型移植到Aidlux上使用，还要进行转换模型，修改推理代码的操作。pt模型转换成tflite模型 ，模型转换的文件是export.py文件，在Aidlux中主要运行的是tflite的方式，因此主要修改其中的三个地方。![1668182550351](https://user-images.githubusercontent.com/73569616/201381091-22ec41d9-bfc5-41b8-906c-a3cc8420fd1a.png)  没有 tensorflow ： 输入：pip3 install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple，下载tensorflow库。安装好再运行export.py文件，在models文件夹下面，可以看到生成的yolov5n-fp16.tflite文件。
        
        针对Aidlux中推理测试的代码，放到yolov5_code/aidlux文件夹的yolov5.py中了，也可以将训练好的tflite放到aidlux文件夹中。其中包含了很多Aidlux专属的函数接口，大家可以在https://docs.aidlux.com/#/intro/ai/ai-aidlite，查看下相关的函数说明。
        
        当然其中的代码和原本PC端的代码有一些不同，主要分为三个部分：
                
        （1）加载相关的函数库
        
        ![1668182655415(1)](https://user-images.githubusercontent.com/73569616/201381452-f2fd5696-46ca-4381-a610-323b9a8cba93.png)
        
        （2）模型初始化及加载
        
        其中主要用到两个函数接口，一个是aidlite_gpu.aidlite()和aidlite.ANNMode()。
        
        ![1668182694025](https://user-images.githubusercontent.com/73569616/201381621-12fee1c9-d172-4607-ad39-5262f01dc9a1.png)

        ![1668182859125](https://user-images.githubusercontent.com/73569616/201385275-ab655686-6397-4602-8950-803c20249ce0.png)

        ![1668182865496](https://user-images.githubusercontent.com/73569616/201385290-6f5ff1ee-da8e-49f8-97db-81f80c3a275d.png)

    此外还有两行in_shape，out_shape，这里可以通过netron查看一下相关的模型参数。我们使用https://netron.app/，打开刚刚的yolov5n_best-fp16.tflite文件。点击最下方的输出单元，可以看到输出的信息。
        （3）视频读取&模型推理代码
        
        ![image](https://user-images.githubusercontent.com/73569616/201387186-0b80e703-f956-4688-9671-fb2189145586.png)

        
        5.3 代码复制到Aidlux中
        
            lessons3_codes都进行上传到网页版的Aidlux中![1668184631711](https://user-images.githubusercontent.com/73569616/201387316-7b56763f-e33d-422c-892a-89c4ad44af2f.png)

        5.4 远程连接Aidlux软件
            使用SSH，连接到Aidlux的方式。大家也可以远程连接到lesson3_codes，当看到红色部分的SSH:AIDLUX，即说明远程连接成功。
            ![1668184679011](https://user-images.githubusercontent.com/73569616/201387443-db1ef727-35ae-49f1-a62a-3da5256348e5.png)
            打开aidlux文件夹中的yolov5.py进行视频推理测试，在手机版本的Aidlux和PC端网页的Aidlux中，都可以看到推理的显示结果。PS：需要注意的是，在运行的时候，需要把手机版本里面的aidlux页面叉掉，免得会有冲突，运行的线程会直接被killed掉。
            

