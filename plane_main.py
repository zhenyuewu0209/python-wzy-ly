import sys
import pygame
pygame.init()
from plane_sprites import *
#在 Python 中，from plane_sprites import * 是一种 导入语句，用于从一个模块中导入所有的内容（类、函数、变量等）。
# 具体来说，plane_sprites 是一个 Python 模块或文件，而 * 表示将该模块中所有公开的元素导入到当前的命名空间中。
# **************************************************************

# FileName: plane_main.py***************************************
# Author:  Junieson *********************************************
# Version:  2019.8.12 ******************************************
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









