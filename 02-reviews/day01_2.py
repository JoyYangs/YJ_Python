# 面向对象相关内容

class Person():
	# 一个类只能有一个__init__方法？？
	# def __init__(self, name):
	# 	self.name = name

	# 这些属性需要用下划线！！！
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name
	
	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, age):
		self._age = age

	def _makeMoney(self):
		print("person makeMoney")

	def study(self):
		print(f"{self._name} study")
	


# 继承一下
class Student(Person):

	def __init__(self, name, age, score):
		super().__init__(name, age)
		self._score = score

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, score):
		self._score = score

	def study(self):
		print("student study")
	

if __name__ == "__main__":
	s = Student("mimen", 24, 100)
	s.study()
	print(s.score)
	
	p1 = Person("rose", 23)
	p1._makeMoney()
	p1.study()

	# 调用getter
	print(p1.name)

	# 调用setter
	p1.name = "rosely"

	print(p1.name)

	p2 = Person("john", 25)
	p2._makeMoney()
	p2.study()





