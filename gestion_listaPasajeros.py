############IMPORTAMOS funciones que vamos a usar de otros ficheros################
#Aqui importamos las funciones
from funciones import  (readSeatMap, 
                        validacioFecha, 
                        errorInID, 
                        validacioSeient, 
                        addPassenger, 
                        printPassengerList, 
                        findPassenger, 
                        delPassengerAt, 
                        readPassengerList, 
                        WritePassengerList)

#aqui importamos variables que usan las funciones
from funciones import errorInDateTbl, errorInIDTbl, errorInSeatTbl

########################### PROGRAMA #######################################################
print("START - Creació de llista de passatgers")
PassengerList = readPassengerList("FI103819.txt")
printPassengerList(PassengerList)
WritePassengerList(PassengerList, "FI103819_backup.txt")
present = True
ID = input("Introdueix DNI o NIE sense espais ni guionets: ")
while present:
    errorcod = errorInID(ID)
    repetit = findPassenger(PassengerList,ID)
    if repetit == True:
        print("Pasajero con ID =", ID, "ya está en la lista")
        delete = input("Borrar el DNI/NIE (s/-)?")
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
                ID = input("Introdueix DNI o NIE sense espais ni guionets: ")
        else:
            print(" Pasajero no eliminado ")
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introdueix DNI o NIE sense espais ni guionets: ")
    else:
        if errorcod == 0:
            PassengerList = addPassenger(PassengerList, ID)
            printPassengerList(PassengerList)
            print(errorInIDTbl[errorcod])
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introdueix DNI o NIE sense espais ni guionets: ")
        else:
            print(errorInIDTbl[errorcod])
            printPassengerList(PassengerList)
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                ID = input("Introdueix DNI o NIE sense espais ni guionets: ")


WritePassengerList(PassengerList, "FI103819.txt")
print("Fin del programa.")