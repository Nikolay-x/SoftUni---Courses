from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        obj = PowerHardware(name, capacity, memory)
        System._hardware.append(obj)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        obj = HeavyHardware(name, capacity, memory)
        System._hardware.append(obj)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        obj = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        hardware.install(obj)
        System._software.append(obj)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        obj = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        hardware.install(obj)
        System._software.append(obj)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware_by_name(hardware_name)
        software = System.find_software_by_name(software_name)
        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / " \
                  f"{sum([h.memory for h in System._hardware])}\n"
        result += f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / " \
                  f"{sum([h.capacity for h in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: " \
                      f"{len([es for es in h.software_components if es.software_type == 'Express'])}\n"
            result += f"Light Software Components: " \
                      f"{len([ls for ls in h.software_components if ls.software_type == 'Light'])}\n"
            result += f"Memory Usage: {h.used_memory} / {h.memory}\n"
            result += f"Capacity Usage: {h.used_capacity} / {h.capacity}\n"
            result += f"Type: {h.hardware_type}\n"
            if h.software_components:
                result += f"Software Components: {', '.join(s.name for s in h.software_components)}\n"
            else:
                result += f"Software Components: None\n"

        return result.strip()

    @staticmethod
    def find_hardware_by_name(name):
        for h in System._hardware:
            if h.name == name:
                return h
        return None

    @staticmethod
    def find_software_by_name(name):
        for s in System._software:
            if s.name == name:
                return s
        return None
