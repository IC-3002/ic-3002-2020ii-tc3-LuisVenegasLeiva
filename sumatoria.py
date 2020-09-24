#############################################
#Calculo de sumatoria		    			#
#Luis Venegas Leiva 2019079322	      	    #
#Ultima modificacion: 23/09/2020 21:00	    #
#############################################

def sumatoria_cubica(n):
	x=0
	for i in range(0,n+2):
		for j in range(1,i):
			for k in range(j,i+j):
				x=x+1
	#print(x)
	return x
def sumatoria_constante(n):
	x=0
	n=n-1
	x=(n*n*n+6*n*n+11*n+6)/3
	#print(x)
	return x
	
#n=3
#sumatoria_cubica(n)
#sumatoria_constante(n)
