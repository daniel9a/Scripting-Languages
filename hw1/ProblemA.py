class polynom():

	#initialize our polynomial
	def __init__(self, poly_in):
		self.poly = poly_in
		self.sanitize()

	#add two polynomials, returns polynom
	def __add__(self,other_polynom):
		#start by getting both lengths
		len1 = len(self.poly)
		len2 = len(other_polynom.poly)

		#set them to be the same size
		if(len1 >= len2):
			d_len = len1 - len2
			other_polynom.poly = d_len*[0] + other_polynom.poly
		else:
			d_len = len2 - len1
			self.poly = d_len*[0] + self.poly

		#generate list to pass output
		poly_out = []
		for i in range(len(self.poly)):
			poly_out.append(self.poly[i] + other_polynom.poly[i])

		#remove leading zeros
		p1.sanitize()
		p2.sanitize()

		#create output polynom
		output = polynom(poly_out)

		#return output
		return output

	#subtract other_polynom from self
	#return a polynom
	def __sub__(self,other_polynom):
		#start by getting both lengths
		len1 = len(self.poly)
		len2 = len(other_polynom.poly)

		#set them to be the same size
		if(len1 >= len2):
			d_len = len1 - len2
			other_polynom.poly = d_len*[0] + other_polynom.poly
		else:
			d_len = len2 - len1
			self.poly = d_len*[0] + self.poly

		#generate list to pass output
		poly_out = []
		for i in range(len(self.poly)):
			poly_out.append(self.poly[i] - other_polynom.poly[i])

		#remove leading zeros
		p1.sanitize()
		p2.sanitize()

		#create output polynom
		output = polynom(poly_out)

		#return output
		return output	

	#multiplies two polynoms, returns a polynom
	def __mul__(self,other_polynom):

		#generate list to pass to output
		poly_out = []
		#note that the length is the sum of both 
		for i in range(len(self.poly) + len(other_polynom.poly) - 1):
			poly_out.append(0);

		#progressivly loop through and multiply each digit in the first poly by each digit in the second
		for i in range(len(self.poly)):
			for j in range(len(other_polynom.poly)):
				poly_out[i+j] += self.poly[i] * other_polynom.poly[j]

		#polynom to be outputted
		output = polynom(poly_out)
		return output

	#Takes the derivative of the polynom, returns a polynom
	def drv(self):
		poly_out = []

		#For each item in a polynomial (that isn't the last one), multiply it's current exponent by itself
		#then in the new list shift it's position left

		for i in range(len(self.poly)):

			#check if last one
			if(i != (len(self.poly) - 1)):

				#multiple by current exponent and self, then add to new list.
				poly_out.append((len(self.poly) - 1 -i) * self.poly[i])

		output = polynom(poly_out)
		return output

	#integrates the polynomial over the range a to b, returns a floating point number
	def intg(self,a,b):
		output = 0

		#for each item in poly, add (b ^ exp +1) * (value/ exp) to output then sub the same thing with a
		for i in range(len(self.poly)):
			index = len(self.poly)-i
			output += (1.0/index) * self.poly[i] * (b**index+1)
			output -= (1.0/index) * self.poly[i] * (a**index+1)

		return output

	#remove leading zeros
	def sanitize(self):
		if(self.poly[0] == 0) and (len(self.poly) != 1):
			del self.poly[0]
			self.sanitize()
