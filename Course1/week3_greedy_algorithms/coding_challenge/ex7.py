def max_salary(nums):
	salary = ''
	while nums:
		max_num = '0'
		for num in nums:
			# for i in range(max(len(max_num), len(num))):
			# 	i_max = min(i, len(max_num) - 1)
			# 	i_num = min(i, len(num) - 1)
			# 	if max_num[i_max] < num[i_num]:
			# 		max_num = num
			# 		break
			# 	elif max_num[i_max] > num[i_num]:
			# 		break
			if max_num == '0' or max_num + num < num + max_num:
				max_num = num
		salary += max_num
		nums.remove(max_num)
	return int(salary)


if __name__ == '__main__':
	n = int(input())
	nums = input().split()
	print(max_salary(nums))