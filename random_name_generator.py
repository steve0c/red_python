import random


instances = input("How many EC2 instances do you want names for?: ")

department = input("What department do you work in?: ")

name = random.choice(department, instances)