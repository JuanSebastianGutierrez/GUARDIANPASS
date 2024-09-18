import customtkinter as ctk
from ejercicios import agregar_contraseña, eliminar_contraseña, obtener_contraseñas, obtener_contraseña_por_id

class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Contraseñas")
        self.geometry("600x400")
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.nombre_entry = ctk.CTkEntry(self.frame, placeholder_text="Nombre")
        self.nombre_entry.pack(pady=5, fill="x")

        self.contraseña_entry = ctk.CTkEntry(self.frame, placeholder_text="Contraseña", show="*")
        self.contraseña_entry.pack(pady=5, fill="x")

        self.agregar_btn = ctk.CTkButton(self.frame, text="Agregar Contraseña", command=self.agregar_contraseña)
        self.agregar_btn.pack(pady=5)

        self.listar_btn = ctk.CTkButton(self.frame, text="Listar Contraseñas", command=self.listar_contraseñas)
        self.listar_btn.pack(pady=5)

        self.option_menu_var = ctk.StringVar(value="Selecciona una contraseña")
        self.option_menu = ctk.CTkOptionMenu(self.frame, variable=self.option_menu_var, values=[])
        self.option_menu.pack(pady=5)

        self.mostrar_btn = ctk.CTkButton(self.frame, text="Mostrar Contraseña", command=self.mostrar_contraseña)
        self.mostrar_btn.pack(pady=5)

        self.borrar_btn = ctk.CTkButton(self.frame, text="Eliminar Contraseña", command=self.eliminar_contraseña)
        self.borrar_btn.pack(pady=5)

    def agregar_contraseña(self):
        nombre = self.nombre_entry.get()
        contraseña = self.contraseña_entry.get()
        try:
            agregar_contraseña(nombre, contraseña)
            self.nombre_entry.delete(0, 'end')
            self.contraseña_entry.delete(0, 'end')
            self.listar_contraseñas()  # Actualiza la lista después de agregar
        except ValueError as e:
            ctk.CTkMessageBox.show_error("Error", str(e))

    def eliminar_contraseña(self):
        seleccion = self.option_menu_var.get()
        if seleccion != "Selecciona una contraseña":
            id = int(seleccion.split(" - ")[0])
            eliminar_contraseña(id)
            self.listar_contraseñas()

    def listar_contraseñas(self):
        contraseñas = obtener_contraseñas()
        if contraseñas:
            values = [f"{row[0]} - {row[1]}" for row in contraseñas]
            self.option_menu.configure(values=values)
        else:
            self.option_menu.configure(values=[])
            ctk.CTkMessageBox.show_info("Información", "No hay contraseñas guardadas.")

    def mostrar_contraseña(self):
        seleccion = self.option_menu_var.get()
        if seleccion != "Selecciona una contraseña":
            id = int(seleccion.split(" - ")[0])
            contraseña = obtener_contraseña_por_id(id)[2]
            ctk.CTkMessageBox.show_info("Contraseña", f"La contraseña es: {contraseña}")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
