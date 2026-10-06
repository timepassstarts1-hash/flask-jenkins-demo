a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

lhs = a * (b + c)
rhs = (a * b) + (a * c)

print("\nDistributive Law")
print("LHS = a * (b + c) =", lhs)
print("RHS = (a * b) + (a * c) =", rhs)

if lhs == rhs:
    print("Distributive Law is VERIFIED.")
else:
    print("Distributive Law is NOT VERIFIED.")
