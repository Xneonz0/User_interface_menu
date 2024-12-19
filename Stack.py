from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, student):
        new_node = Node(student)
        new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        if not self.top:
            print("The stack is empty.")
            return None
        popped_student = self.top.get_data()
        self.top = self.top.get_next()
        return popped_student

    def display(self):
        if not self.top:
            print("The stack is empty.")
            return
        current = self.top
        print("Students in Stack:")
        while current:
            print(current.get_data())
            current = current.get_next()
