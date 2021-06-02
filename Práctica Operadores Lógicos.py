distancia=int(input("Introduzca la distancia al colegio: "))
print(distancia)

num_hermanos=int(input("Introduzca la cantidad de hermanos con los que habita: "))
print(num_hermanos)

salario_familiar=int(input("Introduzca el salario total de todos los miembros de su hogar: "))
print(salario_familiar)

if distancia>40 and num_hermanos>=2 and salario_familiar<20000:
	print("Conceder Beca")
else:
	print("No aplica para recivir Beca")