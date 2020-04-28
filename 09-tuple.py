# tuple：元组

my_tuple = ()

# 当元组不为空的时候可以省略小括号
my_tuple = 10, 20, 30

# 元组只有一个值的时候，元素值后面要用,
my_tuple2 = 40,
my_tuple3 = (50,)

print(type(my_tuple3))

# 元组解包
a,b,c = my_tuple
print(a, b, c)
# 对元组解包的时候变量数量必须和元组元素数量一致
# 如果是不需要的元素可以用*d来接收
# 不能同时出现两个或多个*
a, b, *c = (10, 20, 40, 60, 80)
print("c = ", c)
a, *b, c = (10, 20, 40, 60, 80)
print("b = ", b)


print("*"*30)
# 可变对象
l1 = [10, 20, 30]
g = l1
l2 = [1, 2, 3]
k = l2

print("before [l1]: ", l1 , id(l1))
print("before [g]: ", g , id(g))

print("---------通过索引方式改变对象的值 ")
# 通过索引方式改变对象的值，会对使用该对象的其他变量也产生影响
l1[0] = 100
print("after l[index] change [l1] :", l1 , id(l1))
print("after l[index] change [g] :", g , id(g))

print()

print("before [l2]: ", l2 , id(l2))
print("before [k]: ", k , id(k))
print("---------直接修改变量 ")
# 直接修改变量l2的值相当于创建了一个新的对象l2, 对原来的k对象的指向没有变化
l2 = [10, 2, 3]
print("after l change [l] :", l2 , id(l2))
print("after l change [k] :", k , id(k))


# == != 比较对象值
# is 和 is not 比较对象id