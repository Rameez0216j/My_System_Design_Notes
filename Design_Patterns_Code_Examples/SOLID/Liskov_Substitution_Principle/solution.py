"""
    Definition: Subtypes must be substitutable for their base types without altering the correctness of the program.
    Explanation: If a subclass overrides a method of the base class in a way that breaks the behavior expected from the base class, it violates LSP. This can lead to unexpected errors when the subclass is used in place of the base class.
"""

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "Flying in the sky"

class NonFlyingBird(Bird):
    def move(self):
        return "Walking on the ground"

class Sparrow(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    pass

# Usage
def let_bird_move(bird: Bird):
    print(bird.move())

# Example
sparrow = Sparrow()
let_bird_move(sparrow)  # Output: Flying in the sky

penguin = Penguin()
let_bird_move(penguin)  # Output: Walking on the ground

