print ("ingresa tu nombre: ")
nombre= input ()
print ("hola, " + nombre)
print ("ingresa tu edad: ")
edad= int(input())
print ("Para comenzar oprime 1; para salir oprime 2: ")
comenzar="1"
salir="2" 
op= input ()
if op==salir:
    print ("Ha salido") 
else:
    print ("comencemos")

def preguntar():
    calif=0
    indice=0
    while indice<5:
        print(preguntas[indice])
        resp=input()
        if resp==respuestas[indice]:
            print("correcto")
            calif+=1
        indice=indice+1
    return calif

preguntas = [
    "1.¿Cuál es la suma de 10^2+108%10+754?",
    "2.¿Cuál es el numero entero mas cercano de la división 30/7?",
    "3.Calcula la resta de 7658-12^3",
    "4.Calcula la siguiente multiplicación: 15^2*5*2^2",
    "5.Calcular el resultado de 20%2+5%1-9/8*4"
    ]

respuestas = ["862","4","5930","4500","-4.5"]

calificacion=preguntar()
print(f"Tu calificacion fue {calificacion/5}")



