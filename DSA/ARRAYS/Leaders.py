# Given an array of size n, task is to find all the Leaders in the array ( An element is a Leader if it is greater than or equal to all the elements to its right side).

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
