Last login: Fri May 18 14:08:00 on ttys004
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> mark1 = 45
>>> mark2 = 54
>>> mark3 = 80
>>> mark1 + mark2 + mark3
179
>>> (mark1 + mark2 + mark3)/3
59.666666666666664
>>> mark4 = 43
>>> (mark1 + mark2 + mark3 + mark4)/3
74.0
>>> (mark1 + mark2 + mark3 + mark4)/4
55.5
>>> marks = [45, 54, 80]
>>> sum(marks)
179
>>> sum(marks)/len(marks)
59.666666666666664
>>> marks.append(43)
>>> sum(marks)/len(marks)
55.5
>>> type(marks)
<class 'list'>
>>> import os
>>> os.system('clear')

0
>>> marks = [23,56,67]
>>> sum(marks)
146
>>> max(marks)
67
>>> min(marks)
23
>>> len(marks)
3
>>> marks.append(76)
>>> marks
[23, 56, 67, 76]
>>> marks.insert(2, 60)
>>> marks
[23, 56, 60, 67, 76]
>>> marks.remove(60)
>>> 55 in marks
False
>>> 56 in marks
True
>>> marks.index(67)
2
>>> marks
[23, 56, 67, 76]
>>> marks.index(69)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 69 is not in list
>>> for mark in marks:
...   print(mark)
... 
23
56
67
76
>>> os.system('clear')

0
>>> animals = ['Cat', 'Dog','Elephant']
>>> len(animals)
3
>>> sum(animals)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> animals.append('Fish')
>>> animals
['Cat', 'Dog', 'Elephant', 'Fish']
>>> animals.remove('Dog')
>>> animals
['Cat', 'Elephant', 'Fish']
>>> animals[2]
'Fish'
>>> animals[1]
'Elephant'
>>> animals[0]
'Cat'
>>> animals[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> del animals[2]
>>> animals
['Cat', 'Elephant']
>>> animals.extend('Fish')
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h']
>>> animals.append('Fish')
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h', 'Fish']
>>> animals.extend(['Giraffe', 'Horse'])
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h', 'Fish', 'Giraffe', 'Horse']
>>> animals = animals + ['Jackal','Kangaroo']
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h', 'Fish', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo']
>>> animals += ['Lion','Monkey']
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h', 'Fish', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo', 'Lion', 'Monkey']
>>> animals.append(10)
>>> animals
['Cat', 'Elephant', 'F', 'i', 's', 'h', 'Fish', 'Giraffe', 'Horse', 'Jackal', 'Kangaroo', 'Lion', 'Monkey', 10]
>>> os.system('clear')

0
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> len(numbers)
10
>>> number[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number' is not defined
>>> numbers[2]
'Two'
>>> numbers[2:6]
['Two', 'Three', 'Four', 'Five']
>>> numbers[:6]
['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
>>> numbers[3:]
['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
>>> numbers[1:8:2]
['One', 'Three', 'Five', 'Seven']
>>> numbers[1:8:3]
['One', 'Four', 'Seven']
>>> numbers[::3]
['Zero', 'Three', 'Six', 'Nine']
>>> numbers[::-1]
['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
>>> numbers[::-3]
['Nine', 'Six', 'Three', 'Zero']
>>> del numbers[3:]
>>> numbers
['Zero', 'One', 'Two']
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> del numbers[5:7]
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> numbers[3:7] = [3,4,5,6]
>>> numbers
['Zero', 'One', 'Two', 3, 4, 5, 6, 'Seven', 'Eight', 'Nine']
>>> os.system('clear')







0
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> numbers.reverse()
>>> numbers
['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> numbers
['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
>>> reversed(numbers)
<list_reverseiterator object at 0x109560ba8>
>>> for number in reversed(numbers):
...    print(number)
... 
Nine
Eight
Seven
Six
Five
Four
Three
Two
One
Zero
>>> numbers
['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
>>> numbers.sort()
>>> numbers
['Eight', 'Five', 'Four', 'Nine', 'One', 'Seven', 'Six', 'Three', 'Two', 'Zero']
>>> numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
>>> for number in sorted(numbers):
...   print(number)
... 
Eight
Five
Four
Nine
One
Seven
Six
Three
Two
Zero
>>> numbers
['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
>>> for number in sorted(numbers, key=len):
...   print(number)
... 
One
Two
Six
Zero
Four
Five
Nine
Three
Seven
Eight
>>> for number in sorted(numbers, key=len, reverse=True):
...   print(number)
... 
Three
Seven
Eight
Zero
Four
Five
Nine
One
Two
Six
>>> numbers.sort(key=len)
>>> numbers
['One', 'Two', 'Six', 'Zero', 'Four', 'Five', 'Nine', 'Three', 'Seven', 'Eight']
>>> numbers.sort(key=len, reverse=True)
>>> numbers
['Three', 'Seven', 'Eight', 'Zero', 'Four', 'Five', 'Nine', 'One', 'Two', 'Six']
>>> os.system('clear')

0
>>> numbers = []
>>> numbers.append(1)
>>> numbers.append(2)
>>> numbers.append(3)
>>> numbers.append(4)
>>> numbers.pop()
4
>>> numbers
[1, 2, 3]
>>> numbers.pop()
3
>>> numbers
[1, 2]
>>> numbers.append(10)
>>> numbers.pop()
10
>>> numbers
[1, 2]
>>> numbers = []
>>> numbers.append(1)
>>> numbers.append(2)
>>> numbers.append(3)
>>> numbers.append(4)
>>> numbers.pop(0)
1
>>> numbers
[2, 3, 4]
>>> numbers.pop(0)
2
>>> numbers
[3, 4]
>>> numbers.append(10)
>>> numbers.pop(0)
3
>>> numbers.pop(0)
4
>>> numbers.pop(0)
10
>>> numbers
[]
>>> os.system('clear')

0
>>> numbers = ['Zero', 'One','Two','Three','Four','Five','Six','Seven', 'Eight','Nine']
>>> numbers_length_four=[]
>>> for number in numbers:
...    if len(number)== 4:
...      numbers_length_four.append(number)
... 
>>> numbers_length_four
['Zero', 'Four', 'Five', 'Nine']
>>> numbers_length_four = [ number for number in numbers  ]
>>> numbers_length_four
['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
>>> numbers_length_four = [ len(number) for number in numbers  ]
>>> numbers_length_four
[4, 3, 3, 5, 4, 4, 3, 5, 5, 4]
>>> numbers_length_four = [ number.upper() for number in numbers  ]
>>> numbers_length_four
['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
>>> numbers_length_four = [ number for number in numbers if len(number)==4 ]
>>> numbers_length_four
['Zero', 'Four', 'Five', 'Nine']
>>> values = [3, 6, 9, 1, 4, 15, 6, 3]
>>> values_even = [ value for value in values if value%2==0]
>>> values_even
[6, 4, 6]
>>> values_odd = [ value for value in values if value%2==1]
>>> values_odd
[3, 9, 1, 15, 3]
>>> os.system('clear')

0
>>> numbers = [1,2,3,2,1]
>>> numbers
[1, 2, 3, 2, 1]
>>> numbers_set = set(numbers)
>>> numbers_set
{1, 2, 3}
>>> numbers_set.add(3)
>>> numbers_set
{1, 2, 3}
>>> numbers_set.add(4)
>>> numbers_set
{1, 2, 3, 4}
>>> numbers_set.add(0)
>>> numbers_set
{0, 1, 2, 3, 4}
>>> numbers_set.remove(0)
>>> numbers_set
{1, 2, 3, 4}
>>> numbers_set[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> 1 in numbers_set
True
>>> 5 in numbers_set
False
>>> min(numbers_set)
1
>>> max(numbers_set)
4
>>> sum(numbers_set)
10
>>> len(numbers_set)
4
>>> numbers_1_to_5_set = set(range(1,6))
>>> numbers_1_to_5_set
{1, 2, 3, 4, 5}
>>> numbers_4_to_10_set = set(range(4,11))
>>> numbers_4_to_10_set
{4, 5, 6, 7, 8, 9, 10}
>>> numbers_1_to_5_set + numbers_4_to_10_set
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> numbers_1_to_5_set | numbers_4_to_10_set
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> numbers_1_to_5_set & numbers_4_to_10_set
{4, 5}
>>> numbers_1_to_5_set - numbers_4_to_10_set
{1, 2, 3}
>>> numbers_4_to_10_set - numbers_1_to_5_set
{6, 7, 8, 9, 10}
>>> os.system('clear')

0
>>> occurances = dict(a=5 b=6 c=8)
  File "<stdin>", line 1
    occurances = dict(a=5 b=6 c=8)
                          ^
SyntaxError: invalid syntax
>>> occurances = dict(a=5,b=6,c=8)
>>> occurances
{'a': 5, 'b': 6, 'c': 8}
>>> type(occurances)
<class 'dict'>
>>> occurances['d'] = 15
>>> occurances
{'a': 5, 'b': 6, 'c': 8, 'd': 15}
>>> occurances['d'] = 10
>>> occurances
{'a': 5, 'b': 6, 'c': 8, 'd': 10}
>>> occurances['d']
10
>>> occurances['e']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'e'
>>> occurances.get('d')
10
>>> occurances.get('e')
>>> occurances.get('e', 10)
10
>>> occurances
{'a': 5, 'b': 6, 'c': 8, 'd': 10}
>>> occurances.keys()
dict_keys(['a', 'b', 'c', 'd'])
>>> occurances.values()
dict_values([5, 6, 8, 10])
>>> occurances.items()
dict_items([('a', 5), ('b', 6), ('c', 8), ('d', 10)])
>>> for (key,value) in occurances.items():
...    print(f"{key} {value}")
... 
a 5
b 6
c 8
d 10
>>> occurances['a']=0
>>> occurances
{'a': 0, 'b': 6, 'c': 8, 'd': 10}
>>> del occurances['a']
>>> occurances
{'b': 6, 'c': 8, 'd': 10}
>>> os.system('clear'
... )









0
>>> str = "This is an awesome occasion. This has never happened before."
>>> squares_first_ten_numbers = [  i*i for i in range(1,11) ]
>>> type(squares_first_ten_numbers)
<class 'list'>
>>> squares_first_ten_numbers_set = set(squares_of_first_10_numbers)
>>> squares_first_ten_numbers_set = { i*i for i in range(1,11)}
>>> type(squares_first_ten_numbers_set)
<class 'set'>
>>> squares_first_ten_numbers_dict = { i:i*i for i in range(1,11)}
>>> type(squares_first_ten_numbers_dict)
<class 'dict'>
>>> squares_first_ten_numbers_dict
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>> type([])
<class 'list'>
>>> type({})
<class 'dict'>
>>> type(set())
<class 'set'>
>>> type({1})
<class 'set'>
>>> type({'A':5})
<class 'dict'>
>>> type(())
<class 'tuple'>
>>> type((1,2,3))
<class 'tuple'>
>>> 
