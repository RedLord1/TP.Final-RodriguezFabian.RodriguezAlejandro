from tkinter import messagebox, Label, Tk, StringVar, CENTER
from tkinter.ttk import Combobox, Entry, Button, Style

def convertir_temperatura():
    entrada = entrada_temperatura.get()
    opcion_desde = opcion_desde_var.get()
    opcion_a = opcion_a_var.get()
    
    if not entrada:
        messagebox.showerror("Error", "Ingrese una temperatura.")
        return
    
    try:
        temperatura = float(entrada)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido para la temperatura.")
        return
    
    if opcion_desde == opcion_a:
        resultado.set(temperatura)
        return
    
    if opcion_desde == "Celsius":
        if opcion_a == "Fahrenheit":
            resultado.set((temperatura * 9/5) + 32)
        elif opcion_a == "Kelvin":
            resultado.set(temperatura + 273.15)
    elif opcion_desde == "Fahrenheit":
        if opcion_a == "Celsius":
            resultado.set((temperatura - 32) * 5/9)
        elif opcion_a == "Kelvin":
            resultado.set((temperatura - 32) * 5/9 + 273.15)
    elif opcion_desde == "Kelvin":
        if opcion_a == "Celsius":
            resultado.set(temperatura - 273.15)
        elif opcion_a == "Fahrenheit":
            resultado.set((temperatura - 273.15) * 9/5 + 32)

# Crear la ventana principal
ventana = Tk()
ventana.title("Conversor de Temperaturas")
ventana.geometry("600x500") 

# Estilo y colores
ventana.configure(bg="#1A1A1A")  

# Variables para almacenar las opciones seleccionadas y el resultado
opcion_desde_var = StringVar(ventana)
opcion_desde_var.set("Celsius")
opcion_a_var = StringVar(ventana)
opcion_a_var.set("Fahrenheit")
resultado = StringVar()

# Estilo para los widgets
estilo = Style()
estilo.theme_use('clam')  # Estilo moderno
estilo.configure("TLabel", background="#1A1A1A", foreground="#E74C3C", font=("Helvetica", 14, "bold"))
estilo.configure("TButton", background="#E74C3C", foreground="white", font=("Helvetica", 14, "bold"), padding=10)
estilo.configure("TEntry", font=("Helvetica", 14), fieldbackground="#FFFFFF", foreground="#000000")
estilo.configure("TCombobox", font=("Helvetica", 14), fieldbackground="#FFFFFF", foreground="#000000")
estilo.map("TButton", background=[("active", "#C0392B")])  # Cambiar color al hacer clic

# Etiquetas y controles de entrada
Label(ventana, text="Conversor de Temperaturas", font=("Helvetica", 24, "bold"), bg="#cccccc", fg="#E74C3C").pack(pady=20)
Label(ventana, text="Ingrese la temperatura:", bg="#000099", fg="#ffffff").pack()
entrada_temperatura = Entry(ventana, font=("Helvetica", 16), justify=CENTER)
entrada_temperatura.pack(pady=10)

Label(ventana, text="Convertir desde:", bg="#f99000", fg="#000000").pack()
opciones_desde = Combobox(ventana, textvariable=opcion_desde_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Helvetica", 16))
opciones_desde.pack(pady=10)

Label(ventana, text="Convertir a:", bg="#f99000", fg="#000000").pack()
opciones_a = Combobox(ventana, textvariable=opcion_a_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Helvetica", 16))
opciones_a.pack(pady=10)

# Botón para realizar la conversión
Button(ventana, text="Convertir", command=convertir_temperatura).pack(pady=20)

# Etiqueta para mostrar el resultado
Label(ventana, text="Resultado:", bg="#1A1A1A", fg="#E74C3C", font=("Helvetica", 14)).pack()
Label(ventana, textvariable=resultado, bg="#1A1A1A", font=("Helvetica", 18, "bold"), fg="#E74C3C").pack(pady=10)

# Centrar la ventana en la pantalla
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
posicion_x = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_y = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

ventana.mainloop()
