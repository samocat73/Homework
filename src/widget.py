from src import masks


def mask_account_card(account_number: str) -> str:
    """Функция, которая создает маску для карт и счетов, учитывая их названия"""
    account_or_card_number = ""
    account_or_card_name = ""
    for element in account_number:
        if element.isdigit():
            account_or_card_number += element
        else:
            account_or_card_name += element
    if len(account_or_card_number) == 16:
        return f"{account_or_card_name}{masks.get_mask_card_number(account_or_card_number)}"
    else:
        return f"{account_or_card_name}{masks.get_mask_account(account_or_card_number)}"


def get_date(date_string: str) -> str:
    """Функция, которая делает правильный формат даты"""
    dirty_date = date_string[0:10]
    date_as_a_list = dirty_date.split("-")
    year = str(date_as_a_list[0])
    month = str(date_as_a_list[1])
    day = str(date_as_a_list[2])
    return f"{day}.{month}.{year}"
