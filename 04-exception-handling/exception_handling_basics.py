# Open File/Resource

try:
    # Business Logic to read
    i = 0 # Not hardcoded, getting a input from user
    j = 10/i
    values = [1,2]
    sum(values)
except TypeError:
    print("TypeError")
    j = 10
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
except:
    print("OtherError")
    j = 5
else:
    print("Else")
finally:
    # Close
    print("Finally")

print(j)
print("End")