# Given an array arr[] and an integer k. You can perform an operation in which you can increment any of the number in the array by k. Find the minimum number of operations needed to make all the elements of array equal.
# Time: O(n), Space: O(1)
def minInc(arr, k):
    maxEle = max(arr)
    count = 0
    for num in arr:
        if (maxEle - num) % k != 0:
            return -1
        count += (maxEle - num) // k

    return count


if __name__ == "__main__":
    arr = [4, 4, 4, 2]
    k = 2
    print(minInc(arr, k))
