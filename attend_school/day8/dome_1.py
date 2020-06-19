#day8

# [] 集合 () 元集 {} 集合 {} 字典

"""
List 集合

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。


"""

# 数组翻转 list[-1::-1]

'''
def reverseWords(input):
	#print(input)
	inputWords = input.split(" ")
	#print(inputWords)
	inputWords = inputWords[-1::-1]
	#print(inputWords)
	
	output = " ".join(inputWords)
	return output

if __name__ == "__main__":
	input = 'I like baitiao'
	rw = reverseWords(input)
	print(rw)
'''
# Tuple (元组)
#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开


teple = ("baitiao",'cloud','train')

#teple[0] = 'baitiao233'

# Set (集合)

a = set('baitiao233')
b = set('baitiao5')

print(a)

print( a - b )

print( a | b )

print( a & b )

print( a ^ b )

# Dictionary (字典)

'''

字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

'''

dict = []

dict['one'] = "1 - baitiao"
dict[2] = "2 - cloud"

"""
Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

函数	描述
int(x [,base])	将x转换为一个整数

float(x)	将x转换到一个浮点数

complex(real [,imag])	创建一个复数

str(x)	将对象 x 转换为字符串

repr(x)	将对象 x 转换为表达式字符串

eval(str)	用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)	将序列 s 转换为一个元组

list(s)	将序列 s 转换为一个列表

set(s)	转换为可变集合

dict(d)	创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s)	转换为不可变集合

chr(x)	将一个整数转换为一个字符

ord(x)	将一个字符转换为它的整数值

hex(x)	将一个整数转换为一个十六进制字符串

oct(x)	将一个整数转换为一个八进制字符串
"""