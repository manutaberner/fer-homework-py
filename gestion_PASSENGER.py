############IMPORTAMOS funciones que vamos a usar de otros ficheros################
#Aqui importamos las FUNCIONES
from funciones import  (readSeatMap, 
                        validacioFecha, 
                        errorInID, 
                        validacioSeient, 
                        get_words)

#LECTURA DEL MAPA DE ASIENTOS
cabina = readSeatMap("FI103819_seatmap.txt")

#aqui importamos variables PREDEFINIDAS que usan las funciones
from funciones import errorInDateTbl, errorInIDTbl, errorInSeatTbl

#Aqui importamos las CLASES predefinidas y las funciones que hagan referencia a esa clase
from classPassenger import Passenger, addPassenger, printPassengerList, findPassenger, delPassengerAt, readPassengerList, WritePassengerList


###################### PROGRAMA ##############################
print("###################### PROGRAMA ##############################")
print("START - Creació de llista de PASAJEROS")
PassengerList = []  #Lista de pasajeros
printPassengerList(PassengerList)

#Creacion del nombre de vuelo
ID = input('Introduzca el DNI del pasajero:') 
present = True
while present:
    errorcod = errorInID(ID)
    printPassengerList(PassengerList)
    repetit = findPassenger(PassengerList,ID)
    if repetit == True:
        print("Pasajero con ID =", ID, "ya está en la lista")
        delete = input("Borrar el Pasajero (s/-)?")
        if len(delete) > 0 and (delete[0].upper() == "S"):
            PassengerList = delPassengerAt(PassengerList, ID)
            print(" Borrando registro... ")
            printPassengerList(PassengerList)
            print(" Pasajero eliminado ")
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introduzca el DNI del pasajero: ")
        else:
            print(" Pasajero no eliminado ")
            printPassengerList(PassengerList)
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introduzca el DNI del pasajero: ")
    else:
        #EN ESTE IF ES DONDE SE CREA EL OBJECTO PASSENGER, es decir, donde se introduce DNI+ASIENTO
        if errorcod == 0:
            PassengerList = addPassenger(PassengerList, ID)
            printPassengerList(PassengerList)
            print(errorInIDTbl[errorcod])
            asiento = input("Introduzca el ASIENTO del pasajero: ")
            errorAS = validacioSeient(cabina,asiento)
            if errorAS == 0:
                pasajero = Passenger(ID, asiento)
                pasajero.input()
                PassengerList = addPassenger(PassengerList, pasajero)
                printPassengerList(PassengerList)
                option = input("Continuar (-/n)? ")
                if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                    present = False
                else:
                    # present = True
                    ID = input("Introduzca el DNI del pasajero: ")
            else:
                print(errorInSeatTbl[errorcod])
                print("----------Volviendo al inicio del registro... ----------")
                ID = input("Introduzca el DNI del pasajero: ")
        else:
            print(errorInIDTbl[errorcod])
            printPassengerList(PassengerList)
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introduzca el DNI del pasajero: ")

print("################## FIN ###############################")
