'''
Example test for the main.py file.
'''

from main import main


def test_main_returns_tuple_of_strings() -> None:
    result = main()

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(value, str) for value in result)
