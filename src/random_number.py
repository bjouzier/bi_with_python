import random
import tkinter as tk
from tkinter import messagebox

# Générer un nombre aléatoire entre 1 et 12
random_number = random.randint(1, 12)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.withdraw()  # Masquer la fenêtre principale

# Afficher le résultat dans un dialogue d'information
messagebox.showinfo("Nombre Aléatoire", f"Le nombre aléatoire généré est : {random_number}")

# Fermer la fenêtre Tkinter
root.destroy()