from abc import ABC, abstractmethod


class Shape(ABC):
	@abstractmethod 
	def calculate_perimeter(self):
		pass 

	@abstractmethod 
	def calculate_area(self):
		pass


class Circle(Shape):
	def __init__(self,radius):
		self.radius = radius    

	def calculate_perimeter(self):
		perimeter = 2 * self.radius * 3.14
		print(f'Perimeter (circuference) is {perimeter}')

	def calculate_area(self):
		area = self.radius**2 * 3.14
		print(f'Area is {area}')


class Square(Shape):
	def __init__(self,side):
		self.side = side    

	def calculate_perimeter(self):
		perimeter = 4 * self.side
		print(f'Perimeter is {perimeter}')

	def calculate_area(self):
		area = self.side**2
		print(f'Area is {area}')
		


class Rectangle(Shape):
	def __init__(self,length,width):
		self.length = length
		self.width = width    

	def calculate_perimeter(self):
		perimeter = 2 * self.length + 2 * self.width
		print(f'Perimeter is {perimeter}')

	def calculate_area(self):
		area = self.length * self.width
		print(f'Area is {area}')


my_circle = Circle(5)
my_circle.calculate_perimeter()
my_circle.calculate_area()
print()
my_square = Square(5)
my_square.calculate_perimeter()
my_square.calculate_area()
print()
my_rectangle = Rectangle(4,5)
my_rectangle.calculate_perimeter()
my_rectangle.calculate_area()

