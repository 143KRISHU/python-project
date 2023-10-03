# # taking single input by type casting
# # input function always takes input in the form of string.
name = input("Enter your name\t")
age = int(input("enter your age\t"))
salary = float(input("enter your salary\t"))
print(f"name data type={type(name)}, age datatype={type(age)}")
print(f"Name is {name}, age is {age} and salary is {salary}")
#
# # taking multiple input at a same time
# # split function convert the multiple input values into a list
# # split (separator,max_split)
city_name = input("enter all city name separate with space").split()
print(city_name)

# taking multiple input at a same time

age1, age2, age3 = (input("enter 3 age  separate with space \n")).split()
age1 = int(age1)    # type casting
print(age1)
print(age2)
print(age3)
print(type(age1))
