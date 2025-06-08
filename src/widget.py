from src import masks


# Maestro 1596837868705199

def mask_account_card(account_number: str) -> str:
    account_or_card_number = ''
    account_or_card_name = ''
    for element in account_number:
        if element.isdigit():
            account_or_card_number += element
        else:
            account_or_card_name += element
    if len(account_or_card_number) == 16:
        return f'{account_or_card_name}{masks.get_mask_card_number(account_or_card_number)}'
    else:
        return f'{account_or_card_name}{masks.get_mask_account(account_or_card_number)}'






