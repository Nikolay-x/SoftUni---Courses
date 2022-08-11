from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", 2 * capacity, int(0.75 * memory))
