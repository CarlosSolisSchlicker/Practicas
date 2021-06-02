salario_presidente=int(input("Introduzca el salario del presidente "))
print("Salario del presidente: "+str(salario_presidente))

salario_director=int(input("Introduzca el salario del director "))
print("Salario del director: "+str(salario_director))

salario_jefe_area=int(input("Introduzca el salario del jefe de area "))
print("Salario del jefe de area: "+str(salario_jefe_area))

salario_administrativo=int(input("Introduzca el salario del administrativo "))
print("Salario del administrativo: "+str(salario_administrativo))

if salario_presidente>salario_director>salario_jefe_area>salario_administrativo:
	print("Todo en orden capitalista.")
else:
	print("Revisar error")