from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, student):
        new_node = Node(student)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, student):
        new_node = Node(student)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(new_node)

    def delete_by_id(self, student_id):
        if not self.head:
            print("The linked list is empty.")
            return
        if self.head.get_data().get_student_id() == student_id:
            self.head = self.head.get_next()
            print(f"Student with ID {student_id} has been deleted.")
            return
        current = self.head
        prev = None
        while current and current.get_data().get_student_id() != student_id:
            prev = current
            current = current.get_next()
        if not current:
            print(f"Student with ID {student_id} not found.")
            return
        prev.set_next(current.get_next())
        print(f"Student with ID {student_id} has been deleted.")

    def display(self):
        if not self.head:
            print("The linked list is empty.")
            return
        current = self.head
        print("Students in Linked List:")
        while current:
            print(current.get_data())
            current = current.get_next()
