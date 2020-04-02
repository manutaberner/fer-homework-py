############IMPORTAMOS funciones que vamos a usar de otros ficheros################
#Aqui importamos las FUNCIONES
from funciones import  (readSeatMap, 
                        validacioFecha, 
                        errorInID, 
                        validacioSeient, 
                        addPassenger, 
                        printPassengerList, 
                        findPassenger, 
                        delPassengerAt, 
                        readPassengerList, 
                        WritePassengerList,
                        get_words)

#aqui importamos variables PREDEFINIDAS que usan las funciones
from funciones import errorInDateTbl, errorInIDTbl, errorInSeatTbl

#Aqui importamos las CLASES predefinidas y las funciones que hagan referencia a esa clase
from classFlight import Flight, addFlight, printFlightList, findFlight, delFlightAt, readFlightList,WriteFlightList


###################### PROGRAMA ##############################
print("START - Creació de llista de VOLS")
FlightsList = []  #Lista de vuelos
printFlightList(FlightsList)

#Creacion del nombre de vuelo
vol_name = input('Introduzca el CODIGO de vuelo:') 
loop = True
while loop:
    existe = findFlight(FlightsList, vol_name)
    if existe == True:
        print("Pasajero con ID =", vol_name, "ya está en la lista")
        #Quiero borrar el vuelo?
        borrado = input('Borrar el VUELO (s/-)?')
        if len(borrado) > 0 and (borrado[0].upper() == "S"):
            print(" Borrando registro... ")
            FlightsList = delFlightAt(FlightsList, vol_name)
            print(" Vuelo eliminado ")
            printFlightList(FlightsList)
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                loop = False
            else:
                vol_name = input('Introduzca el CODIGO de vuelo:')
        else:
            print(" Vuelo no eliminado ")
            printFlightList(FlightsList)
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                loop = False
            else:
                # present = True
                vol_name = input('Introduzca el CODIGO de vuelo:')
    else:
        vol = Flight(vol_name)
        vol.input()
        FlightsList = addFlight(FlightsList, vol)
        printFlightList(FlightsList)
        option = input("Continuar (-/n)? ")
        if len(option)>0 and (option[0]=='N' or option[0]=='n'):
            loop = False
        else:
            vol_name = input('Introduzca el CODIGO de vuelo:')


print("################## FIN ###############################")

#vol = Flight("FI103819") # Crea un objecte de la classe Flight
#vol.input() # Obté les dades per a l’objecte de l’entrada estàndard
