import random
valid = 0
options = ['rock', 'paper', 'scissor']

sides = 3
random_integer = random.randint(0, sides)

while valid == 0:
    user = input('Type P for Paper \nType R for Rock\nOr Type S for Scissors: ')
    if user in ('P', 'S', 'R'):
        valid = 1;
if user = 'P':
    me = options[1]
elif user = 'R':
    me = options[2]
else me = options[3]

pc = options[random_integer]
if pc == 0 and
print('PC rolled a {}'.format(pc))
