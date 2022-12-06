from pandas import DataFrame
from src.year_2022.day_2.input_values import input_values


def solve_2022_day_2_first_challenge() -> None:
    input_grid: DataFrame = DataFrame(
        input_values, columns=["opponent_move", "my_move"]
    )
    scores = input_grid.apply(
        lambda x: compute_round_score(x["opponent_move"], x["my_move"]), axis=1
    )
    answer = sum(scores)
    print(f"solve_2022_day_2_first_challenge solution is {answer}")


DECODE_MY_MOVE = {
    "X": "A",  # Rock
    "Y": "B",  # Paper
    "Z": "C",  # Scissors
}

WHO_BEATS_ME = {
    "A": "B",  # Rock lose against Paper
    "B": "C",  # Paper lose against Scissors
    "C": "A",  # Scissors lose against Rock
}

MY_MOVE_POINTS = {
    "A": 1,  # Rock grant 1 point
    "B": 2,  # Paper grant 2 point
    "C": 3,  # Scissors grant 3 point
}

POINTS_FOR_OUTCOME = {
    "lost": 0,
    "draw": 3,
    "won": 6,
}


def compute_round_score(opponent_move: str, my_move: str) -> int:
    my_move_decoded = DECODE_MY_MOVE[my_move]
    points_for_my_move = MY_MOVE_POINTS[my_move_decoded]
    if opponent_move == my_move_decoded:
        return POINTS_FOR_OUTCOME["draw"] + points_for_my_move
    elif opponent_move == WHO_BEATS_ME[my_move_decoded]:
        return POINTS_FOR_OUTCOME["lost"] + points_for_my_move
    else:
        return POINTS_FOR_OUTCOME["won"] + points_for_my_move
