# def greedy_change(money):
# 	coins = [25, 20, 10, 5, 1]
# 	change = []
# 	# coin = 0
# 	while money > 0:
# 		for i in range(len(coins)):
# 			if coins[i] <= money:
# 				coin = coins[i]
# 				break
# 		money -= coin
# 		change.append(coin)
# 	return change

# def recursive_change(money):
# 	if money == 0:
# 		return 0
# 	coins = [6, 5, 1]
# 	min_num_coins = float('inf')
# 	for coin in coins:
# 		if coin <= money:
# 			num_coins = recursive_change(money - coin)
# 			if num_coins + 1 < min_num_coins:
# 				min_num_coins = num_coins + 1
# 	return min_num_coins

def dp_change(money):
	coins = [4, 3, 1]
	min_num_coins = [0] + [float('inf')] * money
	for m in range(1, money + 1):
		for coin in coins:
			if coin <= m:
				num_coins = min_num_coins[m - coin] + 1
				if num_coins < min_num_coins[m]:
					min_num_coins[m] = num_coins
	return min_num_coins[-1]


if __name__ == '__main__':
	money = int(input())
	num_coins = dp_change(money)
	print(num_coins)



