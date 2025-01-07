#polynome sind listen aus int (oder float), in denen der lezte eintrag nicht 0 ist. An der k'ten stelle steht der koeffitien, von x^k, angefangen, bei k=0.

#eingabe: eine liste aus int, rückgabe: ein polynom 
def to_poynomial(polynomial: list):
	if polynomial==[]: return polynomial
	while polynomial[-1]==0:
		del polynomial[-1]
		if polynomial==[]: return polynomial
	return polynomial

#function that devids the leading terms of two polynomials and saves the the quotens of the two coifitions and the power of the variable
def quot_lt(divident: list, divisor: list):
	divident, divisior = to_poynomial(divident),to_poynomial(divisor)
	#spetial cases
	if divisior==[]:return False
	if len(divident)<len(divisor): return False
	#division
	return [divident[-1]/divisor[-1],len(divident)-len(divisor)]

#this function multipylys a polynom, given as a list and power product, given as a tupel [coiffitent,degree]. Gibt ein Polynom inform einer Liste zurück
def mult_polynom_and_powerproduct(powerproduct: list, polynom: list):
	if len(powerproduct)!=2: raise Exception(f"Powerproduct is suposed to have 2 elements: {powerproduct},{polynom}")
	prod = [i*powerproduct[0] for i in polynom]
	for i in range(powerproduct[1]):
		prod.insert(0,0)
	return prod 
	
#adds 2 polynomials
def add_polynomials(poly_1: list, poly_2: list):	
	#makes poly_1 to have a higher or equil order than poly_2
	if len(poly_2)>len(poly_1):
		poly_1,poly_2=poly_2,poly_1
	
	#adds polynomials compount whise
	for i in range(len(poly_2)):
		poly_1[i]+=poly_2[i]
	
	return poly_1
	
#takes a polynom and makes it to a readeble string
def polynom_in_string(polynom: list):
	if len(polynom)==0: return '0'
	if len(polynom)==1: return f'{polynom[0]}'
	sPoly = f'{polynom[-1]}x^{len(polynom)-1}'
	for i in reversed(range(len(polynom)-1)):
		if polynom[i] != 0 and i != 0: sPoly += f'+{polynom[i]}x^{i}'
		elif polynom[i] != 0 and i == 0: sPoly += f'+{polynom[i]}'
	return sPoly


def polynomendivision(divident: list, divisor: list):
	divident=to_poynomial(divident)
	divisor=to_poynomial(divisor)
	#Falls divisor 0 ist.
	if divisor==[]: return('Du Hund willst durch 0 teilen?')  
	
	#initalises the algorithem 
	q=[]
	r=divident.copy()
	
	#the actual algorithem 
	while len(divisor)<=len(r) and len(r)!=0:
		Quot_lt=quot_lt(r,divisor)
		q = add_polynomials(q,mult_polynom_and_powerproduct(Quot_lt,[1]))#könnte funktionieren
		r = add_polynomials(r,mult_polynom_and_powerproduct([-Quot_lt[0],Quot_lt[1]],divisor))
		#makes sure, that the list has the right format.
		q=to_poynomial(q)
		r=to_poynomial(r)
		
	return('The solution of ' + polynom_in_string(divident)+ ' divided by ' + polynom_in_string(divisor) + ' is ' + polynom_in_string(q) + ' whith a remainder ' + polynom_in_string(r))
			
		
	
	#return(q,r)

print(polynomendivision([1],[1,1]))

