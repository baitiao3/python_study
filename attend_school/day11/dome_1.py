#day11

#Python3运算符

'''
算术运算符

+ - * / % ** //

比较关系运算符

== != > < >= <=

赋值运算符

= += -+ /= *= %= **= //= :=

逻辑运算符

and or not

位运算符

& | ^ ~ >> <<

成员运算符

in not in

身份运算符

is is not

运算符优先级
'''

#位运算符

a = 60 #0011 1100

'''
2/60 
2/30 0
2/15 0
2/7  1
2/3  1
2/1  1
  0  1
'''

b = 13 # 0000 1101

'''
2/13 
2/6  1
2/3  0
2/1  1
  0  1
'''

c = 0

c = a & b

## 0011 1100 a
## 0000 1101 b
## 0000 1100 c

print(c) #12 4+8

c = a | b

print(c)

c = a ^ b

print(c)

c = ~a #-x-1

print(c)

c = a << 2

print(c)

c = a >> 2

print(c)

#成员运算符

a = "b"

b = "baitiao"

c = "baitiao"

d = ["baitiao","cloud"]

if(a in b):
	print("baitiao yes")
else:
	print("baitiao no!")

if(a in d):
	print("baitiao yes")
else:
	print("baitiao no!")

a = 20

b = 20

if( a is b ):
	print("yes")
else:
	print("no")

a = 0

if( a is b ):
	print("yes")
else:
	print("no")

a = "20"

if( a is b ):
	print("yes")
else:
	print("no")

c = "20"



if( a is c ):
	print("yes")
else:
	print("no")

d = a

if( d is c ):
	print("yes")
else:
	print("no")
	
