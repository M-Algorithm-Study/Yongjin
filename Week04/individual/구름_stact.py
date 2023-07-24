N, K = map(int,input().split())
st = []

for i in range(N):
	word = input().split()
	if word[0] == 'push':
		if len(st) == K:
			print('Overflow')
		else:
			st.append(int(word[1]))
			
	elif word[0] == 'pop':
		if len(st) == 0:
			print('Underflow')
		else:
			print(st.pop())