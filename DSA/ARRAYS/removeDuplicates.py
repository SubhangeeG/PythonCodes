# Given a sorted array of size n, goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally return the length of the distinct sorted subarray

# Time: O(n^2) & Space: O(n)
def retUniques(arr):
    uniques = []
    for i in arr:
        if i not in uniques:
            uniques.append(i)
    return uniques


if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    uniques = retUniques(arr)
    for i in uniques:
        print(i, end=" ")


# Method 2
# Time: O(n) & Space: O(n)
def removeDuplicates(arr):
    res = set(arr)
    return sorted(list(res))


if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    uniques = removeDuplicates(arr)
    for i in uniques:
        print(i, end=" ")
