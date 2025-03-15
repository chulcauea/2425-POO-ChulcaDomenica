import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Aplicación de GUI")
        self.root.geometry("400x300")

        # Etiquetas
        self.label = tk.Label(root, text="Ingresa un dato:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Campo de texto para ingresar información
        self.texto_entrada = tk.Entry(root, font=("Arial", 12), width=30)
        self.texto_entrada.pack(pady=10)

        # Botón "Agregar"
        self.boton_agregar = tk.Button(root, text="Agregar", font=("Arial", 12), command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(root, text="Limpiar", font=("Arial", 12), command=self.limpiar)
        self.boton_limpiar.pack(pady=5)

        # Lista para mostrar los datos ingresados
        self.lista_datos = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
        self.lista_datos.pack(pady=10)

    def agregar_dato(self):
        """Agregar un dato a la lista."""
        dato = self.texto_entrada.get()
        if dato:
            self.lista_datos.insert(tk.END, dato)
            self.texto_entrada.delete(0, tk.END)  # Limpiar el campo de texto después de agregar
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un dato antes de agregarlo.")

    def limpiar(self):
        """Limpiar la lista y el campo de texto."""
        self.lista_datos.delete(0, tk.END)  # Limpiar la lista
        self.texto_entrada.delete(0, tk.END)  # Limpiar el campo de texto

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    # Crear la aplicación
    app = AplicacionGUI(root)
    # Ejecutar la aplicación
    root.mainloop()
