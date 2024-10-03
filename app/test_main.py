import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_output",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, expected_output: list) -> None:
    assert get_coin_combination(cents) == expected_output
