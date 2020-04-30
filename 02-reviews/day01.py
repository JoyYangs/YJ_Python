# 基础语法
# 严格缩进，大小写敏感，不加分号
num = 10
name = "joye"
address = "beijing"
isRunning = True

''' 关于格式化输出
1- f {}
2- %s %d %f % %x,ys(x表示最少位数，y表示最多位数)
3- ,
4- + (+前后必须是同一数据类型)
'''
print(f"{name}")
print("%d"%num)
print("%s %d"%(name, num))
print("num =", num, "name =", name)
print(name + " " + address)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(num + name) 

''' 关于类型检查type()
就是一个type()方法，里面填需要检查的参数就行
'''


''' 关于 list
1- 空list的创建 [] 或者 list()
2- 可以用字符串转换 list("hello")
3- 不支持转换int类型 TypeError: 'int' object is not iterable
4- tuple, dict, set 也都可以转换为list: 
		list(dict)
		list(tuple)
		list(set)
5- 取值：lst[idx]
6- list的切片操作[s:e] [s:e:step] s或者e可以为负数，表示从后往前
'''
lst1 = []
lst2 = list()
lst3 = [1,6,3,9,5,7,4,8,2]
lst4 = ["hello","world","sunny"]
lst5 = list("hello")
# lst6 = list(1234) TypeError: 'int' object is not iterable



''' 关于 tuple
1- 空元祖的创建 () 或者 tuple()
2- list, dict, set 也都可以转换为tuple
3- tuple是不可变对象,元组的值不允许[idx]这种形式的更改，但是可以直接对整个元组进行更改
'''
tup1 = ()
tup2 = (1,2,3)
tup3 = ("yellow","green","pink")
tup4 = tuple()
tup5 = tuple("hello")
tup5 = "name"



''' 关于 dict
1- 空dict的创建{} 或者 dict()
2- dict转set，set里面只会存储dict的key
'''
dic1 = {}
dic11 = dict()
dic2 = {"name":"joye", "age":24, "address":"beijing"}



''' 关于 set
1- 自动去重
2- 空set只能通过set()来创建
3- dict转set，set里面只会存储dict的key
4- 其他类型如字符串，list，tuple转set的话也会自动去重
'''
set1 = set()
set2 = {"name", "age", "address"}
set3 = {1, 3, 5, 7, 9}
set4 = {1,2,2,3,3,3,3,6,6,5,7,7} 
set5 = set(dic2)


'''关于range()
range(s,e,step)
	s 非必填，默认从0开始
	e 必填，截止数字（不包含该数字）也就是range(10)的结果是0~9
	step 非必填，默认为1
只能在循环中使用，直接print(range(10))显示的还是range(0,10)
'''

''' 关于for-in循环
for item in list/tuple/dict/set:
	xxx
'''
for item in range(10):
	print(item)

for item in list("woshilist"):
	print(item)

test_dict = {"name":"joye", "age":24, "address":"beijing"}
for k in test_dict.keys():
	print(k)

for v in test_dict.values():
	print(v)

for k,v in test_dict.items():
	print(k, "==", v)

# tuple() 括号里只能是一个参数
for item in tuple(["yellow","green","pink"]):
	print(item)

# 空格也会被输出
for item in set("hello world"):
	print(item)


''' 关于if-elif-else 和 while
这个感觉没啥好写的呀...
'''

''' 关于方法
定义：
def function_name([形参列表]):
	方法实现


调用：
function_name([实参列表])

参数形式：关键字参数，位置参数
参数的解包和组包 
*a 元组: 接收的是位置参数，可以有多个
**a 字典: 接收的是关键字参数，只能有一个

解包的时候个数要匹配
*a在最前面的话，后面的所有参数都要用关键字参数

'''

def calculate_sum(a, b):
	return a + b

print(calculate_sum(1, 6))

print("*"*20)

def test1(a, b, c):
	print(a)
	print(b)
	print(c)

test1(1,3,5)
test1(a=1,b=2,c=3)
test1(a=5,c=7,b=9)

print("*"*20)

def test2(a, *b, c):
	print(a)
	print(b)
	print(c)
test2(1,3,5,2,4,6,c=0)
test2((1,3,9),5,2,6,4,c=(6,0))

print("*"*20)

def test3(*a, b, c):
	print(a)
	print(b)
	print(c)

test3(1,3,5,7,9,b=0,c=4)

print("*"*20)

def test4(**a):
	print(a)

test4(a=1,b=4,c=6)

print("*"*20)

def test5(a, b, c):
	print(a)
	print(b)
	print(c)

test5_tup = (1,4,7)
test5(*test5_tup)

print("*"*20)

''' 这里注意的两点
1- dict里面的k要用参数的关键字的来命名
test5_dic = {"age":19,"name":"rose","say":"hello"} 这种是错误的
2- dict里面的k-v对的个数要和方法的形参个数保持一致
'''
test5_dic = {"a":19,"b":"34","c":"hello"}
test5(**test5_dic)







