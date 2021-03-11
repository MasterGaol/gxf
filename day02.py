# 实现输入10个数字，并打印10个数的求和结果
# a = 0
# sum = 0
# while a < 10:
#     c = int(input("请输入数字："))
#     sum = sum + c
#     a+= 1
# print ("请输入数字：",sum)
# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# i = 1
# sum = 0
# a = 0
# while i <= 10:
#     num = input("请输入数：")
#     num = int(num)
#     if i == 1:
#         a = num
#     if num > a:
#         a = num
#     sum = sum + num
#
#     i = i + 1
# print("最大的数是",a,"10次数据的和：",sum,"平均数是：",(sum / 10))
# 使用random模块，如何产生 50~150之间的数？
# import random
# num = random.randint(1,50)
# print(num)
# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a = int(input("输入第一边："))
# b = int(input("输入第二边："))
# c = int(input("输入第三边："))
#
# if a + b > c and a + c > b and b +c >a:
#     if a ==  b  == c:
#         print("等边三角形！")
#     elif (a == b != c) or (a == c !=  b)  or (b == c  != a):
#         print("等腰三角形！")
#     elif (a *a + b * b == c * c)  or (a * a +  c  * c == b * b) or (b * b  +  c *c == a *a):
#         print("直角三角形！")
#     else:
#         print("普通三角形！")
# else:
#     print("无法形成三角形！")
# 有以下两个数，使用+，-号实现两个数的调换。
# a = 56
# b = 78
# a = a + b # 将和放入a中
# b = a - b # 总和减去b =a ,然后将a赋值b
# a = a - b # 将总和减去b(a) =  b,赋值给a
# print(a,b)
# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# name = "root"
# password = "admin"
#
# i = 1
# while True:
#     if i == 4:
#         print("系统已锁定！")
#         break
#     username = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if name != username or password !=  passwd:
#         print("用户名或密码错误，请重新输入！")
#     else:
#         print("登陆成功！")
#         break
#     i = i + 1
# 编程实现下列图形的打印
# num = int(input("请输入层数："))
# i = 1
# while i <= num:
#
#     # 先打印空格
#     j = 1
#     while  j <= (num - i):
#         print(" ",end="")  # end="" 不换行
#         j =  j + 1
#     # 打印星号
#     k = 1
#     while k <= i:
#         print("* ",end="")
#         k = k +1
#     print() #  换到下一行
#
#     i = i +1
# 编程实现99乘法表的打印
# num = int(input("请输入n层："))
# i = 1
# while i <= num: # 控制整体层数走向
#     # 每一层打印
#     k = 1
#     while k <= i: # 控制每层打印
#         print(k,"x",i,"=",(i*k),"\t",end="")
#         k = k +1
#     print()
#
#     i = i + 1

# 编程实现99乘法表的倒叙打印
# x = 9
# y = 9
# while x >= 1:
#     while y >= 1:
#         print(x,"*",y,"=",x*y)
#         y = y - 1
#     y = 9
#     x = x - 1
#     print("\t")
# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# h = 20
# sum = 0
# day = 0
#
# while True:
#
#     day = day + 1  # 先进来就加1天
#
#     sum = sum + 3 # 白天先爬3米
#     if sum >= h: # 然后判断是否爬出来
#         print("爬出来了")
#         break
#     else: # 没有就下滑2米
#         sum = sum  - 2
# print(day)

# 判断下列变量命名是否合法
# char	√	        Cy%ty	×
# Oax_li	√	    $123	×
# fLul	√	        3_3 	×
# BYTE	√	        T_T	√

# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# i = 1
# sum = 0
# while i <= 6:
#
#     k = 1
#     s = 1
#     while k <= i:
#         s = s * k
#         k = k + 1
#     sum = sum + s
#     i = i + 1
# print("阶乘和：",sum)

# 猜字游戏
# a=0
# import  random
# import  time
# random = random.randint(1,10)
# while True:
#     a+=1
#     num = input("请输入您要猜的数字： ")
#     num = int(num)
#     if num > random:
#         print("大了")
#     elif num < random:
#         print("小了")
#     else:
#         if a<3:
#             a+=1
#             print("真不戳 奖励2000金币")
#             break
#         else:
#             print("已锁定")
#             while 1:
#                 time.sleep(1)
