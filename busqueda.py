def busquedaLibros(libros):
    # pre: que el parámetro libros sea una lista de tuplas, donde cada elemento tenga al menos tres elementos: un ID, un nombre y una editorial.
    # pos: imprime los resultados de búsqueda de libros que coinciden con el criterio y valor introducidos por el usuario
    # solicitar al usuario
    print("Criterios de búsqueda disponibles: ")
    print("1 - Buscar por ID")
    print("2 - Buscar por Nombre")
    print("3 - Buscar por Editorial")
    
    criterio = int(input("Seleccione el criterio de busqueda (1, 2, 3): "))
    
    # verifica que sea válido
    if criterio not in [1, 2, 3]:
        print("Criterio no válido. Intente nuevamente.")
        return
    
    # valor que el usuario quiere buscar
    valor = input("Ingrese el valor a buscar: ")
    
    #limitar o no los resultados
    nResultados = input("¿Cuántos resultados quiere mostrar? (Deje en blanco para mostrar todos): ")
    nResultados = int(nResultados) if nResultados else None
    
    # busqueda según el criterio seleccionado
    if criterio == 1:
        # Buscar por ID (convertir el valor a entero)
        valor = int(valor)
        resultados = [libro for libro in libros if libro[0] == valor]
    else:
        # Buscar por Nombre o Editorial (convertir a minúsculas para comparación insensible a mayúsculas/minúsculas)
        resultados = [libro for libro in libros if valor.lower() in libro[criterio - 1].lower()]
    
    # slicing si se aclara el iímite
    if nResultados:
        resultados = resultados[:nResultados]
    
    if resultados:
        print("\nResultados encontrados:")
        for libro in resultados:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Editorial: {libro[2]}")
    else:
        print(f"No se encontraron libros que coincidan con '{valor}'.")