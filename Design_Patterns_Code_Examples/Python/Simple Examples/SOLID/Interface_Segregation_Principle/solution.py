"""
    Definition: Clients should not be forced to implement interfaces they do not use. Instead, many smaller, specific interfaces are better than a large, general-purpose one.
    Explanation: If a class is forced to implement methods that it doesn't need, it leads to unnecessary complexity and violates ISP. The principle ensures that interfaces are tailored to the specific needs of the clients.
"""

from abc import ABC, abstractmethod
# Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Worker implements both Workable and Eatable
class Worker(Workable, Eatable):
    def work(self):
        return "Working hard"

    def eat(self):
        return "Eating lunch"

# Robot implements only Workable
class Robot(Workable):
    def work(self):
        return "Working efficiently"

# Usage
def perform_work(worker: Workable):
    print(worker.work())

def take_break(worker: Eatable):
    print(worker.eat())

# Example
human_worker = Worker()
robot_worker = Robot()

perform_work(human_worker)  # Output: Working hard
perform_work(robot_worker)  # Output: Working efficiently

take_break(human_worker)    # Output: Eating lunch
# take_break(robot_worker)  # This will throw an error if attempted, as Robot does not implement Eatable
