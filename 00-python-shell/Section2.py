Last login: Mon May 14 15:45:09 on ttys003
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
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
>>> for i in range (1,11):
...   print(f"7 * {i} = {7 * i}")
... 
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
>>> print_multiplication_table(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_multiplication_table' is not defined
>>> print_multiplication_table(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print_multiplication_table' is not defined
>>> import os
>>> os.system('clear')

0
>>> print("Hello World")
Hello World
>>> print("Hello World")
Hello World
>>> def print_hello_world_twice():
...     print("Hello World")
...     print("Hello World")
... 
>>> print_hello_world_twice
<function print_hello_world_twice at 0x10a71ef28>
>>> print_hello_world_twice()
Hello World
Hello World
>>> print_hello_world_twice()
Hello World
Hello World
>>> def print_hello_world_thrice():
...     print("Hello World")
...     print("Hello World")
...     print("Hello World")
... 
>>> print_hello_world_thrice()
Hello World
Hello World
Hello World
>>> def print_your_progress():
...     print("Statement 1")
...     print("Statement 2")
...     print("Statement 3")
...     print("Statement 4")
... 
>>> print_your_progress()
Statement 1
Statement 2
Statement 3
Statement 4
>>> def print_your_progress():
...     print("Statement 1\nStatement 2\nStatement 3\nStatement 4")
... 
>>> print_your_progress()
Statement 1
Statement 2
Statement 3
Statement 4
>>> os.system('clear')

0
>>> print_hello_world_twice()
Hello World
Hello World
>>> def print_hello_world_twice():
...     print("Hello World")
...     print("Hello World")
... 
>>> os.system('clear')












0
>>> print_hello_world_twice()
Hello World
Hello World
>>> print_hello_world_thrice()
Hello World
Hello World
Hello World
>>> def print_hello_world(no_of_times):
...    print("Hello World")
...    print(no_of_times)
... 
>>> print_hello_world()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_hello_world() missing 1 required positional argument: 'no_of_times'
>>> print_hello_world(5)
Hello World
5
>>> print_hello_world(10)
Hello World
10
>>> print_hello_world(100)
Hello World
100
>>> def print_hello_world(no_of_times):
...    for i in Range(1,10)
  File "<stdin>", line 2
    for i in Range(1,10)
                       ^
SyntaxError: invalid syntax
>>> def print_hello_world(no_of_times):
...    for i in Range(1,10):
...       print("Hello World")
... 
>>> print_hello_world(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in print_hello_world
NameError: name 'Range' is not defined
>>> def print_hello_world(no_of_times):
...    for i in range(1,10):
...       print("Hello World")
... 
>>> print_hello_world(5)
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
>>> def print_hello_world(no_of_times):
...    for i in range(1,no_of_times):
...       print("Hello World")
... 
>>> print_hello_world(5)
Hello World
Hello World
Hello World
Hello World
>>> def print_hello_world(no_of_times):
...    for i in range(1,no_of_times+1):
...       print("Hello World")
... 
>>> print_hello_world(5)
Hello World
Hello World
Hello World
Hello World
Hello World
>>> print_hello_world(7)
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
>>> os.system('clear')

0
>>> def print_numbers(n):
...    for i in range(1, n+1)
  File "<stdin>", line 2
    for i in range(1, n+1)
                         ^
SyntaxError: invalid syntax
>>> def print_numbers(n):
...    for i in range(1, n+1):
...       print(i)
... 
>>> print_numbers(5)
1
2
3
4
5
>>> def print_squares_of_numbers(n):
...    for i in range(1, n+1):
...       print(i*i)
... 
>>> print_squares_of_numbers(5)
1
4
9
16
25
>>> def print_hello_world(no_of_times):
...    for i in range(1,no_of_times+1):
...       print("Hello World")
... 
>>> def print_string(str, no_of_times):
...    for i in range(1,no_of_times+1):
...       print(str)
... 
>>> print_string("Hello World", 3)
Hello World
Hello World
Hello World
>>> print_string("Welcome to Python", 3)
Welcome to Python
Welcome to Python
Welcome to Python
>>> print_string("Welcome to Python")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_string() missing 1 required positional argument: 'no_of_times'
>>> print_string("Welcome to Python", 4)
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
>>> def print_string(str="Hello World", no_of_times=5):
...    for i in range(1,no_of_times+1):
...       print(str)
... 
>>> print_string()
Hello World
Hello World
Hello World
Hello World
Hello World
>>> print_string("Welcome to Python")
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
>>> print_string("Welcome to Python", 8)
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
Welcome to Python
>>> os.system('clear')

0
>>> for i in range (1,11):
...    print(f"8 * {i} = {8 * i}")
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
>>> for i in range (1,11):
...    print(f"7 * {i} = {7 * i}")
... 
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
>>> def print_multiplication_table(table):
...    for i in range(1,11)
  File "<stdin>", line 2
    for i in range(1,11)
                       ^
SyntaxError: invalid syntax
>>> def print_multiplication_table(table):
...    for i in range(1,11):
...       print(f"table * {i} = {table * i}")
... 
>>> print_multiplication_table(7)
table * 1 = 7
table * 2 = 14
table * 3 = 21
table * 4 = 28
table * 5 = 35
table * 6 = 42
table * 7 = 49
table * 8 = 56
table * 9 = 63
table * 10 = 70
>>> def print_multiplication_table(table):
...    for i in range(1,11):
...       print(f"{table} * {i} = {table * i}")
... 
>>> print_multiplication_table(7)
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
>>> def print_multiplication_table(table, start, end):
...    for i in range(start, end+1):
...       print(f"{table} * {i} = {table * i}")
... 
>>> print_multiplication_table(7, 1 , 6)
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
>>> def print_multiplication_table(table, start=1, end=10):
...    for i in range(start, end+1):
...       print(f"{table} * {i} = {table * i}")
... 
>>> print_multiplication_table(7, 1 , 6)
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
>>> print_multiplication_table(7)
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70
>>> os.system('clear')

0
>>> def method_to_understand_indentation():
...     for i in range(1,11) :
...        print(i)
... 
>>> method_to_understand_indentation()
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
>>> def method_to_understand_indentation():
...     for i in range(1,11) :
...        print(i)
...     print(5)
... 
>>> method_to_understand_indentation()
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
5
>>> def method_to_understand_indentation():
...     for i in range(1,11) :
...        print(i)
...        print(5)
... 
>>> method_to_understand_indentation()
1
5
2
5
3
5
4
5
5
5
6
5
7
5
8
5
9
5
10
5
>>> os.system('clear')

0
>>> def print_string(str="Hello World", no_of_times=5):
...     for i in range(1,no_of_times+1):
...        print(str)
... 
>>> print_string()
Hello World
Hello World
Hello World
Hello World
Hello World
>>> print_string(6)
6
6
6
6
6
>>> print_string(no_of_times=6)
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
>>> print_string(7, 8)
7
7
7
7
7
7
7
7
>>> print_string(7.5, 8)
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
>>> print_string(7.5, "eight")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in print_string
TypeError: must be str, not int
>>> print_string(7.5, 8)
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
>>> print_string(7.5, "8")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in print_string
TypeError: must be str, not int
>>> def 1_print():
  File "<stdin>", line 1
    def 1_print():
         ^
SyntaxError: invalid token
>>> def _1print():
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> def _1print():
...   print("test")
... 
>>> for i in range(1,11) 
  File "<stdin>", line 1
    for i in range(1,11) 
                        ^
SyntaxError: invalid syntax
>>> for i in range(1,11):
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
10
>>> def def():
  File "<stdin>", line 1
    def def():
          ^
SyntaxError: invalid syntax
>>> def in():
  File "<stdin>", line 1
    def in():
         ^
SyntaxError: invalid syntax
>>> def for():
  File "<stdin>", line 1
    def for():
          ^
SyntaxError: invalid syntax
>>> os.system('clear')

0
>>> def product_of_two_numbers(a,b)
  File "<stdin>", line 1
    def product_of_two_numbers(a,b)
                                  ^
SyntaxError: invalid syntax
>>> def product_of_two_numbers(a,b):
...     print(a * b)
... 
>>> product_of_two_numbers(1,2)
2
>>> product = product_of_two_numbers(1,2)
2
>>> product
>>> max(1,2,3)
3
>>> max(1,2,3,4)
4
>>> maximum = max(1,2,3,4)
>>> maximum
4
>>> maximum * 5
20
>>> def product_of_two_numbers(a,b):
...      product = a * b;
...      return product
... 
>>> product_of_two_numbers(2,3)
6
>>> product_result = product_of_two_numbers(2,3)
>>> product_result
6
>>> product_result * 10
60
>>> def sum_of_three_numbers(a, b, c)
  File "<stdin>", line 1
    def sum_of_three_numbers(a, b, c)
                                    ^
SyntaxError: invalid syntax
>>> def sum_of_three_numbers(a, b, c):
...     sum = a + b + c
...     return sum
... 
>>> sum_of_three_numbers(1,2,3)
6
>>> something = sum_of_three_numbers(1,2,3)
>>> something * 5
30
>>> def sum_of_three_numbers(a, b, c):
...     return a + b + c
... 
>>> something = sum_of_three_numbers(1,2,3)
>>> something * 5
30
>>> def calculate_third_angle(first, second) :
...     return 180 - ( first + second )
... 
>>> calculate_third_angle(50, 20)
110
>>> 
