def mostrar_menu():
    print("=== SISTEMA DE INVENTARIO ===")
    print("1. Cargar herramientas")
    print("2. Mostrar inventario")
    print("3. Consultar stock")
    print("4. Reporte de agotados")
    print("5. Alta de producto")
    print("6. Actualizar stock")
    print("7. Salir")

def main():
    inventario = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cargar_herramientas(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            consultar_stock(inventario)
        elif opcion == "4":
            reporte_agotados(inventario)
        elif opcion == "5":
            alta_producto(inventario)
        elif opcion == "6":
            actualizar_stock(inventario)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


##Funciones para cada opción del menú## 


def cargar_herramientas(inventario):
    print("\n=== CARGA DE HERRAMIENTAS ===")
    if len(inventario) > 0:
        print("El inventario ya tiene herramientas cargadas")
        print("Para agregar más herramientas, por favor use la opción de 'Alta de producto'")
        return
    
    try:
        cantidad_herramientas = int(input("Ingrese la cantidad de herramientas a cargar: "))
        if cantidad_herramientas <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
            return
    except ValueError as e:
        print(f"Error: {e}.")
        return
    
    contador = 0

    while contador < cantidad_herramientas:

        try:
            nombre = input(f"\nIngrese el nombre de la herramienta {contador + 1}: ").strip()
            if nombre == "":
                raise ValueError("El nombre no puede estar vacío.")
            
            #Validar duplicados
            for item in inventario: 
                if (item["herramienta"].strip().lower() == nombre.lower()):
                    raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
                
            cantidad = int(input("Ingrese la cantidad inicial: "))
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            herramienta = {"herramienta": nombre, "cantidad": cantidad}
            inventario.append(herramienta)
            contador += 1

        except ValueError as e:
            print(f"Error: {e}.")

    print("\nCarga completada exitosamente.")

def mostrar_inventario(inventario):
    print ("\n=== INVENTARIO DE HERRAMIENTAS ===" )
    
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    for i, item in enumerate(inventario, start=1):
        print(f"{i}. {item['herramienta']} |"
              f" Cantidad: {item['cantidad']}")
        
def buscar_herramienta(inventario, nombre):
    print(f"\nBuscando herramienta: {nombre}")
    nombre = nombre.strip().lower()

    for item in inventario:
        if item["herramienta"].strip().lower() == nombre:
            return item
        
    return None

def consultar_stock(inventario):
    print("\n=== CONSULTA DE STOCK ===")
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return

    nombre = input("Ingrese el nombre de la herramienta: ")
    herramienta = buscar_herramienta(inventario, nombre)
    if herramienta is None:
        print(f"La herramienta '{nombre.strip()}' no se encuentra en el inventario.")
        return
    print(f"Herramienta: {herramienta['herramienta']}")
    print(f"Cantidad disponible: {herramienta['cantidad']}")

def reporte_agotados(inventario):
    print("\n=== REPORTE DE HERRAMIENTAS AGOTADAS ===")
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return
    
    hay_agotados = False
    for item in inventario: 
        if item["cantidad"] == 0:
            print(f"Herramienta: {item['herramienta']} | Cantidad: {item['cantidad']}")
            hay_agotados = True

    if not hay_agotados:
        print("No hay herramientas agotadas en el inventario.")

def alta_producto(inventario):
    print("\n=== ALTA DE NUEVO PRODUCTO ===")
    try:
        nombre = input("Ingrese el nombre de la herramienta: ").strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")
        
        #Validar duplicados
        herramienta = buscar_herramienta(inventario, nombre)
        if herramienta is not None:
            raise ValueError(f"La herramienta '{nombre}' ya existe")
        
        cantidad = int(input("Ingrese la cantidad disponible:"))
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        
        nueva_herramienta = {"herramienta": nombre, "cantidad": cantidad}
        inventario.append(nueva_herramienta)
        print(f"Herramienta '{nombre}' agregada exitosamente.")
    
    except ValueError as e:
        print(f"Error: {e}.")

def actualizar_stock(inventario):
    print("\n=== ACTUALIZACIÓN DE STOCK ===")
    if len(inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")
        return
    
    nombre = input("Ingrese el nombre de la herramienta: ")

    herramienta = buscar_herramienta(inventario, nombre)
    if herramienta is None:
        print(f"La herramienta '{nombre.strip()}' no se encuentra en el inventario.")
        return 
     
    print("\n1. Venta")
    print("2. Ingreso")

    opcion = input("Seleccione una opción: ").strip()
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        
        #VENTA
        if opcion == "1":
            if herramienta["cantidad"] < cantidad:
                raise ValueError("No hay suficiente stock para realizar la venta.")
            herramienta["cantidad"] -= cantidad
            print(f"Venta registrada. Stock actualizado: {herramienta['cantidad']}")

        #INGRESO
        elif opcion =="2":
            herramienta["cantidad"] += cantidad
            print(f"Ingreso registrado. Stock actualizado: {herramienta['cantidad']}")
        else:
            print("Opción inválida. Intente nuevamente.")
            return
        
        print(f"Nuevo stock de '{herramienta['herramienta']}': {herramienta['cantidad']}")
    
    except ValueError as e:
        print(f"Error: {e}.")

if __name__ == "__main__":
    main()