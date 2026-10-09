def select_city_names(
    cities: list[dict[str, object]],
    district: str,
    min_population: int = 0,
) -> list[str]:
    if min_population < 0: raise ValueError(f"min_population < 0\nInput: {min_population}")
    return list(map(lambda x: x["name"], sorted(list(filter(lambda city: city["district"] == district and city["population"] >= min_population, cities)),
                 key=lambda x: -x["population"])))


def test():
    cities: list[dict[str, object]] = [
        {
            "name": "Москва",
            "district": "Центральный",
            "population": 13_000_000,
        },
        {
            "name": "Воронеж",
            "district": "Центральный",
            "population": 1_050_000,
        },
        {
            "name": "Казань",
            "district": "Приволжский",
            "population": 1_310_000,
        },
        {
            "name": "Самара",
            "district": "Приволжский",
            "population": 1_170_000,
        },
    ]

    print(select_city_names(cities, "Центральный", 1_000_000))
    # ['Москва', 'Воронеж']

    print(select_city_names(cities, "Приволжский", 1_200_000))
    # ['Казань']

    print(select_city_names(cities, "Сибирский"))
    # []
    print([city["name"] for city in cities])
    # ['Москва', 'Воронеж', 'Казань', 'Самара']  — исходный список не изменился

    select_city_names(cities, "Центральный", -1)
    # ValueError


test()