class Head:
	def __init__(self):
		pass


class Torso:
	def __init__(self, head, right_arm, right_leg, left_arm, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.right_leg = right_leg
		self.left_arm = left_arm
		self.left_leg = left_leg


class Arm:
	def __init__(self, hand):
		self.hand = hand


class Hand:
	def __init__(self):
		pass


class Leg:
	def __init__(self, foot):
		self.foot = foot


class Foot:
	def __init__(self):
		pass


class Human:
	def __init__(self, torso):
		self.torso = torso


right_hand = Hand()
right_arm = Arm(right_hand)
left_hand = Hand()
left_arm = Arm(left_hand)
right_foot = Foot()
right_leg = Leg(right_foot)
left_foot = Foot()
left_leg = Leg(left_foot)
head = Head()
torso = Torso(head, right_arm, right_leg, left_arm, left_leg)
human = Human(torso)