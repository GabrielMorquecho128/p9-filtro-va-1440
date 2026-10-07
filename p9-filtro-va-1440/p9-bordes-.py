import cv2
import os

# EJEMPLO 2 — Detección de contornos
# AVESTRUZ
# Marco Morquecho NC 1440

# Crear carpeta 'resultados' si no existe
os.makedirs("resultados", exist_ok=True)

# Cargar imagen
imagen = cv2.imread("avestruz.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    print("Revisa que 'avestruz.jpg' esté en la misma carpeta que este programa.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Guardar resultado en la carpeta resultados
cv2.imwrite(
    "resultados/avestruz_contornos_1440.jpg",
    resultado
)

# Mostrar resultados
cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen binaria 1440", binaria)
cv2.imshow("Contornos detectados 1440", resultado)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en: resultados/avestruz_contornos_1440.jpg")


# Esperar tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nPrograma realizado por Marco Morquecho NC = 1440")
