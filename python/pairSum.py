# Given an integer array, output all pairs that sum up to a specific value k.

def pairSum(arr, k):
    if len(arr) < 2:
        return
    arr.sort()
    left, right = (0, len(arr)-1)
    while left<right:
        tempSum=arr[left]+arr[right]
        if tempSum=k:
            print arr[left], arr[right]
        elif tempSum > k:
            right-=1
        else
            left+=1
