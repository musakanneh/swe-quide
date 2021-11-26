class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        linked_list = ""

        while temp:
            linked_list += str(temp.data) + " -> "
            temp = temp.next
        print(linked_list)

    def insert(self, val, pos):
        target = Node(val)
        if pos == 0:
            target.next = self.head
            self.head = target
            return target


linked_list = LinkedList()
linked_list.head = Node(5)

node_two = Node(1)
node_three = Node(3)
node_four = Node(7)

linked_list.head.next = node_two
node_two.next = node_three
node_three.next = node_four

linked_list.print_list()
