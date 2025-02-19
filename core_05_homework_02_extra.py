import re
from typing import Callable, Iterator

# Generator of decimal numbers from a text string
def generator_numbers(text: str) -> Iterator[float]:
    """
    Extracts numbers from a string

    Parameters:
        text (str): text string from which decimal numbers must be extracted
    
    Returns:
        Iterator (float): iterator of decimal numbers
    """
    pattern = r"\s\d+.\d+\s"
    yield from [float(number.strip()) for number in re.findall(pattern, text)]

# Function to calculate sum of generated decimal numbers
def sum_profit(text: str, generator: Callable[[str], float]) -> float:
    """
    Calculates sum of generated decimal numbers

    Parameters:
        text (str): text string from which decimal numbers must be extracted
        generator (Callable[[str], float]): function extracting decimal numbers from a string
    
    Returns:
        total_profit (float): calculated sum
    """
    total_profit = 0
    for value in generator(text):
        total_profit += value
    return total_profit

# text_string = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text_string, generator_numbers)
# print(f"Загальний дохід: {total_income}")