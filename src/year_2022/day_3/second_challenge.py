from pandas import DataFrame
from src.year_2022.day_3.input_values import input_values


def solve_2022_day_3_second_challenge() -> None:
    challenge_input: DataFrame = DataFrame(input_values, columns=["item"])
    challenge_input["group_code"] = challenge_input.index // 3
    grouped_input = challenge_input.groupby(["group_code"]).agg(lambda x: " ".join(x))
    computed_input = grouped_input["item"].apply(lambda x: compute_badge(x))
    answer = computed_input.sum()
    print(f"solve_2022_day_3_second_challenge solution is {answer}")


LETTER_MAPPING = {chr(i + 96): i for i in range(1, 27)}
UPPERCASE_MAPPING = {chr(i + 64): i + 26 for i in range(1, 27)}
LETTER_MAPPING.update(UPPERCASE_MAPPING)


def compute_badge(a_string: str) -> int:
    group_items = a_string.split(" ")
    common_item = group_items[0]
    for item in group_items:
        common_item = find_common_letter(common_item, item)
    return LETTER_MAPPING[common_item]


def find_common_letter(first_str: str, second_str: str) -> str:
    return "".join(set(first_str).intersection(second_str))
