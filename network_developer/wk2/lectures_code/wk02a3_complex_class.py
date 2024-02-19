import math

class Complex:

	def __init__(self, real, imaginary):
		'''constructor'''
		self.real = real
		self.imaginary = imaginary

	def __str__(self):
		'''overrides the str method'''
		return '[%d, %d]' % (self.real, self.imaginary)

	def __add__(self, other):
		'''overloads the + operator'''
		return Complex(self.real + other.real, self.imaginary + other.imaginary)

	def __eq__(self, other):
		'''overloads the == operator'''
		return self.real == other.real and self.imaginary == other.imaginary

	@property
	def argument(self):
		'''trying to do a property'''
		return math.atan(self.real / self.imaginary)


if __name__ == '__main__':
	'''the above checks if this is being used as a program'''
	print('Testing the complex class')
	a = Complex(1, 3)
	b = Complex(1, 3)
	print('a: %s and b: %s' % (a, b))

	c = a + b
	print('%s + %s = %s' % (a, b, c))

	print('%s %s %s' % (a, '==' if a == b else '!=', b))
	print('%s %s %s' % (a, '==' if a == c else '!=', c))
	print(f'{a} is same as {c} {a == c}')
