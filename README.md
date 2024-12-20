# python-wzy-ly
本项目是python及其在工程的应用的课程大作业，主要任务是对GitHub上源码进行解读并做部分拓展；源码参考自https://github.com/Junieson，感谢作者对项目开源和说明。
# 项目名称：GUI交互-飞机大战游戏
## 开源项目介绍
工程文件由一个**idea**文件夹、一个**pycache**文件夹、一个**images**文件夹、一个**music**文件夹、两个**py**文件构成，以下将详细阐述每一部分文件的在项目中的作用。  
**idea**文件夹：用于存储项目中各模块的配置信息;  
**pycache**文件夹：第一次执行代码的时候，Python解释器把编译的字节码放在**pycache**文件夹中，这样以后再次运行的话，如果被调用的模块未发生改变，那就直接跳过编译这一步，直接去**pycache**文件夹中去运行相关的 **pyc** 文件，大大缩短了项目运行前的准备时间(具体解释参考CSDN:https://blog.csdn.net/yitiaodashu/article/details/79023987);  
**images**文件夹：存储游戏中加载的各种游戏的图片，包括”敌方战机”的形象、爆炸效果等;  
**music**文件夹：存储游戏中的音乐特效;  
**plane_main.py**:游戏的操作主体python文件，包括各种人机交互功能、游戏数值数组调用等，主要功能是动态使用sprites中的方法和属性;  
**plane_sprites.py**:游戏中各项数值、图形界面,主要用于游戏的静态属性设置;  
## 项目运行配置  
本项目基于python3.7，主要使用pygame库开发游戏，还包含sys、random两个内部依赖。  
  
首先，在此我们需要再次回顾python、pycharm和anaconda之间的关系。  
* python是开发软件或机器学习等需要使用的一种跨平台的计算机程序语言。  
* PyCharm是一种常用的Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制，简单来说就是将python的各种功能界面化、图形化。  
* Anaconda指的是一个开源的Python发行版本，简单来说anaconda是一个可以定义python版本的虚拟环境构建软件，其本身就包含有部分常用的开发依赖模块，也可以在其中继续更新所需的依赖项。  

准备工作：
* 一、下载anaconda并创建anaconda虚拟环境，相关操作主要参考以下这篇csdn文章https://blog.csdn.net/qq_45160840/article/details/127127610?sharetype=blogdetail&shareId=127127610&sharerefer=APP&sharesource=weixin_74969505&sharefrom=qq
* 二、通过pycharm终端命令行安装外部依赖pygame，命令语句：pip install pygame(==***)



## 项目需求分析
项目基本要求：  
* 本项目是基于GUI交互的飞机大战游戏，首先作为一款游戏需要有对应的游戏界面，这里需要考虑到如何设置游戏窗口的分辨率，如何在打开的窗口上绘制坐标系，从而对游戏界面的细节设置（例如开始键、推出键等固定位置图标的确认）。
* 其次作为游戏核心要素需要考虑的是满足人机交互要求，例如点击开始按键时可以启动游戏，通过键盘可以控制飞机的移动，即飞机在坐标系中位置的变化。
* 再者，人机交互需要达到“动画”的形式，即满足飞机飞行、子弹移动达到足够的帧数（每秒画面的更新速度）要求，需要定义一个函数不断的去更新画面，同时最好在此基础上确保可以优化内存，减少运行空间的占用。
* 最后是游戏的可玩性部分，计分系统、不同“小怪”对应的分数值、生命值的扣除逻辑、不同类型的子弹运行轨迹、音乐配置，以及敌机和补给的随机生成等丰富游戏的部分，该部分占据代码大量篇幅，也是代码中较难理解的内容。
  
最终成品游戏包含以下基本功能：  
* 移动:键盘方向键控制英雄移动
* 攻击:英雄自动发射子弹
* 补给:自动生成补给,有子弹buff,炸弹buff,补血buff;子弹buff最多吃5个,每吃一个子弹数目或者威力提高,吃到第五个召唤"最强形态";炸弹buff可以无限吃,出现几率比较小,吃到的炸弹在屏幕左下角显示,空格键引爆一颗炸弹,毁掉当前所有敌军飞机、boss损血;补血buff,一次补满英雄血条
* 小怪:敌军飞机自动生成,向下运动,发射不同速度炮弹
* 计分:每种敌军对应不同分数,英雄击爆后,屏幕又下角的总分增加相应的分数
* 惩罚:子弹击中和撞击都会时敌机和英雄损血,且英雄还会debuff,就是buff效果会减弱
* 结束:当英雄挂掉,游戏结束,屏幕显示分数,并且可以选择重来或者结束游戏
  
同时包含以下拓展部分，参数可自定义，方便后续游戏优化：
* 补给设置:英雄吃buff初期子弹威力+1,且子弹排数有序增加,均匀分步;血条低于某个值会变红,当吃补给增加后又会恢复原色;三组buff出现频率不同,且出现时机不同,补血在英雄血条为红色时优先出现
* 玩法设置:敌机出现位置随机,速度随机,发射子弹速度随机,数量排数自定义,低级敌机出场较多,中型后来逐渐增多;敌军死后子弹留着;飞机不能飞出屏幕外面;子弹击爆敌机后,不继续集中残骇;最强形态不增加英雄所占面积;撞击对不同对象效果不同,英雄撞boss,英雄死boss损血,敌机撞英雄,敌机爆,英雄损血,且损血和被子弹击中血量不同
* 动画效果:英雄,boss有飞行和爆炸动画,敌机有爆炸动画;背景和bgm循环移动,营造飞行感觉;boss移动速度慢,慢于最低速度,即1像素每帧,游戏定义为60帧/秒,即速度低于60像素/秒;每个动作都有专属音效,如英雄爆,敌机爆,补习,补子弹,补炸弹,扔炸弹,射击......
## 总体框架
## 1.游戏的初始化和退出    
要使用pygame提供的所有功能之前，一定要使用pygame.init()——初始化  
* 在我们要动手用它完成我们的想法之前，电脑这个强迫症需要我们检查一遍，这个工具包是否完整，能否正常给我们提供帮助。而这个检查的动作，就是pygame.init()，其实就是检查，电脑上一些需要的硬件调用接口、基础功能是否有问题。如果有，他会在程序运行之前就反馈给你，方便你进行排查和规避。
  
在结束游戏之前，要使用pygame.quit()卸载所有 pygame 模块
* 通常，由于程序退出之前，Python总是会关闭pygame，这不会真的有什么问题。但是，在IDLE中有一个bug，如果一个Pygame程序在调用pygame.quit()之前就终止了，将会导致IDLE挂起。
## 2 理解游戏中的坐标系
坐标系划定：原点在左上角 (0, 0)；x轴水平方向向右，逐渐增加；y轴垂直方向向下，逐渐增加  
可见元素位置划定：在游戏中所有可见元素的位置都是以矩形描述的
要描述一个矩形区域需要四个变量，分别是起始点的坐标(x,y)和矩形框的宽度和高度(width,length)。pygame专门提供了一个对象pygame.Rect用于描述矩形区域——Rect(x, y, width, height) -> Rect
![Uploading image.png…]()
## 3 创建游戏主窗口
方法  | 说明  
 ---- | -----   
 pygame.display.set_mode()  | 初始化游戏显示窗口 
 pygame.display.update()  | 刷新屏幕内容显示，稍后使用 

 表头  | 表头  | 表头
 ---- | ----- | ------  
 单元格内容  | 单元格内容 | 单元格内容 
 单元格内容  | 单元格内容 | 单元格内容 


### 三级标题  
#### 四级标题  
##### 五级标题  
###### 六级标题 
  
