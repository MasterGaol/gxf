# 1)将中国所有省会城市添加到上述列表中
# a = ["北京","上海","广东"]
# a.extend(["长沙","武汉","南京","成都","贵阳","昆明","南宁","广州","福州","台北","海口","香港","澳门"])
# a.extend(["天津","重庆","哈尔滨","银川","郑州","济南","太原","合肥","长春","沈阳","呼和浩特","石家庄","乌鲁木齐","兰州","南宁","西安"])
#2)广东成为第二大发达城市，将广东排在上海前面
# a.remove("广东")
# a.insert(1,"广东")
# print(a)
#3)这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# GDP = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# a = 0
# b = 0
# while a<=7:
#     b=b+GDP[a]
#     a=a+1
# print(round(b,2)),round(b/8,2)
# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
# cs = 0
# z = 0
# while cs < 8:
#     if a[cs]%5 == 0:
#         z = z + a[cs]
#     cs = cs + 1
# print(z)
#有下列列表，请编程实现列表的数据翻转
# a = [1,2,3,4,5,6,7,8,9]
# b=list(reversed(a))
# print(b)
# 请编程统计列表中的每个数字出现的次数
# a = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# c=1
# while c<=10:
#     print(c,"出现的次数：",a.count(c))
#     c+=1



