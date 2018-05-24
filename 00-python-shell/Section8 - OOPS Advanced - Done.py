Last login: Fri May 18 15:27:46 on ttys003
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> class Animal:
...   def bark():
...     print("bark")
... 
>>> animal = Animal()
>>> animal.bark()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bark() takes 0 positional arguments but 1 was given
>>> class Animal:
...   def bark(self):
...     print("bark")
... 
>>> animal = Animal()
>>> animal.bark()
bark
>>> class Pet:
...   def bark(self):
...     print("bark")
...   def groom(self):
...     print("groom")
... 
>>> pet = Pet()
>>> pet.bark()
bark
>>> pet.groom()
groom
>>> class Pet(Animal):
...   def groom(self):
...     print("groom")
... 
>>> dog = Pet()
>>> os.system('clear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.system('clear')





0
>>> 




















