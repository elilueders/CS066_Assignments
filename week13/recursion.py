def sum_of_n(n):
    if n == 0:
        return 0
    else:
        result = sum_of_n(n-1) + n
        return result

def factorial(n):
    if n == 1:
        return 1
    else:

        result = n * factorial(n-1)
        return result

def listsum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listsum(num_list[1:])


print(listsum([1,2,5,5]))
# print(factorial(4))