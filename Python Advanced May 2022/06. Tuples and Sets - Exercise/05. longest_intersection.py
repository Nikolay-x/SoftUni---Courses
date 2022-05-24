# 5.Longest Intersection
# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
#
# Input
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
#
# Output
# Longest intersection is [6, 7, 8, 9, 10] with length 5

n = int(input())
# intersections = []
longest_intersection = set()

for _ in range(n):

    # set1 = set()
    # set2 = set()
    # sets_borders = input().split("-")
    # start1, end1 = [int(x) for x in sets_borders[0].split(",")]
    # start2, end2 = [int(x) for x in sets_borders[1].split(",")]
    # for i in range(start1, end1 + 1):
    #     set1.add(i)
    # for j in range(start2, end2 + 1):
    #     set2.add(j)
    # result = set1.intersection(set2)
    # intersections.append(result)

    sets_borders = input().split("-")
    start1, end1 = [int(x) for x in sets_borders[0].split(",")]
    start2, end2 = [int(x) for x in sets_borders[1].split(",")]

    set1 = set(range(start1, end1+1))
    set2 = set(range(start2, end2+1))
    current_intersection = set1.intersection(set2)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

# max_length = 0
#
# for i in range(len(intersections)):
#     if len(intersections[i]) > max_length:
#         max_length = len(intersections[i])
#         result_list = intersections[i]


# print(f"Longest intersection is [{', '.join(str(x) for x in result_list)}] with length {max_length}")

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")
