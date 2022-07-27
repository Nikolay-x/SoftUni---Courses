# 3.Bold, Italic, Underline
# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.
#
# Test Code
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
# print(greet("Peter"))
#
# Output
# <b><i><u>Hello, Peter</u></i></b>

def make_bold(func_ref):
    def wrapper(*args):
        return f"<b>{func_ref(*args)}</b>"

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        return f"<i>{func_ref(*args)}</i>"

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        return f"<u>{func_ref(*args)}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet("Peter"))
print(greet_all("Peter", "George"))
