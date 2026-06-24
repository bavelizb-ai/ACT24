

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