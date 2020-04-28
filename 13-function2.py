# 递归函数
# 1- 求任意一个数的任意次方
def fac(n, i) :
	# 递归基：当次方为1的时候停止递归
	if i == 1 :
		return n 

	return n * fac(n, i-1)

print(fac(5, 5))


# 2- 判断字符串是否是回文
def hui_wen(s) :
	# 递归基：当长度为1的时候直接放回True，
	# 当两个字符的时候判断首尾是否相等，
	# 当多个字符的时候依次判断首尾是否相等
	if len(s) < 2 :
		return True
	
	# s[1:-1] 去除字符串s的首尾字符
	return s[0] == s[-1] and hui_wen(s[1:-1])

print(hui_wen("yes"))
print(hui_wen("adbcbda"))
