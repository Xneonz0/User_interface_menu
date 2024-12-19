#for the lols
import tkinter as tk
from tkinter import simpledialog, messagebox
from LinkedList import LinkedList
from Stack import Stack
from Queue import Queue
from Student import Student

class UserInterfaceMenuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User Interface Menu")
        self.root.geometry("1000x600")
        self.root.configure(bg="#2E3440")

        # Persistent data structures
        self.linked_list = LinkedList()
        self.stack = Stack()
        self.queue = Queue()

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Data Structures Visualizer", font=("Helvetica", 20), bg="#2E3440", fg="#D8DEE9").pack(pady=20)
        tk.Button(self.root, text="Linked List", command=self.linked_list_menu, font=("Helvetica", 14), bg="#4C566A", fg="#ECEFF4", width=20).pack(pady=10)
        tk.Button(self.root, text="Stack", command=self.stack_menu, font=("Helvetica", 14), bg="#4C566A", fg="#ECEFF4", width=20).pack(pady=10)
        tk.Button(self.root, text="Queue", command=self.queue_menu, font=("Helvetica", 14), bg="#4C566A", fg="#ECEFF4", width=20).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.destroy, font=("Helvetica", 14), bg="#BF616A", fg="#ECEFF4", width=20).pack(pady=10)

    def linked_list_menu(self):
        self.sub_menu("Linked List", self.linked_list_controls, self.ll_display)

    def stack_menu(self):
        self.sub_menu("Stack", self.stack_controls, self.stack_display)

    def queue_menu(self):
        self.sub_menu("Queue", self.queue_controls, self.queue_display)

    def sub_menu(self, title, control_func, display_func):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=title, font=("Helvetica", 20), bg="#2E3440", fg="#D8DEE9").pack(pady=20)
        self.canvas = tk.Canvas(self.root, bg="#3B4252", height=300, width=900)
        self.canvas.pack(pady=20)
        control_func()
        display_func()  # Automatically display the current state

    def linked_list_controls(self):
        frame = tk.Frame(self.root, bg="#2E3440")
        frame.pack(pady=20)
        tk.Button(frame, text="Insert at Beginning", command=self.ll_insert_beginning, font=("Helvetica", 12), bg="#5E81AC", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Insert at End", command=self.ll_insert_end, font=("Helvetica", 12), bg="#5E81AC", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Delete by ID", command=self.ll_delete_by_id, font=("Helvetica", 12), bg="#BF616A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Display", command=self.ll_display, font=("Helvetica", 12), bg="#A3BE8C", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Back", command=self.main_menu, font=("Helvetica", 12), bg="#4C566A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)

    def stack_controls(self):
        frame = tk.Frame(self.root, bg="#2E3440")
        frame.pack(pady=20)
        tk.Button(frame, text="Push", command=self.stack_push, font=("Helvetica", 12), bg="#5E81AC", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Pop", command=self.stack_pop, font=("Helvetica", 12), bg="#BF616A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Display", command=self.stack_display, font=("Helvetica", 12), bg="#A3BE8C", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Back", command=self.main_menu, font=("Helvetica", 12), bg="#4C566A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)

    def queue_controls(self):
        frame = tk.Frame(self.root, bg="#2E3440")
        frame.pack(pady=20)
        tk.Button(frame, text="Enqueue", command=self.queue_enqueue, font=("Helvetica", 12), bg="#5E81AC", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Dequeue", command=self.queue_dequeue, font=("Helvetica", 12), bg="#BF616A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Display", command=self.queue_display, font=("Helvetica", 12), bg="#A3BE8C", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Back", command=self.main_menu, font=("Helvetica", 12), bg="#4C566A", fg="#ECEFF4").pack(side=tk.LEFT, padx=10)

    def ll_insert_beginning(self):
        student = self.get_student_input()
        if student:
            self.linked_list.insert_at_beginning(student)
            self.ll_display()

    def ll_insert_end(self):
        student = self.get_student_input()
        if student:
            self.linked_list.insert_at_end(student)
            self.ll_display()

    def ll_delete_by_id(self):
        student_id = self.get_student_id_input()
        if student_id is not None:
            self.linked_list.delete_by_id(student_id)
            self.ll_display()

    def ll_display(self):
        self.canvas.delete("all")
        current = self.linked_list.head
        x, y = 50, 150
        spacing = 150  # Consistent spacing
        while current:
            self.canvas.create_rectangle(x, y, x + 120, y + 60, fill="#A3BE8C", outline="#ECEFF4")
            student_details = (
                f"Name: {current.get_data().get_name()}\n"
                f"Gender: {current.get_data().get_gender()}\n"
                f"ID: {current.get_data().get_student_id()}\n"
                f"Age: {current.get_data().get_age()}"
            )
            self.canvas.create_text(x + 60, y + 30, text=student_details, fill="#2E3440")
            if current.get_next():
                self.canvas.create_line(x + 120, y + 30, x + spacing, y + 30, arrow=tk.LAST, fill="#ECEFF4")
            current = current.get_next()
            x += spacing

    def stack_push(self):
        student = self.get_student_input()
        if student:
            self.stack.push(student)
            self.stack_display()

    def stack_pop(self):
        self.stack.pop()
        self.stack_display()

    def stack_display(self):
        self.canvas.delete("all")
        current = self.stack.top
        x, y = 450, 250
        spacing = 60  # Consistent vertical spacing
        while current:
            self.canvas.create_rectangle(x, y, x + 120, y - 60, fill="#5E81AC", outline="#ECEFF4")
            student_details = (
                f"Name: {current.get_data().get_name()}\n"
                f"Gender: {current.get_data().get_gender()}\n"
                f"ID: {current.get_data().get_student_id()}\n"
                f"Age: {current.get_data().get_age()}"
            )
            self.canvas.create_text(x + 60, y - 30, text=student_details, fill="#ECEFF4")
            current = current.get_next()
            y -= spacing

    def queue_enqueue(self):
        student = self.get_student_input()
        if student:
            self.queue.enqueue(student)
            self.queue_display()

    def queue_dequeue(self):
        self.queue.dequeue()
        self.queue_display()

    def queue_display(self):
        self.canvas.delete("all")
        current = self.queue.front
        x, y = 50, 150
        spacing = 150  # Consistent horizontal spacing
        while current:
            self.canvas.create_rectangle(x, y, x + 120, y + 60, fill="#88C0D0", outline="#ECEFF4")
            student_details = (
                f"Name: {current.get_data().get_name()}\n"
                f"Gender: {current.get_data().get_gender()}\n"
                f"ID: {current.get_data().get_student_id()}\n"
                f"Age: {current.get_data().get_age()}"
            )
            self.canvas.create_text(x + 60, y + 30, text=student_details, fill="#2E3440")
            current = current.get_next()
            x += spacing

    def get_student_input(self):
        try:
            name = simpledialog.askstring("Input", "Enter student's name:", parent=self.root)
            gender = simpledialog.askstring("Input", "Enter student's gender:", parent=self.root)
            student_id = simpledialog.askinteger("Input", "Enter student's ID:", parent=self.root)
            age = simpledialog.askinteger("Input", "Enter student's age:", parent=self.root)
            if name and gender and student_id and age:
                return Student(name, gender, student_id, age)
            else:
                messagebox.showerror("Error", "All fields are required!")
                return None
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")
            return None

    def get_student_id_input(self):
        try:
            return simpledialog.askinteger("Input", "Enter student's ID:", parent=self.root)
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")
            return None

if __name__ == "__main__":
    app = UserInterfaceMenuGUI()
    app.root.mainloop()
