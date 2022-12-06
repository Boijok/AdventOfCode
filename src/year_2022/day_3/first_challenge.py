from pandas import Series
from src.year_2022.day_3.input_values import input_values


def solve_2022_day_3_first_challenge() -> None:
    challenge_input: Series = Series(input_values)
    computed_input = challenge_input.apply(lambda x: compute_priority(x))
    answer = computed_input.sum()
    print(f"solve_2022_day_3_first_challenge solution is {answer}")


LETTER_MAPPING = {chr(i + 96): i for i in range(1, 27)}
UPPERCASE_MAPPING = {chr(i + 64): i + 26 for i in range(1, 27)}
LETTER_MAPPING.update(UPPERCASE_MAPPING)


def compute_priority(a_string: str) -> int:
    middle_char_position = len(a_string) // 2
    first_part = a_string[:middle_char_position]
    second_part = a_string[middle_char_position:]
    common_letter = find_common_letter(first_part, second_part)
    return LETTER_MAPPING[common_letter]


def find_common_letter(first_str: str, second_str: str) -> str:
    return "".join(set(first_str).intersection(second_str))
