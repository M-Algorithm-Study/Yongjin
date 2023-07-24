num = int(input())
cnt = 0

while True:
	if num % 40 == 0:
		cnt += num//40
		num = num % 40
	else:
		if num > 40:
			cnt += num// 40
			num = num % 40
		else:
			pass
	
	if num % 20 == 0 : 
		cnt += num//20
		num = num % 20
	else:
		if num > 20:
			cnt += num// 20
			num = num % 20
		else:
			pass
		
	if num % 10 == 0 : 
		cnt += num// 10
		num = num % 10
	else:
		if num > 10:
			cnt += num// 10
			num = num % 10
		else:
			pass	
		
		
	if num % 5 == 0 :
		cnt += num// 5
		num = num % 5
	else:
		if num > 5:
			cnt += num // 5
			num = num % 5
		else:
			cnt += num // 5
			num = num % 5
	

	if num == 0:
		print(cnt)
		break
	else:
		cnt += num
		print(cnt)
		break
		

