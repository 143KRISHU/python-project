# Identity Operators : is and is not
# if the data is same for the same data type then ->
# The memory manager will reuse the object instead of creating the new object.
# Identity operator is comparing the memory address not the data.
# equality operator == compares the values
# To check the memory address we use id(object) function.
a = 5
b = '5'
print(f"Id of a = {id(a)} Id of b = {id(b)} Hence a is b = {a is b}")
print(f"Id of a = {id(a)} Id of b = {id(b)} Hence a is not b = {a is not b}")
print(a == b)