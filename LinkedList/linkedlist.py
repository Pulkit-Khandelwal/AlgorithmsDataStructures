"""

Author: Pulkit Khandelwal
Credits: https://github.com/donnemartin/interactive-coding-challenges

"""


class Node(object):

	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return self.data
		

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head


	def __len__(self):
		curr = self.head

		counter = 0
		while curr is not None:
			counter+=1
			curr = curr.next_node
		return counter

	def insert_to_front(self, data):

		if data is None:
			return None

		if self.head is None:
			self.head = Node(data, next_node=None)

		node = Node(data, self.head)
		self.head = node

		return node

	def append(self, data):
		if data is None:
			return None
		node = Node(data, next_node = None)
		# the curr_node keeps track of the previous nodes starting from the head node
		if self.head is None:
			self.head = node
			return node
		curr_node = self.head
		while curr_node.next_node is not None:
			curr_node = curr_node.next_node

		curr_node.next_node = node

		return node

	def find(self, data):
		if data is None:
			return None

		if self.head is None:
			return self.head

		curr_node = self.head
		while curr_node.next_node is not None:
			if curr_node.data == data:
				return curr_node
			curr_node = curr_node.next_node


	def delete(self, data):
		if data is None:
			return

		if self.head is None:
			return

		if self.head.data == data:
			self.head = self.head.next_node
			return

		curr_node = self.head
		while curr_node.next_node is not None:
			if curr_node.next_node.data == data:
				curr_node.next_node = curr_node.next_node.next_node
				return curr_node.next_node
			curr_node = curr_node.next_node


	def get_all_data(self):
		if self.head is None:
			return []
		all_data = []
		curr_node = self.head
		while curr_node is not None:
			all_data.append(curr_node.data)
			curr_node = curr_node.next_node
		return all_data

	def print_list(self):
		curr_node = self.head
		if self.head is None:
			print('It is an empty linked list!')
		while curr_node is not None:
			print(curr_node.data)
			curr_node = curr_node.next_node


	def remove_dupes(self):
		if self.head is None:
			return None

		if self.head.next_node is None:
			return None
			
		new_dict = {}
		curr_node = self.head
		new_dict[curr_node.data] = 1

		while curr_node.next_node is not None:
			next_data = curr_node.next_node.data

			if next_data not in new_dict:
				new_dict[next_data] = 1
				curr_node = curr_node.next_node

			else:
				new_dict[next_data] += 1

			if new_dict[next_data] > 1:
				#delete the node and then decrement the value of the counter
				#for that key
				curr_node.next_node = curr_node.next_node.next_node
				new_dict[next_data] -= 1
				#curr_node = curr_node.next_node
		return curr_node



	def kth_to_last_elem(self, k):
		pass

	def reverse_linked_list(self):
		#In place reverse a linked list
		if self.head is None:
			return None

		if self.head.next_node is None:
			return self.head

		prev_node = self.head
		curr_node = prev_node.next_node
		prev_node.next_node = None

		temp = curr_node.next_node
		while temp is not None:
			temp = curr_node.next_node

			curr_node.next_node = prev_node
			prev_node = curr_node

			if temp is None:
				self.head = curr_node
				return temp
			else:
				curr_node = temp

		return prev_node

			







if __name__ == '__main__':
	new_list = LinkedList(None)
	print 'original linked list'
	new_list.append(3)
	new_list.insert_to_front(6)
	new_list.append(4)
	new_list.append(5)
	new_list.append(11)

	new_list.append(3)
	new_list.append(8)
	new_list.append(7)
	new_list.append(7)
	new_list.append(9)
	new_list.append(9)
	new_list.append(9)
	new_list.append(9)
	new_list.append(4)
	new_list.append(1)



	new_list.print_list()

	new_list.remove_dupes()
	print 'removed duplicates'
	new_list.print_list()

	print 'reversed linked list'
	new_list.reverse_linked_list()
	new_list.print_list()

	print 'length of linked list'
	print len(new_list)




