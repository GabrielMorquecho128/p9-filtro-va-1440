# marco morquecho 1440
#================= EJEMPLO 2====================
# [Tinta Negra]
import cv2

# 1. Cargar imagen desde la carpeta de imágenes
imagen = cv2.imread("avetruz.jpg")

# 2. Comprobar que la imagen cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# 3. Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 4. Convertir a imagen binaria mediante umbralización (Threshold)
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# 5. Detectar contornos usando findContours()
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 6. Dibujar los contornos encontrados sobre una copia
resultado = imagen.copy()
cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),  # Color verde en BGR
    2             # Grosor de la línea
)

# 7. Mostrar resultados en ventanas
cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen binaria 1440", binaria)
cv2.imshow("Contornos detectados 1440", resultado)

# 8. Guardar la imagen resultante
cv2.imwrite(
    "../resultados/ejemplo2_avetruz.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en resultados/ejemplo2_avetruz.jpg")

# 9. Esperar tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
print("programa realizado por marco morquecho 1440")


# ================EJEMPLO 4==========================

# [Tinta Negra]
import cv2

# 1. Cargar imagen desde la carpeta de imágenes
imagen = cv2.imread("avetruz.jpg")

# 2. Comprobar que la imagen cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# 3. Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 4. Aplicar umbralización (Threshold)
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# 5. Encontrar contornos externos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 6. Crear copia de la imagen original
resultado = imagen.copy()

# Contador de objetos válidos
cantidad = 0

# 7. Analizar cada contorno encontrado
for contorno in contornos:

    # Calcular el área del contorno
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños (filtrado por ruido)
    if area > 500:

        cantidad += 1

        # Dibujar el contorno en verde
        cv2.drawContours(
            resultado,
            [contorno],
            -1,
            (0, 255, 0),
            2
        )

        # Obtener las coordenadas del rectángulo delimitador
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar el rectángulo delimitador en azul
        cv2.rectangle(
            resultado,
            (x, y),
            (x + ancho, y + alto),
            (255, 0, 0),
            2
        )

        # Escribir el número del objeto en rojo sobre la imagen
        cv2.putText(
            resultado,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# 8. Mostrar el resultado en pantalla
cv2.imshow("Objetos identificados", resultado)

# 9. Guardar la imagen procesada
cv2.imwrite(
    "avetruz.jpg",
    resultado
)

print("Objetos identificados:", cantidad)
print("Resultado guardado en resultados/ejemplo3_avetruz.jpg")

# 10. Esperar tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Marco morquecho NC 1440")