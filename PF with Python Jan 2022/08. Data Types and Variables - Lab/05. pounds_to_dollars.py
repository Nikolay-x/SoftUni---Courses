# 5.Pounds to Dollars
# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.
#
# Input
# 80
#
# Output
# 104.800

pounds = int(input())

dollars = pounds * 1.31

print(f"{dollars:.3f}")
