"""
text: "fooziman" output => "foozimaN"
"""


def fn_hack_4():
    """ultima letra en mayuscula"""
    result = "fooziman"
    result = result.replace('n', 'N')
    return result


print(fn_hack_4())
