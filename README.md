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
首先，在此我们需要再次回顾python、pycharm和anaconda之间的关系。  
* python是开发软件或机器学习等需要使用的一种跨平台的计算机程序语言。  
* PyCharm是一种常用的Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制，简单来说就是将python的各种功能界面化、图形化。  
* Anaconda指的是一个开源的Python发行版本，简单来说anaconda是一个可以定义python版本的虚拟环境构建软件，其本身就包含有部分常用的开发依赖模块，也可以在其中继续更新所需的依赖项。
### 三级标题  
#### 四级标题  
##### 五级标题  
###### 六级标题 
  
