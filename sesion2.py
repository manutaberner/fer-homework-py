##########Funcion de validar asientos###################################
def asientoValido(SeatMap,seat):
    #Asientos por fila, en este caso es el primer caracter de la STRING
    seatsperrow = int(SeatMap[0]) #Seleccionamos el primer caracter y lo convertimos a String


    #Numero de filas que hay = (longitud STRING - 1)/ seatsperrow
    rows = (len(SeatMap) - 1 ) // seatsperrow #la doble barra hace la division redondeando al numero mas pequeno

    #Validacion del codigo y extraccion del asiento o errores posibles

    if 1<len(seat) and len(seat)<4:         #Comprueba que la longitud del codigo es correcta
        if len(seat) == 2:                  #Rellena los codigos con numeros menores de diez
                seat = '0' + seat       
        if seat[0:2].isdigit():             #Comprueba que los dos primeros caracteres son numeros
            row = int(seat[0:2])
        else:
            row = 0
        if 0 < row and row <= rows:         #Comprueba que el numero de fila existe
            letra = seat[2].upper()         #La letra la cambia a mayuscula por si acaso
            nseat = ord(letra) - ord('A')   #Comprueba que es menor que 4(Maximo de asientos por fila)
            if 0 <= nseat and nseat < seatsperrow: #Comprueba que la l
                errcod = 0
            else:
                errcod = 1
        else:
            errcod = 2
    else:
            errcod = 3

    return errcod



