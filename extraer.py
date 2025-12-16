"""
Esteganografía LSB

Trabajo para la asignatura SPSI 2025-2026 impartido por Francisco Manuel García Olmedo

Francisco Jose Ramos Moya
Pedro Castaño Garcia
"""

import base64
from stegano import lsb
import os

imagen_para_analizar = "paisaje_stegano.png"

# --- Verificación previa ---
if not os.path.exists(imagen_para_analizar):
    print(f"Error: No se encuentra la imagen '{imagen_para_analizar}'")
    exit()

print(f"Analizando la imagen: {imagen_para_analizar}...")

try:
    #  Lectura de bits y reconstrucción del mensaje
    # lsb.reveal extrae la información oculta en los bits LSB
    datos_extraidos_b64 = lsb.reveal(imagen_para_analizar)
    
    if datos_extraidos_b64:
        print(f"\n[!] Se han detectado datos ocultos.")
        print(f"Datos en Base64: {datos_extraidos_b64}")
        
        # Decodificación del payload 
        # Convertimos el Base64 de nuevo a texto legible
        mensaje_original = base64.b64decode(datos_extraidos_b64).decode()
        
        print(f"\n>>> MENSAJE RECUPERADO: {mensaje_original} <<<")
    else:
        print("\n[i] El análisis ha finalizado sin encontrar datos ocultos.")

except Exception as e:
    # Esto suele ocurrir si la imagen no es PNG o está corrupta
    print(f"Error al intentar leer la imagen: {e}")

