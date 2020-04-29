# 使用封装定义一个类的属性信息

class Dog() :

	def __init__(self, name, age):
		self.hidden_name = name
		self.hidden_age = age
	
	def say_hello(self) :
		print(f"hello 我是 {self.hidden_name}, 我今年 {self.hidden_age} 岁了")

	# 如果希望属性不可见，就不提供getter
	def get_name(self) :
		return self.hidden_name

	# 如果希望属性只读，就不提供setter
	def set_name(self, name) :
		# 这里可以对传过来的数值进行校验保证值的合法性正确性
		self.hidden_name = name

d1 = Dog("wangcai", 3)

d1.say_hello()

d1.set_name("xiaohei")
d1.say_hello()

print("*"*40)

class Cat() :

	# 使用装饰器@property来定义getter和setter的话
	# 需要用 下划线形式 的属性
	def __init__(self, name):
		self._name = name

	# getter方法通过属性的方式来实现
	@property
	def name(self) :
		return self._name

	# setter方法通过属性的方式来实现
	@name.setter
	def name(self, name) :
		self._name = name

	
c1 = Cat("芒果")

# getter
print(c1.name)

c1.name = "坚果"
print(c1.name)


# 通过super()返回的对象调用父类的方法的时候不需要self这个参数
# super().__init__(self, name)

# 类名.__bases__ 获取当前类的所有父类

# 多重继承 : a同时继承b和c
# class A(B, C) :
# 	xxx