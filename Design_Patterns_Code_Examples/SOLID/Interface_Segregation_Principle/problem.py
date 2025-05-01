class WorkerInterface:
    def work(self):
        pass

    def eat(self):
        pass

class Worker(WorkerInterface):
    def work(self):
        return "Working hard"

    def eat(self):
        return "Eating lunch"

class Robot(WorkerInterface):
    def work(self):
        return "Working efficiently"

    def eat(self):
        raise NotImplementedError("Robots don't eat!")

# Issue:
# - The `Robot` class is forced to implement the `eat` method even though it doesn't need it.
# - This violates ISP, as the interface contains methods that are not relevant to all clients.
