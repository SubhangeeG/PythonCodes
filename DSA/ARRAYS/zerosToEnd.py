# Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.
# METHOD 1: Time = O(n), Space = O(n)
def zerosToEnd(arr):
    count = 0
    res = []
    for num in arr:
        if num != 0:
            res.append(num)
        elif num == 0:
            count += 1

    for _ in range(count):
        res.append(0)
    return res


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(zerosToEnd(arr))

# METHOD 2: Time = O(n), Space = O(1)
def zerosToEnd(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

    return arr


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print(zerosToEnd(arr))
