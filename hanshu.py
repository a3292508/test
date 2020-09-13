def Myfirst():
    print("第一个函数")
Myfirst()

def Myfirst2(name):
    print(name+"lin")
Myfirst2("林")

# 定义一个参数，行参，return返回值
def add(num1,num2):
    return (num1+num2)
add(1,2)

# 关键字参数
def add1(name,world):
    print(name+"------>"+world)
print("林","爱")

def add2(*parames,exp=100):
    print("参数的长度是:",len(parames),exp)
    print("第一个参数是",parames[0])
add2(1,2,3,4,5,6,7)


def add3():
    return [1,2.2,'ces']
print(add3())


# 局部变量
def discounts(price,rate):
    final_price=price*rate
    return final_price
olde_prise=float(input("请输入原价:"))
rate=float(input("请输入折扣:"))
new_price=discounts(olde_prise,rate)
print("打折后价格是：",new_price)


