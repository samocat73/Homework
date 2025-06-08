from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Получает на вход номер карты из 16 цифр и возвращает её маску в формате 0000 00** **** 0000"""
    if type(card_number) is str:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        converted_number_type = str(card_number)
        return f"{converted_number_type[0:4]} {converted_number_type[4:6]}** **** {converted_number_type[12:]}"


def get_mask_account(account_number: Union[str, int]) -> str:
    '''Функция, которая принимает номер счета и возвращает его маску в формате **0000'''
    if type(account_number) is str:
        return f"**{account_number[-4:]}"
    else:
        account_number_on_line = str(account_number)
        return f"**{account_number_on_line[-4:]}"


