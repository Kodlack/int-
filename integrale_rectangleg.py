#coding: UTF-8

import os

os.system('clear')



def methode_rectanglesga(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n):
		integrale += (hauteur * k + a)**2
	integrale = integrale*hauteur
	return integrale
	
print "Rectangle gauche integrale x**2 entre 0 et 1 avec n = 10: "
print methode_rectanglesga(0, 1, 10)
