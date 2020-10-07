integer, number_list = int(input()), input().split(" ")
result= all([int(x) > 0 for x in number_list]), any([x == x[::-1]  for x in number_list])
print(all(result))
