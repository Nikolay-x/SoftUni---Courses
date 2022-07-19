# 4.Entertainment System
# We have been hired to create a game where the player sets up entertainment systems. Each piece of the system (television, game console, etc.) uses a specific cable to connect to another device. The TV uses an HDMI cable to connect to a game console. Both the game console and TV connect to a router via an ethernet cable to access the internet. And lastly, all the devices are connected to the wall via a power cable so they can turn on. Your job is to extend this behavior in the device classes.
# Interface Segregation
#
# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class DVDPlayer(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)

class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device):
        print(f"{self.__class__.__name__} is connected to {device.__class__.__name__} via HDMI cable")

    def connect_to_device_via_rca_cable(self, device):
        print(f"{self.__class__.__name__} is connected to {device.__class__.__name__} via RCA cable")

    def connect_to_device_via_ethernet_cable(self, device):
        print(f"{self.__class__.__name__} is connected to {device.__class__.__name__} via ethernet cable")

    def connect_device_to_power_outlet(self):
        print(f"{self.__class__.__name__} is connected to power outlet via power cable")


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class DVDPlayer(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_rca_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


tv1 = Television()
dvd_player1 = DVDPlayer()
game_console1 = GameConsole()
router1 = Router()

tv1.connect_to_dvd(dvd_player1)
dvd_player1.connect_to_tv(tv1)
print()
tv1.connect_to_game_console(game_console1)
game_console1.connect_to_tv(tv1)
print()
router1.connect_to_tv(tv1)
print()
tv1.plug_in_power()
dvd_player1.plug_in_power()
game_console1.plug_in_power()
router1.plug_in_power()
print()
game_console1.connect_to_router(router1)
router1.connect_to_game_console(game_console1)
