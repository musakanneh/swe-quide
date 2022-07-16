def find_num(arr=[1, 2, 3, 4], k=4):
    # Compares arr elements to constant(k); returns a bool 
    for i in range(len(arr)):
        if arr[i] == k:
            return "True"

        arr[i] += 1
    return "False"


# print(find_num())

def odd_num(l=2, r=5):
    # Returns odd numbers between left and right params
    pass

