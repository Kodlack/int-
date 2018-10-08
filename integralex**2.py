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

def methode_rectanglesdr(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n+1):
		integrale += (hauteur * k + a)**2
	integrale = integrale * hauteur
	return integrale

def methode_mediant(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n):
		integrale += ((hauteur*(k+1) + hauteur*k + 2*a)/2)**2
	integrale *= hauteur
	return integrale

print "Rectangle gauche : "
print methode_rectanglesga(0, 1, 10)
print "Rectangle droit : "
print methode_rectanglesdr(0, 1, 10)
print "Mediant : "
print methode_mediant(0, 1, 10)



