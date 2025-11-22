import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products_dict, expected_result",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 160
                }
            ],
            [],
            id="should return empty list"),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"],
            id="should check product with expiration date equals today"),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 1, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 1, 21),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["salmon", "chicken", "duck"],
            id="should check products out of date"),
    ]
)
def test_products_out_of_date(
        products_dict: list[dict],
        expected_result: list
) -> None:
    fake_today = datetime.date(2022, 2, 2)
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        result = outdated_products(products_dict)
        assert result == expected_result
