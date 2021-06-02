valido=False

email=input("Introduzca su Email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido==True:
	print("Email correcto.")
else:
	print("Email incorrecto.")

for x in range(1,5):
	print(x)