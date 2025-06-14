# Проект "Виджет банковских операций клиента"

## Цель проекта

*IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента.*

### Инструкция по установке и использованию разработанных функций:

**Клонируйте репозиторий, импортируйте нужные вам функции:**
```commandline
git clone https://github.com/samocat73/Homework.git
```

**На данный момент разработано три модуля masks, widget и processing с шестью функциями.**

**В модуле masks две функции, get_mask_card_number и get_mask_account.**

* Функция get_mask_card_number принимает на вход номер карты из 16 цифр и возвращает её маску в формате 0000 00** **** 0000
* Функция get_mask_account принимает номер счета и возвращает его маску в формате **0000*
```commandline
from src.masks import get_mask_card_number
from src.masks import get_mask_account

result = get_mask_card_number(7000792289606361)
second_result = get_mask_account(73654108430135874305)

print(result)
print(second_result)
```
```
>>> 7000 79** **** 6361
>>> **4305
```

**В модуле widget так же две функции, mask_account_card и get_date.**
* Функция mask_account_card создает маску для карт и счетов, учитывая их названия
* Функция get_date делает понятный формат даты из формата дат ISO 8601 
```commandline
from src.widget import mask_account_card
from src.widget import get_date


result = mask_account_card('Visa Platinum 7000792289606361')
second_result = get_date('2024-03-11T02:26:18.671407')

print(result)
print(second_result)
```
```
>>> Visa Platinum 7000 79** **** 6361
>>> 11.03.2024
```

**В модуле processing ещё две функции, filter_by_state и sort_by_date.**

* Функция filter_by_state сортирует список словарей по ключу state. По умолчанию работает со значением EXECUTED 

* Функция sort_by_date сортирует список словарей, принимает параметр сортировки True или False. По умолчанию работает с параметром сортировки True.
```commandline
from src.processing import filter_by_state
from src.processing import sort_by_date


result = filter_by_state(
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
)
second_result = sort_by_date(
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
)

print(result)
Print(second_result)
```

```
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
