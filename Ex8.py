#se generan llaves de formato en un lista
formatter = "{} {} {} {}"

#se llama a la variable formatter y se concatenan valores con la funcion format
#aqui se concatenana enteros
print(formatter.format(1,2,3,4))
#aqui se concatenan strings
print(formatter.format("one", "two", "three", "four"))
#aqui se cocatenan boleanos
print(formatter.format(True, False, False, True))
#aqui al anidar la variable simplemente imprimie la variable como string al no tener ningun valor definido
print(formatter.format(formatter, formatter, formatter, formatter))
#aqui se concatenan strings, los saltos de linea no hacen nada, el codigo simplemente sigue
print(formatter.format(
        "Try Your",
        "Own text here",
        "maybe a poem",
        "Or a song about fear"
        ))
