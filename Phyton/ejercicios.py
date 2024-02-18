# ------------ EJERCICIOS CORRESPONDIENTES A LA SECCION 1

#1 Verificar si un numero es par o impar (Usar un input).

num = int(input("Ingresa un número: "))

if num % 2 == 0: print("El número es par") 
else: print("El número es impar")


#2 Clasificar una persona en una categoria de edad. Por ejemplo: Si es un niño, si es un adolescente o si es una persona adulta

def clasificar_edad(edad):
    if edad < 13:
        return "Es un niño"
    elif edad < 18:
        return "Es un adolescente"
    else:
        return "Es una persona adulta"

edad = int(input("Ingresa la edad de la persona: "))
categoria = clasificar_edad(edad)
print(categoria)


#3 Evaluar la nota e imprimir el resultado: Por ejemplo: Se recibe una nota con un input (20), y le decimos que letra fue su calificacion (A,B,C,D,E,F)

nota = int(input("Ingresa la nota: "))

if nota >= 90:
    print("Tu calificación es: A")
elif nota >= 80:
    print("Tu calificación es: B")
elif nota >= 70:
    print("Tu calificación es: C")
elif nota >= 60:
    print("Tu calificación es: D")
elif nota >= 50:
    print("Tu calificación es: E")
else:
    print("Tu calificación es: F")


#4 Calcular el descuento en una tienda si el monto supera los 100$ aplicar un 10% de descuento. Por ejemplo: se recibe un numero (el monto de la compra) Usar input.
    
monto = float(input("Ingrese el monto de la compra: "))

if monto > 100: 
    descuento = monto * 0.10 
    total = monto - descuento 
    print(f"Se aplicó un descuento del 10%: ${descuento}") 
    print(f"Total a pagar: ${total}") 
else: 
    print("No se aplicó ningún descuento") 
    print(f"Total a pagar: ${monto}")


#5 Determinar el tipo de triangulo en base a sus lados (EQuilatero, Isosceles o Escaleno) Usar 3 input.

lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es Isósceles")
else:
    print("El triángulo es Escaleno")


#6 Convertir una cantidad de dolares a bolivares o viceversa (usar input).

tasa_de_cambio = 36.33

cantidad = float(input("Introduce la cantidad a convertir: "))
moneda = input("Introduce la moneda de origen (USD para dolares o VES para bolivares): ")

if moneda == "USD":
    cantidad_convertida = cantidad * tasa_de_cambio
    print(f"{cantidad} dolares equivalen a {cantidad_convertida} bolivares")
elif moneda == "VES":
    cantidad_convertida = cantidad / tasa_de_cambio
    print(f"{cantidad} bolivares equivalen a {cantidad_convertida} dolares")
else:
    print("Moneda de origen no reconocida")










































































#6 Convertir una cantidad de dolares a bolivares o viceversa (usar input). 

