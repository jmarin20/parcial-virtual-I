cliente = {
    '1':['Nombre','Direccion','Telefono']
}
estado = {
    '1':'Terminado'
}
departamento = {
    '1':'Izabal'
}
municipio = {
    '1':'Puerto Barrios'
}
proyectos = {
    #id = idClient, idEstado, idDepartamento idMunicipio
    '1':['1','1','1']
}

def insertarEstado():
    id = input("Ingrese el id del Estado")
    if id in estado:
       print("El estado ya existe")
    else:
        nombre = input("Ingrese el nombre del estado")
        estado[id]=nombre
def insertarDepartamento():
    id = input("Ingrese el id del Departamento")
    if id in estado:
       print("El departamento ya existe")
    else:
        nombre = input("Ingrese el nombre del departamento")
        departamento[id]=nombre

def mostrarEstado():#si pero a mi no se me escucha
    for k in estado:
        print(k.ljust(30, " "), end="")
        print("Estado:" + estado[k].ljust(20, " "), end="")
        print("")

def mostrarDepartamento():
    for k in departamento:
        print(k.ljust(30, " "), end="")
        print("Estado:" + departamento[k].ljust(20, " "), end="")
        print("")


def insertarCliente():
    id = input("Ingrese el id del cliente")
    if id in cliente:
        print("El cliente ya Existe")
    else:
        nombre = input("Ingrese el nombre")
        direccion = input("Ingrese la direccion")
        telefono = input("Ingrese el telefono")

        cliente[id] = [nombre,direccion,telefono]

def mostrarClientes():

    for k,v in cliente.items():
        print(k)
        print("Nombre:"+v[0].ljust(20," "),end="")
        print("Direcion:"+v[1].ljust(20," "), end="")
        print("Telefono:"+v[2].ljust(20," "),end="")
        print("")


def insertarProyectos():
    id = input("Ingrese el id del proyecto")
    if id in proyectos:
        print("El proyecto ya existe")
    else:
        idCliente = input("Ingrese el id del cliente")
        idEstado = input("Ingrese el id del estado")
        idDepartamento = input("Ingrese el id del Departamento")
        proyectos[id]=[idCliente,idEstado,idDepartamento]

def mostrarRegistros():

    for k,v in proyectos.items():
        print(k)
        print("Nombre:"+cliente[v[0]][0].ljust(20," ") ,end="")
        print("Estado proyecto:"+estado[v[1]].ljust(20," "), end="")
        print("Departamento:"+departamento[v[2]].ljust(20," "),end="")
        print("")
def menu():

    while True:
        print("===================================================")
        print("\t\t\t\t\t0  - Selecciona una opción")
        print("\t\t\t\t\t1 - Insertar Clientes")
        print("\t\t\t\t\t2 - Mostrar Clientes")
        print("\t\t\t\t\t3 - Insertar Estados")
        print("\t\t\t\t\t4 - Mostrar Estados")
        print("\t\t\t\t\t5 - Insertar Departamento")
        print("\t\t\t\t\t6 - Mostrar Departamento")
        print("\t\t\t\t\t7 - Insertar Proyectos")
        print("\t\t\t\t\t8 - Mostrar Proyectos")
        print("\t\t\t\t\t9 - Insertar Municipio")
        print("\t\t\t\t\t10 - Mostrar Municipio")
        print("\t\t\t\t\t11 - Salir")
        print("=====================================================")

        optionMenu = input("Inserte la opcion>>  ")
        if optionMenu == "1":
            opcion = "1"
            print("==================================================")
            insertarCliente()

        elif optionMenu == "2":
            print("==================================================")
            mostrarClientes()
            input("Pulsa una tecla para continuar")
            print("==================================================")

        elif optionMenu == "3":
            print("==================================================")
            insertarEstado()
        elif optionMenu == "4":
            print("==================================================")
            mostrarEstado()
        elif optionMenu == "5":
            print("==================================================")
            insertarDepartamento()
        elif optionMenu == "6":
            print("==================================================")
            mostrarDepartamento()
        elif optionMenu == "7":
            print("==================================================")
            insertarProyectos()

        elif optionMenu == "8":
            print("==================================================")
            mostrarRegistros()

        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

menu()