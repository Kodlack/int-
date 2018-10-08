#coding: UTF-8

import os
import math

def methode_trapezesx(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(1,n):
		integrale += (hauteur*k + a)**3
	integrale *= 2
	integrale +=a**3 + b**3
	integrale *= hauteur*0.5
	return integrale
	
def methode_trapezescos(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(1,n):
		integrale += math.cos(hauteur*k + a)
	integrale *= 2
	integrale +=math.cos(a) + math.cos(b)
	integrale *= hauteur*0.5
	return integrale
	
def methode_trapezesexp(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(1,n):
		integrale += math.exp(-(hauteur*k + a))
	integrale *= 2
	integrale +=math.exp(-a) + math.exp(-b)
	integrale *= hauteur*0.5
	return integrale

print "Methode trapezes x**3 : "
print methode_trapezesx(0, 1, 10)

print "Methode trapezes cos(x)	 : "
print methode_trapezescos(0, math.pi/2, 10)

print "Methode trapezes exp(-x) n=10: "
print methode_trapezesexp(0, 50, 10)

print "Methode trapezes exp(-x) n=1000: "
print methode_trapezesexp(0, 50, 1000)




