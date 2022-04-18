# 9.* Easter Bread
# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make with the budget you have.
#  First, you will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one bread:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than the price for 1 kg flour. Notice that you need 0.250l milk for one bread, and the calculated price is for 1l.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# For every bread that you make, you will receive 3 colored eggs.
# For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread. The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves – ({current_bread_count} – 2)
# In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have left, formatted to the 2nd decimal place, in the following format:
# "You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."
# Input / Constraints
# On the 1st line, you will receive the budget – a real number in the range [0.0…100000.0]
# On the 2nd line, you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]
# The input will always be in the correct format
# You will always have a remaining budget
# There will not be a case in which the eggs become a negative count
# Output
# In the end, print the number of Easter bread you have made, the colored eggs you have gathered, and the money formatted to the 2nd decimal place in the format described above.
#
# Input
# 20.50
# 1.25
#
# Output
# You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.

budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_l = flour_price_per_kg * 1.25
milk_price_per_bread = milk_price_per_l * 0.25

bread_price = eggs_price_per_pack + flour_price_per_kg + milk_price_per_bread

bread_count = budget // bread_price
colored_eggs_count = 0

for i in range(1, int(bread_count + 1)):
    colored_eggs_count += 3
    if i % 3 == 0:
        colored_eggs_count -= i - 2

print(f"You made {bread_count:.0f} loaves of Easter bread! Now you have {colored_eggs_count} eggs "
      f"and {(budget % bread_price):.2f}BGN left.")
