#Introducción

print ("-----------------------------------------------------------------------------------")

print ("Hola mundo!")

nombre = input("Ingrese su nombre: ")

print (f"Hola {nombre}!")

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia = input("Ingrese su lugar de residencia: ")

print (f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_residencia}")

print ("-----------------------------------------------------------------------------------")

#Area y Perimetro de un Circulo

print ("Calculo de area y perimetro de un Circulo")

pi = 3.14159

radio = float(input("Ingrese el radio del Circulo: "))

perimetro = round (2* pi * radio, 2)
area = round (pi * radio, 2)

print (f"El perimetro del Circulo es {perimetro} y su area es {area}")

print ("-----------------------------------------------------------------------------------")

#Segunods a Horas

print ("Pasar de Segundos a Horas")

segundos = int(input("Ingrese los segundos: "))

conversion_horas = segundos // 3600

print (f"{segundos} segundos son {conversion_horas} horas")

print ("-----------------------------------------------------------------------------------")

#Tabla de Multiplicación 

print ("Tabla de multiplicación")

numero = int(input("Ingrese el numero a multiplicar: "))

for i in range (1,11):
    print (f"{numero} * {i} = {numero * i }")

print ("-----------------------------------------------------------------------------------")

#Suma, resta, multiplicación y división

print ("Suma, resta multiplicación y división")

valor1 = int(input("Ingrese un numero entero: "))
valor2 = int(input("Ingrese otro numero entero: "))

suma_valores = valor1 + valor2
resta_valores = valor1 + valor2
multiplicación_valores = valor1 * valor2
division_valores = valor1 // valor2 

print (f"La suma de ambos numeros es: {suma_valores}")
print (f"La resta de ambos numeros es: {resta_valores}")
print (f"La multiplicación de ambos numeros es: {multiplicación_valores}")
print (f"La división de ambos numeros es: {division_valores}")

print ("-----------------------------------------------------------------------------------")

#Masa Corporal

print ("Calculo de masa corporal")

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso // (altura * altura)

print (f"Su IMC es: {imc:.2f}")

print ("-----------------------------------------------------------------------------------")

#Celsius a Fahrenheit

print ("Pasaje de Celsius a Fahrenheit")

celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = 1.8 * celsius + 32

print (f"{celsius} Celsius son {fahrenheit} Fahrenheit")

print ("-----------------------------------------------------------------------------------")

#Calculo de Promedio

print ("Calculo de promedio")

promedio1 = float(input("Ingrese el primer número: "))
promedio2 = float(input("Ingrese el segundo número: "))
promedio3 = float(input("Ingrese el tercer número: "))

promedio_t = (promedio1 + promedio2 + promedio3)/3

print (f"El promedio es: {promedio_t:.2f}")

print ("-----------------------------------------------------------------------------------")