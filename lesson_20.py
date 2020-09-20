class Teacher:
    def __init__(self,name,age):#实例方法
        self.name=name          #把
        self.age=age
        pass

    def coding(self,lines,language='python'):#实例方法
        print (self.name+"会敲{0}代码,写了{1}行代码".format(language,lines))
    def cooking(self,*args):
        for item in args:
            print (self.name+"会做{0}".format(item))
    @classmethod   #类方法
    def swimming(cls):
        print("还要会游泳")
    @staticmethod
    def sing(name):
        print("还要会{0}唱歌".format(name))
    def play_game(self,game_name):
        return ("会玩{0}".format(game_name))
t1=Teacher("花花","22")
t1.coding(100)
t1.cooking('蛋炒饭','小炒肉')
print(t1.play_game("王者荣耀"))
t1.sing("爱在西元前")

#什么时候需要用初始化函数？
#想用就可以用
#如果某个属性值是多个函数共用的，就可以用初始化函数（提高复用性）