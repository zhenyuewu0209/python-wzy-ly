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
![image](https://github.com/user-attachments/assets/e7bcedf4-145f-421f-9ca7-4ea559fb03d9)
### 1.游戏的初始化和退出    
要使用pygame提供的所有功能之前，一定要使用pygame.init()——初始化  
* 在我们要动手用它完成我们的想法之前，电脑这个强迫症需要我们检查一遍，这个工具包是否完整，能否正常给我们提供帮助。而这个检查的动作，就是pygame.init()，其实就是检查，电脑上一些需要的硬件调用接口、基础功能是否有问题。如果有，他会在程序运行之前就反馈给你，方便你进行排查和规避。
  
在结束游戏之前，要使用pygame.quit()卸载所有 pygame 模块
* 通常，由于程序退出之前，Python总是会关闭pygame，这不会真的有什么问题。但是，在IDLE中有一个bug，如果一个Pygame程序在调用pygame.quit()之前就终止了，将会导致IDLE挂起。
### 2 理解游戏中的坐标系
坐标系划定：原点在左上角 (0, 0)；x轴水平方向向右，逐渐增加；y轴垂直方向向下，逐渐增加  
可见元素位置划定：在游戏中所有可见元素的位置都是以矩形描述的
![image](https://github.com/user-attachments/assets/452ece5a-2629-489f-b945-395dd01bdc77)
要描述一个矩形区域需要四个变量，分别是起始点的坐标(x,y)和矩形框的宽度和高度(width,length)。pygame专门提供了一个对象pygame.Rect用于描述矩形区域——Rect(x, y, width, height) -> Rect
![image](https://github.com/user-attachments/assets/738269bb-f2de-4696-9ffd-465d801ffa04)
### 3 创建游戏主窗口
方法  | 说明  
 ---- | -----   
 pygame.display.set_mode()  | 初始化游戏显示窗口 
 pygame.display.update()  | 刷新屏幕内容显示，稍后使用 
  
set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
* resolution参数是一个二元组，表示宽和高。flags 参数是附件选项的集合。depth参数表示使用的颜色深度。
* 返回的 Surface对象可以像常规的Surface对象那样去绘制，但发生的改变最终会显示到屏幕上。
* 如果没有传入resolution 参数，或者使用默认设置(0, 0)，且Pygame使用SDL1.2.10以上版本，那么创建出来的Surface对象将与当前屏幕用户一样的分辨率。如果只有宽或高其中一项被设置为0，那么Surface对象将使用屏幕分辨率的宽或高代替它。
### 4 理解图像并实现图像绘制
在游戏中，能够看到的游戏元素大多都是图像
图像文件初始是保存在磁盘上的，如果需要使用，第一步就需要被加载到内存
要在屏幕上看到某一个图像的内容，需要按照以下三个步骤：
* 使用pygame.image.load()加载图像的数据
* 使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
* 调用pygame.display.update()方法更新整个屏幕的显示
  
透明图像
* png格式的图像是支持透明的
* 在绘制图像时，透明区域不会显示任何内容
* 但是如果下方已经有内容，会透过透明区域显示出来
* 这里是因为调用的图片都是矩形的，除了模型部分其余是空白，如果不透明化处理会遮盖背景图，使游戏的观感降低
### 5 游戏中的动画实现原理
跟电影的原理类似，游戏中的动画效果，本质上是快速的在屏幕上更新图像
* 电影是将多张静止的电影胶片连续、快速的播放，产生连贯的视觉效果
  
一般在电脑上每秒更新60次，就能够达到非常连续高品质的动画效果
* 每次更新的结果被称为1帧Frame
  
游戏循环的开始就意味着游戏的正式开始
* 保证游戏不会直接退出
* 检测用户交互 —— 按键、鼠标等...
* 变化图像位置 —— 动画效果
  * 每隔0.0167秒移动一下所有图像的位置
  * 调用 pygame.display.update()更新屏幕显示  

游戏时钟
* pygame专门提供了一个对象pygame.time.Clock可以非常方便的设置屏幕绘制速度——刷新帧率
* 要使用时钟对象需要两步：
  * 1）在游戏初始化创建一个时钟对象
  * 2）在游戏循环中让时钟对象调用tick(帧率)方法
    * tick 方法会根据上次被调用的时间，自动设置游戏循环中的延时
  * FPS=60
  * FPSClock=pygame.time.Clock()
  * FPSClock.tick(FPS)

### 6 在游戏循环中 监听 事件
事件event
* 就是游戏启动后，用户针对游戏所做的操作
* 例如：点击关闭按钮，点击鼠标，按下键盘...
  
监听
* 在游戏循环中，判断用户具体的操作
* 只有捕获到用户具体的操作，才能有针对性的做出响应
  
代码实现
* pygame中通过pygame.event.get()可以获得用户当前所做动作的事件列表
用户可以同一时间做很多事情
* 代码通过判断事件列表是否有符合人机交互的操作从而对游戏进程进行设置
  * 例如，当鼠标左键点击了退出时，游戏进程结束
  * 当用户界面从游戏界面调离时，游戏进程暂停
### 7 理解精灵(Sprite)和精灵组(sprite.Group)
为了简化开发步骤，pygame 提供了两个类
* pygame.sprite.Sprite —— 存储图像数据 image和位置rect的对象
* pygame.sprite.Group
  
精灵
* 在游戏开发中，通常把显示图像的对象叫做精灵Sprite
* 精灵需要有两个重要的属性
  * image要显示的图像
  * rect图像要显示在屏幕的位置
* 默认的update()方法什么事情也没做
  * 子类可以重写此方法，在每次刷新屏幕时，更新精灵位置
* 注意：pygame.sprite.Sprite 并没有提供 image和rect两个属性
  * 需要程序员从pygame.sprite.Sprite派生子类
    * 派生：指的是子类继承父类的属性方法，并且派生出自己独有的属性与方法若子类中的方法名与父类的相同，优先用子类的
  * 并在子类的初始化方法中，设置image和rect属性
  
精灵组
* 一个精灵组可以包含多个精灵对象
* 调用精灵组对象的update()方法
  * 可以自动调用组内每一个精灵的update()方法
* 调用精灵组对象的draw(屏幕对象)方法
  * 可以将组内每一个精灵的image绘制在rect位置

## 代码分析
文件中包含两个python源代码文件plane_main.py和plane_sprites.py。
* 其中sprites主要是对游戏中需要定义的一些对象进行定义，给这些对象赋予某些属性和方法；
* main文件只有一个大的子类，主要用来调用sprites中规定的各对象，同时存储游戏过程中产生的对象，统一管理和移除；
* 在源代码中，最核心的思想是创建类，继承和派生新的子类，以及对各个类规定的对象进行交叉调用和处理。
### sprites文件
定义一些游戏中的变量/常量
* 变量score用来记录游戏过程积攒的分数
* color_***是血条的颜色设置，不同类型的敌人、常规血量的操作者以及低血量的操作者有不同的血条颜色
* FRAME_PER_SEC是规定的帧率（图1）  
![image](https://github.com/user-attachments/assets/94e12c3f-205f-471d-9ebc-1d6a283536a1)
定义了一些事件常量，每个常量对应一个数值，在main程序中按需求被调用  
![image](https://github.com/user-attachments/assets/f58ac8ba-94d4-4f61-946d-7a85c998b40b)  
定义了GameScore这个类，该类继承自object（一般如果未说明都默认继承object），类里面定义了它的属性和方法  
![image](https://github.com/user-attachments/assets/aae1445a-df0b-40d4-8beb-ef3b760b8461)    
定义了GameSprite这个类，该类继承自pygame.sprite.Sprite，除了pygame.sprite.Sprite自带的属性和方法，GameSprite还定义了游戏中涉及的参数属性和update这个方法，后面定义的子类都会以GameSprite为父类进行派生。    
![image](https://github.com/user-attachments/assets/5c73050b-97d3-4cc6-8038-416701be075f)
![image](https://github.com/user-attachments/assets/7dc430e6-ee97-4203-98c9-ebffd1d708de)  
定义了游戏背景这个精灵，继承父类的初始化和更新方法，同时规定了图片的交替规则，即当y大于屏幕尺寸时，将其值设置到屏幕上方    
![image](https://github.com/user-attachments/assets/11b8edcf-f7c5-4196-a3f1-85f10863598f)
![image](https://github.com/user-attachments/assets/6fc6bbc9-00c3-4135-87e5-c06ce5268bb4)  
定义了BOSS的精灵，其中包含图片、音乐、位置、爆炸状态等；定义了一系列的帧，分别用来控制子弹的发射、BOSS的移动和爆炸画面  
![image](https://github.com/user-attachments/assets/45d06262-571b-423d-b443-dce4b80904cc)
![image](https://github.com/user-attachments/assets/d6fe9428-1fb1-47be-8187-11f8ed9a7613)      
BOSS的移动逻辑是左右移动，上下固定，每向一边移动固定的帧之后向另一边移动；BOSS的子弹每层5个，中间一个在x轴上固定不动，其他四个根据j的值分配不同的横向速度。  
![image](https://github.com/user-attachments/assets/9fe95356-556f-4995-8a9d-cd3d148aa5af)
![image](https://github.com/user-attachments/assets/32afb4d1-a752-4865-b46a-2cc52df0abf3)  
定义敌机的精灵，敌机分为两种，有参数，默认为1（初始敌机）  
![image](https://github.com/user-attachments/assets/24bb693c-79ca-4762-8dcd-f535f4a99e7e)
![image](https://github.com/user-attachments/assets/09b47313-1d68-473b-a082-a9d771cb17bf)    
和BOSS不同，敌机是上下移动的，因此需要定义这方面的逻辑，不同的敌机初始速度不同，敌机一号不会发射子弹，敌机二号需要定义子弹的逻辑。同时敌机一号和二号都需要判断其是否飞出屏幕，是则消除。isboom不是判断是否爆炸，它是用来判断是否扣血以及作为爆炸需要满足的前置条件之一。  
![image](https://github.com/user-attachments/assets/afad7e23-672e-455a-b15b-15f271250f30)
![image](https://github.com/user-attachments/assets/650caf5d-36a6-424a-b1e1-9cfc56b2e791)
![image](https://github.com/user-attachments/assets/ff260090-745b-4f3f-b3ab-4dcf3773fa4a)  
Hero即玩家精灵的设计，和BOSS、enemy一样首先定义了部分属性，如加载的图片、播放的音乐、血条等，不同的是引入了子弹buff和炸弹buff。玩家接收到子弹buff一到三次会增加同一时间发射的子弹数（需要调整子弹的分布逻辑）；第四次会改变子弹类型，更换贴图，伤害变为2；第五次会增加两架僚机。接收到炸弹会显示在游戏界面左侧，最多可以保留7个  
![image](https://github.com/user-attachments/assets/79460f71-c478-4427-95e9-759732b676ca)
![image](https://github.com/user-attachments/assets/1d66864b-6b9a-47f5-8507-36cdbd515aef)    
僚机的精灵  
![image](https://github.com/user-attachments/assets/8da07820-88e9-4e53-a281-b548754c9a22)
![image](https://github.com/user-attachments/assets/4dcb3b73-cb9f-4f14-95a2-c015a86f505d)    
定义子弹的精灵，BOSS和enemy和Hero的bullet在类中定义后都被加到Bullet类中。BOSS等发射的子弹是Bullet这个类的对象。（color在本段和其他段的定义不同）  
![image](https://github.com/user-attachments/assets/26590476-918e-411b-a4a0-e66892e0d28e)
![image](https://github.com/user-attachments/assets/1c235c6d-3e54-436f-aa7e-ea43e576dda0)  
Buff1、Buff2和Buff3，这里的Buff是一个实际对象。拾取到Buff之后获得的增益以及增益效果是在Hero类和main函数中定义的，Buff1/2/3是定义了子弹/炸弹/医疗包的贴图、随即发生、运动逻辑和存续时间。Buff2和Buff3通过Hero血条区分，实际只有贴图和存在时间有差别。
![image](https://github.com/user-attachments/assets/ac464537-dbe8-4d31-a63b-b761fb4d5ce2)
![image](https://github.com/user-attachments/assets/55a58987-d5ff-4cc5-8ead-e4f8060cfc50)
![image](https://github.com/user-attachments/assets/6bd5fb6a-11d4-46f3-b094-5f0ae9eadf74)  
bloodline主要是定义了一些属性和通过逻辑区分血条的颜色（不同长度（血量）时颜色不同）
![image](https://github.com/user-attachments/assets/e7dbc5f0-72cf-473e-8c5b-b89e89c9fd2f)  
绘制结束界面。第一段将again和gameover的贴图绘制在频幕上；第二段是用来判断人机交互的，当鼠标点击到一定范围内返回1或0，这里的1或0会传递到main函数中，用来决定是否重新开始游戏；第三段是使用pygame内部的文字包，以固定字体、大小绘制“score”，再将“score”文字转变为图像绘制到指定区域。  
![image](https://github.com/user-attachments/assets/8341b3b2-57a0-4769-a548-488bfed15b93)
![image](https://github.com/user-attachments/assets/7bff4c8a-c34c-42c3-8d70-0ba4779f8035)
![image](https://github.com/user-attachments/assets/05ce936f-0565-4195-bd94-a45ea00de678)    
### main文件
主函数只定义了一个PlaneGame类，游戏过程中的操作和参数都是通过调用其属性和方法实现的。  
![image](https://github.com/user-attachments/assets/c07224fb-ca96-4491-af2b-76ac3f736de4)  
self.clock = pygame.time.Clock()创建了一个时钟，通过后面代码赋予参数被设定为60帧/秒。  
set_timer() 方法会每隔这个时间间隔触发一次 CREATE_ENEMY_EVENT 事件。 
![image](https://github.com/user-attachments/assets/c178ce4a-21ce-4857-ad8d-639ad0526610)
![image](https://github.com/user-attachments/assets/07a163c1-b607-4376-9380-b0857ace3482)  
定义了一系列的精灵组，方便在游戏进程中进行统一管理，在游戏结束后其中的数据会被清楚，释放所占用的内存空间。（在 Pygame 中，精灵组（pygame.sprite.Group） 是一个 容器，它用于 存储和管理多个精灵对象（pygame.sprite.Sprite））  
![image](https://github.com/user-attachments/assets/45563c09-fd85-4ddf-8baa-1b612a7b0a1d)
![image](https://github.com/user-attachments/assets/9e7c6b45-6cf2-41f4-9ad5-4e2516830ed6)  
定义了一个对象用来启动游戏，调用了多个方法事件监听、碰撞检测等  
![image](https://github.com/user-attachments/assets/9c26fe4c-0bb9-44c7-9a8a-8e76291f521a)
![image](https://github.com/user-attachments/assets/961734bd-d45a-42b2-9669-74e8b49ed60d)    
事件监测，对一系列事件并列检测，事件中又含有分支和循环。玩家静止时坐标系是不变的，即静止的，通过操控键盘，以5为单位改变坐标（玩家飞机是没有速度的）。   
![image](https://github.com/user-attachments/assets/194a11eb-659e-46a2-8841-996f60a428b1)
![image](https://github.com/user-attachments/assets/e357ef95-5ba7-447d-89b0-fdef484488d5)
![image](https://github.com/user-attachments/assets/ca27ca92-cc28-4a06-a570-8f00b6c4d04b)
![image](https://github.com/user-attachments/assets/ee608115-2c42-446b-8d41-76fd65759d7d)
![image](https://github.com/user-attachments/assets/91dc2c0c-7b41-4d2a-a36c-b67889a4c8cc)
![image](https://github.com/user-attachments/assets/c91212ed-6e80-4dec-844b-92792637eb39)    
炸弹使用后的功能定义：对于非BOSS的敌人直接扣除血量，对于BOSS扣除20滴。  
![image](https://github.com/user-attachments/assets/c0337810-c191-418e-a35e-3dfba228597a)  
碰撞检测，分为有害和有利碰撞检测。飞机与子弹、飞机与飞机之间的碰撞属于有害碰撞，根据碰撞对象的不同扣除不同的血量；玩家飞机与buff碰撞属于有利碰撞，根据飞机状态不同和拾取的buff不同，获得的增益不同。核心是使用了pygame.sprite.collide_mask方法。  
![image](https://github.com/user-attachments/assets/f1a9e7bb-0661-4654-8f18-1e19935f2ea4)
![image](https://github.com/user-attachments/assets/6be30557-839a-4114-bee0-3be1217872d0)  
定义了僚机的显示设置  
![image](https://github.com/user-attachments/assets/f9cb249e-8a98-47f2-bdac-9e019369802f)
对前面调用的更新方法做了定义，再次调用了sprites中的定义  
![image](https://github.com/user-attachments/assets/0784365b-8a67-4dbf-b5da-1f377286f312)
![image](https://github.com/user-attachments/assets/d6065b1b-2601-4028-9b10-7b7095784e4c)  
对玩家飞机范围作出限制；设置了部分游戏界面  
![image](https://github.com/user-attachments/assets/b0b6c74e-f1f2-431b-9004-b09a53eef083)
![image](https://github.com/user-attachments/assets/cd522c29-a140-4a8d-87b0-b6224e11c12a)
![image](https://github.com/user-attachments/assets/33b5de8f-568c-4dbb-b4ab-1325fa19b4ed)  
静态方法
* @staticmethod 是 Python 中的一个装饰器，表示该方法是 静态方法。
* 静态方法与实例方法不同，它不需要访问类的实例（不需要 self 参数），可以直接通过类调用。
* 静态方法通常用于执行不依赖于实例属性和方法的功能。它是属于类的，而不是类的实例。
![image](https://github.com/user-attachments/assets/33bd5bf4-8d68-4744-9216-578ac851b41f)
## 拓展
我们在源代码的基础上进行了改进，增加了一个启动界面和击杀敌人的统计功能
* 启动界面设计
  * 启动界面主要定义了一个CanvasStart类，给其赋予了加载图片并在指定区域判断用户鼠标交互的属性和方法
  * 游戏启动时首先调用该开始界面，当用户选择开始游戏，则进入游戏主体，游戏正式执行
  * ![E9ISU@%6E3 _J443LW4QH9](https://github.com/user-attachments/assets/ec91f616-a8c6-43e2-9c34-9cf3f09b270e)
* 击杀敌人的统计功能
  * 该功能起初的设计思路是将击杀特定敌人放在游戏主体main中判断，当击杀特定敌人后，就将该数值返回给定义好的字典存储
  * 但在实际运行过程中发现，main中的更新并非为实时的，因此在最终显示杀敌统计时，经常会少于实际杀敌数
  * 也考虑过重新编写更新部分代码，但由于其一更新代码庞杂，分布在main中各个部分，容易造成代码错误，其二过快的更新帧率对于用户是没有实质上的体验提升，同时还会占据电脑内存，尽管本游戏较小不会有太大影响，但对于大型游戏还是不合理的
  * 综合以上因素，又联想到杀敌数总是与总分是相对应的，因此只要将定义的杀敌数，使用和score同样的判决条件，在原来的精灵中加上kill_stats这一属性即可，通过value来判断击杀敌人的类型
  * 设计逻辑确定后，就是显示界面的设置，通过定义一个新的类来启动结束过程，将kill_stats的三个变量数值先以文本形式显示，再将该文本绘图并加载在结束界面上即完成击杀敌人的统计功能
  * ![$MOB IW$ORQ699@JT6` 0{V](https://github.com/user-attachments/assets/28bcfc42-b983-4b8b-af05-d80214460ef9)


## 总结  
通过本次课程大作业，我们主要获得了两方面的收获。
* 首先，是对于游戏开发方面。在大一时的课程设计中，我所参与的内容就是一个交互界面的设计，不过当时是用C语言设计了一个静态的答题界面，而这次课程大作业则是去解析一个动态的交互界面。通过两次课设经历，我对于游戏界面的理解更加清晰，对于如何实现人机交互、提升游戏功能有了更深的认识。
* 其次，是对于python本身的。通过解读源码、拓展原来的功能，我们了解到python与其相关插件pycharm、anaconda之间的关系，学会了如何利用上述插件去配置虚拟环境，并导入相关依赖。直观感受到了python是一门面向对象的编程语言，通过类的派生、继承等赋予某一对象独特的属性和方法，并对这些方法进行操作，从而达成指定功能的实现。python具有庞大的开发环境和开源网络，这为python这门语言赋予了十足的发展空间，目前python也是公认的机器学习所必须要掌握的语言之一，与我们未来的专业方向选择不谋而合，通过这门课程和大作业我们对于python从一无所知到了有所涉猎，相信在未来，我们会掌握更多python的开发功能，扬帆起航。

  
## 代码
import sys
import pygame
pygame.init()
from plane_sprites import *
#在 Python 中，from plane_sprites import * 是一种 导入语句，用于从一个模块中导入所有的内容（类、函数、变量等）。
# 具体来说，plane_sprites 是一个 Python 模块或文件，而 * 表示将该模块中所有公开的元素导入到当前的命名空间中。
# **************************************************************

# FileName: plane_main.py***************************************
# First Author:  Junieson *********************************************
# zhenyuewu0209、jinyunyijiu use for reference
# Version:  2024.12.20 ******************************************
# ****************************************************************
class PlaneGame(object):
    #是 Python 中定义一个名为 PlaneGame 的类的语句。
    # 这个类继承自 object 类（所有类在 Python 中默认都会继承 object 类，除非显式地继承其他类）。
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)#pygame自带
        # 创建结束界面
        self.canvas_over = CanvasOver(self.screen)#plane_sprites中定义
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()#pygame自带
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 分数对象
        self.score = GameScore()
        # 程序控制指针
        self.index = 0
        # 音乐bgm
        self.bg_music = pygame.mixer.Sound("./music/game_music.ogg")#创建一个pygame.mixer.Sound类的对象self.bg_music
        self.bg_music.set_volume(0.3)
        self.bg_music.play(-1)#调用了pygame.mixer.Sound的方法，制定播放循环次数，-1表示无限循环
        # 游戏结束了吗
        self.game_over = False
        # 4. 设置定时器事件 - 创建敌机　1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, random.randint(1000, 2000))
        #set_timer() 方法会每隔这个时间间隔触发一次 CREATE_ENEMY_EVENT 事件。
        pygame.time.set_timer(HERO_FIRE_EVENT, 400)
        pygame.time.set_timer(BUFF1_SHOW_UP, random.randint(10000, 20000))
        pygame.time.set_timer(BUFF2_SHOW_UP, random.randint(20000, 40000))
        pygame.time.set_timer(ENEMY_FIRE_EVENT, 2000)

        #改进
        self.start_screen = CanvasStart(self.screen)
        kill_stats = {"Enemy1": 0, "Enemy2": 0, "Boss": 0}
        #改进

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        #定义这些类，是为了方便存储在游戏进行中产生的数据，统一管理，游戏结束后释放内存
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌军子弹组
        self.enemy_bullet_group = pygame.sprite.Group()

        # 血条列表
        self.bars = []
        self.bars.append(self.hero.bar)

        # 创建buff组
        self.buff1_group = pygame.sprite.Group()

        # 创建假象boom组
        self.enemy_boom = pygame.sprite.Group()

        # bomb列表
        self.bombs = []

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            #这个方法名的前两个下划线（__）通常意味着这个方法是 私有的，即该方法是供类内部使用的，不应该被外部直接调用。
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()

            # 是否要结束游戏

            if self.game_over:
                self.canvas_over.update()

            # 5. 更新显示
            pygame.display.update()
            #是 Pygame 中的一个方法，用于 更新屏幕，即将你所绘制的内容（例如图形、文本、背景等）显示到屏幕上。


            # 改进
            if self.game_over:
                global kill_stats
                self.canvas_over.set_stats(kill_stats)
                self.canvas_over.update()
            # 改进

    def __event_handler(self):  # 事件检测

        if self.score.getvalue() > 200+500*self.index:
            self.boss = Boss()
            self.enemy_group.add(self.boss)#add继承自pygame.sprite.Group
            self.bars.append(self.boss.bar)
            self.index += 1

        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                #pygame自带
                pygame.quit()
                sys.exit()
            if event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵将敌机精灵添加到敌机精灵组
                if self.score.getvalue() < 20:
                    enemy = Enemy()
                else:
                    if random.randint(0, 100) % 4:
                        #在这行代码中，random.randint(0, 100)会返回一个0到100之间的整数，包含0和100。
                        enemy = Enemy()
                    else:
                        enemy = Enemy(2)

                self.enemy_group.add(enemy)
                self.bars.append(enemy.bar)

            elif event.type == HERO_FIRE_EVENT:
                for hero in self.hero_group:
                    hero.fire()#只要游戏进行，hero开火持续
            elif event.type == BUFF1_SHOW_UP:
                buff1 = Buff1()
                self.buff1_group.add(buff1)
            elif event.type == BUFF2_SHOW_UP:
                if self.hero.bar.color == color_red:#按需分配，buff2根据血量需求可以是炸弹或者血包
                    buff = Buff3()
                else:
                    buff= Buff2()
                self.buff1_group.add(buff)
            elif event.type == ENEMY_FIRE_EVENT:
                for enemy in self.enemy_group:
                    if enemy.number >= 2:
                        enemy.fire()
                        for bullet in enemy.bullets:
                            self.enemy_bullet_group.add(bullet)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #判断空格键是否触发
                self.bomb_throw()
            else:
                if self.game_over == True:
                    flag = self.canvas_over.event_handler(event)#调用canvas_over里面的event_handler，根据触发位置返回0或1
                    if flag == 1:
                        self.__start__()
                    elif flag == 0:
                        pygame.quit()
                        sys.exit()

        # 使用键盘提供的方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            self.heros_move(5)
        elif keys_pressed[pygame.K_LEFT]:
            self.heros_move(-5)
        elif keys_pressed[pygame.K_UP]:
            self.heros_move(0, -5)
        elif keys_pressed[pygame.K_DOWN]:
            self.heros_move(0, 5)
        else:
            self.heros_move(0, 0)

    def heros_move(self, x=0, y=0):
        self.hero.speedx = x
        self.hero.speedy = y

    def bomb_throw(self):
        music_use_bomb = pygame.mixer.Sound("./music/use_bomb.wav")
        if self.hero.bomb > 0:
            music_use_bomb.play()
            self.hero.bomb -= 1
            self.bombs.pop()
            for enemy in self.enemy_group:
                if enemy.number < 3:
                    enemy.bar.length = 0
                    enemy.isboom = True
                else:
                    enemy.injury = 20
                    enemy.isboom = True#这里是为了启动BOSS的扣血，不是爆炸，见源代码

    def __check_collide(self):

        # 1. 子弹摧毁敌机
        for enemy in self.enemy_group:
            for hero in self.hero_group:
                for bullet in hero.bullets:
                    if pygame.sprite.collide_mask(bullet, enemy):  # 这种碰撞检测可以精确到像素去掉alpha遮罩的那种哦
                        #这是pygame自带的
                        bullet.kill()
                        enemy.injury = bullet.hity#Bullet自带的属性，color伤害
                        enemy.isboom = True
                        if enemy.bar.length <= 0:
                            # #改进
                            # if enemy.number == 1:
                            # if enemy.bar.value == 2:  # 普通敌人
                            #     self.kill_stats["Enemy1"] += 1
                            # elif enemy.bar.value == 4:  # 加强敌人
                            #     self.kill_stats["Enemy2"] += 1
                            # else:  # BOSS
                            #     self.kill_stats["Boss"] += 1
                            #     #改进
                            self.enemy_group.remove(enemy)
                            self.enemy_boom.add(enemy)

        # 2. 敌机撞毁英雄
        for enemy in self.enemy_group:
            if pygame.sprite.collide_mask(self.hero, enemy):
                if enemy.number < 3:
                    enemy.bar.length = 0  # 敌机直接死
                    self.hero.injury = self.hero.bar.value / 4  # 英雄掉四分之一的血
                    if self.hero.buff1_num > 0:
                        self.hero.buff1_num -= 1
                        self.hero.music_degrade.play()
                    self.enemy_group.remove(enemy)
                    self.enemy_boom.add(enemy)
                    enemy.isboom = True
                else:
                    self.hero.bar.length = 0
                self.hero.isboom = True

        # 子弹摧毁英雄
        for bullet in self.enemy_bullet_group:
            if pygame.sprite.collide_mask(self.hero, bullet):
                bullet.kill()
                self.hero.injury = 1
                if self.hero.buff1_num > 0:
                    self.hero.music_degrade.play()
                    if self.hero.buff1_num == 5:
                        self.mate1.kill()
                        self.mate2.kill()
                    self.hero.buff1_num -= 1

                self.hero.isboom = True

        if not self.hero.alive():
            self.hero.rect.right = -10  # 把英雄移除屏幕
            if self.hero.buff1_num == 5:
                self.mate1.rect.right = -10
                self.mate2.rect.right = -10
            self.game_over = True
#2024.12.07
        # 3.buff吸收
        for buff in self.buff1_group:
            if pygame.sprite.collide_mask(self.hero, buff):
                buff.music_get.play()
                if buff.speedy == 1:  # 用速度来区分
                    if self.hero.buff1_num < 6:
                        self.hero.buff1_num += 1
                        self.hero.music_upgrade.play()
                        if self.hero.buff1_num == 5:
                            self.team_show()

                elif buff.speedy==2:#明显炸弹相对屏幕移动，buff1相对屏幕不动
                    self.hero.bomb += 1
                    image = pygame.image.load("./images/bomb.png")
                    self.bombs.append(image)
                elif buff.speedy==3:
                    if self.hero.bar.length < self.hero.bar.weight*self.hero.bar.value:
                        self.hero.bar.length += self.hero.bar.weight*self.hero.bar.value
                        #设计有误，实测发现血量可能会超过能显示的值
                buff.kill()

    def team_show(self):
        self.mate1 = Heromate(-1)
        self.mate2 = Heromate(1)
        self.mate1.image = pygame.image.load("./images/life.png")
        self.mate1.rect = self.mate1.image.get_rect()
        self.mate2.image = pygame.image.load("./images/life.png")
        self.mate2.rect = self.mate2.image.get_rect()
        self.hero_group.add(self.mate1)
        self.hero_group.add(self.mate2)

    # 各种更新
    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.enemy_boom.update()
        self.enemy_boom.draw(self.screen)

        self.heros_update()
        self.hero_group.draw(self.screen)

        for hero in self.hero_group:
            hero.bullets.update()
            hero.bullets.draw(self.screen)

        self.buff1_group.update()
        self.buff1_group.draw(self.screen)

        self.bars_update()
        self.bombs_update()

        self.enemy_bullet_group.update()
        self.enemy_bullet_group.draw(self.screen)

        self.score_show()

    def heros_update(self):
        for hero in self.hero_group:
            if hero.number == 1:
                hero.rect.bottom = self.hero.rect.bottom
                hero.rect.left = self.hero.rect.right
            if hero.number == -1:
                hero.rect.bottom = self.hero.rect.bottom
                hero.rect.right = self.hero.rect.left
            hero.update()

    def bars_update(self):
        for bar in self.bars:
            if bar.length > 0:
                bar.update(self.screen)#传递的参数是画布，即作画背景
            else:
                self.bars.remove(bar)

    def bullet_enemy_update(self):
        for enemy in self.enemy_group:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)

    def bombs_update(self):
        i = 1
        for bomb in self.bombs:
            self.screen.blit(bomb, (0, 700 - (bomb.get_rect().height) * i))
            #存储的炸弹在屏幕上的绘制
            i += 1

    def score_show(self):
        score_font = pygame.font.Font("./STCAIYUN.ttf", 33)#pygame自带的函数，创建字体和大小
        image = score_font.render("SCORE:" + str(int(self.score.getvalue())), True, color_gray)
        #score_font.render(text, antialias, color) 是 Pygame 中用于渲染文本为图像的方法。
        rect = image.get_rect()
        rect.bottom, rect.right = 700, 480
        self.screen.blit(image, rect)
        #self.screen.blit(image, rect) 是将渲染的文本图像绘制到屏幕上的方法。

    # @staticmethod
    #@staticmethod 是 Python 中的一个装饰器，表示该方法是 静态方法。
    #静态方法与实例方法不同，它不需要访问类的实例（不需要 self 参数），可以直接通过类调用。
    #静态方法通常用于执行不依赖于实例属性和方法的功能。它是属于类的，而不是类的实例。
    # def __start__():
    #     # 创建游戏对象
    #     game = PlaneGame()
    #
    #     # 启动游戏
    #     game.start_game()

          #改进
    @staticmethod
    def __start__():
        # 创建游戏对象
        game = PlaneGame()

        # 显示开始界面
        while True:
            game.start_screen.update()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if game.start_screen.event_handler(event):
                    game.start_game()
          #改进





if __name__ == '__main__':
    PlaneGame.__start__()
    #这行代码用于判断当前脚本是否作为主程序运行。__name__ 是一个内置变量，它指示当前模块的名称。
    #如果脚本是被直接运行的（而不是被导入为模块），__name__ 会被设置为 '__main__'，
    # 此时 if 语句为真，程序会执行 PlaneGame.__start__()。
   #如果脚本被导入为模块（而不是直接运行），则 __name__ 不会是 '__main__'，if 语句不执行。

# #2024.12.09


import random
import pygame
pygame.init()
# **************************************************************
# FileName: plane_sprites.py***************************************
# First Author:  Junieson *********************************************
# zhenyuewu0209、jinyunyijiu use for reference
# Version:  2024.12.20 ******************************************
# ****************************************************************
# 分数
kill_stats = {"Enemy1": 0, "Enemy2": 0, "Boss": 0}

SCORE = 0
# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# color
color_blue = (0, 0, 0)
color_green = (0, 0, 0)
color_red = (255, 0, 0)
color_purple = (148, 0, 211)
color_gray = (251, 255, 242)
# 刷新的帧率
FRAME_PER_SEC = 60  # 刷新率是60hz,即每秒update60次
# 创建敌机的定时器常量,自定义用户事件,其实就是int数,不同数表示不同事件
# pygame.USEREVENT 是 Pygame 提供的一个常量，表示用户自定义事件的起始编号，通过加上一个偏移值（如 +1）来避免与系统事件冲突。
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# buff1 出现的事件
BUFF1_SHOW_UP = pygame.USEREVENT + 2
# buff2
BUFF2_SHOW_UP = pygame.USEREVENT + 3
# 敌军发射子弹
ENEMY_FIRE_EVENT = pygame.USEREVENT + 4
# 发射炸弹
BOMB_THROW = pygame.USEREVENT + 5


class GameScore(object):
    global SCORE

    def __init__(self):
        self.score = 0

        pass

    def getvalue(self):
        self.score = SCORE
        return self.score



class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

#若不定义，默认speedy=1，即任何不定义速度的物体会以1在y上变化
    def __init__(self, image_name, speedy=1, speedx=0):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speedy = speedy
        self.speedx = speedx
        self.injury = 1
        self.index = 0  # 记帧数变量
        self.bar = bloodline(color_blue, self.rect.x, self.rect.y - 0, self.rect.width)

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.bar.x = self.rect.x
        self.bar.y = self.rect.y - 10


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Boss(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy3_n1.png", 0, 1)
        self.music_boom = pygame.mixer.Sound("./music/enemy3_down.wav")
        self.music_fly = pygame.mixer.Sound("./music/enemy3_flying.wav")
        self.music_fly.play(-1)
        self.rect.centerx = 240
        self.y = 200
        self.isboom = False
        self.number = 3
        self.index1 = 1  # 控制动画速度
        self.index2 = 0
        self.index3 = 0
        self.index4 = 0
        self.injury = 1
        self.bar = bloodline(color_purple, 0, 0, 480, 8, 200)
        self.bullets = pygame.sprite.Group()

        global kill_stats

    def fire(self):
            for j in range(2, 7):  # 每层5个
                bullet = Bullet(0, 1)
                bullet.injury = 1
                # 2. 设置精灵的位置
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.y = self.rect.bottom
                if j == 2:
                    bullet.speedx = 0
                else:
                    bullet.speedx = (-1) ** j * ((j - 1) // 2) * 1

                self.bullets.add(bullet)

    def update(self):
        # 左右移
        global SCORE
        global kill_stats
        if self.index4 % 2 == 0:  # 降低帧速率,注意这两个指针不能一样
            # 内部为左右移动大概50像素
            if self.index3 % 50 == 0 and (self.index3 // 50) % 2 == 1:
                self.speedx = -self.speedx
            self.rect.x += self.speedx
            self.index3 += 1
        self.index4 += 1

        # 发电动画
        self.image = pygame.image.load("./images/enemy3_n" + str((self.index1 // 6) % 2 + 1) + ".png")#用来切换enemy_n1和_n2两张图片
        self.index1 += 1

        # 爆炸动画
        if self.isboom:
            self.bar.length -= self.injury * self.bar.weight
            if self.bar.length <= 0:  # 此时满足爆炸的条件了
                self.music_fly.stop()
                if self.index2 == 0:
                    self.music_boom.play()
                if self.index2 < 29:  # 4*7+1
                    self.image = pygame.image.load("./images/enemy3_down" + str(self.index2 // 7) + ".png")
                    # 这个地方之所以要整除4是为了减慢爆炸的速度，如果按照update的频率60hz就太快了
                    self.index2 += 1
                else:
                    self.kill()
                    SCORE += self.bar.value
                    # 改进
                    if self.bar.value == 2:
                        kill_stats["Enemy1"] += 1
                    if self.bar.value == 4:
                        kill_stats["Enemy2"] += 1
                    if self.bar.value == 8:
                        kill_stats["Boss"] += 1
                    # 改进
            else:
                self.isboom = False  # 否则还不能死


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self, num=1):
        self.number = num
        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy" + str(num) + ".png")

        # music
        if num == 1:
            self.music_boom = pygame.mixer.Sound("./music/enemy1_down.wav")
        else:
            self.music_boom = pygame.mixer.Sound("./music/enemy2_down.wav")
        # 2. 指定敌机的初始随机速度 1 ~ 3
        self.speedy = random.randint(1, 3)

        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width#敌机也是张方形图片，用屏幕长度减去敌机长度
        self.rect.x = random.randint(0, max_x)

        # 4.爆炸效果
        self.isboom = False
        self.index = 0

        # 5.血条
        if self.number == 1:
            self.bar = bloodline(color_blue, self.rect.x, self.rect.y, self.rect.width)
        else:
            self.bar = bloodline(color_blue, self.rect.x, self.rect.y, self.rect.width, 3, 4)

        # 6,子弹
        self.bullets = pygame.sprite.Group()

        global kill_stats

    def fire(self):
        for i in range(0, 2):
            # 1. 创建子弹精灵
            bullet = Bullet(0, random.randint(self.speedy + 1, self.speedy + 3))
            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.bottom + i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)
#2024.12.4
    def update(self):
        global SCORE
        global kill_stats
        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y > SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()
            self.bar.length = 0

        if self.isboom:
            self.bar.length -= self.bar.weight * self.injury
            if self.bar.length <= 0:
                if self.index == 0:  # 保证只响一次
                    self.music_boom.play()#已经定义过的方法
                if self.index < 17:  # 4*4+1
                    self.image = pygame.image.load(
                        "./images/enemy" + str(self.number) + "_down" + str(self.index // 4) + ".png")
                    # 这个地方之所以要整除4是为了减慢爆炸的速度，如果按照update的频率60hz就太快了
                    self.index += 1
                else:
                    self.kill()
                    SCORE += self.bar.value
                    #改进
                    if self.bar.value == 2:
                        kill_stats["Enemy1"] += 1
                    if self.bar.value == 4:
                        kill_stats["Enemy2"] += 1
                    if self.bar.value == 200:
                        kill_stats["Boss"] += 1
                    # 改进
                    #实际上只用保留对应项就可以，没必要对每个情况都判断，下同

            else:
                self.isboom = False


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1. 调用父类方法，设置image&speed
        super().__init__("./images/me1.png")
        self.music_down = pygame.mixer.Sound("./music/me_down.wav")
        self.music_upgrade = pygame.mixer.Sound("./music/upgrade.wav")
        self.music_degrade = pygame.mixer.Sound("./music/supply.wav")

        self.number = 0#可能用来定义种类
        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120#确实是

        # 3. 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()
        # 4.爆炸
        self.isboom = False
        self.index1 = 1  # 控制动画速度
        self.index2 = 0
        # 5.buff1加成
        self.buff1_num = 0
        # 6,英雄血条
        self.bar = bloodline(color_green, 0, 700, 480, 8, 10)
        # 7，炸弹数目
        self.bomb = 0

    def update(self):

        # 英雄在水平方向移动和血条不同步,特殊
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

        # 英雄喷气动画

        self.image = pygame.image.load("./images/me" + str((self.index1 // 6) % 2 + 1) + ".png")
        self.index1 += 1

        # 英雄爆炸动画
        if self.isboom:
            self.bar.length -= self.injury * self.bar.weight
            if self.bar.length <= 0:  # 此时满足爆炸的条件了
                if self.index2 == 0:
                    self.music_down.play()
                if self.index2 < 17:  # 4*4+1
                    self.image = pygame.image.load("./images/me_destroy_" + str(self.index2 // 4) + ".png")
                    # 这个地方之所以要整除4是为了减慢爆炸的速度，如果按照update的频率60hz就太快了
                    self.index2 += 1
                else:
                    self.kill()
            else:
                self.isboom = False  # 否则还不能死

    # 发射子弹
    def fire(self):
        if self.buff1_num == 0:
            for i in range(0, 1):
                # 1. 创建子弹精灵
                bullet = Bullet()

                # 2. 设置精灵的位置
                bullet.rect.bottom = self.rect.y - i * 20
                bullet.rect.centerx = self.rect.centerx

                # 3. 将精灵添加到精灵组
                self.bullets.add(bullet)
        elif self.buff1_num <= 3:
            for i in (0, 1):#两层
                # 1. 创建子弹精灵
                for j in range(2, self.buff1_num + 3):#每拿一个buff，每层加一个子弹
                    bullet = Bullet(2, -3)
                    # 2. 设置精灵的位置
                    bullet.rect.bottom = self.rect.y - i * 20
                    if (self.buff1_num % 2 == 1):
                        bullet.rect.centerx = self.rect.centerx + (-1) ** j * 15 * (j // 2)
                    if (self.buff1_num % 2 == 0):
                        if j == 2:
                            bullet.rect.centerx = self.rect.centerx
                        else:
                            bullet.rect.centerx = self.rect.centerx + (-1) ** j * 15 * ((j - 1) // 2)
                    # 3. 将精灵添加到精灵组
                    self.bullets.add(bullet)
        elif self.buff1_num >= 4:
            for i in range(0, 1):
                # 1. 表示有几层
                for j in range(2, 5):  # 每层三个

                    bullet = Bullet(3, -3)
                    bullet.injury = 2
                    # 2. 设置精灵的位置
                    bullet.rect.bottom = self.rect.y
                    if j == 2:
                        bullet.rect.centerx = self.rect.centerx
                    else:
                        bullet.rect.centerx = self.rect.centerx + (-1) ** j * (30 + 5 * i)
                        bullet.speedx = (-1) ** j * (i + 1)
                    self.bullets.add(bullet)

#僚机
class Heromate(Hero):
    def __init__(self, num):
        super().__init__()
        self.image = pygame.image.load("./images/life.png")
        self.number = num

    def update(self):

        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        for i in range(0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self, color=1, speedy=-2, speedx=0):
        # 调用父类方法，设置子弹图片，设置初始速度
        self.hity = color  # 子弹伤害值
        self.music_shoot = pygame.mixer.Sound("./music/bullet.wav")
        self.music_shoot.set_volume(0.4)
        if color > 0:  # 只让英雄发子弹响
            self.music_shoot.play()
        super().__init__("./images/bullet" + str(color) + ".png", speedy, speedx)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0 or self.rect.y > 700:
            self.kill()


class Buff1(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet_supply.png", 1)
        self.music_get = pygame.mixer.Sound("./music/get_bullet.wav")
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()


class Buff2(GameSprite):
    def __init__(self):
        super().__init__("./images/bomb_supply.png", 2)
        self.music_get = pygame.mixer.Sound("./music/get_bomb.wav")
        self.rect.bottom = random.randint(0, 700)
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.ran = random.randint(60, 180)  # 在持续1~3s后消失

    def update(self):
        super().update()
        if self.rect.bottom < 0 or self.index == self.ran:
            self.kill()
        self.index += 1

class Buff3(Buff2):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/buff3.png")
        self.speedy=3


class bloodline(object):
    def __init__(self, color, x, y, length, width=2, value=2):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width  # 线宽
        self.value = value * 1.0  # 血量用浮点数
        self.weight = length / value  # 每一滴血表示的距离
        self.color_init = color

    def update(self, canvas):
        if self.length <= self.value * self.weight / 2:
            self.color = color_red
        else:
            self.color = self.color_init
        self.bar_rect = pygame.draw.line(canvas, self.color, (self.x, self.y), (self.x + self.length, self.y),
                                         self.width)

#2024.12.06
class CanvasStart():
    def __init__(self, screen):
        self.img_title = pygame.image.load("./images/title.png")
        self.img_start = pygame.image.load("./images/start.png")
        self.rect_start = self.img_start.get_rect()
        self.rect_title = self.img_title.get_rect()
        self.rect_start.centerx = self.rect_title.centerx = SCREEN_RECT.centerx
        self.rect_title.top = 0
        self.rect_start.top = 550
        self.screen = screen

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect_start.left < pos[0] < self.rect_start.right and \
                    self.rect_start.top < pos[1] < self.rect_start.bottom:
                return True
        return False

    def update(self):
        self.screen.blit(self.img_title, self.rect_title)
        self.screen.blit(self.img_start, self.rect_start)




class CanvasOver():
    def __init__(self, screen):
        self.img_again = pygame.image.load("./images/again.png")
        self.img_over = pygame.image.load("./images/gameover.png")
        self.rect_again = self.img_again.get_rect()
        self.rect_over = self.img_over.get_rect()
        self.rect_again.centerx = self.rect_over.centerx = SCREEN_RECT.centerx
        self.rect_again.bottom = SCREEN_RECT.centery
        self.rect_over.y = self.rect_again.bottom + 20
        self.screen = screen
        global kill_stats

    def event_handler(self, event):
        """处理鼠标点击事件，判断是否点击了重启或退出按钮"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect_again.collidepoint(pos):
                # 点击“重新开始”按钮
                return 1
            elif self.rect_over.collidepoint(pos):
                # 点击“退出”按钮
                return 0

    def update(self):
        self.screen.blit(self.img_again, self.rect_again)
        self.screen.blit(self.img_over, self.rect_over)

        # 显示总分
        score_font = pygame.font.Font("./STCAIYUN.ttf", 50)
        image = score_font.render("SCORE:" + str(int(SCORE)), True, color_gray)
        rect = image.get_rect()
        rect.centerx, rect.bottom = SCREEN_RECT.centerx, self.rect_again.top - 20
        self.screen.blit(image, rect)

        # 显示击杀统计
        stats_font = pygame.font.Font("./STCAIYUN.ttf", 30)
        y_offset = self.rect_again.top - 100
        for enemy_type, count in kill_stats.items():
            stats_image = stats_font.render(f"{enemy_type}: {count}", True, color_gray)
            stats_rect = stats_image.get_rect()
            stats_rect.centerx, stats_rect.top = SCREEN_RECT.centerx, y_offset
            self.screen.blit(stats_image, stats_rect)
            y_offset -= 40

    def set_stats(self, stats):
        global kill_stats
        kill_stats = stats
