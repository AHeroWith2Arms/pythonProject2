def masc_account_card(number: str) -> str:
    """Функция принимает на вход номер карты и счета и возвращает их маску, номер карты и номер счета замаскирован."""
    card_number = ""
    name_card = ""
    if "Счёт" in number or "Счет" in number:
        score_number = number[5:]
        number_mask = number[0:4] + " " + "**" + score_number[-4:]
        return number_mask
    else:
        for i in range(len(number)):
            if number[i].isalpha() or number[i] == " ":
                name_card += number[i]
            else:
                card_number += number[i]

        correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
        number_mask = (
            name_card
            + " "
            + correct_number[0:4]
            + " "
            + correct_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + correct_number[12:16]
        )

        return number_mask


def get_date(date: str) -> str:
    """Функция принимает на вход строку и отдает ответ формате 11.07.2018."""
    correct_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
    return correct_date


n = input()
print(masc_account_card(n))
