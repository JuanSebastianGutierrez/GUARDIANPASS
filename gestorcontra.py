import sqlite3
import os
import string
import random
import customtkinter as ctk
from tkinter import messagebox
import sys

# Asegurarse de que el directorio de trabajo sea el mismo que el del ejecutable
if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

# Obtener la ruta absoluta para el archivo de base de datos
db_path = os.path.join(os.path.dirname(sys.executable), "contrasenas.db")

def generar_contrasena(longitud=12):
    """Genera una contraseña aleatoria de una longitud específica."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def crear_tabla_contrasenas():
    """Crea la tabla de contraseñas si no existe."""
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS contrasenas
                         (aplicacion TEXT PRIMARY KEY, contrasena TEXT)''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla en SQLite: {e}")

def guardar_contrasenas_sqlite(aplicacion, contrasena):
    """Guarda una contraseña en la base de datos SQLite."""
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO contrasenas (aplicacion, contrasena) VALUES (?, ?)", (aplicacion, contrasena))
    except sqlite3.Error as e:
        print(f"Error al guardar en SQLite: {e}")

def mostrar_contrasenas():
    """Muestra las contraseñas guardadas en una nueva ventana."""
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT aplicacion, contrasena FROM contrasenas")
            contrasenas = c.fetchall()
    except sqlite3.Error as e:
        print(f"Error al consultar contraseñas en SQLite: {e}")
        contrasenas = []

    if contrasenas:
        ventana_mostrar = ctk.CTkToplevel()
        ventana_mostrar.title("Contraseñas Guardadas")
        for aplicacion, contrasena in contrasenas:
            ctk.CTkLabel(ventana_mostrar, text=f"Aplicación: {aplicacion} - Contraseña: {contrasena}").pack(pady=5)
    else:
        messagebox.showinfo("Contraseñas Guardadas", "No hay contraseñas guardadas.")

def borrar_contrasena():
    """Muestra una ventana para seleccionar y borrar una contraseña."""
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT aplicacion FROM contrasenas")
            aplicaciones = [row[0] for row in c.fetchall()]
    except sqlite3.Error as e:
        print(f"Error al consultar aplicaciones en SQLite: {e}")
        aplicaciones = []

    if aplicaciones:
        ventana_borrar = ctk.CTkToplevel()
        ventana_borrar.title("Borrar Contraseña")

        lbl_aplicacion = ctk.CTkLabel(ventana_borrar, text="Seleccione la aplicación:")
        lbl_aplicacion.pack(padx=10, pady=10)

        variable_aplicacion = ctk.StringVar(ventana_borrar)
        variable_aplicacion.set(aplicaciones[0])

        opt_aplicacion = ctk.CTkOptionMenu(ventana_borrar, variable=variable_aplicacion, values=aplicaciones)
        opt_aplicacion.pack(padx=10, pady=10)

        def borrar():
            aplicacion = variable_aplicacion.get()
            try:
                with sqlite3.connect(db_path) as conn:
                    c = conn.cursor()
                    c.execute("DELETE FROM contrasenas WHERE aplicacion=?", (aplicacion,))
                    conn.commit()
                    messagebox.showinfo("Contraseña Borrada", f"La contraseña de la aplicación '{aplicacion}' ha sido borrada.")
                    
                    c.execute("SELECT COUNT(*) FROM contrasenas")
                    if c.fetchone()[0] == 0:
                        pass  # No mostrar mensaje aquí
            except sqlite3.Error as e:
                print(f"Error al borrar contraseña en SQLite: {e}")
            finally:
                ventana_borrar.destroy()

        ctk.CTkButton(ventana_borrar, text="Borrar", command=borrar).pack(padx=10, pady=10)
    else:
        messagebox.showinfo("Borrar Contraseña", "No hay contraseñas para borrar.")

def main():
    """Función principal de la aplicación."""
    crear_tabla_contrasenas()

    ctk.set_default_color_theme("dark-blue")

    ventana_principal = ctk.CTk()
    ventana_principal.title("Gestor de Contraseñas")

    def crear_widgets():
        frame_opciones = ctk.CTkFrame(ventana_principal)
        frame_opciones.pack(pady=10)

        # Widgets para generar y guardar contraseñas
        ctk.CTkLabel(frame_opciones, text="Aplicación:").grid(row=0, column=0, padx=5, pady=5)
        entry_aplicacion_longitud = ctk.CTkEntry(frame_opciones)
        entry_aplicacion_longitud.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_opciones, text="Longitud:").grid(row=1, column=0, padx=5, pady=5)
        entry_longitud = ctk.CTkEntry(frame_opciones)
        entry_longitud.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkButton(frame_opciones, text="Generar y Guardar", command=lambda: generar_guardar_contrasena(entry_aplicacion_longitud, entry_longitud)).grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Widgets para guardar contraseñas manualmente
        ctk.CTkLabel(frame_opciones, text="Aplicación:").grid(row=4, column=0, padx=5, pady=5)
        entry_aplicacion = ctk.CTkEntry(frame_opciones)
        entry_aplicacion.grid(row=4, column=1, padx=5, pady=5)

        ctk.CTkLabel(frame_opciones, text="Contraseña:").grid(row=5, column=0, padx=5, pady=5)
        entry_contrasena = ctk.CTkEntry(frame_opciones, show="*")
        entry_contrasena.grid(row=5, column=1, padx=5, pady=5)

        ctk.CTkButton(frame_opciones, text="Guardar Manualmente", command=lambda: guardar_contrasena_manual(entry_aplicacion, entry_contrasena)).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def generar_guardar_contrasena(entry_aplicacion_longitud, entry_longitud):
        aplicacion = entry_aplicacion_longitud.get().strip()
        if aplicacion:
            try:
                longitud = int(entry_longitud.get())
                nueva_contrasena = generar_contrasena(longitud)
                guardar_contrasenas_sqlite(aplicacion, nueva_contrasena)
                messagebox.showinfo("Contraseña Generada y Guardada", "¡Contraseña generada y guardada correctamente!")
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido.")
        else:
            messagebox.showerror("Error", "El nombre de la aplicación no puede estar vacío.")

    def guardar_contrasena_manual(entry_aplicacion, entry_contrasena):
        aplicacion = entry_aplicacion.get().strip()
        contrasena = entry_contrasena.get().strip()
        if aplicacion and contrasena:
            guardar_contrasenas_sqlite(aplicacion, contrasena)
            messagebox.showinfo("Contraseña Guardada", "¡Contraseña guardada correctamente!")
        else:
            messagebox.showerror("Error", "La aplicación o la contraseña no pueden estar vacías.")

    crear_widgets()

    ctk.CTkButton(ventana_principal, text="Mostrar Contraseñas", command=mostrar_contrasenas).pack(pady=10)
    ctk.CTkButton(ventana_principal, text="Borrar Contraseña", command=borrar_contrasena).pack(pady=10)
    
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
