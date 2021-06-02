#print("Verificacion de acceso")

#edad_usuario=int(input("Introduce tu edad: "))

#if edad_usuario>=18:
#	print("Continue adelante")
#else:
#	print("No puedes pasar.")

print("Verificacion de acceso")

nota_estudiante=int(input("Introduce tu nota: "))

if nota_estudiante<5:
	print("Insuficiente")
elif nota_estudiante<6:
	print("Suficiente")
elif nota_estudiante<9:
	print("Bien!")
else:
	print("EXCELENTE!!")