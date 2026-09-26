class CPU:
    def process(self):
        print("CPU is processing")


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.process()
        print("Computer is running")


computer = Computer()
computer.start()