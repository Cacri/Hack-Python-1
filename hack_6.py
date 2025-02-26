"""
loop: for [] output => [0,1,2,3,4,5]
"""


def fn_hack_6():
    """loop"""
    result = []
    for i in range(0, 6):
        result.append(i)
    return result


print(fn_hack_6())
