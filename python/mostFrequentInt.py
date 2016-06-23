# find the most frequent integer in an array
import collections

arrayOfInts = [1, 2, 9, 3, 4, 8, 7, 2, 9, 9]

def mostFrequent(arrayOfInts):
	count = collections.defaultdict(int)
	for i in arrayOfInts:
		count[i]+=1
	for i in arrayOfInts:
		currentMax = 0;
		if count[i] >= currentMax:
			currentMax = i
	print (currentMax)

mostFrequent(arrayOfInts)
