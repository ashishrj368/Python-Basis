from abc import ABC, abstractmethod
class avengers(ABC):
    def strength(self):
        pass

class captain_america(avengers):
    def strength(self):
        print('strength level is 65/100')

class iron_man(avengers):
    def strength(self):
        print("strength level is 75/100")

class thor(avengers):
    def strength(self):
        print('strength level is 95/100')

class hulk(avengers):
    def strength(self):
        print('strength level is 88/100')

c=captain_america()
c.strength()

i=iron_man()
i.strength()

t=thor()
t.strength()

h=hulk()
h.strength()
