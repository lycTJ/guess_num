import random

ans = random.randint(1, 100)
while True:
	num = input('請輸入數字猜大小: ')
	num = int(num)
	if num == ans:
		print('終於猜對了')
		break
	elif num > ans:
			print('比答案大,往下猜')
	elif num < ans:
			print('比答案小,往上猜')
