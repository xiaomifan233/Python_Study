import random

# 1
odd_number = []
while len(odd_number)<10:
    num = random.randint(0,100)
    if num % 2 != 0:
        odd_number.append(num)
print(odd_number)

# 2
Str = 'Ilovepython!'
random_chars = random.sample(Str,4)
print(random_chars)

# 3
colors = ['red','black','blue','while','pink']
random_color = random.choice(colors)
print(random_color)