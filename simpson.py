#coding: UTF-8

import os
import math


os.system('clear')

def methode_simpson(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	S1 = 0
	S2= (a+hauteur/2)**2
	for k in range(1,n):
		S1 += (hauteur*k + a)**2
		S2 += (hauteur*(2*k+1)/2 + a)**2
	integrale = 2*S1 + 4*S2
	integrale += a**2 + b**2
	integrale *=hauteur/6
	return integrale
	
def methode_simpsonln(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	S1 = 0
	S2= math.log((a+hauteur/2))
	for k in range(1,n):
		S1 += math.log((hauteur*k + a))
		S2 += math.log((hauteur*(2*k+1)/2 + a))
	integrale = 2*S1 + 4*S2
	integrale += math.log(a) + math.log(b)
	integrale *=hauteur/6
	return integrale
	
print "Methode simpson x**2 n =10 :"
print methode_simpson(0, 1, 10)

print "Methode simpson ln(x) n = 10"
print methode_simpsonln(2, 5.0/2.0, 10)
