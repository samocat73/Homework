def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и параметр state='EXECUTED' опционально,
    возвращает список словарей, где ключ state равен указаному значению"""
    dictionaries_with_key = []
    for separate_dictionary in list_of_dictionaries:
        for key, value in separate_dictionary.items():
            if separate_dictionary["state"] == state:
                dictionaries_with_key.append(separate_dictionary)
    return dictionaries_with_key


def sort_by_date(list_of_dictionaries: list[dict], sort_order: bool = True) -> list:
    """Функция, которая принимает список словарей и параметр сортировки опционально,
    по умолчанию на убывание, возвращает список словарей отсортированных по дате"""
    return sorted(
        list_of_dictionaries,
        key=lambda dictionary: dictionary["date"],
        reverse=sort_order,
    )
