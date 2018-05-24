Last login: Sat May 19 09:06:10 on ttys000
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> i = 0
>>> j = 10/i
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 2 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> values = [1,'2']
>>> sum(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> value
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'value' is not defined
>>> values.non_existing
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'non_existing'
>>> values.non_existing()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'non_existing'
>>> import builtins
>>> help(builtins)

>>> help(builtins)

>>> k = 10/non_existing_variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'non_existing_variable' is not defined
>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>     values = [1,'1']
  File "<stdin>", line 1
    values = [1,'1']
    ^
IndentationError: unexpected indent
>>>     sum(values)
  File "<stdin>", line 1
    sum(values)
    ^
IndentationError: unexpected indent
>>> values = [1,'1']
>>> sum(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> import builtins
>>> help(builtins)

>>> 
