# Given an array of integers, every element appears twice except for one. Find that single one.
arr = [5, 4, 6, 5, 4, 6, 7, 8, 1, 1, 7]
def singleNumber(arr):
	if len(arr) < 1:
		return
	arr.sort()
	i, j = (0, 1)
	while i<=len(arr)-2:
		if arr[i]==arr[j]:
			i+=2
			j+=2
	print (arr[i])

singleNumber(arr)
