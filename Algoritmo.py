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
    calif = 0
    for conjunto in lista :
        print(conjunto[0])
        resp=float(input())
        if resp == conjunto[1]:
            calif += 1 
    return calif

lista = [
    ['1.¿Cuál es la suma de 10^2+108%10+754?',862],
    ["2.¿Cuál es el numero entero mas cercano de la división 30/7?", 4],
    ["3.Calcula la resta de 7658-12^3",5930,20],
    ["4.Calcula la siguiente multiplicación: 15^2*5*2^2",4500],
    ["5.Calcular el resultado de 20%2+5%1-9/8*4",-4.5]
]

calificacion=preguntar()
print(f"Tu calificacion fue {calificacion/5}")

   



