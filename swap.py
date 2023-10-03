# Using XOR
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print(f"number before swapping a= {a} and b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"number after swapping a= {a} and b = {b}")
# using * and /
print(f"number before swapping a= {a} and b = {b}")
a = a*b
b = a/b
a = a/b
print(f"number after swapping a= {a} and b = {b}")
