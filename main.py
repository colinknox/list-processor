#!/usr/bin/python3

work = [
    "colin",
    "danielle",
    "tim",
    "dave",
    "brian",
    "bryan",
    "sarah",
    "john"
]

num_list = [34, 64, 83, 27, 86]



def print_all(items):
    for current_item in items:
        print(current_item)

def count_items(items):
    count = 0
    
    for current_item in items:
        count += 1

    return count

def sum_list(number):
    sum = 0
    
    for num in number:
        sum += num

    return sum

def find_max(number):
    max = float("-inf")

    for num in number:
        if num <= max:
            pass
        else:
            max = num

    return max

def find_min(number):
    min = float("inf")

    for num in number:
        if num >= min:
            pass
        else:
            min = num

    return min



# # print_all TEST
# print_all(work)

# # count_items TEST
# count_items(work)

# # sum_list TEST
# test = sum_list(num_list)
# print(test)

# # find_max TEST
# test = find_max(num_list)
# print(test)

# # find_min TEST
# test = find_min(num_list)
# print(test)
