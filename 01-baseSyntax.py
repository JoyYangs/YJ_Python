#!/usr/bin/python
# -*- coding: utf-8 -*-

# 严格区分大小写
# 回车就是行结束，不用加;
# 每行不要超过一定长度：80个字符
# 一条语句可以多行编写，用\表示换行
# 严格缩进和空格
# 注释用#号

# 变量
# python使用变量不需要声明，直接初始化就好
num = 10

'''
# 但是不能不初始化
# print(a) 这句话会报错，因为没有对a进行初始化
# py是一个动态类型的语言，可以为变量赋任意类型的值
# 也可以任意修改变量的值
'''

# 标识符
'''
字母数字下划线，数字不能开头，所有自定义的变量名，函数名，类名等都是标识符
Python支持两种命名规范：下划线和驼峰
'''

# 数据类型
'''
整数，浮点，复数
Python中的数值没有限制，可以无穷大
如果数字过于大，可以用_连接
'''
# c = 123_456_678_333 Py2这里报错了，是因为Python版本的问题

# 字符串
'''
可以用双引号，也可以用单引号，相同引号之间不能互相嵌套
单/双引号不能换行
需要换行的语句后面添加\就可以，但是不会在print中体现出换行
可以用多行注释的三个引号来显示换行的内容
'''

s = '''
天涯何处无芳草
何必单恋一枝花
哈哈哈哈哈哈哈
'''

print(s)

'''
\\
\n
\t
\'
\"
'''

# 格式化字符串输出
a = 'hello'
print(a)
print('a = ' + a)
b = 'world'
print(a + ' ' + b)
# + 前后的类型必须匹配
# 常用的是下面这种：哎呀，这种写法好不习惯~~~
c = 123
print('c = %s'%c)
print('a = %s, b = %s'%(a, b))

'''
%s 
%x,ys 表示最少x位，最多y位
%f
%d
'''
d = f'joye {a} {b}'
print(d)

name = 'joye'
# +拼接
print('hello ' + name + ' welcome')
# %s占位
print('hello %s welcome'%name)
# 多个参数
print('hello ', name, ' welcome')
# f格式化
print(f'hello {name} welcome')

e = 'abcde'
e1 = e * 2
e2 = e * 3
print(e1)
print(e2)

# bool
g1 = True
g2 = False 

# None 空值：表示不存在
h = None 
print(h)

# 类型检查
# type()用来检查变量值的类型
i1 = type(123)
i2 = type('123')

print(i1)
print(i2)
