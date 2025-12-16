"""
Esteganografía LSB

SPSI 2025-2026 impartido por Francisco Manuel García Olmedo

Francisco Jose Ramos Moya
Pedro Castaño Garcia
"""

import base64
from stegano import lsb
import os


imagen_original = "paisaje.jpg"  # Imagen a usar para ocultar el mensaje
mensaje_secreto = "https://www.hacker-etico.com/panel-secreto"
nombre_salida = "paisaje_stegano.png"  # IMPORTANTE: Siempre .png por que mantiene todos los bits.

# --- Verificación previa ---
if not os.path.exists(imagen_original):
    print(f"Error: No se encuentra la imagen '{imagen_original}'")
    exit()

print(f"Procesando imagen: {imagen_original}")
print(f"Ocultando mensaje: {mensaje_secreto}")

# --- Paso 1: Codificación del mensaje ---
# Convertimos el texto a bytes y luego lo codificamos en Base64
mensaje_codificado = base64.b64encode(mensaje_secreto.encode()).decode()
print(f"Mensaje codificado (Base64) para insertar: {mensaje_codificado}")

try:
    # --- Paso 2: Algoritmo de inserción (LSB) ---
    # lsb.hide devuelve un objeto de imagen con los datos ya ocultos
    imagen_con_datos = lsb.hide(imagen_original, mensaje_codificado)
    
    # --- Paso 3: Guardado ---
    imagen_con_datos.save(nombre_salida)
    print(f"\n[ÉXITO] Imagen generada: '{nombre_salida}'")
    print("Visualmente es idéntica a la original, pero contiene el secreto.")
except Exception as e:
    print(f"Ocurrió un error durante la ocultación: {e}")

