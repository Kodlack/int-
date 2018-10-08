def methode_rectanglesdr(a, b, n):
	integrale = 0.0
	hauteur = float(b-a)/n
	for k in range(n+1):
		integrale += (hauteur * k + a)**2
	integrale = integrale * hauteur
	return integrale

print "Rectangle droit pour x**2 avec n = 10 : "
print methode_rectanglesdr(0, 1, 10)
