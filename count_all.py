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
        if i.isalpha():
            a += 1
        if i.isdigit():
            b += 1
    return {"LETTERS": a, "DIGITS": b}


print(count_all("1nhnk134"))
