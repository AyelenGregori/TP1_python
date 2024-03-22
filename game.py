import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
#Lista con las vocales
vocales= ['a','e','i','o','u']
# Número máximo de intentos permitidos
max_attempts = 10
#numero de fallos
num_fallos = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print(f"¡Bienvenido al juego de adivinanzas!")
#Elegir el nivel de dificultad
word_displayed = ''
while True:
    dificultad= input("Elige un nivel de dificultad: ")
    if (dificultad == 'facil'):
        for letter in secret_word:
            if letter in vocales:
                word_displayed += letter
            else:
                word_displayed +='_'
        break
    elif (dificultad == 'media'):
        contador = 0
        for letter in secret_word:
            #if el contador es 0 es porque la letra esta al principio y si da 5 es porque esta al final
            if contador == 0 or contador == (len(secret_word)-1):
                word_displayed += letter #entonces word_displayer va hacer la vocal
            else:
                word_displayed += '_'
            contador +=1
    elif (dificultad == 'dificil'):
        word_displayed += '_' * len(secret_word) #va a tener tantos guiones como palabras tenga secret word
        break
    else:
        print('ingresaste un nivel de dificultad invalido')
# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while num_fallos < max_attempts:
    letter= input("Ingrese una letra: ").lower()
    while letter == '':
        print("Lo siento, no ingresaste niguna letra. Intenta de nuevo")
        letter = input('Ingrese una letra: ').lower()
    if (letter in secret_word): #si la letra que lei esta dentro de la palabra secreta
        #Agregar la letra a las palabras adivinadas
        guessed_letters.append(letter)
        print("Bien Hecho!! La letra esta en la palabra")
    else:
        print("Lo siento , la letra no esta en la palabra")
        num_fallos += 1
    letters = []
    if (dificultad == 'facil'):
        for letter in secret_word:
            if letter in guessed_letters or letter == vocales:
                letters.append(letter)
            else:
                letters.append('_')
    elif dificultad =='dificil':
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append('_')
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
print("El numero de fallos fue",num_fallos)
print(f"¡Oh no! Has agotado tus 10 intentos.")
print(f"La palabra secreta era: ",secret_word)