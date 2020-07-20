def max_pairwise_prod(nums):
	n = len(nums)

	# max_index_1 = 0
	# for i in range(1, n):
	# 	if nums[i] > nums[max_index_1]:
	# 		max_index_1 = i
	# nums[n-1], nums[max_index_1] = nums[max_index_1], nums[n-1]

	# max_index_2 = 0
	# for i in range(1, n-1):
	# 	if nums[i] > nums[max_index_2]:
	# 		max_index_2 = i
	# return nums[n-1] * nums[max_index_2]

	max_index_1 = 0
	max_index_2 = 1
	for i in range(1, n):
		if nums[i] > nums[max_index_1]:
			max_index_2 = max_index_1
			max_index_1 = i
		elif nums[i] > nums[max_index_2]:
			max_index_2 = i
	return nums[max_index_1] * nums[max_index_2]

if __name__ == '__main__':
	n = int(input())
	nums = [int(num) for num in input().split()]
	print(max_pairwise_prod(nums))