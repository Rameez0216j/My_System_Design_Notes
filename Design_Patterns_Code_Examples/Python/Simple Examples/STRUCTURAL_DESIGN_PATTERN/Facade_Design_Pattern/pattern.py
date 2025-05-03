# Facade class simplifies interaction with subsystems
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        steps = [
            self.cpu.freeze(),
            self.memory.load(0x00, "OS Boot Loader"),
            self.hard_drive.read(0x100, 64),
            self.cpu.jump(0x00),
            self.cpu.execute(),
        ]
        return "\n".join(steps)

# Client now interacts with just the Facade
computer = ComputerFacade()
print(computer.start_computer())

# Benefits:
# 1. Simplifies usage by hiding complexity from the client.
# 2. Reduces tight coupling by keeping subsystems separate from the client.
# 3. Improves maintainability by centralizing changes in one place.
