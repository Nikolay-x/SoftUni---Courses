# 7.*Store Results
# Create a class called store_results. It should be used as a decorator and store information about the executed functions in a file called results.txt in the format: "Function {func_name} was add called. Result: {func_result}"
# Note: The solutions to this problem cannot be submitted in the judge system
#
# Test Code
# @store_results
# def add(a, b):
#     return a + b
#
# @store_results
# def mult(a, b):
#     return a * b
#
# add(2, 2)
# mult(6, 4)
#
# results.txt
# Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24

def store_results(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        file_path = "./results.txt"
        with open(file_path, "a") as file:
            file.write(f"Function '{func_ref.__name__}' was called. Result: {result}\n")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
