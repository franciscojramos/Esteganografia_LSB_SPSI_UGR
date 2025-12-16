# Proyecto de Esteganografía LSB

**SPSI 2025-2026** impartido por Francisco Manuel García Olmedo

**Autores:**
- Francisco Jose Ramos Moya
- Pedro Castaño Garcia

---

En este proyecto implementamos técnicas de esteganografía utilizando el método LSB (Least Significant Bit) para ocultar mensajes secretos dentro de imágenes.

## Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Instalación

```bash
pip install stegano pillow
```

### Preparar una imagen

Necesitamos una imagen de prueba llamada `paisaje.jpg` en el mismo directorio que los scripts. Podemos:

- Descargar una imagen de internet
- Usar una foto propia
- Renombrar cualquier imagen a `paisaje.jpg`

**Nota importante:** La imagen original puede estar en formato JPG, pero la imagen de salida **siempre será PNG** para preservar los datos ocultos.

## Uso

### Ocultar un mensaje

Para ocultar un mensaje secreto en una imagen:

```bash
python ocultar.py
```

Este script realiza los siguientes pasos:
1. Lee la imagen `paisaje.jpg`
2. Codifica el mensaje en Base64
3. Oculta el mensaje en los bits menos significativos de los píxeles
4. Guarda el resultado como `paisaje_stegano.png`

**Salida esperada:**
```
Procesando imagen: paisaje.jpg
Ocultando mensaje: https://www.hacker-etico.com/panel-secreto
Mensaje codificado (Base64) para insertar: aHR0cHM6Ly93d3cuaGFja2VyLWV0aWNvLmNvbS9wYW5lbC1zZWNyZXRv

[ÉXITO] Imagen generada: 'paisaje_stegano.png'
Visualmente es idéntica a la original, pero contiene el secreto.
```

### Extraer el mensaje oculto

Para recuperar el mensaje de una imagen esteganografiada:

```bash
python extraer.py
```

Este script realiza los siguientes pasos:
1. Lee la imagen `paisaje_stegano.png`
2. Extrae los bits LSB que contienen el mensaje
3. Decodifica el Base64 para obtener el texto original

**Salida esperada:**
```
Analizando la imagen: paisaje_stegano.png...

[!] Se han detectado datos ocultos.
Datos en Base64: aHR0cHM6Ly93d3cuaGFja2VyLWV0aWNvLmNvbS9wYW5lbC1zZWNyZXRv

>>> MENSAJE RECUPERADO: https://www.hacker-etico.com/panel-secreto <<<
```

## Personalización

### Cambiar el mensaje secreto

Podemos editar el archivo `ocultar.py` y modificar la variable:

```python
mensaje_secreto = "Tu mensaje secreto aquí"
```

### Usar diferentes imágenes

Podemos cambiar los nombres de archivo en las variables de configuración:

En `ocultar.py`:
```python
imagen_original = "tu_imagen.jpg"
nombre_salida = "imagen_con_secreto.png"
```

En `extraer.py`:
```python
imagen_para_analizar = "imagen_con_secreto.png"
```

## Conceptos Técnicos

### ¿Por qué PNG y no JPG?

- **JPG**: Usa compresión con pérdida, destruyendo los datos ocultos en los LSB
- **PNG**: Usa compresión sin pérdida, preservando exactamente todos los bits

### ¿Por qué Base64?

Utilizamos Base64 para convertir el texto en una cadena alfanumérica estándar, evitando problemas con caracteres especiales que podrían corromperse durante el proceso de ocultación.

### LSB (Least Significant Bit)

El método LSB que implementamos modifica el bit menos significativo de cada byte de color en los píxeles. Este cambio es imperceptible al ojo humano pero nos permite almacenar información.

Ejemplo:
- Color original: `11010110` (214)
- Con LSB modificado: `11010111` (215)
- Diferencia visual: Prácticamente invisible

## Limitaciones

- El tamaño del mensaje está limitado por el número de píxeles de la imagen
- Solo funciona con formatos sin compresión con pérdida (PNG recomendado)




```

## Información del Proyecto

**Asignatura:** SPSI (Seguridad y Protección de Sistemas Informáticos) 2025-2026  
**Profesor:** Francisco Manuel García Olmedo  
**Autores:**
- Francisco Jose Ramos Moya
- Pedro Castaño Garcia

