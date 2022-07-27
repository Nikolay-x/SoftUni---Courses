# 6.HTML Tags
# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with the given tag and return the new result. For more clarification, see the examples below
#
# Test Code
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
# print(join_strings("Hello", " you!"))
#
# Output
# <p>Hello you!</p>

def tags(html_tag):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f'<{html_tag}>{result}</{html_tag}>'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


print(join_strings("Hello", " you!"))
print(to_upper('hello'))
