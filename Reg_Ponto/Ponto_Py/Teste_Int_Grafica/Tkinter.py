import tkinter as tk

root = tk.Tk()
root.title("Tkinter")

label = tk.Label(root, text="Olá, mundo!")
label.pack(pady=10)

button = tk.Button(root, text="Clique aqui", command=lambda: label.config(text="Você clicou!"))
button.pack(pady=5)

root.mainloop()
