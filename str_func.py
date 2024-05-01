def make_capital_letters(text:str) -> str:
    return ' '.join(x.capitalize() for x in text.split())
