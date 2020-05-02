# 快排：随机选一个值作为基准，大于这个值的放右边，小于这个值的放左边

def quick_sort(nums, L, R):
	if L > R: return 
	left = L
	right = R
	pivot = nums[left]
	while left < right:
		while left < right and nums[right] >= pivot:
			right -= 1
		
		if left < right:
			nums[left] = nums[right]

		while left < right and nums[left] <= pivot:
			left += 1
			
		if left < right:
			nums[right] = nums[left]
		
		if left >= right: 
			nums[left] = pivot

	quick_sort(nums, L, R-1)
	quick_sort(nums, R+1, L)

	return nums

nums = [3,1,10,4,8,2,6,0]
print(quick_sort(nums, 0, len(nums) - 1))

		
