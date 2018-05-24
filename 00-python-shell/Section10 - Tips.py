Last login: Sat May 19 09:06:12 on ttys001
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(4.5 - 3.2)
1.2999999999999998
>>> value1 = Decimal('4.5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Decimal' is not defined
>>> import decimal
>>> from decimal import Decimal
>>> value1 = Decimal('4.5')
>>> value2 = Decimal('3.2')
>>> value1 - value2
Decimal('1.3')
>>> import math
>>> math.
math.acos(       math.erf(        math.inf         math.pi
math.acosh(      math.erfc(       math.isclose(    math.pow(
math.asin(       math.exp(        math.isfinite(   math.radians(
math.asinh(      math.expm1(      math.isinf(      math.sin(
math.atan(       math.fabs(       math.isnan(      math.sinh(
math.atan2(      math.factorial(  math.ldexp(      math.sqrt(
math.atanh(      math.floor(      math.lgamma(     math.tan(
math.ceil(       math.fmod(       math.log(        math.tanh(
math.copysign(   math.frexp(      math.log10(      math.tau
math.cos(        math.fsum(       math.log1p(      math.trunc(
math.cosh(       math.gamma(      math.log2(       
math.degrees(    math.gcd(        math.modf(       
math.e           math.hypot(      math.nan         
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> help(math.factorial)

>>> help(math.ceil)

>>> math.ceil(5.5)
6
>>> math.ceil(-5.5)
-5
>>> import os
>>> os.system('clear')

0
>>> import statistics
>>> statistics.
statistics.Decimal(          statistics.mean(
statistics.Fraction(         statistics.median(
statistics.StatisticsError(  statistics.median_grouped(
statistics.bisect_left(      statistics.median_high(
statistics.bisect_right(     statistics.median_low(
statistics.chain(            statistics.mode(
statistics.collections       statistics.numbers
statistics.decimal           statistics.pstdev(
statistics.groupby(          statistics.pvariance(
statistics.harmonic_mean(    statistics.stdev(
statistics.math              statistics.variance(
>>> marks = [1, 6, 9, 23, 2]
>>> statistics.mean(marks)
8.2
>>> statistics.median(marks)
6
>>> marks = [1, 6, 9, 23, 2, 7]
>>> statistics.median(marks)
6.5
>>> statistics.median_high(marks)
7
>>> statistics.median_low(marks)
6
>>> statistics.variance(marks)
63.2
>>> os.system('clear')

0
>>> from collections import deque
>>> queue = deque(['Zero','One','Two'])
>>> queue.pop()
'Two'
>>> queue.append('Three')
>>> queue
deque(['Zero', 'One', 'Three'])
>>> queue.append('Four')
>>> queue.append('Five')
>>> queue.appendLeft('Minus One')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'collections.deque' object has no attribute 'appendLeft'
>>> queue.append
queue.append(      queue.appendleft(  
>>> queue.appendleft('Minus One')
>>> queue
deque(['Minus One', 'Zero', 'One', 'Three', 'Four', 'Five'])
>>> queue.pop()
'Five'
>>> queue.popleft()
'Minus One'
>>> os.system('clear')

0
>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2018, 5, 21, 9, 59, 57, 450683)
>>> today_date = datetime.datetime.today()
>>> today_date
datetime.datetime(2018, 5, 21, 10, 0, 39, 732463)
>>> today_date.year
2018
>>> today_date.month
5
>>> today_date.day
21
>>> today_date.hour
10
>>> today_date.minute
0
>>> today_date.second
39
>>> some_date = datetime.datetime(2019, 5, 27)
>>> some_date
datetime.datetime(2019, 5, 27, 0, 0)
>>> some_date = datetime.datetime(2019, 5, 27, 9, 5,25)
>>> some_date
datetime.datetime(2019, 5, 27, 9, 5, 25)
>>> some_date = datetime.datetime(2019, 5, 27, 9, 5,25, 234567)
>>> some_date
datetime.datetime(2019, 5, 27, 9, 5, 25, 234567)
>>> some_date.date()
datetime.date(2019, 5, 27)
>>> some_date.time()
datetime.time(9, 5, 25, 234567)
>>> some_date
datetime.datetime(2019, 5, 27, 9, 5, 25, 234567)
>>> day = some_date
>>> day
datetime.datetime(2019, 5, 27, 9, 5, 25, 234567)
>>> day + time.timedelta(day=90)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'time' is not defined
>>> day + datetime.timedelta(day=90)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'day' is an invalid keyword argument for this function
>>> day + datetime.timedelta(days=90)
datetime.datetime(2019, 8, 25, 9, 5, 25, 234567)
>>> day
datetime.datetime(2019, 5, 27, 9, 5, 25, 234567)
>>> day + datetime.timedelta(days=90)
datetime.datetime(2019, 8, 25, 9, 5, 25, 234567)
>>> day + datetime.timedelta(weeks=3)
datetime.datetime(2019, 6, 17, 9, 5, 25, 234567)
>>> day + datetime.timedelta(hours=48)
datetime.datetime(2019, 5, 29, 9, 5, 25, 234567)
>>> os.system('clear')

0
>>> import math
>>> math.
math.acos(       math.erf(        math.inf         math.pi
math.acosh(      math.erfc(       math.isclose(    math.pow(
math.asin(       math.exp(        math.isfinite(   math.radians(
math.asinh(      math.expm1(      math.isinf(      math.sin(
math.atan(       math.fabs(       math.isnan(      math.sinh(
math.atan2(      math.factorial(  math.ldexp(      math.sqrt(
math.atanh(      math.floor(      math.lgamma(     math.tan(
math.ceil(       math.fmod(       math.log(        math.tanh(
math.copysign(   math.frexp(      math.log10(      math.tau
math.cos(        math.fsum(       math.log1p(      math.trunc(
math.cosh(       math.gamma(      math.log2(       
math.degrees(    math.gcd(        math.modf(       
math.e           math.hypot(      math.nan         
>>> math.floor(4.5)
4
>>> help(math.floor)

>>> help(math)

>>> 
>>> from math import *
>>> floor(5)
5
>>> gcd(34,56)
2
>>> from math import gcd
>>> gcd(56,68)
4
>>> os.system('clear')





0
>>> numbers = [1,4,6,3,4]
>>> for number in numbers:
...   print(number)
... 
1
4
6
3
4
>>> for index,number in enumerate(numbers):
...    print(f'{index} - {number}')
... 
0 - 1
1 - 4
2 - 6
3 - 3
4 - 4
>>> values = list('aeiou')
>>> values
['a', 'e', 'i', 'o', 'u']
>>> for index, vowel in enumerate(values):
...     printf(f'{index} - {vowel}')
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'printf' is not defined
>>> for index, vowel in enumerate(values):
...     print(f'{index} - {vowel}')
... 
0 - a
1 - e
2 - i
3 - o
4 - u
>>> import os
>>> os.system('clear')

0
>>> number = 5
>>> if(number%2==0):
...   isEven = True
... else:
...   isEven = False
... 
>>> isEven = True if number%2==0 else False
>>> isEven
False
>>> number = 6
>>> isEven = True if number%2==0 else False
>>> isEven
True
>>> isEven = number%2==0
>>> isEven = "Yes" if number%2==0 else "No"
>>> isEven
'Yes'
>>> os.system('clear')



0
>>> a = 1
>>> len(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> type(a)
<class 'int'>
>>> str = "Value"
>>> str.upper()
'VALUE'
>>> a.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'upper'
>>> type(1)
<class 'int'>
>>> type(1.5)
<class 'float'>
>>> type("1.5")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> type(str)
<class 'str'>
>>> str = 1
>>> type(str)
<class 'int'>
>>> str = True
>>> type(str)
<class 'bool'>
>>> str = [1,2]
>>> type(str)
<class 'list'>
>>> os.system('clear')

0
>>> def create_ranga():
...    return 'Ranga',1981,'India'
... 
>>> ranga = create_ranga()
>>> type(ranga)
<class 'tuple'>
>>> name, year, country = ranga
>>> ranga
('Ranga', 1981, 'India')
>>> name
'Ranga'
>>> year
1981
>>> country
'India'
>>> len(ranga)
3
>>> ranga[0]
'Ranga'
>>> ranga[1]
1981
>>> ranga[2]
'India'
>>> ranga[1] = 1991
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> person = ('Ranga', 5, 'India')
>>> person = 'Ranga', 5, 'India'
>>> type(person)
<class 'tuple'>
>>> name, age, country = person
>>> name, age = person
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> x = 0
>>> y = 1
>>> x, y = 0, 1
>>> x, y = y, x
>>> x
1
>>> y
0
>>> x = (0)
>>> type(x)
<class 'int'>
>>> x = (0,)
>>> x = 1,
>>> type(x)
<class 'tuple'>
>>> os.system('clear')










0
>>> 












>>> sum
<built-in function sum>
>>> sum([12,34,56])
102
>>> number1 = 10
>>> number2 = 20
>>> sum = number1 + number2
>>> sum
30
>>> sum([12,34,56])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> sum_ = number1 + number2
>>> del sum
>>> sum
<built-in function sum>
>>> sum([12,34,56])
102
>>> os.system('clear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.system('clear')

0
>>> None
>>> type(None)
<class 'NoneType'>
>>> def email(subject, content, to , cc , bcc): 
...    print(f" {subject}, {content}, {to}, {cc}, "
... )
... 
>>> email("subject", "great work", in28minutes@gmail.com)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'in28minutes' is not defined
>>> email("subject", "great work", "in28minutes@gmail.com")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: email() missing 2 required positional arguments: 'cc' and 'bcc'
>>> def email(subject, content, to , cc=None , bcc=None): 
...    print(f" {subject}, {content}, {to}, {cc}, {bcc}");
... 
>>> email("subject", "great work", "in28minutes@gmail.com")
 subject, great work, in28minutes@gmail.com, None, None
>>> email("subject", "great work", "in28minutes@gmail.com", None, None)
 subject, great work, in28minutes@gmail.com, None, None
>>> email(None, "great work", "in28minutes@gmail.com", None, None)
 None, great work, in28minutes@gmail.com, None, None
>>> var = "123"
>>> if var is None : print ("do something");
... 
>>> var = None
>>> if var is None : print ("do something");
... 
do something
>>> os.system('clear')

0
>>> class Student: pass
... 
>>> student1 = Student()
>>> student2 = Student()
>>> id(student1)
4554811768
>>> id(student2)
4554811992
>>> student1 is student2
False
>>> student3 = student1
>>> id(student3)
4554811768
>>> student1 is student3
True
>>> student1 == student2
False
>>> student1 == student3
True
>>> class Student:
...    def __init__(self, id): 
...        self.id = id
... 
>>> student1 = Student(1)
>>> student2 = Student(2)
>>> student3 = Student(1)
>>> student4 = student1
>>> id(student1)
4554812160
>>> id(student4)
4554812160
>>> student1 is student4
True
>>> student1 is student2
False
>>> student1 is student3
False
>>> student1 == student3
False
>>> class Student:
...    def __init__(self, id):
...       self.id = id
...    def __eq__(self, other):
...       return self.id == other.id
... 
>>> student1 = Student(1)
>>> student2 = Student(2)
>>> student3 = Student(1)
>>> student4 = student1
>>> student4 == student1
True
>>> student2 == student1
False
>>> student3 == student1
True
>>> os.system('clear')

0
>>>  i=1
  File "<stdin>", line 1
    i=1
    ^
IndentationError: unexpected indent
>>>     i=3
  File "<stdin>", line 1
    i=3
    ^
IndentationError: unexpected indent
>>> i=1
>>> if(i==3):
... print('somethin')
  File "<stdin>", line 2
    print('somethin')
        ^
IndentationError: expected an indented block
>>> if(i==3):
...   print('something')
...  print('') 
  File "<stdin>", line 3
    print('') 
             ^
IndentationError: unindent does not match any outer indentation level
>>> os.system('clear')

0
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
