# 字典
# 创建字典 {} 或者 dict()
d1 = {}
d2 = dict(name="john", age=16, city="北京")
# 也可以将一个包含双值子序列的列表转换为字典
d3 = dict([("name", "rose"), ("age", 18)])

# len()

# in 和 not in 检查键

# d[key] 这种方式没有找到的时候会报错
# get(key[, default]) get()没有找到的时候不会报错
# d[key] = value 找到的话修改，没有找到的话就添加


# d.setdefault(key, defaultValue) 
# 原本就有这个key就返回key对应的value
# 原本没有这个key就添加这个key并设置value为defaultValue

# d.update(d2) 拼接d2到d中， 如果有重复的元素会被d2的元素替换






# 字典操作 之 删除

# del d[key] 删除这个 key-value ,找不到会报错

# d.popitem() 不能用于删除空字典
# 随机删除一个元素，通常是删除最后一个元素。
# 并返回删除的元素的key-value，作为元组返回 (key, value)

# d.pop(key[,default]) 
# 删除key-value，并且返回删除的元素的value
# 没有找到这个key的时候会报错
# 指定了默认值，找不到的时候就会直接返回默认值不会报错

# d.clear() 清空字典

# d.copy() 分别指向两个对象，一个对象更改不会影响另一个(文件副本的概念，理解理解)
# 浅复制：如果这个对象本身里面还包含对象，包含的对象不会被复制，只会复制这个对象的值
# 相当于最终有两个外层对象，这两个外部对象指向同一个内部对象)



# 字典操作 ：遍历
# d.keys()
for k in d2.keys() :
	print(k)

# d.values()
for v in d2.values() :
	print(v)

# d.items() 返回一个序列，包含双值子序列
for k,v in d2.items() :
	print(k,v)


