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
    nuevo_libro = l.nuevo_libro()
    #completar  
    return None

def eliminar_ejemplar_libro():
    #completar
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