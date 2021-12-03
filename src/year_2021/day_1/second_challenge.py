from src.year_2021.day_1.input_values import input_values

input_values_1 = input_values[:-2]
input_values_2 = input_values[1:-1]
input_values_3 = input_values[2:]

window_values = diff = [
    value_1 + value_2 + value_3
    for value_1, value_2, value_3 in zip(input_values_1, input_values_2, input_values_3)
]

window_values_head = window_values[:-1]
window_values_tail = window_values[1:]

window_diff = [
    head - tail for head, tail in zip(window_values_head, window_values_tail)
]
filtered_window_diff = [1 for iteration in window_diff if iteration < 0]

print(len(filtered_window_diff))
