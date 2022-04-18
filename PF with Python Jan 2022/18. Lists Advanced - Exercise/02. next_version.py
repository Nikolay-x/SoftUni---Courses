# 2.Next Version
# You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.
#
# Input
# 1.2.3
#
# Output
# 1.2.4

def next_version(x):
    int_x = int("".join(x))
    result = ".".join(str(int_x +1))
    return result

current_version = input().split(".")
print(next_version(current_version))

# current_version = input().split(".")
#
# int_current_version = int("".join(current_version))
# next_version = ".".join(str(int_current_version + 1))
#
# print(next_version)
