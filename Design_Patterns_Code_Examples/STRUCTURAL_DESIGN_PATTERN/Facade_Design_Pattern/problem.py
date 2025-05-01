# Complex Subsystems
class CPU:
    def freeze(self):
        return "Freezing CPU"

    def jump(self, position):
        return f"Jumping to {position}"

    def execute(self):
        return "Executing instructions"

class Memory:
    def load(self, position, data):
        return f"Loading data '{data}' into memory at position {position}"

class HardDrive:
    def read(self, sector, size):
        return f"Reading {size} bytes from sector {sector}"

# Client has to interact with all components separately
cpu = CPU()
memory = Memory()
hard_drive = HardDrive()

print(cpu.freeze())
print(memory.load(0x00, "OS Boot Loader"))
print(hard_drive.read(0x100, 64))
print(cpu.jump(0x00))
print(cpu.execute())

# Problems:
# 1. The client needs to understand the inner workings of all subsystems.
# 2. Tight coupling: If any subsystem changes, the client must be updated.
# 3. Increased complexity and maintenance effort.
