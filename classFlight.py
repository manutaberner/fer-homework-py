############IMPORTAMOS funciones que vamos a usar de otros ficheros################
#Aqui importamos las FUNCIONES
from funciones import get_words

#Creacion de la CLASE Flight
class Flight:

    #Definicion de la clase
    def __init__(self, name): 
        self.ID = name
        self.origin = ""
        self.departure = ""
        self.destination = ""
        self.arrival = ""
        self.start = ""
        self.rep = 0
        self.seatmap = ""

    #FUNCION que recoge los datos de un vuelo
    def input(self):
        print("Introdueix informació del vol", self.ID)
        self.origin = input("Aeroport d'origen = ")
        self.departure = input("Hora de sortida [hh:mm] = ")
        self.destination = input("Aeroport de destinació = ")
        self.arrival = input("Hora d'arribada [hh:mm] = ")
        self.start = input("Data del primer vol [dd/mm/aaaa] = ")
        self.rep = int(input("Repetició (nombre de dies) = "))
        self.seatmap = input("Nom del fitxer amb el mapa de seients = ")

    #METODO es una funcion parte del objeto este se usa para printear por pantalla
    def __str__(self):
        s = self.ID + ": " + self.origin + " " + self.departure + " -> "
        s = s + self.destination + " " + self.arrival
        s = s + " (" + self.start + " +" + str(self.rep) + ") "
        s = s + self.seatmap
        return s

    #FUNCION 
    def str_input(self, s):
        wl = get_words(s)
        if len(wl)==9:
            l = len(wl[0])
            if l > 1:
                self.ID = wl[0][0:l-1]
                self.origin = wl[1]
                self.departure = wl[2]
                self.destination = wl[4]
                self.arrival = wl[5]
                l = len(wl[7])
                if len(wl[6])>1 and l>2:
                    self.start = wl[6][1:]
                    self.rep = int(wl[7][1:l-1])
                    self.seatmap = wl[8]
                    e = True
                else:
                    e = False
            else:
                e = False
        else:
            e = False
        return e


############FUNCIONES complementarias a la clase 
#FUNCION de anadir vuelo
def addFlight(l, flight):
    l.append(flight)
    return l
#FUNCION de printear lal lista en pantalla
def printFlightList(l):
    print(" Leyendo lista...")
    print("LISTA DE VUELOS:")
    length = len(l)
    if length > 0:
        i = 0
        while i < length:
            print(" ", l[i])
            i = i + 1
    else:
        print("Lista vacia")

#FUNCION de comprobar si existe en la lista un pasjero
def findFlight(l,flightname):
    for x in l:
        if x.ID == flightname:
            return True

#FUNCION de borrar un pasjero de la lista
def delFlightAt(l,flight):
    for x in l:
        if x.ID == flight:
            l.remove(x)
    return l

#FUNCION lectura LISTA de vuelos del fichero
def readFlightList(flights):
    m = []
    try:
        f = open(flights, "rt")
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

#FUNCION que escribe el vuelos en la lista
def WriteFlightList (List, File):
    pos = 0
    f = open(File, "wt")
    while pos < len(List):
        f.write (List[pos])
        f.write('\n')
        pos = pos + 1
