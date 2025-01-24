import ctypes
import tkinter as tk
from tkinter import messagebox

# Load the DLL
lib = ctypes.CDLL(r'./calculator.dll')

# Define argument types for functions in the DLL
lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.sub.argtypes = (ctypes.c_int, ctypes.c_int)
lib.mult.argtypes = (ctypes.c_int, ctypes.c_int)
lib.my_div.argtypes = (ctypes.c_int, ctypes.c_int)
lib.power.argtypes = (ctypes.c_int, ctypes.c_int)

# Define return types for functions in the DLL
lib.add.restype = ctypes.c_int
lib.sub.restype = ctypes.c_int
lib.mult.restype = ctypes.c_int
lib.my_div.restype = ctypes.c_int
lib.power.restype = ctypes.c_int

# Function to perform the calculation
def calculate():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        operation = combo_operation.get()

        # Perform operation based on user input
        if operation == "+":
            result = lib.add(num1, num2)
        elif operation == "-":
            result = lib.sub(num1, num2)
        elif operation == "*":
            result = lib.mult(num1, num2)
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Error: Division by zero!")
                return
            result = lib.my_div(num1, num2)
        elif operation == "^":
            result = lib.power(num1, num2)
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create dropdown for operations
label_operation = tk.Label(root, text="Choose operation:")
label_operation.pack()

combo_operation = tk.StringVar(root)
combo_operation.set("+")  # Default operation
operations = ["+", "-", "*", "/", "^"]
dropdown_operations = tk.OptionMenu(root, combo_operation, *operations)
dropdown_operations.pack()

# Create a button to perform the calculation
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Start the GUI
root.mainloop()
