from funciones import * 
import os 

while True :
    try:
        os.system("pause")
        os.system("cls")

        print(f"""   
========== MENÚ DE GESTIÓN GREMIAL ==========
1. Registrar Personaje
2. Buscar Personaje por Nombre
3. Eliminar Personaje
4. Subir de Nivel a un Personaje
5. Calcular Estadísticas Generales
6. Mostrar Lista de Miembros
7. Salir del Sistema
=============================================""")
        opcion = int(input("Seleccione : "))
        match (opcion) :
            case 1:
                nombre = input("Ingrese nombre : ").title()
                clase = input("Ingrese clase : ").title()
                nivel = int(input("Ingrese Nivel : "))
                agregar(nombre,clase,nivel)

            case 2:
                nombre = input("Ingrese nombre : ").title()
                mostrar(nombre)

            case 3 :
                nombre = input("Ingrese el nombre : ").title()
                eliminar(nombre)
            case 4:
                nombre = input("Ingrese el nombre : ").title()
                lvlup(nombre)

            case 5:estadisticas()
            case 6:listar()
            case 7:break
            case _: print("No valido ")
    except Exception as e :
        print(f"ERROR {e}")