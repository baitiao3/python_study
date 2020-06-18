#day7
"""
https://www.runoob.com/python3/python3-data-type.html
"""

'''

python 基本数据类型

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。

'''

"""
number = 100		#整型
pia = 3.14 			#浮点
name = "string"		#字符串

#多个变量赋值

a = b = c = 1

print(a)
print(b)
print(c)

a,b,c = 1,3.14,'string'

print(a)
print(b)
print(c)

# 内置的 type() 函数可以用来查询变量所指的对象类型。

a,b,c,d = 110,3.14,True,5+1j
print(type(a),type(b),type(c),type(d))
"""
'''
a=110
isinstance(3.1, float)
'''

'''
str = "baitiao"

print(str[2])
print(str[2:4])
print(str[0:-1])
print(str * 2)
print(str+"233")

print(str + "\n233")
print(str + r"\n233")
'''

#list 列表

list = ['baitiao','could','train'];

tinylist = [110,'警察']

print(list)
print(list[1])
print(list[0:1])
print(list[1:])
print(tinylist * 2)
print(list + tinylist)