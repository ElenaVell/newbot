counter=input().split('=')
try:
	counter=' '.join(counter[0])
	counter=counter.split()
	if '-' in counter:
		b=counter.index('-')
		print(float(''.join(counter[:b]))-float(''.join(counter[b+1:])))
	if '+' in counter:
		b=counter.index('+')
		print(float(''.join(counter[:b]))+float(''.join(counter[b+1:])))
	if '/' in counter:
		b=counter.index('/')
		print(float(''.join(counter[:b]))/float(''.join(counter[b+1:])))
	if '*' in counter:
		b=counter.index('*')
		print(float(''.join(counter[:b]))*float(''.join(counter[b+1:])))	
except ZeroDivisionError:
	print('Division by zero is impossible!')



