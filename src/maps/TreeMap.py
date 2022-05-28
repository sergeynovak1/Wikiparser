#from src.maps.BaseMap import BaseMap

class TreeMap:
	head = None

	class NodeTree:
		def __init__(self, key, element = None, left = None, right = None):
			self.element = element
			self.left = left
			self.right = right
			self.key = key

	def __init__(self, left = None, right = None):
		self.head = None
		self.right = right
		self.left = left
		self.root = None

	def __getitem__(self, key):
		node = self.head
		while node:
			if node.key == key:
				return node.element
			else:
				if node.key > key:
					node = node.right
				else:
					node = node.left

	def __setitem__(self, key, element):
		if not self.head:
			self.head = self.NodeTree(key, element)
			return element
		node = self.head
		prev_node = node
		while node:
			if (prev_node.key > key) and (node.key < key):
				prev_node.left = self.NodeTree(key, element, left = node)
			elif (prev_node.key < key) and (node.key > key):
				prev_node.right = self.NodeTree(key, element, right = node)
			else:
				if node.key > key:
					prev_node = node
					node = node.right
				else:
					prev_node = node
					node = node.left

	def __str__(self):
		def return_key_value(node):
			return f" {node.key} : {node.value}"

		def return_all(node):
			if node is None:
				return ' '
			return return_all(node.left) + return_key_value(node) + return_all(node.right)

		return return_all(self.root)
