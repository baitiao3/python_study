#day5

#空行
#函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

#空行与代码缩进不同，空行并不是Python语法的一部分。
#书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

#记住：空行也是程序代码的一部分。

#等待用户输入

#input("\n\n按下 enter 建退出。")

#import sys;x='runoob';sys.stdout.write(x+"\n")

"""
多个语句构成带民族
if while def class 首行以关键词开始，以冒号（:）结束

子句 clause
"""

'''
实例
'''
'''
if expression:
	suite
elif expression:
	suite
else:
	suite
'''

'''
#Print 输出
x="a"
y="b"
#换行输出
print( x )
print( y )

print("-------")
# 不换行输出 end = " "
print( x, end=" " )
print( y, end=" " )
print()
'''

'''
#import 与 from...import
导入模块
将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *

import sys
print('============Python import mode')
print('命令行参数为:')
for i in sys.argv:
	print (i)
print('\n python 路径为',sys.path)

'''
from sys import argv,path # 导入指定函数

print("=========Python from import====")
print('path:',path)

