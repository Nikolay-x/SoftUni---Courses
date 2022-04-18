# 3.Word Filter
# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even. Print each word on a new line.
#
# Input
# kiwi orange banana apple
#
# Output
# kiwi
# orange
# banana

text = input().split(" ")
filtered_text = [word for word in text if len(word) % 2 == 0]
for word in filtered_text:
    print(f"{word}")

# result = [word for word in input().split(" ") if len(word) % 2 ==0]
# print("\n".join(result))
