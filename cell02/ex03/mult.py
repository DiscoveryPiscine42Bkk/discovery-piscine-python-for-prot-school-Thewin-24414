x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
d = x * y

if d > 0:
    print(f"{x} * {y} = {d}")
    print("The result is positive.")
elif d < 0:
    print(f"{x} * {y} = {d}")
    print("The result is negative.")
else:
    print(f"{x} * {y} = {d}")
    print("The result is zero.")

# print(f"{x} * {y} = {d}")