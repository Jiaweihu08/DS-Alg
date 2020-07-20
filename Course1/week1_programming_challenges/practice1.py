from time import process_time
import random
# def max_pairwise_prod(nums):
# 	n = len(nums)
# 	product = 0
# 	for i in range(n):
# 		for j in range(i+1, n):
# 			product = max(product, nums[i] * nums[j])
# 	print(product)

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
	max_index_1 = 0
	max_index_2 = 1
	for i in range(1, n):
		if nums[i] > nums[max_index_1]:
			max_index_2 = max_index_1
			max_index_1 = i
		elif nums[i] > nums[max_index_2]:
			max_index_2 = i
	
	return nums[max_index_1] * nums[max_index_2]

def brute_force_answer(nums):
	nums = nums.copy()
	max_1 = nums.pop(nums.index(max(nums)))
	max_2 = nums.pop(nums.index(max(nums)))
	return max_1 * max_2

def stress_testing(max_len=200000, max_num=200000):
	while True:
		n = random.randint(2, max_len)
		nums = [random.randint(1, max_num) for _ in range(n)]
		print(nums)

		bf_sum = brute_force_answer(nums)
		start = process_time()
		max_sum = max_pairwise_prod(nums)
		end = process_time()

		print('\nCompute time: ', end - start)
		if bf_sum != max_sum:
			print('\nWrong answer:\nbrute force" {}, function: {}'.\
				format(bf_sum, max_sum))
			break
		print('OK\n','-'*50, '\n')

if __name__ == '__main__':
	# n = int(input())
	# nums = [int(num) for num in input().split()]
	stress_testing()
	







