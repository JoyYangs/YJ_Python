# 类的定义：
# class 类名([父类]) :
# 	代码块(成员变量和函数列表)

# 没父类的时候小括号可以省略

class MyClass() :
	pass

class MyClass2() :
	pass

# 实例化
mc_01 = MyClass()
mc_02 = MyClass2()

# <__main__.MyClass object at 0x1067ed590> <class '__main__.MyClass'>
print(mc_01, type(mc_01))

# <class 'type'>
print(type(MyClass))

result1 = isinstance(mc_01, MyClass)
result2 = isinstance(mc_02, MyClass)
print(result1, result2)

print("*"*30)

class Person() :
	print("我是类里面的代码块，我只会在对象创建的时候调用一次")
	# 属性应该是在对象创建的时候直接定义的，不应该按照下面这种方式来定义
	# name = 'john'
	# 属性要通过__init__方法来实现

	# __init__(self)方法在Person()调用的时候就会自动执行
	# 这个__init__(self)方法其实就相当于是JAVA里面的构造器
	def __init__(self, name):
		super().__init__()
		# 属性可以在这里指定
		self.name = name
		print(f"{self} init method {name}")


	# 类里面的方法定义的时候默认要有一个self参数
	# self 就是调用方法的那个对象
	def say_hello(self) :
		print("hello")

	def say_hello2(self) :
		print(f"hello {self.name}")

p1 = Person("john")
p2 = Person("rose")

# print(p1.name)
# print(p2.name)

# p1.name = "rose"
# print(p1.name)

# 属性方法是按照 实例对象-->类对象 的顺序去查找的
# 先找自己有没有，再看类里有没有


p1.say_hello()
p2.say_hello()
p1.say_hello2()
p2.say_hello2()

'''
p1 = Person()的执行顺序：
1- 创建一个变量p1
2- 在内存中创建一个Person类型的对象
3- 调用Person类的__init__(self)方法
4- 将对象的id赋值给变量
'''