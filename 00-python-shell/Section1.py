Last login: Mon May 14 10:20:03 on ttys002
Rangas-MacBook-Pro:~ rangaraokaranam$ 5 X 5
-bash: 5: command not found
Rangas-MacBook-Pro:~ rangaraokaranam$ clear


















Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 5 X 5
  File "<stdin>", line 1
    5 X 5
      ^
SyntaxError: invalid syntax
>>> 5 * 6
30
>>> 5 + 6
11
>>> 5 - 6
-1
>>> 10 / 2
5.0
>>> 10 ** 3
1000
>>> 5 + 5 + 5
15
>>> 5 + 5 * 5
30
>>> import os
>>> os.system('clear')

0
>>> 24 * 60
1440
>>> 24 * 60 * 60
86400
>>> os.system('clear')
















0
>>> 5 + 6 + 10
21
>>> 5 *$ 2
  File "<stdin>", line 1
    5 *$ 2
       ^
SyntaxError: invalid syntax
>>> 5$2
  File "<stdin>", line 1
    5$2
     ^
SyntaxError: invalid syntax
>>> 5+6+10
21
>>> 5/2
2.5
>>> 5 + 5 * 6
35
>>> 5 - 2 * 2
1
>>> (5 - 2) * 2
6
>>> 5 - ( 2 * 2 )
1
>>> os.system('clear')










0
>>> 5 * 6
30
>>> 5 * 6 = 30
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> 5 * 6
30
>>> Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> print Hello
  File "<stdin>", line 1
    print Hello
              ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(Hello)?
>>> print (Hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> print ("Hello")
Hello
>>> print("Hello")
Hello
>>> print("5 * 6 = 30")
5 * 6 = 30
>>> os.system('clear')

0
>>> print("5 * 6 = 30")
5 * 6 = 30
>>> print("5*6")
5*6
>>> print(5*6)
30
>>> print('5*6')
5*6
>>> abs 10.5
  File "<stdin>", line 1
    abs 10.5
           ^
SyntaxError: invalid syntax
>>> abs(10.5)
10.5
>>> abs("10.5")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
>>> pow 2 5
  File "<stdin>", line 1
    pow 2 5
        ^
SyntaxError: invalid syntax
>>> pow(2 5)
  File "<stdin>", line 1
    pow(2 5)
          ^
SyntaxError: invalid syntax
>>> pow(2, 5)
32
>>> pow(10, 3)
1000
>>> 10 ** 3
1000
>>> max(34, 45, 67)
67
>>> min(34, 45, 67)
34
>>> pow(2,5)
32
>>> Pow(2,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Pow' is not defined
>>> print("Hello")
Hello
>>> print("hello")
hello
>>> print("hellO")
hellO
>>> print ( "hellO" ) 
hellO
>>> print ( "hellO World" ) 
hellO World
>>> print ( "hellO     World" ) 
hellO     World
>>> print("Hello"")
  File "<stdin>", line 1
    print("Hello"")
                  ^
SyntaxError: EOL while scanning string literal
>>> print("Hello\"")
Hello"
>>> print("Hello\nWorld")
Hello
World
>>> print("Hello\tWorld")
Hello	World
>>> print("Hello\\World")
Hello\World
>>> print("Hello\\\\\\World")
Hello\\\World
>>> print('Hello"')
Hello"
>>> print("Hello'World")
Hello'World
>>> print("Hello\"World")
Hello"World
>>> print("Hello\"World")
Hello"World
>>> os.system('clear')

0
>>> print("5 * 6 = 30")
5 * 6 = 30
>>> print("VALUE".format(5*2))
VALUE
>>> print("VALUE {0}".format(5*2))
VALUE 10
>>> print("VALUE {0}".format(10,20,30))
VALUE 10
>>> print("VALUE {1}".format(10,20,30))
VALUE 20
>>> print("VALUE {2}".format(10,20,30))
VALUE 30
>>> print("5 * 6 = {2}".format(5,6,5*6))
5 * 6 = 30
>>> print("{0} * {1} = {2}".format(5,6,5*6))
5 * 6 = 30
>>> print("{0} * {1} = {2}".format(5,7,5*7))
5 * 7 = 35
>>> print("{0} * {1} = {2}".format(5,8,5*8))
5 * 8 = 40
>>> print("{0} * {1} = {2}".format(5,8,5*8))
5 * 8 = 40
>>> print("{0} * {1} = {2}".format(5,8,5*8,5*9,5*10))
5 * 8 = 40
>>> print("{0} * {1} = {4}".format(5,8,5*8,5*9,5*10))
5 * 8 = 50
>>> print("{0} * {1} = {4}".format(5,8))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> print("{0} * {1} = {2}".format(2.5,2,2.5*2))
2.5 * 2 = 5.0
>>> print("My name is {0}".format("Ranga"))
My name is Ranga
>>> os.system('clear')










0
>>> print("{0} * {1} = {2}".format(5,7,5*7))
5 * 7 = 35
>>> print("{0} * {1} = {2}".format(5,1,5*1))
5 * 1 = 5
>>> print("{0} * {1} = {2}".format(5,2,5*2))
5 * 2 = 10
>>> print("{0} * {1} = {2}".format(5,3,5*3))
5 * 3 = 15
>>> print("{0} * {1} = {2}".format(5,index,5*index))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'index' is not defined
>>> index = 2
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 2 = 10
>>> index = 3
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 3 = 15
>>> index
3
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 3 = 15
>>> index = 5
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 5 = 25
>>> index = 1
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 1 = 5
>>> index = 2
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 2 = 10
>>> index = 3
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 3 = 15
>>> a = 5
>>> b = 6
>>> c = 7
>>> print("5 + 6 + 7 = 18")
5 + 6 + 7 = 18
>>> print("5 + 6 + 7 = 18".format(a,b,c,a+b+c))
5 + 6 + 7 = 18
>>> print("{0} + {1} + {2} = {3}".format(a,b,c,a+b+c))
5 + 6 + 7 = 18
>>> a = 6
>>> b = 7
>>> c = 8
>>> print("{0} + {1} + {2} = {3}".format(a,b,c,a+b+c))
6 + 7 + 8 = 21
>>> os.system('clear')

0
>>> i = 1
>>> i
1
>>> print(i*2)
2
>>> i = 4
>>> print(i*2)
8
>>> count
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> print(count)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> count = 4
>>> print(count)
4
>>> Count
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Count' is not defined
>>> count
4
>>> Count
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Count' is not defined
>>> 1count = 5
  File "<stdin>", line 1
    1count = 5
         ^
SyntaxError: invalid syntax
>>> count = 5
>>> _count = 5
>>> 1count
  File "<stdin>", line 1
    1count
         ^
SyntaxError: invalid syntax
>>> 2count
  File "<stdin>", line 1
    2count
         ^
SyntaxError: invalid syntax
>>> c12345 = 5
>>> os.system('clear')

0
>>> i = 5
>>> j = i
>>> j
5
>>> j = 2 * i
>>> j
10
>>> j = i
>>> j = 2 * i
>>> j = 3 * i
>>> j
15
>>> 5 = j
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> j = 10
>>> j
10
>>> num1 = 5
>>> num2 = 3
>>> sum = num1 + num2
>>> sum
8
>>> a = 5
>>> b = 6
>>> c = 7
>>> sum = a + b + c
>>> sum
18
>>> print("5 + 6 + 7 = 18")
5 + 6 + 7 = 18
>>> print("{0} + {1} + {2} = {3}", a, b, c ,sum)
{0} + {1} + {2} = {3} 5 6 7 18
>>> print("{0} + {1} + {2} = {3}".format(a, b, c ,sum))
5 + 6 + 7 = 18
>>> num1
5
>>> num1 = 10
>>> num1
10
>>> number_1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number_1' is not defined
>>> number_1 = 15
>>> number_1
15
>>> os.system('clear')

0
>>> a = 1
>>> b = 2
>>> c = 3
>>> sum = a + b + c
>>> print("{0} + {1} + {2} = {3}".format(a, b, c ,sum))
1 + 2 + 3 = 6
>>> print(f"")

>>> print(f"value of a is {a}")
value of a is 1
>>> print(f"value of b is {b}")
value of b is 2
>>> print(f"sum of a and b is {a + b}")
sum of a and b is 3
>>> print(f"{a} + {b} + {c} = {sum}")
1 + 2 + 3 = 6
>>> os.system('clear')




0
>>> index = 1
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 1 = 5
>>> index = 2
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 2 = 10
>>> index = 3
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 3 = 15
>>> index = 4
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 4 = 20
>>> index = index + 1
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 5 = 25
>>> index = index + 1
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 6 = 30
>>> index = index + 1
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 7 = 35
>>> os.system('clear')

0
>>> range(1,10)
range(1, 10)
>>> for i in range(1,10):
...   print(i)
... 
1
2
3
4
5
6
7
8
9
>>> print("{0} * {1} = {2}".format(5,index,5*index))
5 * 7 = 35
>>> print(f"{5} * {index} = {5*index}")
5 * 7 = 35
>>> for i in range(1,11):
...   print(f"{i}")
... 
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11):
...   print(f"5 * {i}")
... 
5 * 1
5 * 2
5 * 3
5 * 4
5 * 5
5 * 6
5 * 7
5 * 8
5 * 9
5 * 10
>>> for i in range(1,11):
...   print(f"5 * {i} = {5 * i}")
... 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
>>> 5 * 4 * 50
1000
>>> os.system('clear')

0
>>> for i in range(1,10):
...   print(i)
... 
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10)
  File "<stdin>", line 1
    for i in range(1,10)
                       ^
SyntaxError: invalid syntax
>>> for i in range(1,10):
... print(i)
  File "<stdin>", line 2
    print(i)
        ^
IndentationError: expected an indented block
>>> for i in range(1,10):
...  print(i)
... 
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10):
...  print(i)
...  print(2*i)
... 
1
2
2
4
3
6
4
8
5
10
6
12
7
14
8
16
9
18
>>> for i in range(2,5): print(i)
... 
2
3
4
>>> for i in range(2,5):
...   print(i)
... 
2
3
4
>>> for i in range(2,5):
...     print(i)
... 
2
3
4
>>> for i in range(1,11):
...     print(i)
... 
1
2
3
4
5
6
7
8
9
10
>>> for i in range (1,11,2):
...   print(i)
... 
1
3
5
7
9
>>> for i in range (2,11,2):
...   print(i)
... 
2
4
6
8
10
>>> for i in range (10,0,-1):
...   print(i)
... 
10
9
8
7
6
5
4
3
2
1
>>> for i in range (1,11):
...   print(i * i)
... 
1
4
9
16
25
36
49
64
81
100
>>> for i in range (10,0,-1):
...     print(i*i)
... 
100
81
64
49
36
25
16
9
4
1
>>> for i in range (10,0,-2):
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> for i in range (10,0,-2):
...     print(i*i)
... 
100
64
36
16
4
>>> for i in range(1,11):
...   print(f"5 * {i} = {5 * i}")
... 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
>>> for i in range (1,11):
...   print(f"6 * {i} = {6 * i}")
... 
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
>>> for i in range (1,11):
...   print(f"8 * {i} = {8 * i}")
... 
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
>>> 
