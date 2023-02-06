value = int(input("Enter a number: "))

if value % 5 == 0 and value % 3 == 0:
    print("Fizz-buzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)
