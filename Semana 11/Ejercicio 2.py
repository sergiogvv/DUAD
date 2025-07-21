class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0


class Bus:
	passengers = 0

	def __init__(self, max_passengers):
		self.max_passengers = max_passengers
		print(f'Se ha creado un bus de {max_passengers} pasajeros')
		
	def add_passenger(self,person):
		if self.passengers < self.max_passengers:
			self.passengers += 1
			print(f'Un pasajero se está subiendo al bus')
		else:
			print("Lo sentimos, este bus va lleno. Por favor espere al siguiente")

	def unboard_passeger(self):
		if self.passengers > 0:
			self.passengers -= 1
			print(f"Parada solicitada, un pasajero se está bajando del bus")
		else:
			print(f"Este bus va vacío")


person_1 = Person('Sergio')
person_2 = Person('Gabriel')
person_3 = Person('Adriana')
person_4 = Person('Marcela')
person_5 = Person('Replicante 1')
print()
my_bus = Bus(54)
print()
my_bus.add_passenger(person_1)
my_bus.add_passenger(person_2)
my_bus.add_passenger(person_3)
my_bus.add_passenger(person_4)
print(f'\nCantidad de pasajeros en este bus: {my_bus.passengers}')
my_bus.unboard_passeger()
my_bus.unboard_passeger()
my_bus.unboard_passeger()
my_bus.unboard_passeger()
print(f'\nCantidad de pasajeros en este bus: {my_bus.passengers}')
my_bus.unboard_passeger()
print()
very_small_bus = Bus(4)
very_small_bus.add_passenger(person_1)
very_small_bus.add_passenger(person_2)
very_small_bus.add_passenger(person_3)
very_small_bus.add_passenger(person_4)
very_small_bus.add_passenger(person_5)




