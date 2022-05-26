# 7.Square with Maximum Sum
# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
#
# Input
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# Output
# 9 8
# 7 9
# 33

# n, m = [int(x) for x in input().split(", ")]
# matrix = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#
# sums_2_2 = {}
#
# for i in range(n-1):
#     for j in range(m-1):
#         ll = [
#             matrix[i][j], matrix[i][j+1],
#             matrix[i+1][j], matrix[i+1][j+1]
#         ]
#         elements_sum = sum(ll)
#         if elements_sum not in sums_2_2:
#             sums_2_2[elements_sum] = ll
#
# max_sum = max(sums_2_2.keys())
#
# print(sums_2_2[max_sum][0], sums_2_2[max_sum][1])
# print(sums_2_2[max_sum][2], sums_2_2[max_sum][3])
# print(max_sum)

n, m = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

sums_2_2 = {}

for i in range(n-1):
    for j in range(m-1):
        ll = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        elements_sum = sum(ll)
        a = tuple(ll)
        sums_2_2[a] = elements_sum

max_sum = max(sums_2_2.values())
for key in sums_2_2:
    if sums_2_2[key] == max_sum:
        print(key[0], key[1])
        print(key[2], key[3])
        print(max_sum)
        break
