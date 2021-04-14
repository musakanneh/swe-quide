#!/usr/bin/python3
"""Dictionary in list"""


def add_new_country(country_visited, time_visited, cities_visited):
    """Allows new countries to be added to the country log"""
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    print(travel_log)


def update_dict_value():
    """Adds one the each value in the dictionary"""
    dict = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    for val in dict:
        dict[val] += 1
    print(dict)


if __name__ == '__main__':
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"],
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hanburg"],
        }
    ]
    add_new_country("Russia", 2, ["Moscow", "Saint Paul"])
    update_dict_value()
