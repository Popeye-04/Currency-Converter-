import requests
import tkinter as tk
from tkinter import messagebox

#URL de la API 
API_URL = "https://v6.exchangerate-api.com/v6/19bb41b4b9dfb53c21fdafb7/latest/USD"

#Funcion para obtener las tasas de cambio desde la APi
def obtener_tasas_cambio():
    response = requests.get(API_URL)
    if response.status_code == 200:
        try:
            data = response.json()
            return data["conversion_rates"]
        except ValueError:
            print("Error al decodificar la respuesta JSON.")
            return None
    else:
        print(f"Error al obtener las tasas de cambio. Código de estado: {response.status_code}")
        return None

#Funcion para convertir las monedas
def convertir_moneda(monto, moneda_origen, moneda_destino):
    try:
        tasas_de_cambio = obtener_tasas_cambio()
        if tasas_de_cambio:
            if moneda_origen == moneda_destino:
                resultado = monto
            elif moneda_destino != "USD":
                monto_en_usd = monto / tasas_de_cambio[moneda_origen]
                if moneda_destino in tasas_de_cambio:
                    resultado = monto_en_usd * tasas_de_cambio[moneda_destino]
                else:
                    resultado = None
            else:
                if moneda_destino in tasas_de_cambio:
                    resultado = monto * tasas_de_cambio[moneda_destino]
                else:
                    resultado = None

            if resultado is not None:
                label_resultado.config(text=f"{monto} {moneda_origen} = {resultado:.2f} {moneda_destino}")
            else:
                messagebox.showerror("Error", "Moneda de destino no válida.")
        else:
            messagebox.showerror("Error", "No se pudo obtener las tasas de cambio.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

        print(f"La moneda de destino {moneda_destino} no es válida.")
        return None

def manejar_evento_convertir():
    try:
        monto = float(entry_monto.get())  # Obtiene el monto del campo de texto
        moneda_origen = entry_moneda_origen.get().upper()  # Obtiene la moneda de origen
        moneda_destino = entry_moneda_destino.get().upper()  # Obtiene la moneda de destino
        
        #Llamamos a la función convertir_moneda con los valores obtenidos
        convertir_moneda(monto, moneda_origen, moneda_destino)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")


# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de Monedas")

# Título
title_label = tk.Label(root, text="Convertidor de Monedas", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Crear un marco para agrupar los widgets
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Etiquetas y campos de texto con mejor estilo
label_monto = tk.Label(frame, text="Monto:", font=("Helvetica", 12), bg="#f0f0f0", anchor="w")
label_monto.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_monto = tk.Entry(frame, font=("Helvetica", 12), width=20, borderwidth=2, relief="solid")
entry_monto.grid(row=0, column=1, padx=10, pady=5)

label_moneda_origen = tk.Label(frame, text="Moneda de origen (USD):", font=("Helvetica", 12), bg="#f0f0f0", anchor="w")
label_moneda_origen.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_moneda_origen = tk.Entry(frame, font=("Helvetica", 12), width=20, borderwidth=2, relief="solid")
entry_moneda_origen.grid(row=1, column=1, padx=10, pady=5)

label_moneda_destino = tk.Label(frame, text="Moneda de destino (Ej: GBP, EUR):", font=("Helvetica", 12), bg="#f0f0f0", anchor="w")
label_moneda_destino.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_moneda_destino = tk.Entry(frame, font=("Helvetica", 12), width=20, borderwidth=2, relief="solid")
entry_moneda_destino.grid(row=2, column=1, padx=10, pady=5)

# Botón para realizar la conversión
button_convertir = tk.Button(root, text="Convertir", font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", command=manejar_evento_convertir)
button_convertir.pack(pady=15)

# Etiqueta para mostrar el resultado con mejor formato
label_resultado = tk.Label(root, text="Resultado:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_resultado.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()