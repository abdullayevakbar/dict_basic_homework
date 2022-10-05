from curses.ascii import isalpha, isdigit


def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    a = b = 0
    for i in txt:
        if isalpha(i):
            a += 1
        if isdigit(i):
            b += 1
    return {"letters": a, "digits": b}
