# Given an array, generate and return all possible subarrays

# Time: O(n^3) & Space: O(n^3)
def genSubArray(arr):
    res = []
    n = len(arr)

    if n <= 1:
        return arr
    for i in range(n):
        for j in range(i, n):
            subArray = []
            for k in range(i, j + 1):
                subArray.append(arr[k])
            res.append(subArray)
    return res


if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    print(genSubArray(arr))
