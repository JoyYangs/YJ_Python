# 高阶函数: 接收函数作为参数或者将函数作为返回值的函数

# 在Python中函数是一等对象
# 一等对象的特点是：
	# 对象是在运行时创建的
	# 能赋值给变量或者作为数据结构中的元素
	# 能作为参数传递
	# 能作为返回值返回

# 1- 将指定列表中的所有偶数放到新的列表进行返回
l = range(1, 10)

def func1(lst) :
	new_list = []
	for n in lst :
		if n % 2 == 0 :
			new_list.append(n)

	return new_list

print(func1(l))


# sort(key=function) 不会影响原来的列表
# sorted() 对任意类型都可以排序，并且返回一个新对象

# l.sort(key=len) 对l中的元素按照字符长度进行排序
# l.sorted() 



# 闭包：对于一些不希望外部/全局知道的变量，可以用闭包来处理进行隐藏
# 闭包的条件：
# 1- 需要隐藏的变量
# 2- 内部函数用到了这个变量
# 3- 内部函数作为外部函数的返回值返回

def get_average() :
	nums = []
	def inner(n) :
		nums.append(n)
		return sum(nums) / len(nums)
	
	# 这里直接写内部函数的函数名，不要加()
	return inner

average = get_average()
print(average(30))
print(average(10))
print(average(20))
print(average(30))
print(average(50))


