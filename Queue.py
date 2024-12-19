from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, student):
        new_node = Node(student)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.set_next(new_node)
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("The queue is empty.")
            return None
        dequeued_student = self.front.get_data()
        self.front = self.front.get_next()
        if not self.front:
            self.rear = None
        return dequeued_student

    def display(self):
        if not self.front:
            print("The queue is empty.")
            return
        current = self.front
        print("Students in Queue:")
        while current:
            print(current.get_data())
            current = current.get_next()
