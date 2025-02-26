"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""


def fn_hack_10():
    """text: fooziman"""
    text = "fooziman"
    transformaciones = {'f': 'F', 'o': '0', 'i': '1', 'a': '@'}

    result = [transformaciones.get(char, char.upper()) for char in text]

    return result


print(fn_hack_10())
