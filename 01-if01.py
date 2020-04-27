# # 1- 判断一个数字是奇数还是偶数
# num = int(input('请输入一个任意的整数:'))

# if num % 2 == 0 :
# 	print(num, "是偶数")
# else :
# 	print(num, "是奇数")

# # 2- 判断平年闰年
# year = int(input("请输入一个年份:"))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
# 	print(year, "是闰年")
# else :
# 	print(year, "是平年")

# # 3- 判断小狗的年龄相当于人的多少岁
# # 小狗的前两年没一年相当于人类的10.5岁，后面每增加一年就增长4岁
# dog_age = float(input("请输入小狗的年龄:"))
# to_person_age = 0;

# if dog_age < 0:
# 	print("输入不合法！！！")
# elif dog_age <= 2 :
# 	to_person_age = dog_age * 10.5
# else :
# 	to_person_age = (dog_age - 2) * 4 + 2 * 10.5

# print("小狗的年龄是 %s, 相当于为人的年龄: %s"%(dog_age, to_person_age))

# 4- 键盘输入小明的成绩，按分数进行奖励
score = int(input("请输入小明的成绩(0-100):"))

if 0 <= score <= 100:
	if score == 100:
		print("老铁666！王者来一把~")
	elif score > 80:
		print("还不错，继续努力，周末带你去看电影吧")
	elif score > 60:
		print("下次带你吃肯德基~")
	else :
		print("不及格要什么自行车！！")
else:
	print("成绩在(0-100)之间")

# 5- 相亲条件
height = int(input("身高(cm):"))
money = int(input("财富(W):"))
face = int(input("颜值:"))

if height > 180 and money > 1000 and face > 500 :
	print("哈哈哈")
elif height > 180 or money > 1000 or face > 500 :
	print("呵呵呵")
else :
	print("拜拜了您勒")
