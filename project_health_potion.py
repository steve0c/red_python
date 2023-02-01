# This is a project creating a health poition for a game 

# import random moudular 

import random

#players beggining health

health = 50

# difficulty mode change number from 1-3 for difficulty level

difficulty = 2

#random health number between 25 and 50 divided by the difficulty which is 2
#int gets rid of the float numbers

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)







