def sumatoria_cubica(n):
	x=0
	for i in range(1,n):
		x=x+1
		for j in range(1,i):
			x=x+1
			for k in range(j,i+j):
				x=x+1
	print(x)
	return x

def sumatoria_constante(n):
	x=0
	for i in range(1,n):
		x=x+1

#sumatoria_cubica(5)
