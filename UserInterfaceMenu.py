from Student import Student
from LinkedList import LinkedList
from Stack import Stack
from Queue import Queue

def get_student_input():
    try:
        name = input("Enter name: ").strip()
        gender = input("Enter gender: ").strip()
        student_id = int(input("Enter ID: "))
        age = int(input("Enter age: "))
        return Student(name, gender, student_id, age)
    except ValueError:
        print("Invalid input. Please enter valid data.")
        return None

def linked_list_menu():
    linked_list = LinkedList()
    while True:
        print("\nLinked List Menu:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete by ID")
        print("4. Display")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student = get_student_input()
            if student:
                linked_list.insert_at_beginning(student)
        elif choice == "2":
            student = get_student_input()
            if student:
                linked_list.insert_at_end(student)
        elif choice == "3":
            try:
                student_id = int(input("Enter ID to delete: "))
                linked_list.delete_by_id(student_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "4":
            linked_list.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def stack_menu():
    stack = Stack()
    while True:
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student = get_student_input()
            if student:
                stack.push(student)
        elif choice == "2":
            student = stack.pop()
            if student:
                print(f"Popped: {student}")
        elif choice == "3":
            stack.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def queue_menu():
    queue = Queue()
    while True:
        print("\nQueue Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student = get_student_input()
            if student:
                queue.enqueue(student)
        elif choice == "2":
            student = queue.dequeue()
            if student:
                print(f"Dequeued: {student}")
        elif choice == "3":
            queue.display()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Linked List")
        print("2. Stack")
        print("3. Queue")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            linked_list_menu()
        elif choice == "2":
            stack_menu()
        elif choice == "3":
            queue_menu()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
