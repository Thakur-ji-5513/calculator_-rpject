# DLL-Based Calculator Project

This project is a cross-language calculator application, where the core arithmetic operations are implemented in **C** and exposed through a DLL, while the user interface and interaction are managed using **Python** and the **Tkinter** library.

## Features
- Perform basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Power (`^`)
- User-friendly GUI built with Tkinter.
- Cross-language functionality using Python for the frontend and C for backend computations.
- Error handling for invalid inputs and division by zero.

## How It Works
1. The **C code** implements the arithmetic functions (`add`, `sub`, `mult`, `my_div`, and `power`) and compiles them into a DLL file.
2. The **Python code** uses the `ctypes` library to load the DLL and call its functions.
3. A Tkinter-based GUI allows users to input two numbers, select an operation, and see the result.

## Technologies Used
- **C**: For implementing the core arithmetic functions.
- **Python**: For the GUI and integration with the DLL.
- **Tkinter**: For building the graphical user interface.

## Installation
### Prerequisites
- Python 3.x installed on your system.
- A C compiler (e.g., GCC) to build the DLL file.
- `tkinter` (included with Python standard library).

### Steps
1. **Compile the C Code**
   - Use the following command to compile the C code into a DLL file:
     ```bash
     gcc -shared -o calculator.dll calculator.c
     ```
   - Ensure the `calculator.dll` file is in the same directory as your Python script.

2. **Run the Python Script**
   - Execute the Python script to start the calculator GUI:
     ```bash
     python calculator.py
     ```

## How to Use
1. Launch the application by running the `calculator.py` script.
2. Enter the first and second numbers in the input fields.
3. Select the desired operation (`+`, `-`, `*`, `/`, `^`) from the dropdown menu.
4. Click the **"Calculate"** button to see the result.

## Screenshots
![image](https://github.com/user-attachments/assets/c1c6bade-dda1-49b3-82e2-87f98efd77f8)


## Future Enhancements
- Add support for floating-point arithmetic.
- Include advanced operations like square root, logarithms, or trigonometric functions.
- Improve the UI design for a modern look.



### Contributors
Rudraksh Thakur(That's me) - Developer

