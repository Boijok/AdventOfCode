from pydantic import BaseModel
from src.year_2021.day_2.input_values import input_list


class Position(BaseModel):
    forward: int = 0
    depth: int = 0
    aim: int = 0

    def move_forward(self, value: str) -> None:
        int_value = int(value.replace("forward ", ""))
        self.forward = self.forward + int_value
        self.depth = self.depth + self.aim * int_value

    def move_down(self, value: str) -> None:
        int_value = int(value.replace("down ", ""))
        self.aim = self.aim + int_value

    def move_up(self, value: str) -> None:
        int_value = int(value.replace("up ", ""))
        self.aim = self.aim - int_value


def solve_day_2_second_challenge() -> None:
    position = Position()
    for value in input_list:
        if "forward" in value:
            position.move_forward(value)
        if "down" in value:
            position.move_down(value)
        if "up" in value:
            position.move_up(value)

    final_value = position.forward * position.depth
    print(f"solve_day_2_second_challenge is {final_value}")
