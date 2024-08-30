my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list.remove (0)
positive_numbers = 0
while  positive_numbers < len(my_list):
    if my_list[positive_numbers] > 0:
        print(my_list[positive_numbers])
        positive_numbers += 1
    if my_list[positive_numbers] < 0:
        break




