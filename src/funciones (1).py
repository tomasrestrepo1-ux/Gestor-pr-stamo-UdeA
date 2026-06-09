def ValidarNombreApellido(nombre: str) -> bool:
    
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
    
    
    longitud = len(cedula)
    if longitud >= 3 and longitud <= 15:
        if cedula.isnumeric():
            return True 
        else:
            return False
    else:
        return False

def ValidarCorreo(correo: str) -> bool:
   
    
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
    
    prefijo = ""
    for posicion in range(3):
        if posicion < len(categoria):
            prefijo += categoria[posicion]
    
    prefijo = prefijo.upper()
    id_generado = prefijo + "-" + str(consecutivo)
    return id_generado

def EvaluarEstadoItem(calificacion: str):
    
   
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
   
    if cedula_usuario not in diccionario_prestamos:
        diccionario_prestamos[cedula_usuario] = []
    diccionario_prestamos[cedula_usuario].append(id_articulo)
        
def RegistrarPrestamo(usuarios: dict, inventario: dict, prestamos: dict):
   
    print("\n--- NUEVO PRÉSTAMO ---")
    cedula_cliente = input("Favor ingresar la cédula del usuario a prestar: ")
    if cedula_cliente not in usuarios:
        print("Error: El préstamo no se puede realizar.")
        print("Gestor de prestamos🤑🤑, el usuario no existe. Deberá registrar al usuario nuevo en la opción 1 del menú.")
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
