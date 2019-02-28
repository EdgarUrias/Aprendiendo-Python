#variable numero de personas
types_of_people = 10
#variable de un string con una variable dentro
x = f"there are {types_of_people} types of people"

#variable con la palabra binario
binary = "binary"
#variable con una palabra
do_not = "don't"
#variable con 2 variables de string dentro
y = f"Those who know {binary} and those who {do_not}."

#imprime variable x
print(x)
#imprime variable y
print(y)

#imprime string con la variable x
print(f"i said: {x}")
#imprime string con la variable y
print(f"i also said: {y}")

#variable boleana False
hilarious = False
#variable string con la variable boleana imprime False
joke_evaluation = "Isn't that joke so funny?! {}"

#imprime la variable joke.. y la formatea para agregarle el boleano
print(joke_evaluation.format(hilarious))

#declara la variable w string
w = "This is the left side of..."
#declara la variable e string
e = "a string with a right side."

#concatena la variable w y e y las imprime
print(w + e)


