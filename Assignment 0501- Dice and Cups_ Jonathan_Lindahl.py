# Jonathan Lindahl
# 2/16/2024
# Video Link: https://youtu.be/X_uv9fn5DIY
#“I have not given or received any unauthorized assistance on this assignment.

import random

class SixSidedDie(object):
    """A class to represent a six-sided die."""

     

    def __init__(self):
        self.faceValue = None

    def roll(self):
        """Roll the die and return the face value between 1 and 6."""
        self.faceValue = random.randint(1,6)
        return self.faceValue
    

    def getFaceValue(self):
        """Return the last rolled face value of the die."""
        if self.faceValue is not None:
            return self.faceValue
        else:
            return "Please roll the die."

    def __repr__(self):
        if self.faceValue is not None:
            return f'SixSidedDie({self.faceValue})'
        else:
            return 'SixSidedDie(Not yet rolled)'

    

    
class TenSidedDie(SixSidedDie):
    """A class to represent a ten-sided die, inheriting from the SixSidedDie class"""
    def roll(self):
        """Roll the die and return the face value between 1 and 10."""

        self.faceValue = random.randint(1,10)
        return self.faceValue

class TwentySidedDie(SixSidedDie):
    """A class to represent a twenty-sided die, inheriting from the SixSidedDie class."""
    def roll(self):
        """Roll the die and return the face value between 1 and 20."""

        self.faceValue = random.randint(1,20)
        return self.faceValue

class Cup:
    def __init__(self, six=1, ten=1, twenty=1):
        """Initialize the cup with the given number of six, ten, and twenty-sided dice."""

        self.dice = [(SixSidedDie, six), (TenSidedDie, ten), (TwentySidedDie, twenty)]
        self.last_roll = []

    def roll(self):
        """Roll all dice in the cup and return the sum of their face values."""

        self.last_roll = []
        for die_class, quantity in self.dice:
            for _ in range(quantity):
                die = die_class()
                self.last_roll.append(die.roll())
        return sum(self.last_roll)
    
    def getSum(self):
        """Return the sum of the face values from the last roll."""
        return sum(self.last_roll)

    def __repr__(self):
        """Return a string representation of the cup with all dice and their face values."""

        results = []
        # For each die class and quantity pair
        for die_class, quantity in self.dice:
            # Roll the die 'quantity' times and append the results to a list
            for _ in range(quantity):
                die = die_class()
                results.append(f'{die_class.__name__}({die.roll()})')
        return f'Cup({", ".join(results)})'
