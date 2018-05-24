Last login: Thu May 17 09:53:08 on ttys002
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
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
>>> for ch in "Hello World":
...   print(ch)
... 
H
e
l
l
o
 
W
o
r
l
d
>>> for word in "Hello World".split():
...   print(word)
... 
Hello
World
>>> for item in (3, 6, 9):
...   print(item)
... 
3
6
9
>>> os.system('clear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.system('clear')

0
>>> i = 5
>>> if i == 5:
...   print("i is 5")
... 
i is 5
>>> i = 0
>>> while i < 5:
...   print(i)
... 
0
0
0
0
0
0
0
0
^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> while i < 5:
...   print(i)
...   i = i + 1
... 
0
1
2
3
4
>>> i = 0
>>> while i < 5:
...   print(i, end=" ")
...   i = i + 1
... 
0 1 2 3 4 >>> for i in range(0,5): print(i)
... 
0
1
2
3
4
>>> os.system('clear')

0
>>> 




















