# User Interface Menu

## Overview
This project, **User Interface Menu**, is a culmination of what I learned during my Python Advanced course. It is an interactive system designed to explore and manipulate fundamental data structures, showcasing both my understanding of core concepts and their practical implementation. The project includes a terminal-based interface and a graphical user interface (GUI) built with Tkinter.

### Key Features:
- **Linked List**: Dynamic list operations.
- **Stack**: LIFO (Last In, First Out) operations.
- **Queue**: FIFO (First In, First Out) operations.

Both the terminal and GUI versions allow for real-time data manipulation and visualization.

---

## Components

### 1. Linked List
- **File**: `LinkedList.py`
- **Features**:
  - Insert nodes at the beginning or end of the list.
  - Delete nodes by student ID.
  - Display all nodes with detailed student information.

### 2. Node
- **File**: `Node.py`
- **Description**:
  - Represents an individual node in a data structure.
  - Contains student data and a reference to the next node.

### 3. Queue
- **File**: `Queue.py`
- **Features**:
  - Enqueue (add) student nodes.
  - Dequeue (remove) nodes from the front.
  - Display the current state of the queue.

### 4. Stack
- **File**: `Stack.py`
- **Features**:
  - Push (add) student nodes onto the stack.
  - Pop (remove) nodes from the top.
  - Display the current state of the stack.

### 5. Student
- **File**: `Student.py`
- **Description**:
  - Represents a student with attributes:
    - Name
    - Gender
    - ID
    - Age

### 6. Terminal-Based Menu
- **File**: `UserInterfaceMenu.py`
- **Description**:
  - A command-line interface to:
    - Manage Linked List, Stack, and Queue.
    - Add, remove, and display student data interactively.

### 7. Graphical User Interface (GUI)
- **File**: `UserInterfaceMenuGUI.py`
- **Features**:
  - Intuitive GUI built with Tkinter.
  - Real-time visualization of data structures.
  - Interactive buttons for each operation (add, remove, display).

---

## How to Run

### Prerequisites
- Python 3.x

### Running the Terminal Version
```bash
python UserInterfaceMenu.py
```

### Running the GUI Version
```bash
python UserInterfaceMenuGUI.py
```

---

## Technologies Used
- **Programming Language**: Python
- **GUI Framework**: Tkinter

---

## Lessons Learned
This project has been a significant milestone in my Python Advanced course, helping me to:
- Understand and implement data structures like Linked List, Stack, and Queue.
- Work with object-oriented programming concepts such as classes and methods.
- Create interactive GUIs with Tkinter.
- Develop problem-solving skills through real-world scenarios.

---

## License
This project is licensed under the MIT License.
