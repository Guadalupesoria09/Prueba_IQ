print ("ingresa tu nombre: ")
nombre= input ()
print ("hola, " + nombre)
print ("ingresa tu edad: ")
edad= int(input())
print ("Para comenzar oprime 1")
comenzar="1"
op= input ()
if op==comenzar:
    print ("comencemos") 
else:
    print ("ocurrio un error :( ")

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
    ["3.Calcula la resta de 7658-12^3",5930,],
    ["4.Calcula la siguiente multiplicación: 15^2*5*2^2",4500],
    ["5.Calcular el resultado de 20%2+5%1-9/8*4",-4.5],
    ["6.Un bate y una pelota cuestas en total $1.10. El bate cuesta $1 más que la pelota. ¿Cuánto cuesta la pelota?",0.05],
    ["7.Si le lleva cinco minutos a cinco máquinas fabricar cinco herramientas." 
    "¿Cuánto le llevaría a 100 máquinas fábricar 100 herramientas?",5],
    ["8.En un lago hay un conjunto de lirios de agua. Cada día, el tamaño se duplica."
    "Si lleva 48 días para que los lirios tapen el lago. ¿ Cuáto tardaría en cubrir la mitad del lago?",47]

]



def puntaje ():
    if calificacion > 0 and calificacion == 8 :
        iq = 100
        print("Estas en el rango promedio. Tu IQ corresponde a 100")
    elif calificacion > 8 and calificacion <= 9:
            iq = 120
            print("Estas arriba del promedio. Tu IQ corresponde a 120")
    else :
            iq = 140
            print("Felicidades, eres una persona dotata. Tu IQ corresponde a 140")
    return puntaje

calificacion=preguntar()
print(f"Tu calificacion fue {calificacion*10/8}")
iq = puntaje ()


