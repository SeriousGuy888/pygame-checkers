import __main__ as main

def clamp(number, minimum, maximum):
    val = number
    if number < minimum:
        val = minimum
    if number > maximum:
        val = maximum
    return val