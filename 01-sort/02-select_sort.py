def select_sort(nums):
	n = len(nums)
	for i in range(n):
		minIdx = i
		minNum = nums[i]
		for j in range(i+1, n):
			if nums[j] < minNum:
				minIdx = j
				minNum = nums[j]

		if minIdx != i:
			nums[minIdx] = nums[i]
			nums[i] = minNum

	return nums

print(select_sort([3,1,10,4,8,2,6,0]))