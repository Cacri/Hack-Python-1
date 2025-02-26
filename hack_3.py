"""
text: "fooziman" output => "Fooziman"
"""


def fn_hack_3():
    """primera letra en mayuscula"""
    result = "fooziman"
    result = result.capitalize()
    return result


print(fn_hack_3())
