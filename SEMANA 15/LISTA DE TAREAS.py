import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas
        self.tareas = []

        # Crear Widgets
        self.create_widgets()

    def create_widgets(self):
        # Campo de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(self.root, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tarea
        self.boton_añadir = tk.Button(self.root, text="Añadir Tarea", command=self.add_tarea)
        self.boton_añadir.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas (Listbox)
        self.listbox_tareas = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.boton_completar = tk.Button(self.root, text="Marcar como Completada", command=self.mark_completada)
        self.boton_completar.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

        # Evento para añadir tarea presionando Enter
        self.entry_tarea.bind('<Return>', lambda event: self.add_tarea())

        # Doble clic para marcar tarea como completada
        self.listbox_tareas.bind("<Double-1>", self.on_doble_click)

    def add_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append({'tarea': tarea, 'completada': False})
            self.entry_tarea.delete(0, tk.END)  # Limpiar campo de entrada
            self.update_listbox()

    def mark_completada(self):
        tarea_seleccionada = self.listbox_tareas.curselection()
        if tarea_seleccionada:
            tarea_index = tarea_seleccionada[0]
            self.tareas[tarea_index]['completada'] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Selección", "Seleccione una tarea para marcar como completada")

    def delete_tarea(self):
        tarea_seleccionada = self.listbox_tareas.curselection()
        if tarea_seleccionada:
            tarea_index = tarea_seleccionada[0]
            del self.tareas[tarea_index]
            self.update_listbox()
        else:
            messagebox.showwarning("Selección", "Seleccione una tarea para eliminar")

    def update_listbox(self):
        self.listbox_tareas.delete(0, tk.END)  # Limpiar Listbox
        for tarea in self.tareas:
            estado = "Completada" if tarea['completada'] else "Pendiente"
            tarea_display = f"{tarea['tarea']} - {estado}"
            self.listbox_tareas.insert(tk.END, tarea_display)

    def on_doble_click(self, event):
        tarea_seleccionada = self.listbox_tareas.curselection()
        if tarea_seleccionada:
            tarea_index = tarea_seleccionada[0]
            if not self.tareas[tarea_index]['completada']:
                self.tareas[tarea_index]['completada'] = True
                self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TareaApp(root)
    root.mainloop()