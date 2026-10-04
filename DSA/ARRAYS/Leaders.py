# Given an array of size n, task is to find all the Leaders in the array ( An element is a Leader if it is greater than or equal to all the elements to its right side).

# Time: O(n^2) & Space: O(n) 
myArr = [1,3,2,4,5,16,8]
leaders = []
lenArr = len(myArr)
if lenArr != 0:
    for i in range(lenArr-1):
        highest = max(myArr[i+1:])
        if myArr[i] >= highest:
            leaders.append(myArr[i])

    leaders.append(myArr[lenArr-1])

print(leaders)

# Time: O(n) & Space: O(1) 
def leaders(arr):
    result = []
    n = len(arr)
    maxRight = arr[-1]
    result.appen(maxRight)

   for i in range(n-2, -1,-1):
       if arr[i] > maxRight:
           maxRight = arr[i]
           result.append(maxRight)

  result.reverse()
  return result

if __name__ == "__main__":
    arr = [16,17,8,9,3,2]
    result = leaders(arr)
    print(" ".join(map(str, result))
