''' 异常 '''

'''
try:
	pass

except [异常类型,如NameError]:
	# 这里是捕获指定类型的异常

except :
	# 这里是捕获所有类型的异常

else:
	没错的时候执行

finally:
	# 无论是否出现异常都会执行的代码
'''
# try必须，else可有可无，finally和except至少要有一个


# 异常的传播
# 异常堆栈回溯的话看最后一个就好

''' 
抛出异常
关键字是 raise
语法格式：raise Exception类型
'''

''' 自定义异常： 直接继承Exception类 '''
# class MyException(Exception) :
# 	pass
