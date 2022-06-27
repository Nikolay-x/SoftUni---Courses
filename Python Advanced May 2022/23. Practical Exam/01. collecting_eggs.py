# 1.Collecting Eggs
# Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.
# On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second line, you will receive another sequence of numbers, each representing a piece of paper with its size.
# You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.
# You should comply with the following conditions:
# If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
# If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
# oOtherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.
# During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him. You should remove this egg from the sequence before it is wrapped with a piece of paper.
# oFurthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to Old MacDonald.
# Note: There will be NO case where there will be just one piece of paper left.
# For more clarification see the examples below.
# Input
# In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
# In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]
# Output
# On the first line:
# oIf you have at least one box filled, print:
# "Great! You filled {total count} boxes."
# oIf you couldn't fill any boxes, print:
# "Sorry! You couldn't fill any boxes!"
# On the following lines, print the eggs left or pieces of paper left if there are any:
# oEggs left: {left eggs joined by ", "}
# oPieces of paper left: {left pieces of paper joined by ", "}
# Constraints
# You will always have at least one egg and at least one piece of paper.
#
# Input
# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9
#
# Output
# Great! You filled 2 boxes.
# Pieces of paper left: 7, 5, 20, 15

from collections import deque

eggs_sizes = deque([int(x) for x in input().split(", ")])
papers_sizes = [int(x) for x in input().split(", ")]
box_size = 50
total_boxes = 0

while eggs_sizes and papers_sizes:
    egg_size = eggs_sizes.popleft()
    paper_size = papers_sizes.pop()

    if egg_size <= 0:
        papers_sizes.append(paper_size)
        continue

    if egg_size == 13:
        papers_sizes.append(paper_size)
        papers_sizes[0], papers_sizes[-1] = papers_sizes[-1], papers_sizes[0]
        continue

    if egg_size + paper_size <= box_size:
        total_boxes += 1
    else:
        continue

if total_boxes > 0:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_sizes:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_sizes])}")
if papers_sizes:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_sizes])}")
