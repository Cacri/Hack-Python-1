"""
text: "fooziman" output => "f00z1m@n"
"""


def fn_hack_5():
    """remplazar caracteres"""
    result = "fooziman"
    tabla = str.maketrans("aeiou", "@e10u")
    result = result.translate(tabla)
    return result


print(fn_hack_5())
