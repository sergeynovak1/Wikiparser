CONST_TO_INCREASE = 0.8

class LinkedList:
	head = None

	class NodeHash:
		def __init__(self, key, element = None, next_node = None):
			self.element = element
			self.next_node = next_node
			self.key = key

	class NodeTree:
		def __init__(self, key, element = None, left = None, right = None):
			self.element = element
			self.left = left
			self.right = right
			self.key = key


	def append(self, key, element):
		if not self.head:
			self.head = self.NodeHash(key, element)
			return element
		node = self.head
		while node.next_node:
			node = node.next_node
		node.next_node = self.NodeHash(key, element)

	def insert(self, key, element, index):
		k = 0
		node = self.head
		while k < index:
			prev_node = node
			node = node.next_node
			k += 1
		prev_node.next_node = self.NodeHash(key, element, next_node = node)

	def delite(self, index):
		k = 0
		node = self.head
		while k < index:
			prev_node = node
			node = node.next_node
			k += 1
		prev_node.next_node = node.next_node

	def delkey(self, key):
		if self.head.key == key:
			self.head = self.head.next_node
		else:
			node = self.head
			prev_node = node
			while node.next_node and node.next_node.key != key:
				prev_node = node
				node = node.next_node
			if node.next_node.key == key:
				prev_node = node
				node = node.next_node
				prev_node.next_node = node.next_node

	#хэш совпал --> ключ совпал --> запись значения по ключу
	def check_key(self, key, element):
		node = self.head
		while node:
			if node.key == key:
				node.element = element
				return True
			node = node.next_node

	def __iter__(self):
		self.node = self.head
		return self

	def __next__(self):
		if self.node is not None:
			x = self.node.element
			self.node = self.node.next_node
			return x
		else:
			raise StopIteration


	def __str__(self):
		node = self.head
		values = []
		while node is not None:
			values.append(str(node.element))
			node = node.next_node
		return ' -> '.join(values)

class HashMap:
	def __init__(self, _size=100):
		self._inner_list = []
		for _ in range(_size):
			a = LinkedList()
			self._inner_list.append(a)
		self._size = _size
		self._cnt = 0


	def __getitem__(self, key):
		linked_list = self._inner_list[hash(key) % self._size]
		node = linked_list.head
		while node:
			if node.key == key:
				return node.element
			node = node.next_node

	def get_cnt(self):
		return self._cnt
	def get_list(self):
		return self._inner_list
	def __setitem__(self, key, value):
		self._inner_list[hash(key) % self._size].append(key, value)
		self._cnt += 1
		# увеличиваем массив
		if self._size * CONST_TO_INCREASE >= self._cnt:
			self._size *= 2
			new_inner_list = []
			for _ in range(self._size):
				a = LinkedList()
				new_inner_list.append(a)
			for elem in self._inner_list:
				node = elem.head
				while node:
					new_inner_list[hash(node.key) % self._size].append(node.key, node.element)
					node = node.next_node
			self._inner_list = new_inner_list

	def __delitem__(self, key):
		self._inner_list[hash(key) % self._size].delkey(key)
		self._cnt -= 1

	def __str__(self):
		mas = []
		for i in range(len(self._inner_list)):
			node = self._inner_list[i].head
			values = []
			while node is not None:
				values.append(str(node.element))
				node = node.next_node
			if len(values) == 0:
				mas.append(f'No elements with hash-key "{i}"')
			else:
				a = ' --> '.join(values)
				b = f'Elements with hash-key "{i}" \t'
				mas.append(f'{b} {a}')
		return '\n'.join(map(str, mas))

class TreeMap:
	head = None
	class NodeTree:
		def __init__(self, key, element = None, left = None, right = None):
			self.element = element
			self.left = left
			self.right = right
			self.key = key

	def __init__(self, left = None, right = None):
		self.list = []
		self.head = None
		self.right = right
		self.left = left

	def __getitem__(self, key):
		node = self.head
		while node:
			if node.key == key:
				return node.element
				break
			else:
				if node.key < key:
					node = node.right
				else:
					node = node.left

	def get_list(self):
		return self.list
	def __setitem__(self, key, element):
		if not self.head:
			self.head = self.NodeTree(key, element)
			self.list.append(key)
		else:
			node = self.head
			prev_node = node
			while node:
				if (prev_node.key > key) and (node.key < key):
					prev_node.left = self.NodeTree(key, element, left = node)
					self.list.append(key)
					break
				elif (prev_node.key < key) and (node.key > key):
					prev_node.right = self.NodeTree(key, element, right = node)
					self.list.append(key)
					break
				else:
					if node.key < key:
						if node.right is not None:
							prev_node = node
							node = node.right
						else:
							node.right = self.NodeTree(key, element)
							self.list.append(key)
							break
					else:
						if node.left is not None:
							prev_node = node
							node = node.left
						else:
							node.left = self.NodeTree(key, element)
							self.list.append(key)
							break

	def __str__(self):
		def retur_key(node):
			return f" {node.key}:{node.element} "
		def return_all(node):
			if node is None:
				return ''
			return return_all(node.left) + retur_key(node) + return_all(node.right)
		return return_all(self.head)
