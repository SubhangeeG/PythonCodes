# Given an array, print its reverse without using built-in function

# Time: O(n) & Time: O(1)
def reverseArray(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

    return arr


if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    print(reverseArray(arr))
