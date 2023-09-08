import cod_generator       

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    
    nuevo_codigo=generar_codigo()               
    cant_nuevo_ejemplar=int(input("Indique la cantidad de libros que ingresan: "))
    titulo_nuevo_ejemplar=input("Título del nuevo libro: ")
    autor_nuevo_ejemplar=input("Autor del nuevo libro: ")
    respuesta=""
    while respuesta != "SI" and respuesta != "NO":
        respuesta=input("Confirma el alta del nuevo libro? (SI/NO):")
        if respuesta=="SI":
            alta_nuevo_libro={"cod": nuevo_codigo, 
                              "cant_ej_ad": cant_nuevo_ejemplar,
                              "cant_ej_pr": 0,
                              "titulo": titulo_nuevo_ejemplar,
                              "autor": autor_nuevo_ejemplar}
            print("\nSe ha ingresado un nuevo registro. Datos del nuevo registro:\n")
            print(f"Código: {nuevo_codigo}\nTítulo del libro: {titulo_nuevo_ejemplar}\nAutor: {autor_nuevo_ejemplar}\nCantidad total: {cant_nuevo_ejemplar}")
        elif respuesta=="NO": 
            print("Se cancela el registro de un nuevo libro")
            alta_nuevo_libro={}
        else:   
            print("La palabra ingresada no pertenece a ninguna de las opciones, por favor ingrese SI o NO")
    return alta_nuevo_libro
    return None

def generar_codigo():

    nuevo_codigo=cod_generator.generar()
    return nuevo_codigo
    return None