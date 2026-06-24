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

            case 2:pass
            case 3:pass
            case 4:pass
            case 5:pass
            case 6:pass
            case 7:pass
            case _: print("No valido ")
    except Exception as e :
        print(f"ERROR {e}")