### Setmana 6:
## Execució
# Falla per a NIE
# Hi ha problemes amb l’eliminació de passatgers, tant si es vol  eliminar-los com si no
## Programació
# Per què es comprova len(PassengerList)
# 65292343N
# 42972192G
# X7942365M
# Y9872602G
# 11622852D
# 71438118A> 0 en el recorregut de findPassenger()?
# Encara es pot millorar més la programació de findPassenger() no fent servir la variable x
# I a delPassengerAt() seguint l’esquema de recorregut, tot posant el pas al següent al final del bucle
# Reviseu la lògica del programa principal 

#fernando taberner 
def errorInID(num):
    LletraDeControl = "TRWAGMYFPDXBNJZSQVHLCKE"

    if len(num) == 9:

        if num[0:8].isdigit() and num[8].isalpha():
            lletrac = int(num[0:8]) % 23

            if LletraDeControl[lletrac] == (num[8].upper()):
                errcod = 0
            else:
                errcod = 1
        else:
            if nombre[1:8].isdigit() and nombre[8].isalpha() and nombre[0].upper() >= "X" and nombre[0].upper() <= "Z":
                num = ((ord(num[0].upper()) - 88)) * 10000000
                lletra = (num + int(nombre[1:8])) % 23

                if LletraDeControl[lletra] == (num[8].upper()):
                    errcod = 0
                else:
                    errcod = 1
            else:
                errcod = 2
    else:
        errcod = 3

    return errcod


errorInIDTbl = [
    "Identificación valida",
    "Identificación incorrecta (letra de control equivocada)",
    "Identificación incorrecta (formato erroneo)",
    "Identificación incorrecta (longitud erronea)",
]


def findPassenger(ID, PassengerList):
    i = 0
    encontrado = False
    while not (encontrado) and i < len(PassengerList) :
        if PassengerList[i] == ID.upper():
            encontrado = True
        else:
            i = i + 1
    if encontrado:
        x = i
    else:
        x = - 1
    return x


def addPassenger(l, idno):
    l = l + [idno.upper()]
    return l


def printPassengerList(l):
    print("LISTA PASAJEROS ")
    length = len(l)
    if length > 0:
        pos = 0
        while pos < length:
            print(" ", l[pos])
            pos = pos + 1
    else:
        print(" LISTA VACIA ")


def delPassengerAt(repetit, PassengerList):
    PassengerList.pop(repetit)
    return print(" Borrando pasjero... ")


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



def WritePassengerList (List, File):
    pos = 0
    f = open(File, "wt")
    while pos < len(List):
        f.write (List[pos])
        f.write('\n')
        pos = pos + 1


print("Manipulación de la lista de pasatjeros")
PassengerList = readPassengerList("FI103819.txt")
printPassengerList(PassengerList)
WritePassengerList(PassengerList, "FI103819_backup.txt")
present = True
ID = input(" Introduce DNI/NIE sin espacios ni guiones: ")
while present:
    errcod = errorInID(ID)
    repetit = findPassenger(ID, PassengerList)
    if repetit != -1:
        print("Pasajero con ID =", ID, "ya está en la lista")
        delete = input("Borrar el DNI/NIE (s/-)?")
        if len(delete) > 0 and (delete[0].upper() == "S"):
            PassengerList = delPassengerAt(repetit, PassengerList)
            print(" Pasajero eliminado ")
        else:
            print(" Pasajero no eliminado ")
            
    else:
        if errcod == 0 and repetit == -1:
            PassengerList = addPassenger(PassengerList, ID)
        else:
            print(errorInIDTbl[errcod])
        printPassengerList(PassengerList)
        option = input("Continuar (s/-)? ")
        if len(option) > 0 and (option[0].upper() == 'N'):
            present = False
        else:
            ID = input("Introduce DNI o NIE sin espacios ni guiones: ")
WritePassengerList (PassengerList, "FI103819.txt")
print("Fin del programa.")