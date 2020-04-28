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

