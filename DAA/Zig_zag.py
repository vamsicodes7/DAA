def print_list(list):
  while len(list) > 1:
    print(list[0], list[-1], sep = " ", end= " ")
    list.pop(0)
    if list:
      list.pop(-1)
  print(list[0])

list = [4,3,7,8,9,2,1]
list.sort()
print_list(list)