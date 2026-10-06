a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

lhs = (a + b) + c
rhs = a + (b + c)

print("\nLeft Side  ((a+b)+c) =", lhs)
print("Right Side (a+(b+c)) =", rhs)

if lhs == rhs:
    print("Associative Law of Addition is VERIFIED.")
else:
    print("Associative Law of Addition is NOT VERIFIED.")
