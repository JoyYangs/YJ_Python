# 集合：
# 自动去重，无序

# 创建 {} 或者 set()
# 创建空集合：只能用set()
s1 = set()
s2 = {1,3,5,7,9}
s3 = {1,1,1,3,4,4,5,5,7,7,7}

# 用字典的时候只会加入字典的key
s4 = set({"name":"john", "age":16, "address":"beijing"})
print(s4)


# 集合运算： 交并补集
result = s2 & s3
print("result = ", result)

result2 = s3 | s2 
print("result2 = ", result2)

result3 = s3 - s2 
print("result3 = ", result3)

# 只在一个集合中出现的元素
result4 = s3 ^ s2 
print("result4 = ", result4)

# <= 子集：如果a的元素在b中都有，就是b的子集(这里包含a和b相同的情况)
result5 = s2 <= s3 
print("result5 = ", result5)

# < 真子集：不包含a和b相同的情况下的子集
# >= 超集
# > 真超集

