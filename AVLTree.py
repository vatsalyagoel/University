import pdb
class AVLTreeNode:
	def __init__(self, item=None):
		self.item = item
		self.left = None
		self.right = None
		self.height = 0
	def __str__(self):
		return str(self.item)
class AVLTree:
	#pdb.set_trace()
	def __init__(self):
		self.root = None
	def reset(self):
		self.__init__()
	def is_empty(self):
		return self.root is None
	def insert(self, item):
		self.root = self.insert_aux(self.root, item)
	def insert_aux(self, current, item):
		if current is None:
			current = AVLTreeNode(item)
		elif item < current.item:
			current.left = self.insert_aux(current.left, item)
			if self.calc_height(current.left) - self.calc_height(current.right) == 2:
				if item < current.left.item:
					current = self.rotate_left(current)
				else:
					current=self.double_left(current)
		elif item > current.item:
			current.right = self.insert_aux(current.right, item)
			if self.calc_height(current.right) - self.calc_height(current.left) == 2:
				if item > current.right.item:
					current = self.rotate_right(current)
				else:
					current=self.double_right(current)
					print("here")
					self.print_in_order()
					#self.search_print(current.item)
					#print(current.item,current.left.item,current.right.item)
					#self.assign(n)
		current.height=max(self.calc_height(current.left),self.calc_height(current.right))+1
		#current.height=self.max_height_aux(current)
		return current
	def assign(self, node):
		self.root = self.assign_aux(self.root, node)

	def assign_aux(self, current, node):
		#self.print_in_order_aux(node)
		if current is not None:
			print("here",current.item)
		if current is None:
			print(node)
			current = node
			print(current.item,current.left.item,current.right.item)
		elif node.item < current.item:
			current.left = self.assign_aux(current.left, node)
		elif node.item > current.item:
			current.right = self.assign_aux(current.right, node)
		return current
	def calc_height(self,current):
		if current is None:
			return -1
		else:
			return current.height
	def rotate_left(self,current):
		#print(current.item)
		#print("here"+str(current.left.item))
		#tree.search_print(40)
		temp = current.left
		current.left = temp.right
		#tree.search_print(100)
		temp.right=current
		current=temp
		#print(temp.right.item)
		current.height=max(self.calc_height(current.left),self.calc_height(current.right))+1
		temp.height=max(self.calc_height(temp.left),self.calc_height(temp.right))+1
		return current
	def rotate_right(self,current):
		temp = current.right
		current.right = temp.left
		temp.left=current
		current=temp
		temp.height=max(self.calc_height(temp.left),self.calc_height(temp.right))+1
		current.height=max(self.calc_height(current.left),self.calc_height(current.right))+1
		return current
	def double_left(self,current):
		current.left=self.rotate_right(current.left)
		current=self.rotate_left(current)
		return current
	def double_right(self,current):
		#print(current)
		#tree.search_print(40)
		current.right=self.rotate_left(current.right)
		current=self.rotate_right(current)
		return current
	def search(self,item):
		return self.search_aux(self.root,item)
	def search_aux(self, current,item):
		# base case: empty
		if current is None:
			raise KeyError("Item  not found")
		# base case: found
		elif item == current.item:
			return True
		elif item < current.item:
			return self.search_aux(current.left, item)
		# item> current.item
		else:
			return self.search_aux(current.right, item)
	
	def search_print(self,item):
		return self.search_print_aux(self.root,item)
	def search_print_aux(self,current,item,string=""):
		# base case: empty
		if current is None:
			print("Item  not found")
		# base case: found
		elif item == current.item:
			string=string+str(current.item)+','+str(current.height)
			print(string)
		elif item < current.item:
			string=string+str(current.item)+','+str(current.height)+'  -> '
			self.search_print_aux(current.left, item,string)
		elif item > current.item:
			string=string+str(current.item)+','+str(current.height) + '  -> '
			self.search_print_aux(current.right, item,string)			
	def print_in_order(self):
		self.print_in_order_aux(self.root)
	def print_in_order_aux(self,current):
		if current is not None:
			self.print_in_order_aux(current.left)
			print(current.item)
			self.print_in_order_aux(current.right)
if __name__ == '__main__':
	#traceback.print_stack()
	tree=AVLTree()
	tree.insert(12)
	tree.search_print(12)
	tree.insert(20)
	tree.search_print(20)
	tree.insert(2)
	tree.search_print(2)
	tree.insert(100)
	tree.search_print(100)
	tree.insert(40)
	tree.search_print(40)
	tree.search_print(100)
	#tree.print_in_order()
	#print(tree.root.height)
