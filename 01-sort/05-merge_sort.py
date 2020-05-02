# 归并排序：对两个已经排好序的数组进行再次排序合并为一个新的有序数组

def merge_sort(nums1, nums2):
	# 取下标
	i = 0
	j = 0
	k = 0 #用来表示大数组的下标
	l1 = len(nums1)
	l2 = len(nums2)

	nums = list(range(0, l1 + l2))
	while i < l1 or j < l2:
		if i < l1 and j < l2:
			# 比较
			if nums1[i] <= nums2[j]:
				nums[k] = nums1[i]
				i += 1
			else:
				nums[k] = nums2[j]
				j += 1
			k += 1
		elif i < l1:
			# 说明nums2已经遍历完毕
			nums[k] = nums1[i]
			i += 1
			k += 1
		elif j < l2:
			nums[k] = nums2[j]
			j += 1
			k += 1
		else:
			break
	
	return nums

print(merge_sort([1,2,3,4], [5,6,7,8,9,10]))