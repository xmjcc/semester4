class Astronaut:
	max_astronaut = 5
	count = 0

	def __init__(self, name, nationality):
		'''constructor'''
		self.name = name
		self.nationality = nationality
		self.id = Astronaut.count
		Astronaut.count += 1

	def __str__(self):
		'''overrideing the print method'''
		return str(self.id) + ' ' + self.name + ' ' + self.nationality + ' ' + str(Astronaut.max_astronaut)

a = Astronaut('Neil', 'Usa') 
b = Astronaut('Yuri', 'Russian')
c = Astronaut('Chri', 'Canadian')
print(a)
print(b)
print(c)