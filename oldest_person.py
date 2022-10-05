def oldest(people: dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    a = 0
    ans = ""
    for i, j in people:
        if (a < i):
            ans = j
            a = i

    return ans
