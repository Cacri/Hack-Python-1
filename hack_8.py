"""
list: [1,3,5,7,9] output => [3,5,7]
"""


def fn_hack_8():
    """primos"""
    result = [1, 3, 5, 7, 9]
    primos = []

    for num in result:
        if num > 1:
            primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                primos.append(num)

    return primos


print(fn_hack_8())
