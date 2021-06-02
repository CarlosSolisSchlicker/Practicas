class CLASE1():
	def METODO1(self):
		print("A")

class CLASEn():
	def METODO1(self):
		print("B")

def METODO2(VAR1):
	VAR1.METODO1()

OBJETO1=CLASEn()

METODO2(OBJETO1)