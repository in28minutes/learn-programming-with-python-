Last login: Thu May 17 09:41:15 on ttys002
Rangas-MacBook-Pro:~ rangaraokaranam$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> message = "Hello World"
>>> message = 'Hello World'
>>> message = 'Hello World"
  File "<stdin>", line 1
    message = 'Hello World"
                          ^
SyntaxError: EOL while scanning string literal
>>> message = "Hello World"
>>> type(message)
<class 'str'>
>>> message.upper()
'HELLO WORLD'
>>> message.lower()
'hello world'
>>> message = "hello"
>>> message.capitalize()
'Hello'
>>> "hello".capitalize()
'Hello'
>>> 'hello'.capitalize()
'Hello'
>>> 'hello'.islower()
True
>>> 'Hello'.islower()
False
>>> 'Hello'.istitle()
True
>>> 'hello'.istitle()
False
>>> 'hello'.isupper()
False
>>> 'Hello'.isupper()
False
>>> 'HELLO'.isupper()
True
>>> '123'.isdigit()
True
>>> 'A23'.isdigit()
False
>>> '2 3'.isdigit()
False
>>> '23'.isdigit()
True
>>> '23'.isalpha()
False
>>> '2A'.isalpha()
False
>>> 'ABC'.isalpha()
True
>>> 'ABC123'.isalnum()
True
>>> 'ABC 123'.isalnum()
False
>>> 'Hello World'.endswith('World')
True
>>> 'Hello World'.endswith('ld')
True
>>> 'Hello World'.endswith('old')
False
>>> 'Hello World'.endswith('Wo')
False
>>> 'Hello World'.startswith('Wo')
False
>>> 'Hello World'.startswith('He')
True
>>> 'Hello World'.startswith('Hell0')
False
>>> 'Hello World'.startswith('Hello')
True
>>> 'Hello World'.find('Hello')
0
>>> 'Hello World'.find('ello')
1
>>> 'Hello World'.find('Ello')
-1
>>> 'Hello World'.find('bello')
-1
>>> 'Hello World'.find('Ello')
-1
>>> os.system('clear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.system('clear')

0
>>> str(True)
'True'
>>> bool('True')
True
>>> bool('true')
True
>>> bool('tru')
True
>>> bool('false')
True
>>> bool('False')
True
>>> bool('')
False
>>> str(123)
'123'
>>> str(12345)
'12345'
>>> str(12345.45678)
'12345.45678'
>>> int('45')
45
>>> int('45.56')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '45.56'
>>> int('45dfsafk')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '45dfsafk'
>>> int('45abc',16)
285372
>>> int('a',16)
10
>>> int('b',16)
11
>>> int('c',16)
12
>>> int('f',16)
15
>>> int('g',16)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 16: 'g'
>>> float("34.43")
34.43
>>> float("34.43rer")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '34.43rer'
>>> os.system('clear')

0
>>> message = "Hello"
>>> message.upper()
'HELLO'
>>> message
'Hello'
>>> message = message.upper()
>>> message
'HELLO'
>>> message = "Hello"
>>> message.upper()
'HELLO'
>>> message_upper = message.upper()
>>> message = "ABC"
>>> message = message.lowercase()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'lowercase'
>>> message = message.lower()
>>> os.system('clear')


0
>>> message = "Hello World"
>>> message[0]
'H'
>>> type(message[0])
<class 'str'>
>>> type(message)
<class 'str'>
>>> message[0]
'H'
>>> message[1]
'e'
>>> message[2]
'l'
>>> message[3]
'l'
>>> message[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> for ch in message:
...    print(ch)
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
>>> os.system('clear')

0
>>> import string
>>> string.
string.Formatter(       string.ascii_uppercase  string.octdigits
string.Template(        string.capwords(        string.printable
string.ascii_letters    string.digits           string.punctuation
string.ascii_lowercase  string.hexdigits        string.whitespace
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> 'a' in string.ascii_letters
True
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> 'ab' in string.ascii_letters
True
>>> 'abc' in string.ascii_letters
True
>>> 'a' in string.ascii_letters
True
>>> '1' in '13579'
True
>>> '2' in '13579'
False
>>> '4' in '13579'
False
>>> char = 'a'
>>> vowel_string = 'aeiouAEIOU'
>>> char in vowel_string
True
>>> char = 'b'
>>> char in vowel_string
False
>>> vowel_string = 'AEIOU'
>>> char.upper() in vowel_string
False
>>> char = 'a'
>>> char.upper() in vowel_string
True
>>> vowel_string = 'aeiou'
>>> char.lower() in vowel_string
True
>>> char = 'A'
>>> char.lower() in vowel_string
True
>>> import string
>>> string.
string.Formatter(       string.ascii_uppercase  string.octdigits
string.Template(        string.capwords(        string.printable
string.ascii_letters    string.digits           string.punctuation
string.ascii_lowercase  string.hexdigits        string.whitespace
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> for char in string.ascii_uppercase:
...   print(char)
... 
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
>>> for char in string.ascii_lowercase:
...   print(char)
... 
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
>>> for char in string.
string.Formatter(       string.ascii_uppercase  string.octdigits
string.Template(        string.capwords(        string.printable
string.ascii_letters    string.digits           string.punctuation
string.ascii_lowercase  string.hexdigits        string.whitespace
>>> for char in string.digits:
...   print(char)
... 
0
1
2
3
4
5
6
7
8
9
>>> vowel_string = 'aeiou'
>>> char.lower() in vowel_string
False
>>> 'b'.lower() not in vowel_string
True
>>> 'a'.lower() not in vowel_string
False
>>> '1'.lower() not in vowel_string
True
>>> '1'.isalpha() and '1'.lower() not in vowel_string
False
>>> char.isalpha() and char.lower() not in vowel_string
True
>>> char
'b'
>>> char = '1'
>>> char.isalpha() and char.lower() not in vowel_string
False
>>> os.system('clear')

0
>>> string_example = "This is a great thing"
>>> string_example.
string_example.capitalize(    string_example.join(
string_example.casefold(      string_example.ljust(
string_example.center(        string_example.lower(
string_example.count(         string_example.lstrip(
string_example.encode(        string_example.maketrans(
string_example.endswith(      string_example.partition(
string_example.expandtabs(    string_example.replace(
string_example.find(          string_example.rfind(
string_example.format(        string_example.rindex(
string_example.format_map(    string_example.rjust(
string_example.index(         string_example.rpartition(
string_example.isalnum(       string_example.rsplit(
string_example.isalpha(       string_example.rstrip(
string_example.isdecimal(     string_example.split(
string_example.isdigit(       string_example.splitlines(
string_example.isidentifier(  string_example.startswith(
string_example.islower(       string_example.strip(
string_example.isnumeric(     string_example.swapcase(
string_example.isprintable(   string_example.title(
string_example.isspace(       string_example.translate(
string_example.istitle(       string_example.upper(
string_example.isupper(       string_example.zfill(
>>> string_example.split()
['This', 'is', 'a', 'great', 'thing']
>>> for word in string_example.split():
...    print(word)
... 
This
is
a
great
thing
>>> string_example = "This\nis\n\ngreat\nthing"
>>> print(string_example)
This
is

great
thing
>>> string_example = "This\nis\na\ngreat\nthing"
>>> print(string_example)
This
is
a
great
thing
>>> string_example.split
string_example.split(       string_example.splitlines(  
>>> string_example.splitlines()
['This', 'is', 'a', 'great', 'thing']
>>> 1 + 2
3
>>> "1" + "2"
'12'
>>> "1" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> "ABC" + "DEF"
'ABCDEF'
>>> 1 * 20
20
>>> '1' * 20
'11111111111111111111'
>>> 'A' * 10
'AAAAAAAAAA'
>>> str = "test"
>>> str2 = "test1"
>>> str == str2
False
>>> str2 = "test"
>>> str == str2
True
>>> 
