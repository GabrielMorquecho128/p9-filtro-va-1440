# ==============================================================================
# EJEMPLO 2 — Detección de contornos
# AVESTRUZ
# Marco Morquecho NC 1440
# ==============================================================================

import cv2
import os

# 1. Obtener la ruta del directorio donde reside este archivo de script (.py)
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Definir rutas flexibles para encontrar la imagen y crear resultados
rutas_posibles = [
    os.path.join(DIRECTORIO_ACTUAL, "imagenes", "avestruz.jpg"),
    os.path.join(DIRECTORIO_ACTUAL, "images", "avestruz.jpg"),
    os.path.join(DIRECTORIO_ACTUAL, "avestruz.jpg"),
    os.path.join(DIRECTORIO_ACTUAL, "..", "avestruz.jpg"),
    os.path.join(DIRECTORIO_ACTUAL, "..", "imagenes", "avestruz.jpg"),
]

ruta_imagen = None
for ruta in rutas_posibles:
    if os.path.exists(ruta):
        ruta_imagen = ruta
        break

if ruta_imagen is None:
    ruta_imagen = "avestruz.jpg"

# Definir la carpeta de resultados
carpeta_resultados = os.path.join(DIRECTORIO_ACTUAL, "resultados")
os.makedirs(carpeta_resultados, exist_ok=True)

# 3. Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# 4. Comprobar que la imagen cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    print(f"Revisa que 'avestruz.jpg' esté dentro de la carpeta 'imagenes'. Ruta intentada: {ruta_imagen}")
    exit()

# 5. Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 6. Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# 7. Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 8. Dibujar los contornos en verde sobre una copia de la imagen
resultado = imagen.copy()
cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# 9. Guardar LAS 3 IMÁGENES en la carpeta de resultados
ruta_original = os.path.join(carpeta_resultados, "1_avestruz_original_1440.jpg")
ruta_binaria = os.path.join(carpeta_resultados, "2_avestruz_binaria_1440.jpg")
ruta_contornos = os.path.join(carpeta_resultados, "3_avestruz_contornos_1440.jpg")

cv2.imwrite(ruta_original, imagen)
cv2.imwrite(ruta_binaria, binaria)
cv2.imwrite(ruta_contornos, resultado)

# 10. Mostrar métricas en la terminal
print("--- PROCESAMIENTO EXITOSO ---")
print(f"Imagen leída desde: {ruta_imagen}")
print("Cantidad de contornos encontrados:", len(contornos))
print("\n--- IMÁGENES GUARDADAS EN 'resultados/' ---")
print(f"1. Original:  {ruta_original}")
print(f"2. Binaria:   {ruta_binaria}")
print(f"3. Contornos: {ruta_contornos}")

# 11. Mostrar ventanas con los resultados
cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen binaria 1440", binaria)
cv2.imshow("Contornos detectados 1440", resultado)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("marco morquecho NC 1440")