#coding: UTF-8

import os
import math


os.system('clear')

def methode_mediantx3(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n):
		integrale += ((hauteur*(k+1) + hauteur*k + 2*a)/2)**3
	integrale *= hauteur
	return integrale
	
def methode_mediantsin(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n):
		integrale += math.sin((hauteur*(k+1) + hauteur*k + 2*a)/2)
	integrale *= hauteur
	return integrale
	
def methode_mediantln(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n):
		integrale += math.log((hauteur*(k+1) + hauteur*k + 2*a)/2)
	integrale *= hauteur
	return integrale



print "Mediant x**3 : "
print methode_mediantx3(0, 1, 10)

print "Mediant sin(x) : "
print methode_mediantsin(math.pi/2 *(-1), math.pi/2, 10)

print "Mediant ln(x) : "
print methode_mediantln(1, math.exp(1), 10)

print "Mediant ln(x) : "
print methode_mediantln(2, 5.0/2.0, 10)
