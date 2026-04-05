print ("------------------------------------------------------------------------------------")

#Edad de usuario

print ("Edad de usuario")
edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print ("Es mayor de edad")
else:
    print ("Es menor de edad")

print ("------------------------------------------------------------------------------------")

#Nota de usuario

print ("Nota de usuario")
nota_usuario = int(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

print ("------------------------------------------------------------------------------------")

#Numero par e impar

print ("Numero par e impar")
numero_usuario = int(input("Ingrese un número par: "))

if numero_usuario % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número impar")

print ("------------------------------------------------------------------------------------")

#Edad

edad_usuario2 = int(input("Ingrese su edad: "))

if edad_usuario2 < 12:
    print ("Niño")
elif 12 <= edad_usuario2 < 18:
    print ("Adolescente")
elif 18 <= edad_usuario2 < 30:
    print ("Adulto/a joven")
else:
    print ("Adulto/a")

print ("------------------------------------------------------------------------------------")

#Contraseña

print ("Contraseña")
contraseña_usuario = input("Crear una contraseña entre 8 y 14 caracteres: ")

if 8 <= len(contraseña_usuario) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña entre 8 y 14 caracteres")


print ("------------------------------------------------------------------------------------")

#Consumo de energia

consumo_usuario = int(input("Ingrese su consumo de energia eléctrica mensual en KW: "))

if consumo_usuario < 150:
    print ("Consumo bajo")
elif 150 < consumo_usuario < 300:
    print ("Consumo medio")
elif consumo_usuario > 300:
    print ("Consumo alto")

if consumo_usuario > 500:
    print ("Cosnidere medidas de ahorro energético")

print ("------------------------------------------------------------------------------------")

#Vocales

print ("Vocales")

texto_usuario = input ("Ingrese una palabra o frase: ")
vocales = ("a", "b", "c", "i", "o", "u", "A", "B", "C", "I", "O", "U")

if texto_usuario.endswith(vocales):
    texto_usuario2 = texto_usuario + "!"

print (texto_usuario2)

print ("------------------------------------------------------------------------------------")

#Nombre y edición

print ("Ingreso de nombre y edición")

nombre_usuario = input ("Ingrese su nombre: ")

print ("Seleccione una opción: ")
print ("Presione 1 si quiere su nombre en Mayusculas")
print ("Presione 2 si quiere su nombre en minusculas")
print ("Presione 3 si quiere su nombre con inicial Mayuscula")

opcion = int(input("Ingrese la opción deseada: "))

if opcion == 1:
    resultado1 = nombre_usuario.upper()
    print (f"{resultado1}")
elif opcion == 2:
    resultado2 = nombre_usuario.lower()
    print (f"{resultado2}")
elif opcion == 3:
    resultado3 = nombre_usuario.title()
    print (f"{resultado3}")
else:
    print ("Opción no valida, por favor ingrese 1, 2 o 3")

print ("------------------------------------------------------------------------------------")

#Magnitud de terremoto

print ("Magnitud de terremoto")

magnitud_usuario = int(input("Ingrese la magnitud del terremoto: "))

if magnitud_usuario < 3:
    print ("Muy leve")
elif 3 >= magnitud_usuario < 4:
    print ("Leve")
elif 4 >= magnitud_usuario < 5:
    print ("Moderado")
elif 5 >= magnitud_usuario < 6:
    print ("Fuerte")
elif 6 >= magnitud_usuario < 7:
    print ("Muy fuerte")
elif magnitud_usuario > 7:
    print ("Extremo")

print ("------------------------------------------------------------------------------------")

#Hemisferio

hemisferio_usuario = (input("Ingresse el hemisferio en el cual se encuentra (NORTE o SUR): ")).upper()
if hemisferio_usuario != "NORTE" and hemisferio_usuario != "SUR":
    print ("Caracter invalido: Por favor solo ingrese NORTE o SUR")

dia_usuario = int(input("Ingrese el día que se encuentra: "))
if 1 < dia_usuario > 31:
    print ("Dia incorrecto, debe ser entre el 1 y 31")

mes_usuario = int(input("Ingrese el mes en el que se encuentra: "))
if 1 < mes_usuario > 12:
    print ("Mes incorrecto, debe ingresar un mes valido")

if hemisferio_usuario == "NORTE":
    if (mes_usuario == 12 and dia_usuario >= 21) or (mes_usuario == 1 or mes_usuario == 2) or (mes_usuario == 3 and dia_usuario <= 20):
        print ("Es Invierno")
    if (mes_usuario == 3 and dia_usuario >= 21) or (mes_usuario == 4 or mes_usuario == 5) or (mes_usuario == 6 and dia_usuario <= 20):
        print ("Es Primavera")
    if (mes_usuario == 6 and dia_usuario >= 21) or (mes_usuario == 7 or mes_usuario == 8) or (mes_usuario == 9 and dia_usuario <= 20):
        print ("Es Verano")
    if (mes_usuario == 7 and dia_usuario >= 21) or (mes_usuario == 10 or mes_usuario == 11) or (mes_usuario == 12 and dia_usuario <= 20):
        print ("Es Otoño")

if hemisferio_usuario == "SUR":
    if (mes_usuario == 12 and dia_usuario >= 21) or (mes_usuario == 1 or mes_usuario == 2) or (mes_usuario == 3 and dia_usuario <= 20):
        print ("Es Verano")
    if (mes_usuario == 3 and dia_usuario >= 21) or (mes_usuario == 4 or mes_usuario == 5) or (mes_usuario == 6 and dia_usuario <= 20):
        print ("Es Otoño")
    if (mes_usuario == 6 and dia_usuario >= 21) or (mes_usuario == 7 or mes_usuario == 8) or (mes_usuario == 9 and dia_usuario <= 20):
        print ("Es Invierno")
    if (mes_usuario == 7 and dia_usuario >= 21) or (mes_usuario == 10 or mes_usuario == 11) or (mes_usuario == 12 and dia_usuario <= 20):
        print ("Es Primavera")