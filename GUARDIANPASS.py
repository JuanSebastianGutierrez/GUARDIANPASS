import sqlite3
import os
import string
import random
import customtkinter as ctk
from tkinter import messagebox
import sys

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

db_path = os.path.join(os.path.dirname(sys.executable), "contrasenas.db")

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def crear_tabla_contrasenas():
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS contrasenas
                     (aplicacion TEXT PRIMARY KEY, contrasena TEXT)''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla en SQLite: {e}")
    finally:
        conn.close()

def guardar_contrasenas_sqlite(aplicacion, contrasena):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO contrasenas (aplicacion, contrasena) VALUES (?, ?)", (aplicacion, contrasena))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al guardar en SQLite: {e}")
    finally:
        conn.close()

def mostrar_contrasenas():
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT aplicacion, contrasena FROM contrasenas")
        contrasenas = c.fetchall()
    except sqlite3.Error as e:
        print(f"Error al consultar contraseñas en SQLite: {e}")
        contrasenas = []
    finally:
        conn.close()

    if contrasenas:
        ventana_mostrar = ctk.CTkToplevel()
        ventana_mostrar.title("Contraseñas Guardadas")
        ventana_mostrar.iconbitmap('icono.ico')  # Cambia 'icono.ico' por el nombre de tu archivo de ícono

        for aplicacion, contrasena in contrasenas:
            lbl = ctk.CTkLabel(ventana_mostrar, text=f"Aplicación: {aplicacion} - Contraseña: {contrasena}")
            lbl.pack(pady=5)
    else:
        messagebox.showinfo("Contraseñas Guardadas", "No hay contraseñas guardadas.")

def borrar_contrasena():
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT aplicacion FROM contrasenas")
        aplicaciones = [row[0] for row in c.fetchall()]
    except sqlite3.Error as e:
        print(f"Error al consultar aplicaciones en SQLite: {e}")
        aplicaciones = []
    finally:
        conn.close()

    if aplicaciones:
        ventana_borrar = ctk.CTkToplevel()
        ventana_borrar.title("Borrar Contraseña")
        ventana_borrar.iconbitmap('icono.ico')  # Cambia 'icono.ico' por el nombre de tu archivo de ícono

        lbl_aplicacion = ctk.CTkLabel(ventana_borrar, text="Seleccione la aplicación:")
        lbl_aplicacion.pack(padx=10, pady=10)

        variable_aplicacion = ctk.StringVar(ventana_borrar)
        variable_aplicacion.set(aplicaciones[0])

        opt_aplicacion = ctk.CTkOptionMenu(ventana_borrar, variable=variable_aplicacion, values=aplicaciones)
        opt_aplicacion.pack(padx=10, pady=10)

        def borrar():
            aplicacion = variable_aplicacion.get()
            try:
                conn = sqlite3.connect(db_path)
                c = conn.cursor()
                c.execute("DELETE FROM contrasenas WHERE aplicacion=?", (aplicacion,))
                conn.commit()
                messagebox.showinfo("Contraseña Borrada", f"La contraseña de la aplicación '{aplicacion}' ha sido borrada.")
                
                c.execute("SELECT COUNT(*) FROM contrasenas")
                count = c.fetchone()[0]
                if count == 0:
                    pass
                
            except sqlite3.Error as e:
                print(f"Error al borrar contraseña en SQLite: {e}")
            finally:
                conn.close()
                ventana_borrar.destroy()

        btn_borrar = ctk.CTkButton(ventana_borrar, text="Borrar", command=borrar)
        btn_borrar.pack(padx=10, pady=10)
    else:
        messagebox.showinfo("Borrar Contraseña", "No hay contraseñas para borrar.")

def main():
    crear_tabla_contrasenas()

    ctk.set_default_color_theme("dark-blue")

    ventana_principal = ctk.CTk()
    ventana_principal.title("GUARDIANPASS")
    ventana_principal.iconbitmap('Logo guardianpass.ico')  

    global entry_aplicacion, entry_aplicacion_longitud, entry_longitud, entry_contrasena
    entry_aplicacion, entry_longitud, entry_contrasena, entry_aplicacion_longitud = None, None, None, None

    def crear_widgets():
        global entry_aplicacion, entry_longitud, entry_contrasena, entry_aplicacion_longitud
        
        frame_opciones = ctk.CTkFrame(ventana_principal)
        frame_opciones.pack(pady=10)

        lbl_aplicacion = ctk.CTkLabel(frame_opciones, text="Aplicación:")
        lbl_aplicacion.grid(row=0, column=0, padx=5, pady=5)

        entry_aplicacion_longitud = ctk.CTkEntry(frame_opciones)
        entry_aplicacion_longitud.grid(row=0, column=1, padx=5, pady=5)

        lbl_longitud = ctk.CTkLabel(frame_opciones, text="Longitud:")
        lbl_longitud.grid(row=1, column=0, padx=5, pady=5)

        entry_longitud = ctk.CTkEntry(frame_opciones)
        entry_longitud.grid(row=1, column=1, padx=5, pady=5)

        btn_generar_guardar = ctk.CTkButton(frame_opciones, text="Generar y Guardar", command=generar_guardar_contrasena)
        btn_generar_guardar.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        lbl_aplicacion = ctk.CTkLabel(frame_opciones, text="Aplicación:")
        lbl_aplicacion.grid(row=4, column=0, padx=5, pady=5)
        
        lbl_contrasena = ctk.CTkLabel(frame_opciones, text="Contraseña:")
        lbl_contrasena.grid(row=5, column=0, padx=5, pady=5)

        entry_aplicacion = ctk.CTkEntry(frame_opciones)
        entry_aplicacion.grid(row=5, column=1, padx=5, pady=5)

        entry_contrasena = ctk.CTkEntry(frame_opciones, show="*")
        entry_contrasena.grid(row=4, column=1, padx=5, pady=5)

        btn_guardar_manual = ctk.CTkButton(frame_opciones, text="Guardar Manualmente", command=guardar_contrasena_manual)
        btn_guardar_manual.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def generar_guardar_contrasena():
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

    def guardar_contrasena_manual():
        aplicacion = entry_aplicacion.get().strip()
        contrasena = entry_contrasena.get().strip()
        if aplicacion and contrasena:
            guardar_contrasenas_sqlite(aplicacion, contrasena)
            messagebox.showinfo("Contraseña Guardada", "¡Contraseña guardada correctamente!")
        else:
            messagebox.showerror("Error", "La aplicación o la contraseña no pueden estar vacías.")

    crear_widgets()

    btn_mostrar_contrasenas = ctk.CTkButton(ventana_principal, text="Mostrar Contraseñas", command=mostrar_contrasenas)
    btn_mostrar_contrasenas.pack(pady=10)

    btn_borrar_contrasena = ctk.CTkButton(ventana_principal, text="Borrar Contraseña", command=borrar_contrasena)
    btn_borrar_contrasena.pack(pady=10)
    
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
