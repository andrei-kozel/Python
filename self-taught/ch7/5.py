first_list = [8, 19, 148, 4]
second_list = [9, 1, 33, 83]
third_list = []

for i in first_list:
    for x in second_list:
        third_list.append(i * x)

print(third_list)
