"""import random

x = 1
y = 1
for x in range(2):
    print(random.randint(1,6))
#print(random.randint(x,y))"""

#answer:

import random


class Dice:


    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second # be careful here!!!


dice = Dice()
print(dice.roll())

# pep 8 : python enchancement proposal.