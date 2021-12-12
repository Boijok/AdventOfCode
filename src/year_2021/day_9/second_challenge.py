from typing import List, Tuple, Dict, Any, Set
from src.year_2021.day_9.first_challenge import get_low_point_list, is_lower_than
from src.year_2021.day_9.input_values import input_values


def solve_day_9_second_challenge() -> None:
    low_point_list = get_low_point_list(input_values)
    points_direction = get_points_direction(input_values)

    basins_size_and_points: List[Tuple[int, Set[Any]]] = []
    for point in low_point_list:
        basin_size, point_list = compute_basins_size(
            input_values, points_direction, point, []
        )
        basins_size_and_points.append((basin_size, point_list))

    basins_size = [elem[0] for elem in basins_size_and_points]
    sorted_basin_size = sorted(basins_size, reverse=True)
    current_count = sorted_basin_size[0] * sorted_basin_size[1] * sorted_basin_size[2]

    print(f"solve_day_9_second_challenge solution is {current_count}")


def get_points_direction(input_grid: List[List[int]]) -> List[List[int]]:
    points_direction: List[List[int]] = []
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    for x in range(max_x_value):
        row: List[int] = []
        for y in range(max_y_value):
            row.append(compute_point_direction(input_grid, (x, y)))
        points_direction.append(row)
    return points_direction


def compute_point_direction(input_grid: List[List[int]], point: Tuple[int, int]) -> int:
    point_value = input_grid[point[0]][point[1]]
    if point_value == 9:
        return 9
    else:
        return 0


def get_direction_from_neighbors(neighbors: Dict[str, int], point_value: int) -> str:
    counter_lower_neighbors = 0
    direction = ""
    for key, value in neighbors.items():
        if is_lower_than(value, point_value):
            counter_lower_neighbors = counter_lower_neighbors + 1
            direction = key
    if counter_lower_neighbors != 1:
        direction = "0"
    return direction


def pretty_print(matrix: List[List[Any]]) -> None:
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in matrix]))
    print("\n")


def compute_basins_size(
    input_grid: List[List[int]],
    direction_grid: List[List[int]],
    point: Tuple[int, int],
    point_list: List[Tuple[int, int]],
) -> Tuple[int, Set[Tuple[int, int]]]:
    if point in point_list:
        return 0, set(point_list)

    point_list.append(point)
    basins_size = 1
    neighbors = get_neighbors(input_grid, point)
    for key, value in neighbors.items():
        if 0 == direction_grid[value[0]][value[1]]:
            new_basins_size, new_point_list = compute_basins_size(
                input_grid, direction_grid, value, point_list
            )
            basins_size = basins_size + new_basins_size
            point_list.extend(new_point_list)

    return basins_size, set(point_list)


def get_neighbors(
    input_grid: List[List[int]],
    point: Tuple[int, int],
) -> Dict[str, Tuple[int, int]]:
    x_coord = point[0]
    y_coord = point[1]
    max_x_value = len(input_grid)
    max_y_value = len(input_grid[0])
    neighbors: Dict[str, Tuple[int, int]] = {}
    if x_coord > 0:
        upper_neighbor = (x_coord - 1, y_coord)
        neighbors["d"] = upper_neighbor
    if x_coord < max_x_value - 1:
        lower_neighbor = (x_coord + 1, y_coord)
        neighbors["u"] = lower_neighbor
    if y_coord > 0:
        left_neighbor = (x_coord, y_coord - 1)
        neighbors["r"] = left_neighbor
    if y_coord < max_y_value - 1:
        right_neighbor = (x_coord, y_coord + 1)
        neighbors["l"] = right_neighbor
    return neighbors
