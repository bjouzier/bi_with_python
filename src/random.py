import random
import tkinter as tk
from tkinter import messagebox

def generate_random_number():
    return random.randint(1, 12)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    random_number = generate_random_number()
    messagebox.showinfo("Random Number", f"The generated random number is: {random_number}")

    root.destroy()  # Destroy the main window after the message box is closed