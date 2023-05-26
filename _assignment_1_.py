#1. program to find all pairs of an integer array whose sum is equal to a given number

def check_pair(arr, given_number):
    pairs = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == given_number:
                pairs.append((arr[i], arr[j]))

    return pairs

given_array = [2, 4, 5, 6, 7, 8, 9]
num = 10
print(check_pair(given_array, num))