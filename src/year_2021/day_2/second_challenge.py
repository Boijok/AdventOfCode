from src.year_2021.day_2.input_values import input_list

forward = 0
depth = 0
aim = 0

for value in input_list:
    print(f"Current value is {value}")
    if "forward" in value:
        int_value = int(value.replace("forward ", ""))
        forward = forward + int_value
        aim_step = aim * int_value
        print(f"aim_step is {aim_step}")
        depth = depth + aim_step
    if "down" in value:
        int_value = int(value.replace("down ", ""))
        aim = aim + int_value
    if "up" in value:
        int_value = int(value.replace("up ", ""))
        aim = aim - int_value
    print(f"new position is forward by {forward},depth by {depth},aim by {aim}")

final_value = forward * depth
print(f"final_value is {final_value}")
