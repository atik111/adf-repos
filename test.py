
from datecalc import duration, when
from datetime import date

def test_duration():
    # Arrange
    start_date = date(2022, 8, 21)
    end_date  = date(2022, 9, 21)
    expected_output = 31.0

    # Act
    actual_output = duration(start_date, end_date)


    # Assert
    assert actual_output == expected_output


def test_when():
    # Arrange
    start_date = date(2022, 8, 21)
    days_between = 10.0
    expected_output = date(2022, 8, 31)

    # Act
    actual_output = when(start_date, days_between)


    # Assert
    assert actual_output == expected_output