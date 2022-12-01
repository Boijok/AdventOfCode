from pandas import DataFrame
from src.year_2022.day_1.input_values import input_values


def solve_2022_day_1_first_challenge() -> None:
    input_grid: DataFrame = DataFrame(input_values)
    answer = max(input_grid.sum(axis=1))
    print(f"solve_day_15_first_challenge solution is {answer}")
