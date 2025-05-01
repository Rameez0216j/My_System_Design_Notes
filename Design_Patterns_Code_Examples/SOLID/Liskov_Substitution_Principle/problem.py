class Bird:
    def fly(self):
        return "Flying in the sky"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")

# Usage
def let_bird_fly(bird: Bird):
    print(bird.fly())

# Issue:
# - While `Sparrow` works fine with the `let_bird_fly` function, passing a `Penguin` will break the code with an exception.
# - The `Penguin` class does not fulfill the expectation that all birds can fly, violating LSP.
