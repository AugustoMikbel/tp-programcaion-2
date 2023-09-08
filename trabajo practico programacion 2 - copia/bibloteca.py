import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for i in libros:
        print(i)

def registrar_nuevo_libro():
   #Opción 3.
    registro_nuevo_ejemplar=l.nuevo_libro()
    if registro_nuevo_ejemplar:
        libros.append(registro_nuevo_ejemplar)
        print("")
        print("Los nuevos libros han sido agregados al registro de la biblioteca")
    else:
        print("No se realizó ningún alta por elección del usuario")  
    return None

def eliminar_ejemplar_libro():
    #Opción 4.
    codigo_a_borrar=input("Por favor ingrese el código del libro a eliminar: ")
    for libro in libros:
        if codigo_a_borrar==libro["cod"]:
            print(f"Se ha restado una unidad del stock total de ese libro. *Código: {codigo_a_borrar}")
            libro["cant_ej_ad"]-=1
            print("El total en stock de ese libro es: \t")
            print(libro["cant_ej_ad"])
            return
    print(f"El código ingresado: {codigo_a_borrar} no se pertenece a ningún libro existente.\n")
    return None

def prestar_ejemplar_libro():
    print("Ingrese un codigo de libro")
    codl=input()

    for i in libros:

    
        if i["cod"]==codl:
            print("el titulo es:",i['titulo'])
            print("la cantidad de ejemplares disponibles es: ",i['cant_ej_ad'])
            print("el autor es:", (i['autor']))
            if i['cant_ej_ad']>0:
                print("quiere este libro: si(1), no(2)")
                sino=int(input())
                if sino==1:
                    i['cant_ej_ad']-=1
                    i['cant_ej_pr']+=1

                    print("Ejemplares disponibles",i['cant_ej_ad'])
                    print("Ejemplares prestados",i['cant_ej_pr'])
                    print("gracias y vuelva pronto")
            else:
                print("no hay mas libros de este titulo")        
        elif i==libros:
            print("Este libro no existe")

def devolver_ejemplar_libro():
    print("Ingrese un codigo de libro que desea devolver")
    codld=input()
    for i in libros:
        if i['cod'] == codld and i["cant_ej_pr"]>0:
            print("el libro es", i['titulo'])
            print("Tiene ",i["cant_ej_pr"]," ejemplares prestados")
            print("Usted desea devolver este libro: si(1) no(2)")
            sino2=int(input())
            if sino2==1:
                i['cant_ej_ad']+=1
                i['cant_ej_pr']-=1
                print("Ejemplares disponibles",i['cant_ej_ad'])
                print("Ejemplares prestados",i['cant_ej_pr'])
                print("gracias y vuelva pronto")

        elif i==libros:
            print("Este libro no existe")

def nuevo_libro():
    #completar
    return None