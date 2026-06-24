

personajes = []

def buscar(nombre):
    for i in range (len(personajes)):
        if personajes [i]["nombre"]==nombre:
            return i # retornamos la posicion en la que esta 
    return -1 # si el personaje no se encuentra retorna -1





def agregar (nombre,clase,nivel):
    if len(nombre.strip())==0 or len(nombre.strip()) > 20:
        print("nombre no valido ")
        return
    elif buscar(nombre) >=0:
        print("Nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago", "Picaro"):
        return
    




    rango = "recluta"
    if nivel >= 30 :rango="Elite"

    pj = {"nombre": nombre, "clase":clase, "nivel":nivel , "rango" : rango}
    personajes.append(pj)
    print("Personaje registrado")


def mostrar(nombre):
    posicion = buscar(nombre)
    if posicion >=0:
        print(f"Persona encontrada : {personajes[posicion]}")
    else:
        print("Nombre no existe")

        
def listar():
    
    if len(personajes)>0:
        print(f"{"N°": <3}.-{"nombre":<15} {"Clase":<10} {"nivel" :<4} {"rango":<10}")
        for i in range (len(personajes)):
            print(f"{i+1:<3}.-{personajes[i]["nombre"]:<15} {personajes[i]["clase"]:<10} {personajes[i]["nivel"]:<4} {personajes[i]["rango"]:<10}")

    else:
        print("No hay personajes registrados")


def eliminar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        personajes.pop(posicion)
        print("personaje eliminado ")
    else:
        print("Personaje no existe")


def lvlup(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
       nivel =  personajes[posicion]["nivel"]
       if nivel <50:
            personajes[posicion]["nivel"] = nivel+1
            print("Nivel aumentado")
            if nivel >= 30:
                personajes[posicion]["rango"] = "Elite"
       else:
           print("Ya a alcanzado el nivel maximo ")

        
    else:
        print("Personaje no existe")
