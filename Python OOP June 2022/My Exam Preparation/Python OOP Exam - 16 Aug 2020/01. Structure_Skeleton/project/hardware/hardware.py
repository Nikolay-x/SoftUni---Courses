from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_capacity(self):
        return sum(s.capacity_consumption for s in self.software_components)

    @property
    def used_memory(self):
        return sum(s.memory_consumption for s in self.software_components)

    def install(self, software: Software):
        if self.capacity - self.used_capacity >= software.capacity_consumption \
                and self.memory - self.used_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        result = next((s for s in self.software_components if s.name == software.name), None)
        if result:
            self.software_components.remove(result)
