# User Interface Menu

## Overview
The **User Interface Menu** is an interactive Python project that provides a user-friendly interface to explore and manipulate fundamental data structures:

- **Linked List**
- **Stack**
- **Queue**

The application supports two modes:
1. **Terminal-Based Interface**: For direct interaction through the command line.
2. **Graphical User Interface (GUI)**: A visually intuitive system built with Tkinter to demonstrate real-time operations on data structures.



---

## Features

### Linked List
- Insert nodes at the beginning or end of the list.
- Delete nodes by student ID.
- Display all nodes with detailed student information:
  - **Name**
  - **Gender**
  - **ID**
  - **Age**

### Stack
- Push student nodes onto the stack.
- Pop the top node off the stack.
- Display all nodes with complete student details.

### Queue
- Enqueue student nodes into the queue.
- Dequeue the front node from the queue.
- Display all nodes with detailed information.

### Graphical User Interface (GUI)
- **Modern Design**: Built using Tkinter for an intuitive experience.
- **Dynamic Real-Time Updates**:
  - Adding nodes.
  - Deleting nodes.
  - Displaying the current state of the data structure.
- Maintains data integrity and visualization when navigating menus.

### Error Handling
- Validates user input (e.g., name, gender, ID, age).
- Handles invalid operations gracefully (e.g., deleting from an empty stack or queue).

---

## Technologies Used
- **Programming Language**: Python
- **Modules**:
  - `tkinter` for GUI development.
  - Custom implementations for:
    - `LinkedList`
    - `Stack`
    - `Queue`
    - `Node`
    - `Student`

---

## How to Run

### Requirements
- Python 3.x installed on your system.

### Running the Terminal Version
```bash
python UserInterfaceMenu.py
