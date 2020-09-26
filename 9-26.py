#超继成
class Mathmethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print (self.a+self.b)
    def sub(self):
        return  self.a-self.b

class MathMethod_1(Mathmethod):
    def divide(self):#拓展(父类里面没有的)
        return  self.a/self.b
    def add(self): #重写（改掉父类里面的）
        super(MathMethod_1,self).add()#超继承
        print("我是调用子类的方法",self.a+self.b+10)
if __name__ == '__main__':
    MathMethod_1(5,6).add()


