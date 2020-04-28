# 列表：list
# 创建列表 用[]
my_list = []
print(type(my_list)) # <class 'list'>

# python列表可以存储任意对象，但通常不这样做

print(len(my_list)) 

# 切片: 不会影响原来的列表
# 列表的索引可以是负数
# 当索引为负数的时候表示从后向前获取数据，-1表示倒数第一个，-2表示倒数第二个

my_list = ['hello', 'world', 'haha', 'hehe', 'www', 'you', 'are']

#包含0不包含4， 4可以理解为长度
print(my_list[0:3]) 

# 不写前面索引表示从1开始
print(my_list[:3])

# 不写后面的索引表示到最后一个
print(my_list[2:])

# 相当于复制了一个my_list
print(my_list[:]) 

# [起始:结束:步长] 步长也可以为负数，表示从后往前取
# 步长不能为0
print(my_list[0::2]) # ['hello', 'haha', 'www', 'are']
print(my_list[::-2]) # ['are', 'www', 'haha', 'hello']

# in 在为True 不在为False
print("you" in my_list) 
print("our" in my_list)

# not in 不在为True 在为False
print("you" not in my_list)
print("our" not in my_list)

# 获取最大最小值
my_list2 = [100,90, 10, 80, 70, 60, 10, 20, 10, 30, 40, 50]
print(min(my_list2))
print(max(my_list2))

# index(value) 获取value在列表中第一次出现的索引
# index(value, start) start表示开始查找的位置
# index(value, start, end) end表示结束查找的位置
# index方法如果找不到就会报错
print(my_list.index('haha'))

# count(value) 方法获取value出现的次数
print(my_list2.count(10))




# 序列：sequence
# 序列用于保存一组有序的数据，元素会按照添加顺序来分配索引
# 序列分为两种
# 可变(list): 序列中的元素可以改变
# 不可变(str, tuple): 序列中的元素不能改变


print("-*"*30)

# 修改列表
list01 = ['hello', 'world', 'haha', 'hehe', 'www', 'you']
list01[0] = 'yellow'
print(list01)

# 删除index=2的元素
del list01[2]
print("修改后: ", list01)

# 通过切片修改列表
# 在给切片进行复制的时候只能使用序列
list01[0:2] = [1, 3]
print("修改后: ", list01)
# 这里切片数量可以和序列数量不一致
# 设置了步长时，切片数量和序列数量要保持一致
list01[0:2] = [1, 3, 5, 7]
print("修改后: ", list01)
list01[0:] = [1, 2, 3, 5]
print("修改后: ", list01)




s = 'my name'
s = list(s) # 将原本的不可变对象s转换为可变对象

# 可变序列的方法
list02 = ['hello', 'world', 'haha', 'hehe', 'www', 'you']
print("修改前: ", list02)
list02.append('queue')
print("修改后: ", list02)

# insert(index, value)
list02.insert(2, 'name')
print("修改后: ", list02)

# extend() 使用新的序列扩展当前序列, 相当于多次调用append(value)
list02.extend(['value1', 'name', 'val3'])
print("修改后: ", list02)
# pop(index) 删除指定索引位置的元素并返回被删除的元素值
# pop() 不写索引的话就删除最后一个元素
print(list02.pop(3))
print("修改后: ", list02)
print(list02.pop())
print("修改后: ", list02)

# remove(value) 删除指定元素值，有多个时候只删除第一个
list02.remove('name')
print("修改后: ", list02)

# reverse()
list02.reverse()
print("修改后: ", list02)

# sort() 默认升序
list02.sort()
print("修改后: ", list02)

# 降序排列
list02.sort(reverse = True)
print("修改后: ", list02)

# list02.clear()
# print("修改后: ", list02)



