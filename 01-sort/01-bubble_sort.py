def bubble_sort(nums):
	n = len(nums)
	for i in range(n):
		for j in range(i+1,n):
			if nums[i] > nums[j]:
				nums[i] ^= nums[j]
				nums[j] ^= nums[i]
				nums[i] ^= nums[j]

	
	return nums

print(bubble_sort([3,1,10,4,8,2,6,0]))
