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

#CALIFICACIÓN 
def calificacion (respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):

  #primera pregunta 
  intentos = 0
  correcto= 0
 while (intentos < 2):
     print("1.¿Cuál es la suma de 10^2+108%10+754?")
     respuesta= int (862)
     respuesta1= int (input())
      if respuesta1 == respuesta:
          print ("Correcto")
          correcto = correcto + 1 
      else:
          print ("Incorrecto") 
          intentos = intentos + 1
   if intentos == 2 :
       print("Has ocupado todos tus intentos")

      print ("oprime enter para continuar: ")
      input ()
   
      #Suegunda pregunta
     print("2.¿Cuál es el numero entero mas cercano de la división 30/7?")
     respuesta02 = int (4)
     respuesta2= int (input())
      if respuesta2==respuesta02:
         print ("Correcto")
         correcto = correcto + 1 
      else:
         print("Incorrecto")
         intentos = intentos + 1
   if intentos == 2 :
       print("Has ocupado todos tus intentos")
    
       print ("oprime enter para continuar: ")
       input ()

       #Tercera pregunta 
     print("3.Calcula la resta de 7658-12^3")
     respuesta03= int (5930)
     respuesta3= int (input())
      if respuesta3== respuesta03:
         print ("Correcto")
         correcto = correcto + 1 
      else:
         print ("Incorrecto")
         intentos = intentos + 1
   if intentos = 2 :
       print ("Has ocupado todos tus intentos")

       print ("oprime enter para continuar: ")
       input ()

       #Cuarta pregunta 
     print ("4.Calcula la siguiente multiplicación: 15^2*5*2^2")
     respuesta04= int (4500)
     respuesta4= int (input())
      if respuesta4== respuesta04:
         print("Correcto")
         correcto = correcto + 1 
      else:
         print ("Incorrecto")
         intentos = intentos + 1
   if intentos == 2 :
       print ("Has ocupado todos tus intentos")

       print ("oprime enter para continuar: ")
       input ()

       #Quinta pregunta
     print ("Calcular el resultado de 20%2+5%1-9/8*4")
     respuesta05= float (-4.5)
     respuesta5= float (input())
      if respuesta5 == respuesta05:
         print("Correcto")
         correcto = correcto + 1 
      else:
         print("Incorecto")
         intentos = intentos + 1
   if intentos == 2 :
       print ("Has ocupado todos tus intentos")
    return aciertos

 resultado = calificacion (respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
 resultado = respuesta1 + respuesta2 + respuesta3 + respuesta4 + respuesta5
 return resultado 
print (f"Su total de aciertos son: {resultado}") 
if calificacion >0 and <2 :
    print ("Su puntaje IQ es de 120")
elif calificacion <=4 :
    print ("Su puntaje de IQ es de 140")
else:
    print ("Su puntaje de IQ es de 160")




