def cities_dict(cities: list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    di = {}
    for i in range(len(cities)):
        di[cities[i]] = i+1
    return di
