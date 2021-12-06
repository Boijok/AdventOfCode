from typing import List, Tuple, Any
from numpy import zeros
from pydantic.main import BaseModel
from src.year_2021.day_5.input_values import input_values


class Coordinate(BaseModel):
    x: int
    y: int


class Line(BaseModel):
    origin: Coordinate
    end: Coordinate

    def is_vertical(self) -> bool:
        return self.origin.x == self.end.x

    def is_horizontal(self) -> bool:
        return self.origin.y == self.end.y

    def is_diagonal(self) -> bool:
        return abs(self.origin.x - self.end.x) == abs(self.origin.y - self.end.y)

    def vertical_range(self) -> range:
        if self.origin.x < self.end.x:
            return range(self.origin.x, self.end.x + 1)
        else:
            return range(self.end.x, self.origin.x + 1)

    def horizontal_range(self) -> range:
        if self.origin.y < self.end.y:
            return range(self.origin.y, self.end.y + 1)
        else:
            return range(self.end.y, self.origin.y + 1)

    def diagonal_ranges(self) -> Tuple[range, range]:
        if self.origin.y < self.end.y and self.origin.x < self.end.x:
            return range(self.origin.y, self.end.y + 1), range(
                self.origin.x, self.end.x + 1
            )
        elif self.origin.y > self.end.y and self.origin.x > self.end.x:
            return range(self.end.y, self.origin.y + 1), range(
                self.end.x, self.origin.x + 1
            )
        elif self.origin.y < self.end.y and self.origin.x > self.end.x:
            return range(self.origin.y, self.end.y + 1), range(
                self.origin.x, self.end.x - 1, -1
            )
        elif self.origin.y > self.end.y and self.origin.x < self.end.x:
            return range(self.origin.y, self.end.y - 1, -1), range(
                self.origin.x, self.end.x + 1
            )
        else:
            print("Warning, should not be here")
            return range(0), range(0)


def solve_day_5_second_challenge() -> None:
    input_lines = convert_input_values_to_list_of_lines(input_values)
    filtered_lines = keep_only_vertical_horizontal_and_diagonal_lines(input_lines)
    grid = create_grid(filtered_lines)
    completed_grid = fill_grid(filtered_lines, grid)
    number_of_points_to_avoid = count_points_to_avoid(completed_grid)
    print(f"solve_day_5_second_challenge solution is {number_of_points_to_avoid}")


def convert_input_values_to_list_of_lines(
    input_list: List[List[Tuple[int, int]]]
) -> List[Line]:
    return [
        Line(origin=Coordinate(x=x1, y=y1), end=Coordinate(x=x2, y=y2))
        for (x1, y1), (x2, y2) in input_list
    ]


def keep_only_vertical_horizontal_and_diagonal_lines(
    input_lines: List[Line],
) -> List[Line]:
    return [
        line
        for line in input_lines
        if line.is_horizontal() or line.is_vertical() or line.is_diagonal()
    ]


def create_grid(input_lines: List[Line]) -> Any:
    max_x_coordinate = get_max_x_coordinate(input_lines)
    max_y_coordinate = get_max_y_coordinate(input_lines)
    return zeros((max_x_coordinate, max_y_coordinate))


def get_max_x_coordinate(input_lines: List[Line]) -> int:
    max_x_coordinate = 0
    for line in input_lines:
        max_x_coordinate = max(max_x_coordinate, line.origin.x)
        max_x_coordinate = max(max_x_coordinate, line.end.x)
    return max_x_coordinate + 1


def get_max_y_coordinate(input_lines: List[Line]) -> int:
    max_y_coordinate = 0
    for line in input_lines:
        max_y_coordinate = max(max_y_coordinate, line.origin.x)
        max_y_coordinate = max(max_y_coordinate, line.end.x)
    return max_y_coordinate + 1


def fill_grid(input_lines: List[Line], grid: Any) -> Any:
    for line in input_lines:
        if line.is_horizontal():
            for point in line.vertical_range():
                grid[point, line.origin.y] = grid[point, line.origin.y] + 1
        if line.is_vertical():
            for point in line.horizontal_range():
                grid[line.origin.x, point] = grid[line.origin.x, point] + 1
        if line.is_diagonal():
            y_range, x_range = line.diagonal_ranges()
            for x_coordinate, y_coordinate in zip(x_range, y_range):
                grid[x_coordinate, y_coordinate] = grid[x_coordinate, y_coordinate] + 1
    return grid


def count_points_to_avoid(grid: Any) -> int:
    counter = 0
    for line in grid:
        for point in line:
            if point > 1:
                counter = counter + 1
    return counter
