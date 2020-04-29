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