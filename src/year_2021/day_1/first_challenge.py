from src.year_2021.day_1.input_values import input_values

input_values_head = input_values[:-1]
input_values_tail = input_values[1:]

diff = [head - tail for head, tail in zip(input_values_head, input_values_tail)]
filtered_diff = [1 for iteration in diff if iteration < 0]

print(len(filtered_diff))
