#Creacion CLASE Passenger
class Passenger:

    #Definicion de la clase
    def __init__(self, idno, seat):
        self.ID = idno
        self.seat = seat

    #FUNCION que recoge los datos de un pasajero
    def input(self):
        print("El pasajero tiene DNI/NIF ", self.ID)
        self.seat = input("Asiento correspondiente: ", self.seat)
        

    #METODO es una funcion parte del objeto este se usa para printear por pantalla
    def __str__(self):
        s = self.ID + " " + self.seat 
        return s

############FUNCIONES complementarias a la clase 
#FUNCION de anadir pasajero
def addPassenger(l, pssgr):
    l.append(pssgr)
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
def findPassenger(l,pssgr_name):
    for x in l:
        if x.ID == pssgr_name:
            return True

#FUNCION de borrar un pasjero de la lista
def delPassengerAt(l,pssgr):
    for x in l:
        if x.ID == pssgr:
            l.remove(x)
    return l

#FUNCION lectura LISTA de vuelos del fichero
def readPassengerList(pssgr):
    m = []
    try:
        f = open(pssgr, "rt")
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
def WritePassengerList (List, File):
    pos = 0
    f = open(File, "wt")
    while pos < len(List):
        f.write (List[pos])
        f.write('\n')
        pos = pos + 1
