def validarVacios(dato):
	if(dato == ""):
		return True
	else:
		return False
def validarSoloNumeros(dato):
	print(dato)
	dato = str(dato)
	for caracter in dato:
		if(not(caracter.isdigit())):
			if(ord(caracter)!=46):
				return True
		else:
			return False
