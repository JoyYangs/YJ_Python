# 函数：
# 格式：
# def function_name([形参列表]) :
# 	代码块

# 调用语句： function_name([实参列表])

def printHW() :
	print("hello world!")

printHW()

def sum(a, b) :
	print(a+b)

sum(1,3)

def showMsg(user) :
	print(f"欢迎光临！{user}")

showMsg("john")

# 形参默认值
def threeNumberSum(a, b, c = 5) :
	print(a+b+c)

# 位置参数
threeNumberSum(1,2,4)

# 关键字参数
threeNumberSum(b = 1, c = 2, a = 4)

# 位置参数和关键字参数可以混合使用：位置参数必须在前面

# 调用函数的时候，解析器不会检查函数的实参参数类型

# 实参可以是任意类型的对象


# 不定长参数，只能写一个，可以和其他参数配合使用
def unsureLength(*a) :
	print(a)

unsureLength(1,2,3)
unsureLength(1,3,6,9,7,5,8)

# 这种情况下需要对*后面的所有参数使用关键字参数的类型
def func2(a, *b, c, d) :
	print(a, b, c, d)
func2(1,2,3,4,5,6,7,8,c = 9,d = 10)


# 如果*在最前面，后面的每一个参数都要用关键字参数
def func3(*i, a, b) :
	print(a, b)
func3(1,2,3,4,5,a = 9,b = 10)

# *只能接收位置参数

# **a是接收关键字参数，类型是字典
# **参数只能有一个，并只能在最后面
def function4(**a) :
	print(a)

function4(a = 1, b = 3, c = 5)


def func4(a, b, c):
	print(a, b, c)

t = (10, 20, 30)
d = {"a":2,"b":5,"c":7}
# 实参解包,个数要一致
# 对元组解包
func4(*t)
# 对字典解包
func4(**d)



# 函数返回值：要返回什么直接用return xxx;就可以
