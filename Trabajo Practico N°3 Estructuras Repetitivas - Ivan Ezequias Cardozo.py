print ("-------------------------------------------------------------------------")

# Ejercicio 1 - Caja del Kiosko
print ("Caja del Kiosko")

#1
nombre = (input("Ingrese el nombre del cliente: "))

while not nombre.isalpha():
    print ("El nombre debe contener solamente letras.")
    nombre = int(input("Vuelva a ingresar el nombre del cliente"))

#2

cantidad_productos = (input("Ingrese la cantidad de productos: "))

while not cantidad_productos.isdigit() or int(cantidad_productos) == 0:
    print ("Debe ingresar un numero mayor a 0.")
    cantidad_productos = (input("Vuelva a ingresar la cantidad de productos: "))

descuento = 0.0
sin_descuento = 0.0
cantidad_p = int(cantidad_productos)

#3
for i in range (cantidad_p):
    print (f"Ingrese el producto n° {i + 1}: ")
    producto_precio = (input("Ingrese el precio del producto: "))
    while not producto_precio.isdigit():
        print ("El precio debe ser un numero")
        producto_precio = input("Vuelva a ingresar el precio del producto: ")

    precio = int(producto_precio)

    dto_producto = input("¿El producto tiene descuento? (S/N): ").lower()
    while dto_producto not in ['s', 'n']:
        print ("Error de ingreso, presione S para si y N para no")
        dto_producto = int(input("¿El producto tiene descuento? (S/N): ")).lower()

    total_sin_descuento = sin_descuento + precio

    if dto_producto == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuento = descuento + precio_final

#4
total_ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_p

print("\n" + "="*30)
print (f"Cliente: {nombre}")
print (f"Cantidad de Productos: {cantidad_p}")
print (f"Total sin descuentos: ${total_sin_descuento:.2f}")
print (f"Total con descuentos: ${total_con_descuento:.2f}")
print (f"Ahorro total: ${total_ahorro:.2f}")
print (f"Promedio por producto: ${promedio:.2f}")
print ("="*30)

print ("-------------------------------------------------------------------------")

#Ejercicio 2 - Acceso al Campus y Menu Seguro

#1
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3
acceso = False

#2
while intentos < max_intentos:
    print (f"Intento {intentos + 1}/{max_intentos}")
    usuario = input("Ingrese el usuario: ")
    clave = input ("Ingrese el password: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print ("Acceso Concedido")
        acceso = True
        break
    else:
        print ("Credenciales inválidas")
        intentos = intentos + 1

if not acceso:
    print ("Demasiados intentos, cuenta bloqueada.")
else:
    while True:
        print ("1. Estado")
        print ("2. Cambiar Clave")
        print ("3. Mensaje")
        print ("4. Salir")
        opcion_ingresada = input("Ingrese la opción: ")

        if not opcion_ingresada.isdigit():
            print ("Ingrese un valor correspondiente")
            continue

        opcion1 = int(opcion_ingresada)

        if opcion1 < 1 or opcion1 > 4:
            print ("Ingrese un valor correspondiente")
            continue

        if opcion1 == 1:
            print ("Inscripto")
        elif opcion1 == 2:
            clave_nueva = input("Nueva clave: ")
            if len (clave_nueva) < 6:
                print ("Debe ingresar una clave con un minimo de 6 caracteres")
            else:
                clave_confirmada = input ("Confirme nueva clave: ")
                if clave_nueva == clave_confirmada:
                    clave_correcta == clave_nueva
                    print ("Clave cambiada con exito")
                else:
                    print ("Las claves no coinciden")
        elif opcion1 == 3:
            print ("Por mas dificil que sea nunca te rindas!")
        elif opcion1 == 4:
            print ("Saliendo del sistema...")
            break
        
print ("-------------------------------------------------------------------------")

#Ejercicio 3 - Agenda de Turnos con Listas

#Dias
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador_nombre = input("Ingrese el nombre del operador: ")
while not operador_nombre.isalpha():
    print (input("Debe ingresar un nombre (Solo letras, no numeros): "))

opcion_turno = "0"
while opcion_turno != "5":
    print ("-----AGENDA DE TURNOS-----")
    print ("1. Reservar turno")
    print ("2. Cancelar turno (por nombre)")
    print ("3. Ver agenda del día")
    print ("4. Ver resumen general")
    print ("5. Cerrar sistema")
    opcion_turno = input("Seleccione la opción deseada: ")

    if opcion_turno == "1":
        dia_turno = input ("Elegir día: 1 = Lunes; 2 = Martes: ")
        while dia_turno not in {"1", "2"}:
            dia_turno = input ("Dia invalido. Seleccione el dia correcto; 1 = Lunes 2 = Martes: ")

        paciente_nombre = input("Ingrese el nombre del paciente: ")
        while not paciente_nombre.isalpha():
            paciente_nombre = input("Debe ingresar el nombre del paciente (solo letras): ")
    
        if dia_turno == "1":
            if paciente_nombre == lunes1 or paciente_nombre == lunes2 or paciente_nombre == lunes3 or paciente_nombre == lunes4:
                print ("El paciente ya tiene un turno ese día")
            elif lunes1 == "": 
                lunes1 = paciente_nombre
            elif lunes2 == "": 
                lunes2 = paciente_nombre
            elif lunes3 == "": 
                lunes3 = paciente_nombre
            elif lunes4 == "": 
                lunes4 = paciente_nombre
            else:
                print ("No hay cupos disponibles para el Lunes")
        else:
            if paciente_nombre == martes1 or paciente_nombre == martes2 or paciente_nombre == martes3:
                print("El paciente ya tiene un turno este día.")
            elif martes1 == "":
                martes1 = paciente_nombre
            elif martes2 == "":
                martes2 = paciente_nombre
            elif martes3 == "":
                martes3 = paciente_nombre
            else: print("No hay cupos disponibles para el Martes")

    elif opcion_turno == "2":
        dia_turno = input ("Elegir el día para cancelar (1, 2): ")
        cancelar_nombre = input ("Ingrese el nombre del paciente a cancelar: ")

        encontrado = False
        if dia_turno == "1":
            if lunes1 == cancelar_nombre:
                lunes1 = ""; encontrado = True
            elif lunes2 == cancelar_nombre:
                lunes2 = ""; encontrado = True
            elif lunes3 == cancelar_nombre:
                lunes3 = ""; encontrado = True
            elif lunes4 == cancelar_nombre:
                lunes4 = ""; encontrado = True
        else:
            if martes1 == cancelar_nombre:
                martes1 = ""; encontrado = True
            if martes2 == cancelar_nombre:
                martes2 = ""; encontrado = True
            if martes3 == cancelar_nombre:
                martes3 = ""; encontrado = True

        if encontrado:
            print ("Turno cancelado")
        else:
            print ("No se encontró el paciente en el día indicado")

    elif opcion_turno == "3":
        dia_turno = input ("Elegir día para ver (1, 2): ")
        if dia_turno == "1":
            print ("-------------------------------------------")
            print (f"1. {lunes1 if lunes1 != "" else "(libre)"}")
            print (f"2. {lunes2 if lunes2 != "" else "(libre)"}")
            print (f"3. {lunes3 if lunes3 != "" else "(libre)"}")
            print (f"4. {lunes3 if lunes3 != "" else "(libre)"}")
            print ("-------------------------------------------")
        else:
            print ("---------------------------------------------")
            print (f"1. {martes1 if martes1 != "" else "(libre)"}")
            print (f"2. {martes2 if martes2 != "" else "(libre)"}")
            print (f"3. {martes3 if martes3 != "" else "(libre)"}")
            print ("---------------------------------------------")

    elif opcion_turno == "4":
        lunes_cantidad = 0
        if lunes1 != "":
            lunes_cantidad = lunes_cantidad + 1
        if lunes2 != "":
            lunes_cantidad = lunes_cantidad + 1
        if lunes3 != "":
            lunes_cantidad = lunes_cantidad + 1
        if lunes4 != "":
            lunes_cantidad = lunes_cantidad + 1
    
        martes_cantidad = 0
        if martes1 != "":
            martes_cantidad = martes_cantidad + 1
        if martes2 != "":
            martes_cantidad = martes_cantidad + 1
        if martes3 != "":
            martes_cantidad = martes_cantidad + 1

        print ("-----------------------------------------------------------------------")
        print (f"Lunes: {lunes_cantidad} ocupados, {4 - lunes_cantidad} disponibles")
        print (f"Martes: {martes_cantidad} ocupados, {3 - martes_cantidad} disponibles")
        print ("------------------------------------------------------------------------")

        if lunes_cantidad >= martes_cantidad:
            print ("----------------------------------------")
            print ("El día con mas turnos o empate es: Lunes")
            print ("-----------------------------------------")
        else:
            print ("----------------------------------")
            print ("El día con mas turnos es: Martes")
            print ("----------------------------------")

    elif opcion_turno == "5":
        print ("Saliendo del sistema...")
    else:
        print ("Opción invalida.")
        break

print ("-------------------------------------------------------------------------")

#Ejercicio 4 - Escape Room: La Boveda

#Valores iniciales

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

print ("- - - - - - - - - Escape Room: La Boveda - - - - - - - - -")

forzar_numero = 0
bloqueo = False

nombre_agente = input("Ingrese su nombre de Agente: ")

while not nombre_agente.isalpha():
    print ("Debe ingresar un nombre de Agente: ")
    nombre_agente = input ("Ingrese su nombre de Agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    print ("---------------------------------------------------")
    print (f"ENERGIA: {energia} /// TIEMPO: {tiempo} /// CERRADURAS: {cerraduras_abiertas}")
    print (f"ALARMA: {'ON' if alarma else 'OFF'}")
    print ("---------------------------------------------------")
    print ("1. FORZAR CERRADURA")
    print ("2. HACKEAR PANEL")
    print ("3. DESCANSAR")

    opcion_juego = input ("Elija una opción: ")
    while not opcion_juego.isdigit() or opcion_juego not in ["1", "2", "3"]:
        print ("Opción invalida: Debe seleccionar 1, 2 o 3")
        opcion_juego = input ("Elija una opción: ")
    
    opcion_juego = int (opcion_juego)

# Opcion 1: FORZAR CERRADURA
    if opcion_juego == 1:
        energia = energia - 20
        tiempo = tiempo - 2
        forzar_numero = forzar_numero + 1
    
        print ("Intentando forzar la cerradura... ")

        if forzar_numero == 3:
            alarma = True
            print ("Haz forzado la cerradura demasiadas veces...")
            print ("¡¡¡La cerradura se trabó y la Alarma se activó!!!")
        else:
            if energia < 40:
                print ("ALERTA: ¡¡¡Tu energia se encuentra debajo de 40, existe un riesgo de que la Alarma se active!!!")
                riesgo_alarma = input ("Elija una opción; 1 2 o 3: ")

                while not riesgo_alarma.isdigit() or riesgo_alarma not in ["1", "2", "3"]:
                    print ("Debe seleccionan una opción valida")
                    riesgo_alarma = input ("Elija una opción; 1 2 o 3: ")
            
                if riesgo_alarma == "3":
                    alarma = True
                    print ("ALERTA: NIVEL DE RIESGO ALTO, LA ALARMA SE HA ACTIVADO")
            if not alarma:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print (f"SE HA LOGRADO ABRIR UNA CERRADURA /// {cerraduras_abiertas}/3")
            else:
                print ("La alarma se encuentra activada, es imposible abrir la cerradura")

    elif opcion_juego == 3:
        tiempo = tiempo - 1
        forzar_numero = 0

        energia = energia + 15
        if energia > 100:
            energia = 100

        print ("Has decidio descansar, recuperaste un poco de energia")

        if alarma:
            energia = energia - 10
        print ("La alarma se encuentra encendida, pierdes 10 de energia")

    elif opcion_juego == 2:
        energia = energia - 10
        tiempo = tiempo - 3
        forzar_numero = 0

        print ("Hackeando...")

        for paso in range (1,5):
            codigo_parcial = codigo_parcial + "A"
            print (f"Paso {paso}/4 completado... Codigo parcial actual: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print (f"Hackeo exitoso. Se abrió 1 cerradura; Cerraduras: {cerraduras_abiertas}/3")

if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
    bloqueo = True

print ("---------------------------------------------")
print ("---------------------------------------------")
print ("------------- FIN DEL JUEGO -----------------")
print ("---------------------------------------------")
print ("---------------------------------------------")

if cerraduras_abiertas >= 3:
    print ("¡Victoria! Lograste abrir la boveda y escapar a tiempo")
elif bloqueo:
    print ("¡DERROTA! La alarma bloqueo el sistema de seguridad debido al tiempo")
elif energia <= 0:
    print ("¡DERROTA! Te quedaste sin energía")
elif tiempo <= 0:
    print ("¡DERROTA! Te quedaste sin tiempo para abrir las 3 cerraduras")


print ("-------------------------------------------------------------------------")
    
#Ejercicio 5 - Escape Room: La Arena del Gladiador

hp_gladiador = 100
hp_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo = 12
juego_activo = True
turno_gladiador = True

nombre_valido = False
while not nombre_valido:
    nombre_gladiador = input ("Ingresa el nombre del Gladiador: ")
    if nombre_gladiador.isalpha():
        nombre_valido = True
    else:
        print ("Solo se permiten letras")

print ("------------------ COMIENZA LA BATALLA! ----------------------------")

while hp_gladiador > 0 and hp_enemigo > 0:
    if turno_gladiador:
        print (f"STATS: {nombre_gladiador}")
        print (f"HP: {hp_gladiador}")
        print (f"HP ENEMIGO: {hp_enemigo}")
        print (f"POCIONES: {pociones}")

        print ("---------------------")
        print ("SELECCIONE UNA ACCIÓN: ")
        print ("1. ATAQUE PESADO")
        print ("2. RÁFAGA VELOZ")
        print ("3. CURAR")
        print ("---------------------")

        opcion_valida = False
        while not opcion_valida:
            opcion_ag = input ("Elige (1, 2 o 3): ")
            if opcion_ag.isdigit():
                if opcion_ag == "1" or opcion_ag == "2" or opcion_ag == "3":
                    opcion_valida = True
                else:
                    print ("Elige 1, 2 o 3")
            else:
                print ("Debe ser un número")
    
        if opcion_ag == "1":
            daño_final = float (ataque_pesado_base)
            if hp_enemigo < 20:
                daño_final = ataque_pesado_base * 1.5
                print ("GOLPE CRÍTICO!")

            hp_enemigo = hp_enemigo - daño_final
            print (f"¡HAS CAUSADO AL ENEMIGO {daño_final} PUNTOS DE DAÑO!")

        elif opcion_ag == "2":
            for i in range (3):
                daño_rafaga = 5
                hp_enemigo = hp_enemigo - daño_rafaga
                print ("GOLPE COONECTADO CON 5 DE DAÑO")

        elif opcion_ag == "3":
            if pociones > 0:
                hp_gladiador = hp_gladiador + 30
                pociones = pociones - 1
                print (f"USASTE UNA POCION. VIDA ACTUAL: {hp_gladiador}")
            else:
                print ("¡NO QUEDAN POCIONES!")
        
        turno_gladiador = False

    else:
        if hp_enemigo > 0:
            print ("----- TURNO DEL ENEMIGO -----")
            hp_gladiador = hp_gladiador - ataque_enemigo
            print (f"¡EL ENEMIGO TE CASUO {ataque_enemigo} PUNTOS DE DAÑO!")
        
        turno_gladiador = True


print ("---------------------------------------------------------")
print ("---------------------------------------------------------")
if hp_gladiador > 0:
    print (f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print ("DERROTA. Has caido en combate.")

print ("------------------------------------------------------------------------------------")