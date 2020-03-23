import csv 



def matrix_transponse(n):
	k = []
	for numbers in n:
		k .append(numbers)
	return k
m = [[23, 56, 44],
     [70, 56, 77],
     [26, 27, 10]]
t = matrix_transponse(m)
print('\n'.join(str(r) for r in t))


def category_stat(data_file):
	with open(data_file) as f:
		reader = csv.reader(f)
		row = next(reader,1)



