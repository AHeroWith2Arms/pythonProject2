import pytest

from src.generators import filter_by_currency, transaction_descriptions


@pytest.fixture()
def dict_list_with_currency() -> list[dict]:
    return [
        {"id": 432432883, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
        {"id": 123445667, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
        {"id": 873234345, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
        {"id": 983243242, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    ]


@pytest.fixture()
def dict_list_for_descriptions() -> list[dict]:
    return [
        {"id": 1, "description": "Перевод со счета на счет"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод со счета на счет"},
        {"id": 5, "description": "Перевод с карты на карту"},
    ]


def test_filter_by_currency_usd(dict_list_with_currency: list[dict]) -> None:
    """Проверяет правильность фильтрации по USD"""
    result = list(filter_by_currency(dict_list_with_currency, "USD"))
    assert len(result) == 3
    assert result[0]["id"] == 432432883
    assert result[1]["id"] == 123445667
    assert result[2]["id"] == 873234345
    assert all(r["operationAmount"]["currency"]["code"] == "USD" for r in result)


def test_filter_by_currency_rub(dict_list_with_currency: list[dict]) -> None:
    """Проверяет правильность фильтрации по RUB"""
    result = list(filter_by_currency(dict_list_with_currency, "RUB"))

    assert len(result) == 1

    assert result[0]["id"] == 432432883
    assert result[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_transaction_descriptions(dict_list_for_descriptions: list[dict]) -> None:
    """Проверяет правильность работы генератора """
    result = list(transaction_descriptions(dict_list_for_descriptions))

    assert len(result) == 5

    assert result[0] == "Перевод со счета на счет"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Перевод со счета на счет"
    assert result[3] == "Перевод со счета на счет"
    assert result[4] == "Перевод организации"
