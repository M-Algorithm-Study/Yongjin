from collections import deque

cnt, M = map(int,input().split())
st = deque()

for i in range(M):
	word = input().split()
	if word[0] == 'deposit':
		cnt += int(word[1])
		while st and st[0] <= cnt:
			cnt -= st[0]
			st.popleft()

	elif word[0] == 'pay':
		if cnt >= int(word[1]):
			cnt -= int(word[1])
	
	elif word[0] == 'reservation':
		if not st and cnt >= int(word[1]):
			cnt -= int(word[1])
		else:
			st.append(int(word[1]))

print(cnt)