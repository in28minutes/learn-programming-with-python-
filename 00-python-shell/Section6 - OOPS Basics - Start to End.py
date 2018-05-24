>>> class Country: 
...     pass
... 
>>> india = Country()
>>> usa = Country()
>>> netherlands = Country()
>>> india.name = 'India'
>>> india.capital = 'New Delhi'
>>> usa.name = 'USA'
>>> usa.capital = 'Washington'
>>> netherlands.name = 'Netherlands'
>>> netherlands.capital = 'Amsterdam'
>>> india.name
'India'
>>> class Planet: pass
... 
>>> earth = Planet()
>>> earth = new Planet()
  File "<stdin>", line 1
    earth = new Planet()
                     ^
SyntaxError: invalid syntax
>>> earth = Planet('Earth')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object() takes no parameters
>>> earth.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Planet' object has no attribute 'name'
>>> earth.name = 'The Earth'
>>> earth.name
'The Earth'
>>> venus = Planet()
>>> venus.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Planet' object has no attribute 'name'
>>> venus.name = 'Venus'
>>> venus.name
'Venus'
>>> venus.do_something()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Planet' object has no attribute 'do_something'
>>> os.system('clear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.system('clear')

0
>>> class Planet:
...    def __init__(): pass
... 
>>> Planet()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes 0 positional arguments but 1 was given
>>> class Planet:
...    def __init__(self): pass
... 
>>> Planet()
<__main__.Planet object at 0x10426bc88>
>>> class Planet:
...    def __init__(self): pass
...    def __init__(self, name): pass
... 
>>> Planet()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'name'
>>> class Planet:
...    def __init__(self, name): pass
...    def __init__(self): pass
... 
>>> Planet()
<__main__.Planet object at 0x10426bdd8>
>>> Planet("Jupiter")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes 1 positional argument but 2 were given
>>> class Planet:
...    def __init__(self, name="Earth"): pass
... 
>>> Planet()
<__main__.Planet object at 0x10426beb8>
>>> Planet("Jupiter")
<__main__.Planet object at 0x10426bef0>
>>> class Planet:
...    def __init__(self, name="Earth"):
...        self.speed = 10
...        self.name = name
...        self.distance_from_sun = 10000
... 
>>> earth = Planet()
>>> earth.name
'Earth'
>>> earth.speed
10
>>> earth.distance_from_sun
10000
>>> os.system('clear')

0
>>> class Planet:
...    def revolve(): pass
... 
>>> earth = Planet()
>>> earth.revolve()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: revolve() takes 0 positional arguments but 1 was given
>>> class Planet:
...    def revolve(self): pass
... 
>>> earth = Planet()
>>> earth.revolve()
Revolve
>>> os.system('clear')















0
>>> 5
5
>>> type(5)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('Hello')
<class 'str'>
>>> 'Hello'.upper()
'HELLO'
>>> type(5.5)
<class 'float'>
>>> def do_something(): pass
... 
>>> do_something
<function do_something at 0x104275488>
>>> def do_something():
...    print("something")
... 
>>> do_something
<function do_something at 0x104275510>
>>> do_something()
something
>>> test = do_something
>>> test
<function do_something at 0x104275510>
>>> test()
something
>>> 



















