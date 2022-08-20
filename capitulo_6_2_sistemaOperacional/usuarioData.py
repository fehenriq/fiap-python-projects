import getpass
from datetime import datetime

print("Usuario.......: ", getpass.getuser())
print("Data Completa.: ", datetime.now())
print("Dia...........: ", datetime.now().day)
print("Mes...........: ", datetime.now().month)
print("Ano...........: ", datetime.now().year)
print("Hora..........: ", datetime.now().hour)
print("Minuto........: ", datetime.now().minute)
print("Segundo.......: ", datetime.now().second)
