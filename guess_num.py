import random
start = input('請輸入起始值: ')
end = input('請輸入結束值: ')

start = int(start)
end = int(end)

ans = random.randint(start, end)

count = 0
while True:
	count += 1
	num = input('請輸入數字猜大小: ')
	num = int(num)
	if num == ans:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > ans:
			print('比答案大,往下猜')
	elif num < ans:
			print('比答案小,往上猜')
	print('這是你猜的第', count, '次')
