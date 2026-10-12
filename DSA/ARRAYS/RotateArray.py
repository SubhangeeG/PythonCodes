# Given an array of size n, rotate it clockwise d times
# METHOD 1: Time = O(n^2), Space = O(1)
def rotateRight(arr, d):
    n = len(arr)
    if d%n == 0:
        return arr
    if d >= n:
        d = d%n
    for i in range(d):
        temp = arr[n-1]
        arr.pop()
        arr.insert(0, temp)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 3
    print(rotateRight(arr,d))

# METHOD 2: Time = O(n), Space = O(1)
def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotateRight(arr, d):
    n = len(arr)
    if not arr or d % n == 0:
        return arr
    d = d % n

    # Step 1: Reverse the whole array
    reverseArray(arr, 0, n - 1)

    # Step 2: Reverse the first d elements
    reverseArray(arr, 0, d - 1)

    # Step 3: Reverse the remaining n - d elements
    reverseArray(arr, d, n - 1)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    print(rotateRight(arr, d))
