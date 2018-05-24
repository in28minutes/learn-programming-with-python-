# try:
#     10/0
# except TypeError:
#     print("TypeError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
#
# print("End")

# try:
#     10/0
# except object:
#     print("ZeroDivisionError")
# # catching classes that do not inherit from BaseException is not allowed
# print("End")

# try:
#     10/0
# except BaseException:
#     print("BaseException")
#
# print("End")

# try:
#     10/0
# except Exception:
#     print("Exception")

# try:
#     sum([1, '1'])
# except (ZeroDivisionError, TypeError):
#     print("Exception")
#
# print("End")

# try:
#     sum([1,'1'])
# except (ZeroDivisionError, TypeError):
#     print("Exception")
#
# print("End")

try:
    sum([1,'1'])
except TypeError as error:
    print(error)
print("End")