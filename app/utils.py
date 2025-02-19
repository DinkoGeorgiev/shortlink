from random import choice

from app.config import SHORT_LINK_CHARACTERS


def generate_random_string(size: int) -> str:
    """Generates random string with given size

    :param size: The size of the string
    :return: The generated string
    """
    return "".join(choice(SHORT_LINK_CHARACTERS) for i in range(size))


def get_invalid_characters(value: str) -> str:
    """Returns a string of invalid characters found in the given value

    :param value: The value to check
    :return: String of invalid characters
    """
    return "".join(set(value) - set(SHORT_LINK_CHARACTERS))
