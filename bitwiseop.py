# bitwise operator
a = 15
b = 14
print(f"bitwise and of a and b is = {a & b}")
print(f"bitwise or of a and b is = {a | b}")
print(f"bitwise XOR of a and b is = {a ^ b}")
print(f"bitwise not of b ={~ b} and a = {~a}")
# in left shift we will gain bits : formula = (x<<n) => ans: x*pow(2,n)
print(f"bitwise left shift of a = {a<<2} and b = {b<<2}")
# in right shift we will lose bits : formula = (x>>n) => ans: x/pow(2,n)
print(f"bitwise right shift of a = {a>>1} and b = {b>>2}")