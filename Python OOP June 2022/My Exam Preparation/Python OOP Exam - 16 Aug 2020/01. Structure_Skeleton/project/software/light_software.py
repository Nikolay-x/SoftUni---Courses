from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", int(1.5 * capacity_consumption), int(0.5 * memory_consumption))
