# while 条件表达式 :
#    操作语句
# else :
#  print("else中的代码在条件为false的情况下执行")

# i = 0
# while i > 10 :
# 	print(i)
# 	i += 1
# else :
# 	print("else...")

# 1- 100以内奇数和
# i = 1
# sum = 0
# while i < 100 :
# 	sum += i
# 	i += 2
# print("sum = ", sum)

i = 0
sum = 0
while i < 100 :
	i += 1
	if i % 2 != 0 :
		sum += i
print("sum = %d"%sum)

# 2- 100以内7的倍数的和以及个数
count = 0
num = 0
sum1 = 0
while num < 100:
	if num % 7 == 0 :
		sum1 += num
		count += 1
	num += 1
print("100以内7的倍数有 %d 个，他们的和是 %d"%(count, sum1))

# 3- 判断水仙花数
# 水仙花数是指一个 3 位数，
# 它的每个位上的数字的 3次幂之和等于它本身
# 例如：1^3 + 5^3+ 3^3 = 153
i = 100
while i < 1000 :
	# 百位数
	a = i // 100
	# 十位数
	b = i // 10 % 10
	# 个位数
	c = i % 10
	sum = a**3 + b**3 + c**3
	if sum == i :
		print(i)
	i += 1


# print(i // 10 % 10)

# 4- 判断用户输入的是否为质数
num = int(input("请输入一个任意的正整数:"))
i = 2
flag = True

while i < num:
	if num % i == 0 :
		flag = False
	i += 1

if flag :
	print(num, "是质数")
else :
	print(num, "不是质数")



# 5- 99乘法表
i = 1
while i < 10 :
	j = 1
	while j <= i :
		print(j,"*",i,"=",i*j, end='  ')
		j += 1
	print()
	i += 1


# 6- 100以内的质数
i = 2
count = 0
while i < 100000 :
	isZhishu = True
	j = 2
	# 这一步可以大大减少循环次数
	while j <= i ** 0.5:
		count += 1
		if i % j == 0 :
			isZhishu = False
			break
		else :
			j += 1
	if isZhishu :
		print(i, "是质数")
	i += 1

# 2745628
# 315699
print(count)


		

