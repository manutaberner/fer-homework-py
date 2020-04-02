
#Este ejemplo es importando datetime que lo valida por nosotros FACIL!

"""import datetime

inputDate = input("Introduzca la fecha de la siguiente manera 'dd/mm/yy' : ")

dia,mes,ano = inputDate.split('/')#separa el dia el mes y la fecha

esFechaValida = True
try :
    datetime.datetime(int(ano),int(mes),int(dia))
except ValueError :
    esFechaValida = False

if(esFechaValida) :
    print ("La fecha es valida")
else :
    print ("La fecha NO es valida")
"""
##############################################################################
#ESTE TE GESTIONA LOS ERRORES y puede poner el rango
def fechaValida(fecha):
    from datetime import datetime, date 

    date_input = fecha
    try:
        #convierte la fecha intrducida a formate date
        valid_date = datetime.strptime(date_input, '%d/%m/%Y').date()
        #aqui decides el rango de fechas en el que queires comprobar
        if not (date(2000, 1, 1) <= valid_date <= date(2100, 12, 31)): 
            errcod = 1          
        else:
            errcod = 0      
    except ValueError:
        errcod = 2
    return errcod

      

##################################################################################
#Programa que valida los DNI  o NIF extranjeros
def validoDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
            and tabla[int(dni)%23] == dig_control
    return False