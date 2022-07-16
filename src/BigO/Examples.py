# def numbers(num=[1, 2, 3, 4]):
# num = [1, 2, 3, 4]
# n = len(num)
# print("Sum of arrays ", n * (n + 1) / 2)


# def find_sum(arr=[1, 4, 3, 4]):
#     n = len(arr)
#     return n * (n + 1) / 2

# print(find_sum())


def find_sum(arr=[1, 2, 44, 3]):
    sum = 0
    n = len(arr)

    for i in range(0, n + 1):
        sum += i
    return sum


print(find_sum())
