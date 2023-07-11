import os
import datetime

departamento1 = []
for floor in range(1, 11):
    matrix = []
    for type in ["A", "B", "C", "D"]:
        matrix.append(1 if (floor, type) in departamento1 else 0)
    departamento1.append(matrix)

precio = {"A": 3800, "B": 3000, "C": 2800, "D": 3500}

compradores = []

def validate_menu_option(op):
    if op< 1 or op > 5:
        print("opcion invalida")
        return False
    return True

def compra_departamento():
    floor = int(input("elija el piso: "))
    type = input("ingrese su tipo de departamento : ")

    if departamento1[floor - 1][type] == 0:
        print("el departamento elejido no es valido")
        return

    departamento1[floor - 1][type] = 0
    compradores.append((floor, type))

    print("Felicidades el departamento es suyo")

def departamentos_disponibles():
    print("los departamentos disponibles son estos:")
    for floor in range(1, 11):
        for type in ["A", "B", "C", "D"]:
            if departamento1[floor - 1][type] == 1:
                print(f"{floor}-{type}")

def lista_de_compradores():
    print("The list of buyers is:")
    for buyer in compradores:
        print(f"RUN: {compradores[2]}, Floor: {compradores[0]}, Type: {compradores[1]}")

def show_total_sales():
    compradores_totales = 0
    for apartment in compradores:
        compradores_totales += precio[apartment[1]]

    print(f"El precio total es de : {compradores_totales}")

def exit_system():
    print(f"System exit by {__author__} on {datetime.datetime.today()}")
    exit()




