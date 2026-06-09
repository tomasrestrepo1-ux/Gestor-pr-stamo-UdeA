import funciones

usuarios = {}
inventario = {}         
prestamos = {}          
consecutivo_items = 0   
devoluciones = {}
ventas = []
pagos_acumulados = 0.0  

gest = """
Gestor de prestamos🤑🤑
"""

def MostrarMenu():
    separador = '-' * 100
    menu = f"""{separador}
{separador}
{gest}
Bienvenido a Gestor de prestamos🤑🤑
    1. Registrar Usuario
    2. Registrar Prestamo e Items
    3. Registrar Devolucion
    4. Consultar Items con mas de 30 dias
    5. Consultar Articulos Prestado
    6. Administrador
    7. Salir
{separador}
{separador}"""
    return menu


OPCIONES_VALIDAS = ['1', '2', '3', '4', '5', '6', '7']

while True:
    print(MostrarMenu())
    opcion = input('Favor registrar la opcion deseada--> ')
    if opcion in OPCIONES_VALIDAS:
        match opcion:
            case '1':
                print('\tRegistrar Usuario')
                cedula = input('Favor ingresar la cedula: ')
                nombre = input('ingrese el nombre ->')
                apellido = input('ingrese el apellido ->')
                correo = input('ingrese el correo -> ')
                dias_prestamo = input('Favor ingresar los dias del prestamo asignados (5, 10, 15, 30): ')               
                if dias_prestamo.isnumeric():
                    dias_pasar = int(dias_prestamo)
                else:
                    dias_pasar = dias_prestamo
                if funciones.ValidarCedula(cedula):
                    if funciones.ValidarNombreApellido(nombre):
                        if funciones.ValidarNombreApellido(apellido):
                            if funciones.ValidarCorreo(correo):
                                if funciones.ValidarTiempoPrestamo(dias_pasar) == True: 
                                    usuarios[cedula] = [nombre, apellido, correo, dias_pasar]
                                    print('Usuario registrado con exito!')
                                else:
                                    print('Cordial saludo, querido prestamista, el tiempo ingresado no cumple con las reglas requeridas')
                                    continue
                            else:
                                print('Cordial saludo, querido prestamista, su correo no cumple con las reglas requeridas')
                                continue
                        else:
                            print('Cordial saludo, querido prestamista, su apellido no cumple con las reglas requeridas')
                            continue
                    else:
                        print('Cordial saludo, querido prestamista, su nombre no cumple con las reglas requeridas')
                        continue
                else:
                    print('Cordial saludo, querido prestamista, su cedulano cumple con las reglas requeridas')
                    continue
            
            case '2':
                print('\n\t===! MODULO DE INVENTARIO Y PRESTAMOS !===')
                print('1. Registrar un NUEVO Item en el almacen')
                print('2. Registrar el PRESTAMO de un Item a un usuario')
                sub_opcion = input('Favor ingresar la opcion deseada (1 o 2)--> ')   
                if sub_opcion == '1':
                    print('\n=== REGISTRO DE NUEVO ARTICULO ===')
                    nombre_item = input('Favor ingresar el nombre del Item -> ')
                    categoria_item = input('Favor ingresar la categoria -> ')
                    if len(categoria_item) > 0:
                        categoria_item = categoria_item[0].upper() + categoria_item[1:].lower()
                    precio_item = input('Favor ingresar el precio de compra del item -> ')
                    calificacion_item = input('Califique el estado fisico del item (0 al 10) -> ')
                    if funciones.ValidarNombreItem(nombre_item):
                        if funciones.ValidarCategoria(categoria_item):
                            if funciones.ValidarPrecio(precio_item):
                                estado_texto = funciones.EvaluarEstadoItem(calificacion_item)
                                if estado_texto != False:
                                    id_item_generado = funciones.CrearIdItem(categoria_item, consecutivo_items)
                                    print(f" el ID generado automaticamente para el Item es: {id_item_generado}")
                                    inventario[id_item_generado] = [nombre_item, categoria_item, precio_item, estado_texto]
                                    consecutivo_items += 1
                                    print('item registrado en el inventario con exito!')
                                else:
                                    print('Cordial saludo, querido prestamista, la calificacion del estado no cumple con las reglas requeridas')
                            else:
                                print('Cordial saludo, el precio ingresado no cumple con las reglas requeridas')
                        else:
                            print('Cordial saludo, la categoriaa ingresada no cumple con las reglas requeridas')
                    else:
                        print('Cordial saludo, el nombre del item no cumple con las reglas requeridas')    
                elif sub_opcion == '2':
                    funciones.RegistrarPrestamo(usuarios, inventario, prestamos)
                else:
                    print('Opcion no disponible en este menu. Volviendo al menu principal.')
            
            case '3':
                print('\tRegistrar Devolucion')
                prestamos, devoluciones, ventas, pagos_acumulados = funciones.RegistrarDevolucion(usuarios, prestamos, devoluciones, inventario, ventas, pagos_acumulados)
            
            case '4':
                print('\tConsultar Items con mas de 30 dias ')
                funciones.ConsultarItemsMas30Dias(usuarios, prestamos, inventario)
            
            case '5':
                print('\tConsultar Articulos Prestado')             
                if len(prestamos) == 0:
                    print("Aun no se ha realizado ningun prestamo en el sistema.")
                else:
                    nombre_txt = 'registro_prestamos.txt'
                    funciones.GenerarArchivoPrestamos(usuarios, inventario, prestamos, nombre_txt)
                    funciones.ConsultarEstadoPrestamos(nombre_txt)
            
            case '6':
                print('\tAdministrador')
                user_ingresado = input("Favor ingresar el usuario del administrador -> ")
                pass_ingresada = input("Favor ingresar la contraseña -> ")
                
                es_admin = funciones.ValidarCredencialesAdmin(user_ingresado, pass_ingresada)
                
                if es_admin == True:
                    print("\nAcceso concedido. Cargando reportes del sistema...")
                    funciones.GenerarReportesAdmin(usuarios, prestamos, devoluciones, ventas, pagos_acumulados)
                else:
                    print("\nError: Usuario o contraseña incorrectos. Volviendo al menu.")
            
            case '7':
                print('Gracias por usar Gestor de prestamos🤑🤑')
                break
        
    else:
        error = 'Opcion no disponible, por favor vuelve a intentarlo.'
        print(error)
        continue
