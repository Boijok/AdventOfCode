import copy
from typing import List, Tuple
from src.year_2021.day_12.input_values import input_values


def solve_day_12_second_challenge() -> None:
    inputs_links = input_values
    lines = [["start"]]
    lines = complete_line(inputs_links, lines)
    non_start_inputs_links = [link for link in inputs_links if "start" not in link]
    for i in range(15):
        lines = complete_line(non_start_inputs_links, lines)
        lines = remove_triple_time_in_small_cave(lines)

    filtered_lines = [line for line in lines if line[-1] == "end"]
    print(f"solve_day_12_second_challenge solution is {len(filtered_lines)}")


def complete_line(
    inputs_links: List[Tuple[str, str]], current_lines: List[List[str]]
) -> List[List[str]]:
    new_lines = []
    for current_line in current_lines:
        added_new_line = False
        if current_line[-1] != "end":
            for link in inputs_links:
                if link[0] == current_line[-1]:
                    new_line = copy.deepcopy(current_line)
                    new_line.append(link[1])
                    new_lines.append(new_line)
                    added_new_line = True

                if link[1] == current_line[-1]:
                    new_line = copy.deepcopy(current_line)
                    new_line.append(link[0])
                    new_lines.append(new_line)
                    added_new_line = True

        if not added_new_line:
            new_lines.append(current_line)

    return new_lines


def remove_triple_time_in_small_cave(current_lines: List[List[str]]) -> List[List[str]]:
    new_lines = []
    for current_line in current_lines:
        explore_twice_a_small_cave = 0
        points = [point for point in current_line if point == point.lower()]
        for point in points:
            if points.count(point) > 1:
                explore_twice_a_small_cave = explore_twice_a_small_cave + 1
        if explore_twice_a_small_cave < 3:
            new_lines.append(current_line)
    return new_lines
