from src.year_2021.day_2.input_values import input_list

forward_list = [input_value for input_value in input_list if "forward" in input_value]
down_list = [input_value for input_value in input_list if "down" in input_value]
up_list = [input_value for input_value in input_list if "up" in input_value]
print(f"forward_list is {forward_list}")
print(f"down_list is {down_list}")
print(f"up_list is {up_list}")

forward_int_list = [
    int(input_value.replace("forward ", "")) for input_value in forward_list
]
down_int_list = [int(input_value.replace("down ", "")) for input_value in down_list]
up_int_list = [int(input_value.replace("up ", "")) for input_value in up_list]
print(f"forward_int_list is {forward_int_list}")
print(f"down_int_list is {down_int_list}")
print(f"up_int_list is {up_int_list}")

forward_sum = sum(forward_int_list)
down_sum = sum(down_int_list)
up_sum = sum(up_int_list)
print(f"Forward by {forward_sum},Down by {down_sum},Up by {up_sum}")

down_value = down_sum - up_sum
print(f"down_value is {down_value}")

final_value = forward_sum * down_value
print(f"final_value is {final_value}")
