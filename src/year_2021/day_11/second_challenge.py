from src.year_2021.day_11.first_challenge import (
    increase_every_one,
    flash,
    count_flash,
    reset_every_one,
)
from src.year_2021.day_11.input_values import (
    input_values,
)
from src.year_2021.day_9.second_challenge import pretty_print


def solve_day_11_second_challenge() -> None:
    current_input_values = input_values
    is_first = True
    i = 0
    while is_first:
        increased_input_values = increase_every_one(current_input_values)
        flashed_input_values = increased_input_values
        for j in range(20):
            flashed_input_values = flash(flashed_input_values)
        if count_flash(flashed_input_values) == 100 and is_first:
            is_first = False
            first_step = i + 1
        current_input_values = reset_every_one(flashed_input_values)
        i = i + 1
    pretty_print(current_input_values)

    print(f"solve_day_11_second_challenge solution is {first_step}")
