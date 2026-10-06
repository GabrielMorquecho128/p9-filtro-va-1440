# marco morquecho 1440
import cv2
import os

# 0. Crear la carpeta 'resultados' automáticamente si no existe
os.makedirs("resultados", exist_ok=True)

# =========================================================
# ===================== EJEMPLO 2 =========================
# =========================================================

# 1. Cargar imagen
imagen = cv2.imread("avetruz.jpg")

# 2. Comprobar que la imagen cargó correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen 'avetruz.jpg'. Revisa que esté en la raíz del proyecto.")
    exit()

# 3. Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 4. Convertir a imagen binaria mediante umbralización (Threshold)
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

# 5. Detectar contornos usando findContours()
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 6. Dibujar los contornos encontrados sobre una copia
resultado_ej2 = imagen.copy()
cv2.drawContours(
    resultado_ej2,
    contornos,
    -1,
    (0, 255, 0),  # Color verde en BGR
    2             # Grosor de la línea
)

# 7. Guardar la imagen resultante en la carpeta resultados
cv2.imwrite("resultados/ejemplo2_avetruz.jpg", resultado_ej2)

print("--- EJEMPLO 2 ---")
print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en: resultados/ejemplo2_avetruz.jpg")


# =========================================================
# ===================== EJEMPLO 4 =========================
# =========================================================

# Crear copia limpia para el segundo ejercicio
resultado_ej4 = imagen.copy()
cantidad = 0

# Analizar cada contorno encontrado
for contorno in contornos:

    # Calcular el área del contorno
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños (filtrado por ruido)
    if area > 500:
        cantidad += 1

        # Dibujar el contorno en verde
        cv2.drawContours(resultado_ej4, [contorno], -1, (0, 255, 0), 2)

        # Obtener las coordenadas del rectángulo delimitador
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar el rectángulo delimitador en azul
        cv2.rectangle(resultado_ej4, (x, y), (x + ancho, y + alto), (255, 0, 0), 2)

        # Escribir el número del objeto en rojo sobre la imagen
        cv2.putText(
            resultado_ej4,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# Guardar la imagen procesada en la carpeta resultados (NO SOBRESCRIBE la original)
cv2.imwrite("resultados/ejemplo4_avetruz.jpg", resultado_ej4)

print("\n--- EJEMPLO 4 ---")
print("Objetos identificados:", cantidad)
print("Resultado guardado en: resultados/ejemplo4_avetruz.jpg")


# =========================================================
# ================= MOSTRAR VENTANAS ======================
# =========================================================

cv2.imshow("Imagen original 1440", imagen)
cv2.imshow("Imagen binaria 1440", binaria)
cv2.imshow("Ejemplo 2 - Contornos 1440", resultado_ej2)
cv2.imshow("Ejemplo 4 - Objetos Identificados 1440", resultado_ej4)

# Esperar tecla y cerrar todas las ventanas al final
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nPrograma realizado por Marco Morquecho NC 1440")