class Circle:
	def __init__(self, radius):
		self.radius = radius

	
	def get_area(self):
		self.area = 3.1415 * self.radius**2
		print(self.area)


my_circle = Circle(5)
my_circle.get_area()
print()