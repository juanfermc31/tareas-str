# 1. Definición de variables y datos
usuario = "Juan"
proyecto = "Controlador principal"
nivel_bateria = 85
estado = "Conectado"

# 2. Impresión de datos en el panel de control
print("========================================")
print("       PANEL DE CONTROL DE DATOS        ")
print("========================================")
print(f"Usuario registrado : {usuario}")
print(f"Nombre del proyecto: {proyecto}")
print(f"Estado del sistema : {estado}")
print(f"Nivel de batería   : {nivel_bateria}%")


# 1. Solicitar el número al usuario
numero = int(input("Ingresa un número entero: "))

# 2. Evaluar si es primo
if numero <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

# 3. Imprimir el resultado
if es_primo:
    print(f"¡El número {numero} SÍ es primo!")
else:
    print(f"El número {numero} NO es primo.")