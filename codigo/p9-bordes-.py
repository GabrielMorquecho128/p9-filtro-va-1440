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
# Busca la imagen en la misma carpeta o una carpeta arriba (raíz)
ruta_imagen_local = os.path.join(DIRECTORIO_ACTUAL, "avestruz.jpg")
ruta_imagen_raiz = os.path.join(DIRECTORIO_ACTUAL, "..", "avestruz.jpg")

if os.path.exists(ruta_imagen_local):
    ruta_imagen = ruta_imagen_local
elif os.path.exists(ruta_imagen_raiz):
    ruta_imagen = ruta_imagen_raiz
else:
    ruta_imagen = "avestruz.jpg"

# Definir la carpeta de resultados en la raíz del proyecto
carpeta_resultados = os.path.join(DIRECTORIO_ACTUAL, "..", "resultados")
if not os.path.exists(os.path.dirname(carpeta_resultados)):
    carpeta_resultados = os.path.join(DIRECTORIO_ACTUAL, "resultados")

os.makedirs(carpeta_resultados, exist_ok=True)

# 3. Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# 4. Comprobar que la imagen cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    print(f"Revisa que 'avestruz.jpg' esté en la carpeta del proyecto. Ruta intentada: {ruta_imagen}")
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

# 9. Guardar la imagen procesada en la carpeta de resultados
ruta_guardado = os.path.join(carpeta_resultados, "avestruz_contornos_1440.jpg")
cv2.imwrite(ruta_guardado, resultado)

# 10. Mostrar métricas en la terminal
print("--- PROCESAMIENTO EXITOSO ---")
print("Cantidad de contornos encontrados:", len(contornos))
print(f"Resultado guardado en: {ruta_guardado}")
print("\nPrograma realizado por Marco Morquecho NC = 1440")

# 11. Mostrar ventanas con los resultados
cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen binaria 1440", binaria)
cv2.imshow("Contornos detectados 1440", resultado)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("marco morquecho NC 1440")