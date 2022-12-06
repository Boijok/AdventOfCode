from pandas import DataFrame
from src.year_2022.day_2.input_values import input_values


def solve_2022_day_2_second_challenge() -> None:
    input_grid: DataFrame = DataFrame(
        input_values, columns=["opponent_move", "my_move"]
    )
    scores = input_grid.apply(
        lambda x: compute_round_score(x["opponent_move"], x["my_move"]), axis=1
    )
    answer = sum(scores)
    print(f"solve_2022_day_2_second_challenge solution is {answer}")


DECODE_MY_MOVE = {
    "X": "lost",
    "Y": "draw",
    "Z": "won",
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
    if my_move_decoded == "lost":
        i_win_against = {v: k for k, v in WHO_BEATS_ME.items()}
        return POINTS_FOR_OUTCOME["lost"] + MY_MOVE_POINTS[i_win_against[opponent_move]]
    elif my_move_decoded == "draw":
        return POINTS_FOR_OUTCOME["draw"] + MY_MOVE_POINTS[opponent_move]
    else:
        return POINTS_FOR_OUTCOME["won"] + MY_MOVE_POINTS[WHO_BEATS_ME[opponent_move]]
