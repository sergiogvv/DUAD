colors = [
	'black',
	'yellow',
	'red',
	'blue',
]

for color in colors:
	if color == 'yellow' or color == 'red':
		continue

	print(color)
	
first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list)
print(first_list)