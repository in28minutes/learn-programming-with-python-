Last login: Wed May 16 14:30:51 on ttys001
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> number = 5
>>> value = 2.5
>>> type(number)
<class 'int'>
>>> type(5)
<class 'int'>
>>> type(2.5)
<class 'float'>
>>> type(2.55)
<class 'float'>
>>> type(5/2)
<class 'float'>
>>> type(4/2)
<class 'float'>
>>> 4/2
2.0
>>> 1 + 2
3
>>> i = 10
>>> j = 2
>>> i + j
12
>>> i - j
8
>>> i / j
5.0
>>> i * j
20
>>> i % 2
0
>>> value1 = 4.5
>>> value2 = 3.2
>>> value1 + value2
7.7
>>> value1 - value2
1.2999999999999998
>>> value1 / value2
1.40625
>>> value1 % value2
1.2999999999999998
>>> i + value1
14.5
>>> i - value1
5.5
>>> i / value1
2.2222222222222223
>>> 
>>> import os
>>> os.system('clear')

0
>>> i = 1
>>> i = i + 1
>>> i
2
>>> i += 1
>>> i
3
>>> i++
  File "<stdin>", line 1
    i++
      ^
SyntaxError: invalid syntax
>>> ++i
3
>>> i += 1
>>> i
4
>>> i -= 1
>>> i
3
>>> i /= 1
>>> i *= 2
>>> i
6.0
>>> type(i)
<class 'float'>
>>> number1 = 5
>>> number2 = 2
>>> number1/number2
2.5
>>> number1//number2
2
>>> number1 //= 2
>>> number1
2
>>> 5 ** 3
125
>>> pow(5,3)
125
>>> 5.6
5.6
>>> int(5.6)
5
>>> round(5.6)
6
>>> round(5.4)
5
>>> round(5.5)
6
>>> round(5.67, 1)
5.7
>>> round(5.678, 2)
5.68
>>> float(5)
5.0
>>> os.clear('system')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'clear'
>>> os.system('clear')

0
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> is_even = True
>>> is_odd = False
>>> i = 10
>>> i > 15
False
>>> i < 15
True
>>> i >= 15
False
>>> i >= 10
True
>>> i > 10
False
>>> i <= 10
True
>>> i < 10
False
>>> i == 10
True
>>> i == 11
False
>>> os.system('clear')

0
>>> i = 5
>>> if i>3:
...     print(f"{i} is greater than 3")
... 
5 is greater than 3
>>> i = 2
>>> if i>3:
...     print(f"{i} is greater than 3")
... 
>>> if i<10:
...   print(f"{i} is less than 10")
... 
2 is less than 10
>>> i = 15
>>> if i<10:
...   print(f"{i} is less than 10")
... 
>>> if(False):
...   print("False")
... 
>>> if(True):
...   print("True")
... 
True
>>> a = 5
>>> b = 7
>>> if(a>b):
...   print("a is greater than b")
... 
>>> a = 9
>>> if(a>b):
...   print("a is greater than b")
... 
a is greater than b
>>> os.system('clear')

0
>>> a = 1
>>> b = 2
>>> c = 3
>>> d = 5
>>> if a+b > c+d :
...    print("a+b > c +d")
... 
>>> a = 9
>>> if a+b > c+d :
...    print("a+b > c +d")
... 
a+b > c +d
>>> angle1 = 30
>>> angle2 = 20
>>> angle3 = 60
>>> if(angle1 + angle2 + angle3 = 180):
  File "<stdin>", line 1
    if(angle1 + angle2 + angle3 = 180):
                                ^
SyntaxError: invalid syntax
>>> if(angle1 + angle2 + angle3 == 180):
...      print("Valid Triangle")
... 
>>> angle2 = 90
>>> if(angle1 + angle2 + angle3 == 180):
...      print("Valid Triangle")
... 
Valid Triangle
>>> i = 2
>>> if(i%2==0): 
...   print("i is even")
... 
i is even
>>> i = 3
>>> if(i%2==0): 
...   print("i is even")
... 
>>> os.system('clear')

0
>>> True and False
False
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or False
True
>>> False or True
True
>>> True or True
True
>>> False or False
False
>>> not True
False
>>> not(True)
False
>>> not False
True
>>> not(False)
True
>>> True ^ True
False
>>> True ^ False
True
>>> False ^ True
True
>>> False ^ False
False
>>> os.system('clear')

0
>>> i = 10
>>> j = 15
>>> if i%2==0 and j%2==0:
...   print("i and j are even")
... 
>>> j = 14
>>> if i%2==0 and j%2==0:
...   print("i and j are even")
... 
i and j are even
>>> if i%2==0 or j%2==0:
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> if i%2==0 or j%2==0:
...   print("atleast one of i and j are even")
... 
atleast one of i and j are even
>>> i = 15
>>> j
14
>>> if i%2==0 or j%2==0:
...   print("atleast one of i and j are even")
... 
atleast one of i and j are even
>>> j = 23
>>> if i%2==0 or j%2==0:
...   print("atleast one of i and j are even")
... 
>>> i
15
>>> if(True ^ False)
  File "<stdin>", line 1
    if(True ^ False)
                   ^
SyntaxError: invalid syntax
>>> if(True ^ False):
...     print("This will Print")
... 
This will Print
>>> if(False ^ True):
...     print("This will Print")
... 
This will Print
>>> if(True ^ True):
...     print("This will Print")
... 
>>> x = 5
>>> if not x == 6:
...   print("This")
... 
This
>>> x = 6
>>> if not x == 6:
...   print("This")
... 
>>> if x!=6:
...   print("This")
... 
>>> x=5
>>> if x!=6:
...   print("This")
... 
This
>>> if x=6:
  File "<stdin>", line 1
    if x=6:
        ^
SyntaxError: invalid syntax
>>> int(True)
1
>>> int(False)
0
>>> x = -6
>>> if x:
...   print("something")
... 
something
>>> bool(6)
True
>>> bool(-6)
True
>>> bool(0)
False
>>> os.system('clear')

0
>>> i = 2
>>> if i%2 == 0:
...   print("i is even");
... else:
...   print("i is odd");
... 
i is even
>>> i = 3
>>> if i%2 == 0:
...   print("i is even");
... else:
...   print("i is odd");
... 
i is odd
>>> if i==1:
...   print("i is 1")
... elif i==2:
...   print("i is 2")
... else:
...   print("i is not 1 or 2")
... 
i is not 1 or 2
>>> 

