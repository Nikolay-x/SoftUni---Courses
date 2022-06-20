# 01. Ramen Shop
# You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:
# Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.
# Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.
# Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next bowl of ramen.
# Look at the examples provided for a better understanding of the problem.
# Input
# On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a comma ", ".
# On the second line, you will receive integers representing the customers, separated by a single space and a comma ", ".
# Output
# If all customers are served, print: "Great job! You served all the customers."
# oPrint all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of ramen left: {bowls of ramen left}"
# Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
# oPrint all customers left separated by comma and space in the format "Customers left: {customers left}"
#
# Input
# 14, 25, 37, 43, 19
# 58, 23, 37
#
# Output
# Great job! You served all the customers
# Bowls of ramen left: 14, 6

from collections import deque

ramen_bowls = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while ramen_bowls and customers:
    ramen_bowl = ramen_bowls.pop()
    customer = customers.popleft()

    if ramen_bowl == customer:
        continue
    elif ramen_bowl > customer:
        ramen_bowl -= customer
        ramen_bowls.append(ramen_bowl)
    elif ramen_bowl < customer:
        customer -= ramen_bowl
        customers.appendleft(customer)

if not customers and ramen_bowls:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen_bowls])}")
if not ramen_bowls and customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
if not customers and not ramen_bowls:
    print("Great job! You served all the customers.")
