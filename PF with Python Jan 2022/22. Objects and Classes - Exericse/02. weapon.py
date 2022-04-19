# 2.Weapon
# Create a class Weapon. The __init__ method should receive a number of bullets (integer). Create an attribute called bullets to store that number. The class should also have the following methods:
# shoot()
# oIf there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
# oIf there are no bullets left, return: "no bullets left"
# __repr__()
# oReturns "Remaining bullets: {amount_of_bullets}"
# oYou can read more about the method here: link
#
# Test Code
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
#
# Output
# shooting...
# shooting...
# Remaining bullets: 3
# shooting...
# shooting...
# shooting...
# no bullets left
# Remaining bullets: 0

class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
