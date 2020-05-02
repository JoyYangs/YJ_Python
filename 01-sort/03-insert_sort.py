# 插入排序：分两组，一组有序，一组无序，将无序组的元素一个个插入到有序中

# i 表示arr的第i个元素的下标
def insert_num(arr, i):
	key = arr[i]
	while(arr[i-1] > key) :
		arr[i] = arr[i-1]
		i -= 1
		if i == 0:
			break
	arr[i] = key
	

def insert_sort(nums):
	for i in range(1, len(nums)):
		insert_num(nums, i)

	return nums

print(insert_sort([3,1,10,4,8,2,6,0]))
	