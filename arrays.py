
N = int(raw_input('Please enter the number of elements: '))
v = [0]

for i in range(1, N + 1):
	v.append(int(raw_input('Please enter number: ')))

for i in range(1, N + 1):
	print 'i is', i, ' and the ith element is ', v[i]
