def make_capital_letters(text:str) -> str:
    """
    домашнее задание 3_4
    """
    return ' '.join(x.capitalize() for x in text.split())
