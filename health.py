import random

health = 50

difficulty = 3 #easy 1, medium 2, hard 3

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)

