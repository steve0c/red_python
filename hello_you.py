# Ask user for name 

name = input("What is your name?: ")

# Ask user for their age

age = input("What is your age?: ")

# Ask them where they live

live = input("Where do you live?: ")

# Ask user what they enjoy 

enjoy =input("What do you enjoy?: ")

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, live, enjoy)

# Print output to screen 
print(output)