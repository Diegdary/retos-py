import math
semana ={"lunes": 2.00, "martes": 2.00, "miercoles": 2.00, "jueves": 2.50, "viernes": 2.50, "sabado": 3.00, "domingo": 3.00}
dia= input("ingrese el dia en el que se estaciono ").lower()
tiempo=int(input("ingrese cuanto tiempo estuvo estacionado (en minutos) ")) 
horas= math.floor(tiempo/60) 
minutos=tiempo-horas*60
horas= horas+1 if minutos>=5 else horas
precio=horas*semana[dia]

print(f"para el dia {dia} con uso de {horas} horas con {minutos} minutos su precio es de: {precio}")