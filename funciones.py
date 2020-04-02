############IMPORTAMOS funciones que vamos a usar de otros ficheros################
from sesion1 import fechaValida, validoDNI
from sesion2 import asientoValido

###########Se crea el mapa de asientos del avion####################################################
# R = Vacio  T = Economy  E = Economy Plus  T = Bussiness

#FUNCION que lee el mapa del fichero
def readSeatMap(filename):
    m = ""
    try:
        f = open(filename,"rt")
    except FileNotFoundError:
        f = None
        if f!=None:
            r = f.read(1)
            while r!="":
                if not r.isspace():
                    m = m + r
                r = f.read(1)
            f.close()
    return m

#Leyendo el fichero y creando el mapa llamando a la funcion
SeatMap = readSeatMap("FI103819_seatmap.txt")


############### FECHA ################################################################################
#Inicializacion de tabala de errores
errorInDateTbl = [
    ' La fecha es valida\n', #...................... errcod==0
    ' Por favor, introduzca una fecha dentro del rango 01/01/2000 - 31/12/2100\n', # errcod==1
    ' Introduzca la fecha correctamente con fromato dd/mm/yyyy (eg. 20/10/2012)\n', #................ errcod==2
]

#print("Comprovació de fecha")
#fecha_input = input('Introduzca la fecha de la siguiente manera (dd/mm/yyyy):')
def validacioFecha(fecha):
    fecha_control = False #varaible para controlar el loop while

    while fecha_control == False:
        errcod = fechaValida(fecha) #devuelve el codigo de error

        if errcod != 0:
            print(errorInDateTbl[errcod])
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                fecha_control = True
            else:
                fecha_control = False
                fecha = input('Introduzca la fecha de la siguiente manera (dd/mm/yyyy):')
        else:
            print(errorInDateTbl[errcod])
            fecha_control = True



############### Validacion DNI ##########################################################################
errorInIDTbl = [
    ' DNI valido\n', #................... errcod==0
    ' Longitud incorrecta del DNI\n', #.. errcod==1
    ' DNI no valido\n', #.... errcod==2
]

def errorInID(idno): #FUNCION A UTILIZAR
    dni_control = False     #varaible para controlar el loop while
    while dni_control == False:
        if len(idno) == 9:
            
            if validoDNI(idno) == False: #Se usa la funcion validar dni
                errcod = 2
                dni_control = True
            else: 
                errcod = 0
                dni_control = True
        else:
            errcod = 1
            dni_control = True

    return errcod          

################Validacion de asientos##################################################################
#Inicializacion de tabla de errores
errorInSeatTbl = [
    " Codi vàlid.", #................... errcod==0
    " Lletra de seient incorrecte.", #.. errcod==1
    " Número de fila inexistent.", #.... errcod==2
    " Format incorrecte." #............. errcod==3
]

#print("Comprovació de seients")
#seat = input("Codi de seient = ? ")
def validacioSeient(SeatMap,seat): #FUNCION A UTILIZAR
    if len(SeatMap) > 1:
        present = True
        # Recorregut
        while present:
            # Processament
            errcod = asientoValido(SeatMap, seat)
            # Sortida de dades
            print(errorInSeatTbl[errcod])
            # Entrada de dades
            option = input("Continuar (-/n)? ")
            if len(option)>0 and (option[0]=='N' or option[0]=='n'):
                present = False
            else:
                # present = True
                seat = input("Codi de seient = ")
    else:
        print("No s'ha trobat el mapa de seients")    


############################### FUNCIONES LISTA DE PASAJEROS#####################################

#FUNCION de anadir pasajeros
def addPassenger(l, idno):
    l = l + [idno.upper()]
    return l
    
#FUNCION de printear lal lista en pantalla
def printPassengerList(l):
    print(" Leyendo lista...")
    print("LISTA DE PASAJEROS:")
    length = len(l)
    if length > 0:
        i = 0
        while i < length:
            print(" ", l[i])
            i = i + 1
    else:
        print("Lista vacia")

#FUNCION de comprobar si existe en la lista un pasjero
def findPassenger(l,idno):
    if idno in l:
        return True

#FUNCION de borrar un pasjero de la lista
def delPassengerAt(l,idno):
    l.remove(idno)
    return l

#FUNCION lectura LISTA de pasajeros del fichero
def readPassengerList(passengers):
    m = []
    try:
        f = open(passengers, "rt")
    except FileNotFoundError:
        f = None
    if f != None:
        r = f.read(9)
        while r != "":
            if not r.isspace():
                m = m + [r]
            r = f.read(1)
            r = f.read(9)
        f.close()
    return m

#FUNCION que escribe el pasajero en la lista
def WritePassengerList (List, File):
    pos = 0
    f = open(File, "wt")
    while pos < len(List):
        f.write (List[pos])
        f.write('\n')
        pos = pos + 1

#FUNCION 
def get_words(s):                   # Retorna les paraules que hi ha a la cadena s
    wl = []                         # Llista de paraules que hi ha
    i = 0                           # Posició inicial de la paraula
    l = len(s)                      # Longitud de la cadena s
    while i < l:                    # Recorregut d's per extraure'n les paraules
        f = False                   # Cerca del primer caràcter de la paraula
        while not f and i < l:
            if not s[i].isspace():
                f = True
            else:
                i = i + 1
            j = i + 1                   # Cerca de l'últim caràcter de la paraula
            f = False
            while not f and j < l:
                if s[j].isspace():
                    f = True
                else:
                    j = j + 1
            if i < l:                   # Si hi ha inici vàlid,
                wl = wl + [s[i:j]]      # afegeix la paraula a la llista
            i = j + 1                   # Pas a la posició de la nova paraula
    return wl