def ValidarNombreApellido(nombre: str) -> bool:
    """primero cuenta la cantidad de caracters que tiene el nombre ingresado (se ingresa desde el main) 
    si es mayor o igual a 3 continua, si no entonces lo rompe
    definimos 'numeros' para asi hacer un doble ciclo for, donde primero se crea una variables llamada letra, y viendo que letra no sea un numero. 
    en caso de que nombre no tenga numeros entonces entregara un True
    """
    longitud = len(nombre)
    if longitud >= 3:
        numeros = '0123456789'
        for letra in nombre:
            if letra in numeros:
                return False
        return True
    else:
        return False

def ValidarCedula(cedula: str) -> bool:
    """ se reviza la longitud de de la cedula, si es mayor a 3 Y menor a 15 continua con el condicional de '.isnumeric' 
    en caso de que todo se compla lanzara un True
    """
    
    longitud = len(cedula)
    if longitud >= 3 and longitud <= 15:
        if cedula.isnumeric():
            return True 
        else:
            return False
    else:
        return False

def ValidarCorreo(correo: str) -> bool:
    """
    se define una variable que este en falso
    se crea un doble ciclo for para poder revizar cada caracter del correo, de esa manera si se encuentra un @ voolvera la variable True
    y rompe el ciclo
    si la variable queda en False, entregara False para toda la funcion
    luego contamos el rango de ese correo, y una losta que se llamara 'finalo correo'
    creamos un doble ciclo for, donde tomara los ultimos 4 caracters del largo del correo, y los guardara en en la lista
    si los ultimos son iguales a '., c, o, m' ebtrega un True para la funcion
    """
    
    if isinstance(correo, str):
        tiene_arroba = False
        for caracter in correo:
            if caracter == "@":
                tiene_arroba = True
                break          
        if tiene_arroba == False:
            return False
        largo = len(correo)
        final_correo = []
        for posicion in range(largo - 4, largo):
            final_correo.append(correo[posicion]) 
        if final_correo == ['.', 'c', 'o', 'm']:
            return True
        else:
            return False
    else:
        return False

def ValidarTiempoPrestamo(dias) -> bool:
    """
     unicamente crea una lista de 4 variables, y reviza que lo que se ingrese en el main sea perteneciente a ese lista, usando un ciclo for
    """
    if isinstance(dias, int):
        opciones_validas = [5, 10, 15, 30]
        if dias in opciones_validas:
            return True
        else:
            return False
    else:
        return False

def ValidarNombreItem(nombre: str) -> bool:
    """
    unicamente valida que su longitud sea mator o igual a 3
    """
    longitud = len(nombre)
    if longitud >= 3:
        return True
    else:
        return False
    
def ValidarCategoria(categoria: str) -> bool: 
    """
    se crea una lista de categorias, y se reviza que lo que se ingrese en main pertenezca a esa lista, para que entregue un True en la funcion
    """
    if isinstance(categoria, str):
        categorias_validas = [
            "Videojuegos", 
            "Libros", 
            "Música y video", 
            "Herramientas", 
            "Dinero", 
            "Misceláneo y varios"]
        if categoria in categorias_validas:
            return True
        else:
            return False  
    else:
        return False
    
def ValidarPrecio(precio: str) -> bool:
    """
    reviza que la longitud sea mayor a cero, y define un variable 'puntos' que empiece en cero, otra que contenga los nomeros
    crea un doble ciclo for donde si algun caracter del precio dado no esta en 'numeros' entregue un False
    ademas, cada vez que un caracter sea un punto agregara un +1 en la variables de 'puntos'
    si puntos es menor a 1 Y la longitud de caracters es mayor a 'puntos' entrega un True
    """
    if isinstance(precio, str):
        longitud = len(precio)
        if longitud > 0:
            puntos = 0
            caracteres_validos = '0123456789.'
            for caracter in precio:
                if caracter not in caracteres_validos:
                    return False
                if caracter == '.':
                    puntos += 1
            if puntos <= 1 and longitud > puntos:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
def CrearIdItem(categoria: str, consecutivo: int) -> str:
    """
    se crea una Variable vacia llamada prefijo. se crea un ciclo for de 3 de rango unicamente donde crea una variable llamada posicion
    si posicion es menor a la longitud de categoria entonces a la variable 'prefijo' le agregara esos 3 primeros digitos de la categoria
    
    luego convertiremos esa variable 'prefijo' a mayusculas
    creamos una nueva variable 'id_generado' que junte prefijo con el texto de consecutivo que se encuentra en el main
    por ultimo retorna la variable 'id_generado' para que se use en el resto de la funcion
    """
    prefijo = ""
    for posicion in range(3):
        if posicion < len(categoria):
            prefijo += categoria[posicion]
    
    prefijo = prefijo.upper()
    id_generado = prefijo + "-" + str(consecutivo)
    return id_generado

def EvaluarEstadoItem(calificacion: str):
    
    """
    primero debe cumplir que sea numerica
    luego la calificacion ingresada en el main se pasara a llamar 'puntaje'
    si puntaje es mayor o igual a cero Y menor o igual a 10 continuara con los retornos que se muestran en la funcion
    """
    if isinstance(calificacion, str):
        if calificacion.isnumeric():
            puntaje = int(calificacion)
            if puntaje >= 0 and puntaje <= 10:
                if puntaje >= 9:
                    return "Excelente (Perfectas condiciones)"
                elif puntaje >= 7:
                    return "Bueno (Tiene detalles menores)"
                elif puntaje >= 4:
                    return "Regular (Desgaste notable pero funcional)"
                elif puntaje >= 1:
                    return "Malo (necesita reparación urgente)"
                else:
                    return "Inservible (Articulo para renovar)"
            else:
                return False
        else:
            return False
    else:
        return False

def RegistrarUsuarioEnPrestamos(diccionario_prestamos: dict, cedula_usuario: str, id_articulo: str):
    """
    crwamos un diccionario donde esten los usuarios con prestamos, en caso de que la cedula de un usuarion no este en ese diccionario lo guardara como una llave
    luego el Id del articulo que se definio previamente pasara a ser el contenido de dicha llave.
    """
    if cedula_usuario not in diccionario_prestamos:
        diccionario_prestamos[cedula_usuario] = []
    diccionario_prestamos[cedula_usuario].append(id_articulo)
        
def RegistrarPrestamo(usuarios: dict, inventario: dict, prestamos: dict):
    """
    se abre un meno y se solicita la cedula del usuario que va a prestar
    en caso que la cedula no exista en la lista de usuarios, imprimira la informacion y entregara un False para que se detenga
    si el inventario esta vacio, osea su longitud es cero, tambien se informara y entregara el False
    en caso de si haber items los mostrara de forma ordenada, colocando primero su Id, el nombre y estado en que esta
    luego pide un Id de item, si o existe en el inventario lo dira y retornara False
    creamos un variable en False y hacemos un ciclo for donde revice que el item no este porestado ya, si lo esta deja la variable en True
    si la variable es True avisara que el item ya esta prestado.
    en caso de que no haya problemas, asiganara cada cosa donde debe, el item, los dias prestados, y el nombre del cliente que se lo lleva
    guardando al cliente en el diccionario de prestamos con el respectivo item que presto
    por ultimo informara de lo que se hizo y arrojara True para la funcion
    
    """
    print("\n--- NUEVO PRÉSTAMO ---")
    cedula_cliente = input("Favor ingresar la cédula del usuario a prestar: ")
    if cedula_cliente not in usuarios:
        print("Error: El préstamo no se puede realizar.")
        print("Loans_Nicker, el usuario no existe. Deberá registrar al usuario nuevo en la opción 1 del menú.")
        return False 
    print("\n--- OBJETOS ACTUALES EN EL INVENTARIO ---")
    if len(inventario) == 0:
        print("Lo sentimos, actualmente no hay ítems registrados en el almacén.")
        return False
        
    for id_item in inventario:
        nombre_articulo = inventario[id_item][0]
        estado = inventario[id_item][3]
        print(f"ID: {id_item} | Artículo: {nombre_articulo} | Estado: {estado}")
        
    id_seleccionado = input("\nIngrese el ID del ítem que desea prestar: ")
    if id_seleccionado not in inventario:
        print("Error: El ID ingresado no coincide con ningún artículo del inventario.")
        return False
        
    item_ya_prestado = False
    for lista_articulos in prestamos.values():
        if id_seleccionado in lista_articulos:
            item_ya_prestado = True
            break
            
    if item_ya_prestado == True:
        print("Error: Este artículo ya se encuentra prestado a otro usuario. Elija otro.")
        return False
        
    dias_asignados = usuarios[cedula_cliente][3]
    nombre_usuario = usuarios[cedula_cliente][0]
    nombre_item = inventario[id_seleccionado][0]
    
    if cedula_cliente not in prestamos:
        prestamos[cedula_cliente] = []
    prestamos[cedula_cliente].append(id_seleccionado)
    
    print("--------------------------------------------------")
    print(f"¡Préstamo exitoso! Se ha prestado el ítem '{nombre_item}'")
    print(f"Al usuario: {nombre_usuario} (C.C. {cedula_cliente})")
    print(f"Tiempo autorizado: {dias_asignados} días.")
    print("--------------------------------------------------")
    return True

def GenerarArchivoPrestamos(usuarios: dict, inventario: dict, prestamos: dict, nombre_archivo: str):
    """
    primero abre el archivo en modo de escritura
    luego con un ciclo for recorre la lista de cedulkas que tienen prestamos, obtiene los IDS prestados por ese usuario
    obtiene los dias de prestamo que puede tener un usuario
    luego un ciclo for para ver si cual item corresponde por si tiene varios prestados
    obtenemos el nombre del item
    y por ultimo obtenemos la linea con todos los elementos ya mencionados
    ponemos la linea en el archivo
    y cerramos el archivo    
    """
    archivo = open(nombre_archivo, 'w', encoding='utf-8')
    for cedula in prestamos:
        lista_ids_prestados = prestamos[cedula]
        dias = usuarios[cedula][3]
        for id_item in lista_ids_prestados:
            nombre_item = inventario[id_item][0]
            linea = f"{cedula},{id_item},{nombre_item},{dias}\n"
            archivo.write(linea)
    archivo.close()
    
def ConsultarEstadoPrestamos(nombre_archivo: str):
    """
    llamamos el archivo en modo lectura
    y creamos una lista vacia para ver los prestamos
    hacemos un ciclo for para ver cada linea en el archivo 
    y hacemos un variable vacia
    hacemos que cada que pase por el ciclo for, tome una linea y la escriba en la linea limpia, al repetir nos ira dejando el listado de informacion de los prestamos
    cuando la longitud de las lineas limpias sean cero, se detendra
    luego de esto unicamente creamos variables para poder hacer una impresion del estado de los prestamos
    
    """
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    lista_prestamos = []
    
    for linea in archivo:
        linea_limpia = ""
        for caracter in linea:
            if caracter != "\n":
                linea_limpia = linea_limpia + caracter
        
        if len(linea_limpia) == 0:
            continue
            
        datos = linea_limpia.split(",")
        
        prestamo = {
            "cedula": datos[0],
            "id_item": datos[1],
            "nombre_item": datos[2],
            "dias": int(datos[3]) 
        }
        lista_prestamos.append(prestamo)
        
    archivo.close()
    
    if len(lista_prestamos) == 0:
        print("No hay ningún préstamo registrado en el archivo plano para mostrar.")
        return

    tamano = len(lista_prestamos)
    for i in range(tamano):
        for j in range(0, tamano - i - 1):
            if lista_prestamos[j]["dias"] < lista_prestamos[j + 1]["dias"]:
                temporal = lista_prestamos[j]
                lista_prestamos[j] = lista_prestamos[j + 1]
                lista_prestamos[j + 1] = temporal

    total_items = len(lista_prestamos)
    suma_dias = 0

    maximo_dias = lista_prestamos[0]["dias"]
    minimo_dias = lista_prestamos[total_items - 1]["dias"]
    
    print("\n========================================================")
    print("   REPORTE: ESTADO GENERAL DE PRÉSTAMOS (Gestor de prestamos🤑🤑)   ")
    print("========================================================")
    print("Artículos actualmente prestados (Ordenados de Mayor a Menor días):")

    for p in lista_prestamos:
        print(f"- Ítem: {p['nombre_item']} (ID: {p['id_item']}) | Días: {p['dias']} | Usuario C.C: {p['cedula']}")
        suma_dias = suma_dias + p["dias"]
        
    promedio_dias = suma_dias / total_items
    
    print("--------------------------------------------------------")
    print("                ESTADÍSTICAS GENERALES                  ")
    print("--------------------------------------------------------")
    print(f"• Total de artículos prestados: {total_items}")
    print(f"• Promedio de tiempo de préstamos: {promedio_dias:.1f} días")
    print(f"• Préstamo más antiguo (Máximo de días): {maximo_dias} días")
    print(f"• Préstamo más reciente (Mínimo de días): {minimo_dias} días")
    print("========================================================\n")

def ValidarCredencialesAdmin(usuario: str, contrasena: str) -> bool:
    """
    crearemos un diccionarios donde la llave son lso usuarios y las contraseñas algo ramdom
    luego en el main pedimos una contaseña si la que ingreso es igual a la que esta registrada en el diccionario la funcion se hara True
    
    """
    admins_autorizados = {
        "Juan": "juan123",
        "tomas": "tomas123",
        "julian": "julian123"
    }
    
    if usuario in admins_autorizados:
        if admins_autorizados[usuario] == contrasena:
            return True
            
    return False

def GenerarReportesAdmin(usuarios: dict, prestamos: dict, devoluciones: dict, ventas: list, total_pagos: float):
    
    """
    esto es solo un reguero de informacion donde primero se imprime un repositorio bonito y luego se crean variables para poder llenar ese repositorio de forma ordenada
    juega mucho tambien con la informacion registrada en las demas funciones, osea reviza los diccionarios que creamos con atelacion, para ver si estan vacios o extraer informacion de ahi
    
    """
    print("\n" + "="*100)
    print(" PANEL DE CONTROL - ADMINISTRADOR ".center(100))
    print("="*100)
    total_prestamos = 0
    for cedula in prestamos:
        for item in prestamos[cedula]:
            total_prestamos += 1
    print(f"• Total de préstamos registrados: {total_prestamos}")
    total_devueltos = 0
    for cedula in devoluciones:
        for item in devoluciones[cedula]:
            total_devueltos += 1
    print(f"• Total de ítems devueltos: {total_devueltos}")
    total_ventas = 0
    for venta in ventas:
        total_ventas += 1
    print(f"• Total de ventas realizadas: {total_ventas}")
    print(f"• Total pagos recibidos: ${total_pagos}")
    print("-" * 100)
    print("• LISTA DE USUARIOS REGISTRADOS:")
    if len(usuarios) == 0:
        print("  Aún no hay usuarios en el sistema.")
    else:
        for cedula in usuarios:
            nombre = usuarios[cedula][0]
            apellido = usuarios[cedula][1]
            print(f"  - C.C: {cedula} | Nombre: {nombre} {apellido}")
    print("-" * 100)
    if len(prestamos) == 0:
        print("• Estadísticas: No hay préstamos registrados para calcular mayor/menor.")
    else:
        mayor_cantidad = -1
        menor_cantidad = 999999
        cedula_mayor = ""
        cedula_menor = ""
        for cedula in prestamos:
            amount_actual = 0
            for item in prestamos[cedula]:
                amount_actual += 1
            if amount_actual > mayor_cantidad:
                mayor_cantidad = amount_actual
                cedula_mayor = cedula
            if amount_actual < menor_cantidad:
                menor_cantidad = amount_actual
                cedula_menor = cedula
        nombre_mayor = usuarios[cedula_mayor][0] + " " + usuarios[cedula_mayor][1]
        nombre_menor = usuarios[cedula_menor][0] + " " + usuarios[cedula_menor][1]
        print(f"• Usuario con MAYOR cantidad de préstamos: {nombre_mayor} ({mayor_cantidad} ítems)")
        print(f"• Usuario con MENOR cantidad de préstamos: {nombre_menor} ({menor_cantidad} ítems)")
    print("="*100 + "\n")

def RegistrarDevolucion(usuarios: dict, prestamos: dict, devoluciones: dict, inventario: dict, ventas: list, pagos_acumulados: float):
    """
    primero pregunta la cedula y reviza que exista como llave en el diccionario de usuarios y usuarios con prestamos 
    luego llama los items en la lista de Ids que tengan esa cedula como llave
    y con ese Id llamara el nombre del item correspondiente para mostrarlos al admin
    luego de eso pedira que item devolvera, obviamente solo dejando seleccionar entre los Id que el archivo trajo
    despues solo empezara a sacar la informacion de los diccionarios pertienentes y decirlo con unos bonitos Prints 
    creara diferentes variables para poder generar una factura
    por ultimo hara un return para actualizar la informacion en todo el main
    
    """
    print("\n--- REGISTRAR DEVOLUCIÓN ---")
    cedula = input("Ingrese la cédula del usuario que va a devolver: ")
    
    if cedula not in usuarios:
        print("Error: El usuario no está registrado en el sistema.")
        return prestamos, devoluciones, ventas, pagos_acumulados
    
    if cedula not in prestamos or len(prestamos[cedula]) == 0:
        print("Error: Este usuario no tiene préstamos activos para devolver.")
        return prestamos, devoluciones, ventas, pagos_acumulados
    
    print("\n--- ÍTEMS PRESTADOS ACTUALMENTE ---")
    lista_ids = prestamos[cedula]
    for i in range(len(lista_ids)):
        id_item = lista_ids[i]
        nombre_item = inventario[id_item][0]
        print(f"{i+1}. ID: {id_item} | Artículo: {nombre_item}")
    
    try:
        seleccion = int(input("\nSeleccione el número del ítem a devolver: "))
        if seleccion < 1 or seleccion > len(lista_ids):
            print("Error: Selección no válida.")
            return prestamos, devoluciones, ventas, pagos_acumulados
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return prestamos, devoluciones, ventas, pagos_acumulados
    
    id_a_devolver = lista_ids[seleccion - 1]
    nombre_item = inventario[id_a_devolver][0]
    precio_item = float(inventario[id_a_devolver][2])
    
    dias_permitidos = usuarios[cedula][3]
    
    print(f"\nEl usuario tiene permitido {dias_permitidos} días de préstamo.")
    try:
        dias_transcurridos = int(input("¿Cuántos días han pasado desde el préstamo? "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return prestamos, devoluciones, ventas, pagos_acumulados
    
    prestamos[cedula].remove(id_a_devolver)
    
    if len(prestamos[cedula]) == 0:
        del prestamos[cedula]

    if cedula not in devoluciones:
        devoluciones[cedula] = []
    devoluciones[cedula].append(id_a_devolver)
    
    if dias_transcurridos > 30:
        print("\n" + "="*60)
        print("ATENCION: EL ITEM SUPERA LOS 30 DIAS DE PRESTAMO")
        print("Se procederá a generar una FACTURA DE VENTA forzosa.")
        print("="*60)
        
        impuesto = precio_item * 0.23
        total = precio_item + impuesto
        
        factura = {
            'cedula_usuario': cedula,
            'nombre_usuario': usuarios[cedula][0] + " " + usuarios[cedula][1],
            'id_item': id_a_devolver,
            'nombre_item': nombre_item,
            'precio_compra': precio_item,
            'impuesto_23': impuesto,
            'total': total,
            'motivo': "Préstamo superior a 30 días sin devolución"
        }
        ventas.append(factura)
        pagos_acumulados = pagos_acumulados + total
        
        nombre_archivo = f"factura_{cedula}_{id_a_devolver}.txt"
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        archivo.write("="*60 + "\n")
        archivo.write("FACTURA DE VENTA - PRESTAMO FORZOSO\n")
        archivo.write("="*60 + "\n")
        archivo.write(f"Cliente: {factura['nombre_usuario']} (C.C. {cedula})\n")
        archivo.write(f"Artículo: {nombre_item} (ID: {id_a_devolver})\n")
        archivo.write(f"Precio de adquisición: ${precio_item:,.0f}\n")
        archivo.write(f"Impuesto por concluidez (23%): ${impuesto:,.0f}\n")
        archivo.write(f"TOTAL A PAGAR: ${total:,.0f}\n")
        archivo.write("-"*60 + "\n")
        archivo.write(f"Motivo: {factura['motivo']}\n")
        archivo.write("="*60 + "\n")
        archivo.close()
        
        print(f"Factura generada: {nombre_archivo}")
        print(f"Total a pagar por {nombre_item}: ${total:,.0f}")
        
    else:
        print("\nDevolución registrada exitosamente dentro del plazo.")
        
        nombre_archivo = f"certificado_{cedula}_{id_a_devolver}.txt"
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        archivo.write("="*60 + "\n")
        archivo.write("CERTIFICADO DE DEVOLUCION\n")
        archivo.write("="*60 + "\n")
        archivo.write(f"Usuario: {usuarios[cedula][0]} {usuarios[cedula][1]} (C.C. {cedula})\n")
        archivo.write(f"Artículo devuelto: {nombre_item} (ID: {id_a_devolver})\n")
        archivo.write(f"Días permitidos: {dias_permitidos}\n")
        archivo.write(f"Días transcurridos: {dias_transcurridos}\n")
        archivo.write("-"*60 + "\n")
        archivo.write("El artículo fue devuelto en buen estado.\n")
        archivo.write("Queda sin deudas pendientes con el admin.\n")
        archivo.write("="*60 + "\n")
        archivo.close()
        
        print(f"Certificado de devolución generado: {nombre_archivo}")
    
    return prestamos, devoluciones, ventas, pagos_acumulados

def ConsultarItemsMas30Dias(usuarios: dict, prestamos: dict, inventario: dict):
    """
    primero revisara que en el diccionario de prestamos exista algo, si no lo informara 
    crearemos una lista con los prestamos de mas de 30 dias
    con un ciclo for recorrera la informacion de ids qie estan en prestamos usando las llaves de las cedulas
    y traera la cantidad de dias de prestamos registradas por cada usuario
    luego traera toda la informacion del item desde el diccionario de inventario
    hara un print con la informacion del cliente incluyendo los dias que tiene permitido
    luego preguntara cuanto tiempo se paso esa persona con el prestamo
    y si es mayor a 30, los guaradara y advertira al admin de que debe generar la factura de cobro
    """
    print("\n--- ITEMS CON MAS DE 30 DIAS EN PRESTAMO ---")
    
    if len(prestamos) == 0:
        print("Actualmente no hay préstamos activos en el sistema.")
        return
    
    items_mas_30 = []
    
    for cedula in prestamos:
        lista_ids = prestamos[cedula]
        dias_permitidos = usuarios[cedula][3]
        
        for id_item in lista_ids:
            nombre_item = inventario[id_item][0]
            categoria = inventario[id_item][1]
            precio = inventario[id_item][2]
            
            print(f"\nArtículo: {nombre_item} (ID: {id_item})")
            print(f"  Usuario: {usuarios[cedula][0]} {usuarios[cedula][1]}")
            print(f"  Días permitidos por el adimin: {dias_permitidos}")
            
            try:
                dias = int(input("  ¿Cuántos días han pasado desde el préstamo? "))
            except ValueError:
                print("  Entrada inválida. Se omitirá este ítem.")
                continue
            
            if dias > 30:
                items_mas_30.append({
                    'cedula': cedula,
                    'usuario': usuarios[cedula][0] + " " + usuarios[cedula][1],
                    'id_item': id_item,
                    'nombre_item': nombre_item,
                    'categoria': categoria,
                    'precio': precio,
                    'dias_transcurridos': dias,
                    'dias_permitidos': dias_permitidos
                })

    print("\n" + "="*70)
    print(f"RESULTADOS: {len(items_mas_30)} item(es) con mas de 30 dias")
    print("="*70)
    
    if len(items_mas_30) == 0:
        print("No hay ítems que superen los 30 días de préstamo.")
        return
    
    for item in items_mas_30:
        print(f"\n{item['nombre_item']} (ID: {item['id_item']})")
        print(f"   Usuario: {item['usuario']} (C.C. {item['cedula']})")
        print(f"   Categoría: {item['categoria']}")
        print(f"   Precio de compra: ${float(item['precio']):,.0f}")
        print(f"   Días transcurridos: {item['dias_transcurridos']}")
        print(f"   Días permitidos: {item['dias_permitidos']}")
        print("   Este artículo debe ser VENDIDO al usuario (aplica impuesto del 23%)")
    
    print("\n" + "="*70)
    print("Recomendación: Use la opción 3 (Registrar Devolución) para proceder con la venta.")
    print("="*70) 