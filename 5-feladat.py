my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

inner_list = []
extended_list = []

for p in my_list:
    inner_list = p
    summ = sum(inner_list)
    inner_list.append(summ)
    extended_list.append(inner_list)

print(extended_list)