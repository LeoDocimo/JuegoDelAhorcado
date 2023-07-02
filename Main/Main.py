import random

dibujos_ahorcado = [
       """
          +---+
              |
              |
              |
              |
              |
       =========""",
       """
          +---+
          |   |
              |
              |
              |
              |
       =========""",
       """
          +---+
          |   |
          O   |
              |
              |
              |
       =========""",
       """
          +---+
          |   |
          O   |
          |   |
              |
              |
       =========""",
       """
          +---+
          |   |
          O   |
         /|   |
              |
              |
       =========""",
       """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
       =========""",
       """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
       =========""",
       """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
       ========="""
   ]
   
letras_adivinadas=[]
palabra_oculta = []

def mensaje_de_bienvenida():
    print("\nBienvenido al juego del ahorcado")
    print("--------------------------------")

#el sistema eligeuna palabra al azar   
def elegir_palabra():
    palabras_disponibles = ["azulejo","pileta","computadora","manaos","televisor","sasha"]
    return  random.choice(palabras_disponibles)

#genera la palabra con guiones
def generar_palabra_oculta(palabra):
    for i in range(len(palabra)):
        palabra_oculta.append("_") 

#remplaza los guiones por las letras adivinadas
def actualizar_palabra_oculta(palabra,letra):
     for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            
#Muestra la pelicula oculta como va actualmente
def mostrar_palabra_oculta(palabra_oculta):
    print("Palabra:", " ".join(palabra_oculta))

#muestra la figura a medida que el jugador se equivoca    
def mostrar_figura(intentos_fallidos):
    figura = dibujos_ahorcado[intentos_fallidos]
    print(figura)

#contabiliza los intentos acertados o fallidos del jugador
def intentos():
    print("Intentos acertados: ", intentos_acertados)
    print("intentos fallidos: ",intentos_fallidos)

#valida si la letra es correcta o no
def validar_letra(letra,palabra,):
    global intentos_fallidos
    global intentos_acertados 
    if len(letra) == 1:
        if letra in "abcdefghijklmnopqrstuvwxyz":
            if letra in palabra:
                if letra in letras_adivinadas:
                    print("Letra ya ingresada, intente con otra")
                    return
                
                else:
                    print("letra adivinada!")
                    intentos_acertados += 1
                    letras_adivinadas.append(letra)
                    mostrar_figura(intentos_fallidos)
                    actualizar_palabra_oculta(palabra,letra)
                    mostrar_palabra_oculta(palabra_oculta)
                    
            else:
                intentos_fallidos +=1
                print("Letra incorrecta")
                mostrar_figura(intentos_fallidos)
                mostrar_palabra_oculta(palabra_oculta)
        else:
            print("Caracter incorrecto, ingrese una letra")
    else:
        print("Ingrese 1 sola letra")

#Muestra el puntaje final del jugador
def puntaje(palabra):
        if intentos_fallidos == 0:
            print("Felicidades, no fallaste ninguna, obtuviste un puntaje perfecto: 100!")
        elif intentos_fallidos >= 1 and intentos_fallidos <= 5:   
            print(f"Puntaje: {100-(intentos_fallidos*10)}")
        elif intentos_fallidos == len(dibujos_ahorcado)-1:
             print("puntaje: " + str(len(letras_adivinadas)))
        input("Presione enter para continuar")     

#flujo principal del juego
def jugar():
     global intentos_fallidos 
     global intentos_acertados 
     intentos_fallidos = 0
     intentos_acertados = 0
     mensaje_de_bienvenida()
     palabra = elegir_palabra()
     palabra_oculta.clear()
     generar_palabra_oculta(palabra)
     mostrar_figura(intentos_fallidos)
     letras_adivinadas.clear()
     mostrar_palabra_oculta(palabra_oculta)
     while True:
         letra = input("Ingrese una letra: ").lower()
         validar_letra(letra,palabra)
         if intentos_fallidos == len(dibujos_ahorcado)-1:
             print("Que lastima, perdiste!")
             print("la palabra oculta era: "+ palabra)
             puntaje(palabra)
             break
         if all(letra in letras_adivinadas for letra in palabra):
             print("Felicidades ganaste, adivinaste la palabra")
             print("La palabra oculta era: "+palabra )
             puntaje(palabra)
             break        
         
#Menu del juego, el usuario elige si jugar o salir
def menu():
    while True:
        print("\n-----------------------------------------")
        print("Bienvenido al menu del juego del ahorcado")
        print("-----------------------------------------")
        print("Ingresa una de las siguientes opciones!")
        try:    
            opcion = int(input("Opcion 1: Jugar (ingrese 1) \nOpcion 2: Salir (ingrese 2)\n"))    
        
            if opcion == 1:
                    jugar()
            elif opcion == 2:
                    break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")



            
if __name__ == "__main__":
    menu()