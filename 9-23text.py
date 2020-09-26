# class Student():
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def get_name(self):
#         return (str(self.name))
#     def get_age(self):
#         return (int(self.age))
#     def get_course(self):
#         return sorted(self.grade,reverse=True )
#
# if __name__ == '__main__':
#     student1=Student("张",25,{21,121,31})
#     print(student1.get_name())
#     print(student1.get_age())
#     print(student1.get_course())

# class Ticket:
#     def __init__(self,price=100):
#         self.price = price
#     def cost_ticket(self):#统计票价
#         day = int(input("您输入购买的票？1-5和6-7"))
#         man = input("请输入大人的票")
#         child = input("请输入小孩的票")
#         if day in range(1,6):
#             total=int(man)*self.price+int(child)*self.price*0.5
#         elif day in range(6,8):
#             total = int(man) * self.price*1.2 + int(child) * self.price*1.2*0.5
#         else:
#             print("输入的选项不对")
#         return  total
# if __name__ == '__main__':
#     total=Ticket().cost_ticket()
#     print("您需要付款{0}元".format(total))


num=[1,2,3,4]
i=0
for a in num:
    for b in num:
        for c in num:
            if (a!=b) and (b!=c) and (c!=a):
                i+=1
                print(a,b,c)
print('总数是：',i)