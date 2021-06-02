print("Programa de evaluacion de notas")
print("Introduzca nota")
nota_alumno=float(input())

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<7:
		valoracion="Reprobado"
	return valoracion

print(evaluacion(nota_alumno))