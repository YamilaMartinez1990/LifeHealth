#from Libraries.validaciones import *
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import os
import time
from PIL import Image, ImageTk
import sqlite3
from tqdm.auto import tqdm 
from datetime import datetime
import datetime
from tkcalendar import Calendar
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os.path

conexion = sqlite3.connect("Bd/LifeHealth.db")
nombrePrograma = "Life Health"

def misEstilos():
	global estilos
	color_navegacion="black"
	color_navegacion2= 'SkyBlue4'
	estilos = ttk.Style()
	estilos.theme_use("alt")
	estilos.configure("programa.TLabel",
					  background="black",

					  foreground="ivory3",
					  font=('Georgia',50,"italic","bold")
					 )
	estilos.configure("tituloLogin.TLabel",
					  background= 'black',
					  foreground='plum4',
					  font=("Georgia",30,"italic","bold")
					 )
	estilos.configure("subTitulo.TLabel",
					  background= 'black',
					  foreground='snow',
					  font=('Georgia',15,"bold")
					 )
	estilos.configure("labelNavegacion.TLabel",
					  background= 'ivory3',
					  foreground='black',
					  font=('Georgia',15,"bold"))
	estilos.configure("entradasNavegacion.TLabel",
					  background= 'snow',
					  foreground='black',
					  font=('Georgia',20,"bold"))
	
	estilos.configure("frameSecundarios.TFrame",
					  background= 'black',
					  relief=FLAT,border=0)
	estilos.configure("frameTerciarios.TFrame",
					  background= 'SkyBlue4',
					  relief=FLAT,border=0)

	estilos.configure("entradasLogin.TLabel",
					  background='snow',
					  foreground='black',
					  font=('Calibri',20)
					 )
	estilos.configure("entradasNavegacion2.TLabel",
					  background='ivory3',
					  foreground='black',
					  font=('Calibri',25)
					  )
	estilos.configure('login.TFrame',background='black',relief=FLAT,border=0)
	estilos.configure('loginCentrado.TFrame',background='SkyBlue4',relief=FLAT,border=0)

	estilos.configure('fondo.TFrame',background='Black',relief=FLAT,border=0)
	estilos.configure('principal.TFrame',background='snow',relief=FLAT,border=0)
	estilos.configure('navegacion.TFrame',background="SkyBlue4",relief=FLAT,border=0)
	estilos.configure('botonLabel.TLabel',foreground='snow',
					  font=('Calibri',24),
					  background=color_navegacion,
					  relief=FLAT,border=0)
	estilos.configure('botonNavegacion.TButton',
   					  background="ivory3",
   					  foreground='black',
   					  font=('Georgia',12,"bold"),
   					  relief=FLAT,
   					  bd=0,
					 )
	estilos.map('botonNavegacion.TButton',
		       background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	estilos.configure('botonLogin.TButton',
					  background="ivory3",
   					  foreground='black',
   					  font=('Georgia',20),
   					  relief=FLAT,
   					  bd=0,
					 )
	estilos.map('botonLogin.TButton',
		       background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	return estilos

def validate_entry_numeros(content):
	return content.isdigit()

def validate_entry_letras_espacios(content):
	return content.isalpha() or str(content.isspace())

def validate_entry_decimal(content):
	return content.isdecimal()

def login_principal():

	db_nombre = "Bd/LifeHealth.db"

	global imagenLogoPrincipal

	ventana_principal.geometry("900x900")
	ventana_principal.title("LifeHealt")
	icono = PhotoImage(file ="icon.png")
	ventana_principal.iconphoto(True,icono)

	frame_login = ttk.Frame(ventana_principal,style='login.TFrame')
	frame_login.pack(fill=BOTH,expand=1)

	frame_login_centrado =ttk.Frame(frame_login,style='loginCentrado.TFrame')
	frame_login_centrado.pack(pady=80,ipady=40)

	label_login = ttk.Label(frame_login_centrado,text="**** LOGIN ****",style="tituloLogin.TLabel")
	label_login.pack(pady=20)

	imagenLogoPrincipal=PhotoImage(file="imagenes/imagenLogo.png")
	label_Logo = Label(frame_login_centrado,image=imagenLogoPrincipal)
	label_Logo.pack(padx=90)

	def validacion(usuario,clave):
			return len(usuario) > 0 and len (clave) > 0

	def eje_consulta(consulta, parametros=()):
		try:
			with sqlite3.connect(db_nombre) as conexion:
				cursor = conexion.cursor()
				cursor.execute(consulta, parametros)
				conexion.commit()
		except sqlite3.Error as e:
			messagebox.showerror("LifeHealth", "Error al ejecutar la consulta, {e}")

	def crear_tabla():
		consulta = '''
		CREATE TABLE IF NOT EXISTS usuarios (
			idUsuario INTEGER PRIMARY KEY, 
			usuario_info TEXT, 
			clave_info TEXT
		)
		'''
		eje_consulta(consulta)
		

	def registro():
		global imagen_pil_volver_login
		global login_principal
		global entry_usuario_registro
		global entry_contraseña_registro
		global entry_codigoRegistro
		global frame_login_registro

		usuario = StringVar()
		clave = StringVar()
		frame_login.pack_forget()

		def comando_contraseña():
			if entry_contraseña_registro.cget('show') == "*":
				entry_contraseña_registro.config(show="")
			else:
				entry_contraseña_registro.config(show="*")

		def comando_usuario():
			if entry_usuario_registro.cget('show') == "*":
				entry_usuario_registro.config(show="")
			else:
				entry_usuario_registro.config(show="*")
		

		frame_login_registro = ttk.Frame(ventana_principal,style='login.TFrame')
		frame_login_registro.pack(fill=BOTH,expand=1)

		frame_login_centrado_registro =ttk.Frame(frame_login_registro,style='loginCentrado.TFrame')
		frame_login_centrado_registro.pack(pady=100,ipady=60,ipadx=50)

		label_login_registro = ttk.Label(frame_login_centrado_registro,text="**** Log in ****",style="tituloLogin.TLabel")
		label_login_registro.pack(pady=30)
		
		label_usuario_registro = ttk.Label(frame_login_centrado_registro,text="     Usuario     ",style="subTitulo.TLabel")
		label_usuario_registro.pack(pady=10)
		entry_usuario_registro = ttk.Entry(frame_login_centrado_registro,textvariable=usuario,style="entradasLogin.TLabel",width=20,show="*")
		entry_usuario_registro.pack(pady=5,ipadx=10)
			    
		label_contraseña_registro = ttk.Label(frame_login_centrado_registro,text="  Contraseña  ",style="subTitulo.TLabel")
		label_contraseña_registro.pack(pady=10)
		entry_contraseña_registro = ttk.Entry(frame_login_centrado_registro,style="entradasLogin.TLabel",textvariable=clave,width=20,show="*")
		entry_contraseña_registro.pack(pady=5,ipadx=10)

		label_codigoRegistro = ttk.Label(frame_login_centrado_registro,text="   Código  ",style="subTitulo.TLabel")
		label_codigoRegistro.pack(pady=10)
		entry_codigoRegistro = ttk.Entry(frame_login_centrado_registro,style="entradasLogin.TLabel",width=20,show="*")
		entry_codigoRegistro.pack(pady=5,ipadx=10)
		#boton_registrar.config(state="disabled")

		mostrar_contraseña_registro = Checkbutton(frame_login_centrado_registro, text="Mostrar contraseña", bg="#C6D9E3", font=("sans", 10, "bold"), command=comando_contraseña)
		mostrar_contraseña_registro.pack(pady=5, ipadx=10)
		mostrar_usuario_registro = Checkbutton(frame_login_centrado_registro, text="Mostrar usuario", bg="#C6D9E3", font=("sans", 10, "bold"), command=comando_usuario)
		mostrar_usuario_registro.pack(pady=5, ipadx=10)


		imagen_pil_volver_login= Image.open("iconos/btnVolver.png")
		imagen_resize_volver_login = imagen_pil_volver_login.resize((30,30))
		imagen_tk_volver_login= ImageTk.PhotoImage(imagen_resize_volver_login)

		def volver_login_registro():
			global frame_login_registro
			global imagen_pil_volver_login
			frame_login_registro.pack_forget()
			login_principal()

		boton_volver_login= ttk.Button(frame_login_centrado_registro,text="VOLVER",style="botonNavegacion.TButton",command = volver_login_registro)
		boton_volver_login.config(image=imagen_tk_volver_login,compound=LEFT)
		boton_volver_login.image = imagen_tk_volver_login 
		boton_volver_login.pack(side=BOTTOM,padx=20,pady=10)
	
		boton_registrarse = ttk.Button(frame_login_centrado_registro,text="Registrarse",style='botonLogin.TButton',command=registro_usuario)
		boton_registrarse.pack(pady=20,side=BOTTOM)

		
	def registro_usuario():
		global login_principal

		usuario = entry_usuario_registro.get()
		clave = entry_contraseña_registro.get()
		codigo = entry_codigoRegistro.get()
		
		if validacion(usuario, clave):
			if len(clave) < 6:
				messagebox.showinfo("LifeHealth", "Error: Contraseña demasiado corta")
				entry_usuario_registro.delete(0, 'end')
				entry_contraseña_registro.delete(0, 'end')
			else:
				if codigo=="1234":
					crear_tabla()
					consulta = "INSERT INTO usuarios VALUES (?,?,?)"
					parametros = (None, usuario, clave)
					eje_consulta(consulta, parametros)
					messagebox.showinfo("LifeHealth", "Usuario creado correctamente")
					frame_login_registro.pack_forget()
					login_principal()
				else:
					messagebox.showerror("LifeHealth","Error al ingresar el código de registro")
						
		else:	
			messagebox.showwarning("LifeHealth","¡Complete todos los campos!")
			
	def login():
		global login_principal
		global entry_usuario_acceso
		global entry_contraseña_acceso
		global frame_login_acceso

		frame_login.pack_forget()

		def comando_contraseña():
			if entry_contraseña_acceso.cget('show') == "*":
				entry_contraseña_acceso.config(show="")
			else:
				entry_contraseña_acceso.config(show="*")
		
		def comando_usuario():
			if entry_usuario_acceso.cget('show') == "*":
				entry_usuario_acceso.config(show="")
			else:
				entry_usuario_acceso.config(show="*")
		

		frame_login_acceso = ttk.Frame(ventana_principal,style='login.TFrame')
		frame_login_acceso.pack(fill=BOTH,expand=1)

		frame_login_centrado_acceso =ttk.Frame(frame_login_acceso,style='loginCentrado.TFrame')
		frame_login_centrado_acceso.pack(pady=100,ipady=60,ipadx=50)

		label_login_acceso= ttk.Label(frame_login_centrado_acceso,text="**** Log in ****",style="tituloLogin.TLabel")
		label_login_acceso.pack(pady=30)
	    
		label_usuario_acceso = ttk.Label(frame_login_centrado_acceso,text="     Usuario     ",style="subTitulo.TLabel")
		label_usuario_acceso.pack(pady=10)
		entry_usuario_acceso = ttk.Entry(frame_login_centrado_acceso,style="entradasLogin.TLabel",width=20,show="*")
		entry_usuario_acceso.pack(pady=5,ipadx=10)
			    
		label_contraseña_acceso = ttk.Label(frame_login_centrado_acceso,text="  Contraseña  ",style="subTitulo.TLabel")
		label_contraseña_acceso.pack(pady=10)
		entry_contraseña_acceso = ttk.Entry(frame_login_centrado_acceso,style="entradasLogin.TLabel",width=20,show="*")
		entry_contraseña_acceso.pack(pady=5,ipadx=10)

		mostrar_contraseña_acceso = Checkbutton(frame_login_centrado_acceso, text="Mostrar contraseña", bg="#C6D9E3", font=("sans", 10, "bold"), command=comando_contraseña)
		mostrar_contraseña_acceso.pack(pady=5, ipadx=10)
		mostrar_usuario_registro = Checkbutton(frame_login_centrado_acceso, text="Mostrar usuario", bg="#C6D9E3", font=("sans", 10, "bold"), command=comando_usuario)
		mostrar_usuario_registro.pack(pady=5, ipadx=10)
		
		imagen_pil_volver_login= Image.open("iconos/btnVolver.png")
		imagen_resize_volver_login = imagen_pil_volver_login.resize((30,30))
		imagen_tk_volver_login= ImageTk.PhotoImage(imagen_resize_volver_login)

		def volver_login_acceso():
			global frame_login_registro
			global imagen_pil_volver_login
			frame_login_acceso.pack_forget()
			login_principal()

		boton_volver_login= ttk.Button(frame_login_centrado_acceso,text="VOLVER",style="botonNavegacion.TButton",command = volver_login_acceso)
		boton_volver_login.config(image=imagen_tk_volver_login,compound=LEFT)
		boton_volver_login.image = imagen_tk_volver_login 
		boton_volver_login.pack(side=BOTTOM,padx=20,pady=10)

		boton_acceso = ttk.Button(frame_login_centrado_acceso,text="Ingresar",style='botonLogin.TButton',command=verificacion_login)
		boton_acceso.pack(pady=20,side=BOTTOM)

	def verificacion_login():
		global login_principal
		usuario = entry_usuario_acceso.get()
		clave = entry_contraseña_acceso.get()
		if validacion(usuario, clave):
			consulta = "SELECT * FROM usuarios WHERE usuario_info=? AND clave_info=?"
			parametros = (usuario, clave)
			try:
				with sqlite3.connect(db_nombre) as conexion:
					cursor = conexion.cursor()
					cursor.execute(consulta, parametros)
					resultado = cursor.fetchall()

					if resultado:
						messagebox.showinfo("LifeHealth", "Bienvenido "+ usuario)
						frame_login_acceso.pack_forget()
						barraCarga()
						frame_carga.pack_forget()	
						principal()
						
					
					else:
						entry_usuario_acceso.delete(0, 'end')
						entry_contraseña_acceso.delete(0, 'end')
						messagebox.showerror("LifeHealth", "Usuario y/o contraseña incorrecta")
						frame_login_acceso.pack_forget()
						login_principal()

			except sqlite3.Error as e:
				messagebox.showerror("LifeHealth","No se conectó a la base de datos,{e}")
		else:
			messagebox.showerror("LifeHealth", "Complete todos los campos")
 
	
	boton_registrar = ttk.Button(frame_login_centrado,text="Registro",style='botonLogin.TButton',command=registro).pack(pady=10,side=BOTTOM)
	boton_login = ttk.Button(frame_login_centrado,text="Acceso",style='botonLogin.TButton',command=login).pack(pady=10,side=BOTTOM)	

def barraCarga():
	global frame_carga
	global progressbar
	global imagenLogo

	frame_carga = ttk.Frame(ventana_principal,style='login.TFrame')
	frame_carga.pack(fill=BOTH,expand=1)
	frame_carga_centrado =ttk.Frame(frame_carga,style='loginCentrado.TFrame')
	frame_carga_centrado.pack(pady=80,ipady=40,ipadx=40)
	label_carga = ttk.Label(frame_carga_centrado,text="Cargando....",font=("Georgia",30),style="tituloLogin.TLabel")
	label_carga.pack(pady=40)
	imagenLogo=PhotoImage(file="imagenes/imagenLogo.png")
	label_Logo = Label(frame_carga_centrado,image=imagenLogo)
	label_Logo.pack(padx=90)

	percent = StringVar()
	text = StringVar()

	progressbar = ttk.Progressbar(frame_carga_centrado,orient=HORIZONTAL,length=300)
	progressbar.pack(pady=70)

	percentLabel = ttk.Label(frame_carga_centrado, textvariable=percent,style="subTitulo.TLabel").pack(ipady=5,pady=5,padx=5)
	taskLabel = ttk.Label(frame_carga_centrado, textvariable=text,style="subTitulo.TLabel").pack(ipady=5,pady=5,padx=5)
	
	GB = 100
	descarga = 0
	speed = 1
	while(descarga<GB):
		time.sleep(0.08)
		progressbar ["value"]+=(speed/GB)*100
		descarga+=speed
		percent.set(str(int(descarga/GB)*100)+"%")
		text.set(str(descarga)+" Completando ")
		
		ventana_principal.update_idletasks()

	button = Button(frame_carga_centrado, text= "Descarga").pack()
	
def principal():
	
	if(not(os.path.isfile("Bd/LifeHealth.db"))):
		messagebox.showwarning(title="LifeHealth",message="Ingrese algo que buscar")	
	else:

		global vcmd
		global vcmd2
		global frame_botones
		global frame_botones2

		ventana_principal.state("zoomed")
		vcmd=(ventana_principal.register(validate_entry_numeros),"%S")
		vcmd2=(ventana_principal.register(validate_entry_letras_espacios),"%p")
		
		frame_contenido = ttk.Frame(ventana_principal,style='principal.TFrame')
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)

		inicio(frame_contenido)

		def verInicio():
		
			global imagen_pil_inicio
			global frame_botones
			global frame_botones2
		
			borrarFrames()
		
			if 'frame_inicio' not in globals():
				inicio(frame_contenido)
			else:		
				frame_inicio.pack(fill=BOTH,expand=1)
		
		
		def verInventario():
			global imagen_pil_stock
			global frame_botones
			global frame_botones2
		
			
			borrarFrames()
			if 'frame_inventario' not in globals():
				inventario(frame_contenido)
			else:
				frame_inventario.pack(fill=BOTH,expand=1)

		imagen_pil_stock= Image.open("iconos/btnStock.png")
		imagen_resize_inventarios = imagen_pil_stock.resize((50,50))
		imagen_tk_inventarios= ImageTk.PhotoImage(imagen_resize_inventarios)

		boton_inventario = ttk.Button(frame_botones,text='Inventario',style='botonNavegacion.TButton',command=verInventario)
		boton_inventario.config(image=imagen_tk_inventarios,compound=LEFT)
		boton_inventario.image = imagen_tk_inventarios
		boton_inventario.pack(pady=20)

		def verClientes():

			global imagen_pil_clientes

			borrarFrames()
			if 'frame_clientes' not in globals():
				clientes(frame_contenido)
			else:
				frame_clientes.pack(fill=BOTH,expand=1)

		imagen_pil_clientes= Image.open("iconos/btnClientes.png")
		imagen_resize_clientes = imagen_pil_clientes.resize((50,50))
		imagen_tk_clientes= ImageTk.PhotoImage(imagen_resize_clientes)

		boton_clientes = ttk.Button(frame_botones,text='Clientes',style='botonNavegacion.TButton',command=verClientes)
		boton_clientes.config(image=imagen_tk_clientes,compound=LEFT)
		boton_clientes.image = imagen_tk_clientes
		boton_clientes.pack(pady=20)

		def verProveedores():

			global imagen_pil_proveedores

			borrarFrames()

			if 'frame_proveedores' not in globals():
				proveedores(frame_contenido)
			else:
				frame_proveedores.pack(fill=BOTH,expand=1)

		imagen_pil_proveedores= Image.open("iconos/btnProveedores.png")
		imagen_resize_proveedores = imagen_pil_proveedores.resize((50,50))
		imagen_tk_proveedores= ImageTk.PhotoImage(imagen_resize_proveedores)

		boton_proveedores = ttk.Button(frame_botones,text='Proveedores',style='botonNavegacion.TButton',command=verProveedores)
		boton_proveedores.config(image=imagen_tk_proveedores,compound=LEFT)
		boton_proveedores.image = imagen_tk_proveedores
		boton_proveedores.pack(pady=20)

		def verPedidos():

			global imagen_pil_compras
			borrarFrames()

			if 'frame_pedidos' not in globals():
				pedidos(frame_contenido)
			else:
				frame_pedidos.pack(fill=BOTH,expand=1)

		imagen_pil_compras= Image.open("iconos/btnCompras.png")
		imagen_resize_compras = imagen_pil_compras.resize((50,50))
		imagen_tk_compras= ImageTk.PhotoImage(imagen_resize_compras)

		boton_compras = ttk.Button(frame_botones,text='Pedidos',style='botonNavegacion.TButton',command=verPedidos)
		boton_compras.config(image=imagen_tk_compras,compound=LEFT)
		boton_compras.image = imagen_tk_compras
		boton_compras.pack(pady=20)

		def verVentas():
			global imagen_pil_ventas
			borrarFrames()
			if 'frame_ventas' not in globals():
				ventas(frame_contenido)
			else:
				frame_ventas.pack(fill=BOTH,expand=1)

		imagen_pil_ventas= Image.open("iconos/btnVentas.png")
		imagen_resize_ventas = imagen_pil_ventas.resize((50,50))
		imagen_tk_ventas= ImageTk.PhotoImage(imagen_resize_ventas)
			
		boton_ventas = ttk.Button(frame_botones,text='Ventas',style='botonNavegacion.TButton',command=verVentas)
		boton_ventas.config(image=imagen_tk_ventas,compound=LEFT)
		boton_ventas.image = imagen_tk_ventas
		boton_ventas.pack(pady=20)
		
		def verReportes():
			global imagen_pil_reportes
			borrarFrames()
			if 'frame_reportes' not in globals():
				reportes(frame_contenido)
			else:
				frame_reportes.pack(fill=BOTH,expand=1)

		imagen_pil_reportes= Image.open("iconos/btnReportes.png")
		imagen_resize_reportes = imagen_pil_reportes.resize((50,50))
		imagen_tk_reportes= ImageTk.PhotoImage(imagen_resize_reportes)

		boton_reportes = ttk.Button(frame_botones2,text='Reportes',style='botonNavegacion.TButton',command=verReportes)
		boton_reportes.config(image=imagen_tk_reportes,compound=LEFT)
		boton_reportes.image = imagen_tk_reportes
		boton_reportes.pack(pady=20)

		def verUsuarios():
			global imagen_pil_usuarios
			borrarFrames()
			if 'frame_usuarios' not in globals():
				usuarios(frame_contenido)
			else:
				frame_usuarios.pack(fill=BOTH,expand=1)
		
		imagen_pil_usuarios= Image.open("iconos/btnUsuarios.png")
		imagen_resize_usuarios = imagen_pil_usuarios.resize((50,50))
		imagen_tk_usuarios= ImageTk.PhotoImage(imagen_resize_usuarios)

		boton_usuarios = ttk.Button(frame_botones2,text='Usuarios',style='botonNavegacion.TButton',command=verUsuarios)
		boton_usuarios.config(image=imagen_tk_usuarios,compound=LEFT)
		boton_usuarios.image = imagen_tk_usuarios
		boton_usuarios.pack(pady=20)

		def verGastos():
			borrarFrames()
			global imagen_pil_gastos
			if 'frame_gastos' not in globals():
				gastos(frame_contenido)
			else:
				frame_gastos.pack(fill=BOTH,expand=1)
		
		imagen_pil_gastos= Image.open("iconos/btnGastos.png")
		imagen_resize_gastos = imagen_pil_gastos.resize((50,50))
		imagen_tk_gastos= ImageTk.PhotoImage(imagen_resize_gastos)

		boton_gastos = ttk.Button(frame_botones2,text='Gastos',style='botonNavegacion.TButton',command=verGastos)
		boton_gastos.config(image=imagen_tk_gastos,compound=LEFT)
		boton_gastos.image = imagen_tk_gastos
		boton_gastos.pack(pady=20)

		def verEmpleados():
			global imagen_pil_empleados
			borrarFrames()
			if 'frame_empleados' not in globals():
				empleados(frame_contenido)
			else:
				frame_empleados.pack(fill=BOTH,expand=1)

		imagen_pil_empleados= Image.open("iconos/btnEmpleados.png")
		imagen_resize_empleados = imagen_pil_empleados.resize((50,50))
		imagen_tk_empleados= ImageTk.PhotoImage(imagen_resize_empleados)

		boton_empleados = ttk.Button(frame_botones2,text='Empleados',style='botonNavegacion.TButton',command=verEmpleados)
		boton_empleados.config(image=imagen_tk_empleados,compound=LEFT)
		boton_empleados.image = imagen_tk_empleados
		boton_empleados.pack(pady=20)

		def verAcerca():
			global imagen_pil_acerca
			borrarFrames()
			if 'frame_acerca' not in globals():
				acerca(frame_contenido)
			else:
				frame_acerca.pack(fill=BOTH,expand=1)

		imagen_pil_acerca= Image.open("iconos/btnAcerca.png")
		imagen_resize_acerca = imagen_pil_acerca.resize((50,50))
		imagen_tk_acerca= ImageTk.PhotoImage(imagen_resize_acerca)

		boton_acerca = ttk.Button(frame_botones2,text='Acerca',style='botonNavegacion.TButton',command=verAcerca)
		boton_acerca.config(image=imagen_tk_acerca,compound=LEFT)
		boton_acerca.image = imagen_tk_acerca
		boton_acerca.pack(pady=20)

		def cierreSesion():
			ventana_principal.destroy()

		imagen_pil_cierre= Image.open("iconos/btnCierre.png")
		imagen_resize_cierre = imagen_pil_cierre.resize((50,50))
		imagen_tk_cierre= ImageTk.PhotoImage(imagen_resize_cierre)

		Boton_cierre = ttk.Button(frame_botones2,text='Cierre Sesion',style='botonNavegacion.TButton',command=cierreSesion)
		Boton_cierre.config(image=imagen_tk_cierre,compound=LEFT)
		Boton_cierre.image = imagen_tk_cierre
		Boton_cierre.pack(pady=20)

def borrarFrames():
	if 'frame_inicio' in globals():
		frame_inicio.pack_forget()

	if 'frame_clientes' in globals():
		frame_clientes.pack_forget()

	if 'frame_proveedores' in globals():
		frame_proveedores.pack_forget()

	if 'frame_pedidos' in globals():
		frame_pedidos.pack_forget()

	if 'frame_ventas' in globals():
		frame_ventas.pack_forget()

	if 'frame_inventario' in globals():
		frame_inventario.pack_forget()

	if 'frame_reportes' in globals():
		frame_reportes.pack_forget()

	if 'frame_usuarios' in globals():
		frame_usuarios.pack_forget()

	if 'frame_gastos' in globals():
		frame_gastos.pack_forget()

	if 'frame_acerca' in globals():
		frame_acerca.pack_forget()

	if "frame_empleados" in globals():
		frame_empleados.pack_forget()
	
def inicio(frame_contenido):
	global frame_inicio
	global imagenFrameInicio
	global imagenDeLogoPrincipal
	global imagenLatido
	global inicio
	global frame_botones
	global frame_botones2

	frame_inicio = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_inicio.pack(fill=BOTH,expand=1)
	frame_botones= ttk.Frame(frame_inicio,style='navegacion.TFrame')
	frame_botones2= ttk.Frame(frame_inicio,style='navegacion.TFrame')
				
	frame_botones.pack(side=LEFT,fill=Y)
	frame_botones2.pack(side=RIGHT,fill=Y)
		

	frame_contenido_inicio=ttk.Frame(frame_inicio,style="fondo.TFrame")
	frame_contenido_inicio.pack(fill=Y,side=LEFT,padx=70,pady=20)

	frame_contenido_calendario=Frame(frame_inicio,bg="black")
	frame_contenido_calendario.pack(fill=Y,side=RIGHT,ipadx=100,padx=50,pady=50)
	
	cal = Calendar(frame_contenido_calendario,selectmode = "day", year =2024,month =7,day=22,bg="black")
	cal.pack(ipadx=30,ipady=30)

	imagenLatido=PhotoImage(file="imagenes/latido.png")
	labelLatido= Label(frame_contenido_calendario,image=imagenLatido)
	labelLatido.pack(pady=60)

	titulo_programa = ttk.Label(frame_contenido_inicio,text=nombrePrograma,anchor="c",justify=RIGHT,style="programa.TLabel")
	titulo_programa.pack(pady=50)

	imagenDeLogoPrincipal=PhotoImage(file="imagenes/imagenLogo.png")
	label_De_Logo_Principal = Label(frame_contenido_inicio,image=imagenDeLogoPrincipal)
	label_De_Logo_Principal.pack(pady=20)

	label_direccion = ttk.Label(frame_contenido_inicio,text="Bienvenido/a a Sistema de Ventas",anchor="c",justify=RIGHT,style='subTitulo.TLabel')
	label_direccion.pack(pady=20)

	label_contacto = ttk.Label(frame_contenido_inicio,text="Insumos médicos",anchor="c",justify=RIGHT,style='subTitulo.TLabel')
	label_contacto.pack(pady=10)

	label_mail = ttk.Label(frame_contenido_inicio,text="Clínicas-Hospitales-Ortopedias-Uso dosmético",anchor="c",justify=RIGHT,style='subTitulo.TLabel')
	label_mail.pack(pady=20)

def clientes(frame_contenido):

	#Variable Global
	global frame_clientes
	global vcmd
	global vcmd2

	#Frame
	frame_clientes = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_clientes.pack(fill=BOTH,expand=1)

	frame_contenido_clientes = ttk.Frame(frame_clientes,style="navegacion.TFrame")
	frame_contenido_clientes.pack(side=LEFT,fill=Y,ipadx=50)

	frame_botones_cliente= ttk.Frame(frame_clientes,style="navegacion.TFrame")
	frame_botones_cliente.pack(side=RIGHT,fill=Y)

	#Creación de listbox
	
	listbox_clientes = Listbox(frame_clientes)
	listbox_clientes.place(x=480,y=100,width=500,height=500)
	scrol_y_c = ttk.Scrollbar(listbox_clientes,orient=VERTICAL)
	scrol_y_c.pack(side=RIGHT,fill=Y)
	scrol_x_c = ttk.Scrollbar(listbox_clientes,orient=HORIZONTAL)
	scrol_x_c.pack(side=BOTTOM,fill=X)

	
	#Evento mostrar en listbox
	def mostrarClientes(evento):
		indiceClientes=listbox_clientes.curselection()[0]
		mensajeClientes=listbox_clientes.get(indiceClientes)
		messagebox.showinfo("LifeHealth",mensajeClientes)
	listbox_clientes.bind("<<ListboxSelect>>",mostrarClientes)

	#Label y Entry CRUD
	label_clientes = LabelFrame(frame_contenido_clientes,bg="SkyBlue4",text="Datos del cliente",font= "Georgia 20 bold")
	label_clientes.pack(anchor=W,padx=10,pady=20)

	label_buscar_clientes =ttk.Label(label_clientes,text="Buscar Cliente por ID",style="labelNavegacion.TLabel")
	label_buscar_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_buscar_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35)
	entry_buscar_clientes.pack(anchor=NW,padx=20)	

	label_id_clientes = ttk.Label(label_clientes,text="ID cliente",style="labelNavegacion.TLabel")
	label_id_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_id_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35)
	entry_id_clientes.pack(anchor=NW,padx=20)

	entry_id_clientes.config(state="readonly")

	label_dni_clientes = ttk.Label(label_clientes,text="DNI",style="labelNavegacion.TLabel")
	label_dni_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_dni_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_dni_clientes.pack(anchor=NW,padx=20)

	label_nombre_clientes = ttk.Label(label_clientes,text="Nombre",style="labelNavegacion.TLabel")
	label_nombre_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_nombre_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35,validate="key",validatecommand=vcmd2)
	entry_nombre_clientes.pack(anchor=NW,padx=20)

	label_tel_clientes = ttk.Label(label_clientes,text="Telefono",style="labelNavegacion.TLabel")
	label_tel_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_tel_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_tel_clientes.pack(anchor=NW,padx=20)

	label_cuit_clientes = ttk.Label(label_clientes,text="CUIT",style="labelNavegacion.TLabel")
	label_cuit_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_cuit_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_cuit_clientes.pack(anchor=NW,padx=20)

	label_direccion_clientes = ttk.Label(label_clientes,text="Dirección",style="labelNavegacion.TLabel")
	label_direccion_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_direccion_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35)
	entry_direccion_clientes.pack(anchor=NW,padx=20)

	label_email_clientes = ttk.Label(label_clientes,text="E-MAIL",style="labelNavegacion.TLabel")
	label_email_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_email_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35)
	entry_email_clientes.pack(anchor=NW,padx=20)

	label_iva_clientes = ttk.Label(label_clientes,text="IVA",style="labelNavegacion.TLabel")
	label_iva_clientes.pack(anchor=NW,pady=10,padx=20)
	entry_iva_clientes = ttk.Entry(label_clientes,style="entradasNavegacion.TLabel",width=35,validate="key",validatecommand=vcmd2)
	entry_iva_clientes.pack(anchor=NW,padx=20)

	#categorias=["Monotributo","Responsable Inscripto","Exento","Otros"]
	#label_iva_clientes = ttk.Label(label_clientes,text="IVA",style="labelNavegacion.TLabel")
	#label_iva_clientes.pack(anchor=NW,pady=10,padx=20)
	#entry_iva_clientes = ttk.Combobox(label_clientes, style="entradasNavegacion.TLabel",width=35,values=categorias,state="readonly")
	#entry_iva_clientes.set("Seleccione una categoria")
	#entry_iva_clientes.pack(anchor=NW,padx=20)

	
	#Buscar Cliente
	def buscarClientes():
		global datos
		buscarClientes=entry_buscar_clientes.get() 
		if(buscarClientes !=""):
			try:
				ver=True
				for letra in buscarClientes:
					if(not(letra.isdigit())):
						ver=False
						break
				if(ver):
					buscarClientes = (entry_buscar_clientes.get(),)
					conexion = sqlite3.connect("Bd/LifeHealth.db")
					tabla=conexion.cursor()
					tabla.execute("SELECT * FROM clientes WHERE idClientes=?",buscarClientes)
					datos = tabla.fetchall()

					entry_id_clientes.config(state="normal")
					entry_id_clientes.delete(0,END)
					entry_dni_clientes.config(state="normal")
					entry_dni_clientes.delete(0,END)
					entry_nombre_clientes.delete(0,END)
					entry_tel_clientes.delete(0,END)
					entry_cuit_clientes.delete(0,END)
					entry_direccion_clientes.delete(0,END)
					entry_email_clientes.delete(0,END)
					entry_iva_clientes.delete(0,END)

					boton_modificar_clientes.config(state="normal")
					boton_eliminar_clientes.config(state="normal")
					if(len(datos)>0):
						boton_guardar_clientes.config(state="disabled")
						for dato in datos:
							idClientes=dato[0]
							dniClientes=dato[1]
							nombre=dato[2]
							telClientes=dato[3]
							cuitClientes=dato[4]
							direccionClientes=dato[5]
							correoClientes=dato[6]
							ivaClientes=dato[7]

							entry_id_clientes.insert(END,idClientes)
							entry_dni_clientes.insert(END,dniClientes)
							entry_nombre_clientes.insert(END,nombre)
							entry_tel_clientes.insert(END,telClientes)
							entry_cuit_clientes.insert(END,cuitClientes)
							entry_direccion_clientes.insert(END,direccionClientes)
							entry_email_clientes.insert(END,correoClientes)
							entry_iva_clientes.insert(END,ivaClientes)
					else:
						messagebox.showwarning("LifeHealth","No se encrontró cliente")
						entry_id_clientes.config(state="readonly")
						limpiarClientes()
				else:
					messagebox.showwarning(title="LifeHealth",message="Ingrese solo números")
			except ValueError:
				messagebox.showwarning(title="LifeHealth",message="Registro incorrecto")
		else:
			messagebox.showwarning(title="LifeHealth",message="Ingrese algo que buscar")		
	
	boton_buscar_clientes = ttk.Button(frame_botones_cliente,text="BUSCAR",style="botonNavegacion.TButton",command = buscarClientes)
	boton_buscar_clientes.pack(padx=20,pady=30)
	
	#Guardar Cliente
	def guardarClientes():
		try:
			boton_guardar_clientes.config(state="normal")
			dniClientes = entry_dni_clientes.get()
			nombre = entry_nombre_clientes.get()
			telClientes = entry_tel_clientes.get()
			cuitClientes = entry_cuit_clientes.get()
			direccionClientes = entry_direccion_clientes.get()
			correoClientes = entry_email_clientes.get()
			ivaClientes = entry_iva_clientes.get()

			if(dniClientes != "" and nombre != "" and telClientes != "" and cuitClientes  !="" and direccionClientes != "" and correoClientes != "" and ivaClientes !=""):
				datos = (dniClientes,nombre,telClientes,cuitClientes,direccionClientes,correoClientes,ivaClientes)
				conexion = sqlite3.connect("Bd/LifeHealth.db")				
				tabla = conexion.cursor()
				tabla.execute("INSERT INTO clientes(dniClientes,nombre,telClientes,cuitClientes,direccionClientes,correoClientes,ivaClientes)VALUES(?,?,?,?,?,?,?)",datos)
				conexion.commit()
				messagebox.showinfo("LifeHealth","Guardado con éxito")
				
				limpiarClientes()
				listarClientes()
				
			else:
				messagebox.showwarning("LifeHealth","Complete todos los campos")

		except ValueError   as e:
			messagebox.showerror("Error","Error datos de la base de datos, {e}")

	boton_guardar_clientes = ttk.Button(frame_botones_cliente,text="GUARDAR",style="botonNavegacion.TButton",command = guardarClientes)
	boton_guardar_clientes.pack(padx=20,pady=30)

	#Modificar Cliente
	def modificarClientes():
		boton_guardar_clientes.config(state="normal")

		idClientes = entry_id_clientes.get()
		dniClientes = entry_dni_clientes.get()
		nombre = entry_nombre_clientes.get()
		telClientes = entry_tel_clientes.get()
		cuitClientes = entry_cuit_clientes.get()
		direccionClientes = entry_direccion_clientes.get()
		correoClientes = entry_email_clientes.get()
		ivaClientes = entry_iva_clientes.get()
		datos = (dniClientes,nombre,telClientes,cuitClientes,direccionClientes,correoClientes,ivaClientes,idClientes)
		conexion = sqlite3.connect("Bd/LifeHealth.db")
		tabla=conexion.cursor()
		tabla.execute("UPDATE clientes SET dniClientes=?,nombre=?,telClientes=?,cuitClientes=?,direccionClientes=?,correoClientes=?,ivaClientes=? WHERE idClientes =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Modificado con éxito")
		limpiarClientes()
		listarClientes()
		
	boton_modificar_clientes = ttk.Button(frame_botones_cliente,text="MODIFICAR",style="botonNavegacion.TButton",command = modificarClientes)
	boton_modificar_clientes.pack(padx=20,pady=30)
	boton_modificar_clientes.config(state="disabled")

	#Eliminar Cliente
	def eliminarClientes():
		boton_guardar_clientes.config(state="normal")
		idClientes = entry_id_clientes.get()
		datos = (idClientes,)
		conexion = sqlite3.connect("Bd/LifeHealth.db")
		tabla=conexion.cursor()
		tabla.execute("DELETE FROM clientes WHERE idClientes =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Eliminado con éxito")	
		limpiarClientes()
		listarClientes()

	boton_eliminar_clientes = ttk.Button(frame_botones_cliente,text="ELIMINAR",style="botonNavegacion.TButton",command = eliminarClientes)
	boton_eliminar_clientes.pack(padx=20,pady=30)
	boton_eliminar_clientes.config(state="disabled")

	#Limpiar Cliente
	def limpiarClientes():
		boton_guardar_clientes.config(state="normal")
		entry_buscar_clientes.delete(0,END)
		entry_id_clientes.config(state="normal")
		entry_id_clientes.delete(0,END)
		entry_id_clientes.config(state="readonly")
		entry_dni_clientes.delete(0,END)
		entry_nombre_clientes.delete(0,END)
		entry_tel_clientes.delete(0,END)
		entry_cuit_clientes.delete(0,END)
		entry_direccion_clientes.delete(0,END)
		entry_email_clientes.delete(0,END)
		entry_iva_clientes.delete(0,END)

		boton_modificar_clientes.config(state="disable")
		boton_eliminar_clientes.config(state="disable")

	boton_limpiar_clientes = ttk.Button(frame_botones_cliente,text="LIMPIAR",style="botonNavegacion.TButton",command = limpiarClientes)
	boton_limpiar_clientes.pack(padx=20,pady=30)

	def listarClientes():
		conexion = sqlite3.connect("Bd/LifeHealth.db")

		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM clientes")
		listado = tabla.fetchall()
		listbox_clientes.delete(0,END)

		for elemento in listado:
			informacionCliente = "ID:"+"  "+str(elemento[0])+"  "+"DNI:"+"  "+str(elemento[1])+"  "+"Nombre:"+"  "+elemento[2]   
			listbox_clientes.insert(END,informacionCliente)
	listarClientes()
	#boton_listar_clientes = ttk.Button(frame_botones_cliente,text="LISTAR",style="botonNavegacion.TButton",command = listarClientes())
	#boton_listar_clientes.pack(padx=20,pady=30)	

	def volverPrincipalCliente():
		global imagen_pil_volver_cliente
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		

	imagen_pil_volver_cliente= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_cliente = imagen_pil_volver_cliente.resize((30,30))
	imagen_tk_volver_cliente= ImageTk.PhotoImage(imagen_resize_volver_cliente)

	boton_volver_cliente = ttk.Button(frame_botones_cliente,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalCliente)
	boton_volver_cliente.config(image=imagen_tk_volver_cliente,compound=LEFT)
	boton_volver_cliente.image = imagen_tk_volver_cliente 
	boton_volver_cliente.pack(side=BOTTOM,padx=20,pady=30)

def proveedores(frame_contenido):
	global frame_proveedores
	global combo
	frame_proveedores = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_proveedores.pack(fill=BOTH,expand=1)

	frame_buscador_proveedores=ttk.Frame(frame_proveedores,style="fondo.TFrame")
	frame_buscador_proveedores.pack(fill=X,pady=40)

	frame_datos_proveedores=ttk.Frame(frame_buscador_proveedores,style="principal.TFrame")
	frame_datos_proveedores.pack(fill=X,expand=1,padx=30)

	frame_buscado_proveedores=ttk.Frame(frame_proveedores,style="navegacion.TFrame")
	frame_buscado_proveedores.pack(ipadx=150,ipady=50,padx=40,pady=40)
	
	label_busqueda_proveedores=ttk.Label(frame_datos_proveedores,text="Buscar proveedor por nombre",style="labelNavegacion.TLabel")
	label_busqueda_proveedores.pack(side=LEFT,padx=20,pady=20)
	entry_busqueda_proveedores=ttk.Entry(frame_datos_proveedores,style="entradasNavegacion2.TLabel",width=35)
	entry_busqueda_proveedores.pack(side=LEFT,padx=10,pady=20)

	combo = ttk.Combobox(frame_datos_proveedores)

	label_datos_proveedor=ttk.Label(frame_buscado_proveedores,text="Datos proveedor",style="subTitulo.TLabel")
	label_datos_proveedor.grid(row=1,column=1,pady=20,padx=5)

	label_numero_proveedor=ttk.Label(frame_buscado_proveedores,text="N°",style="labelNavegacion.TLabel")
	label_numero_proveedor.grid(row=1,column=2,pady=10)
	entry_numero_proveedor=ttk.Entry(frame_buscado_proveedores,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_numero_proveedor.grid(row=1,column=3,ipady=5,ipadx=5,pady=10)
	entry_numero_proveedor.config(state="readonly")

	label_cuit_proveedor=ttk.Label(frame_buscado_proveedores,text="CUIT",style="labelNavegacion.TLabel")
	label_cuit_proveedor.grid(row=2,column=1,pady=10,padx=5)
	entry_cuit_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate= "key",validatecommand=vcmd)
	entry_cuit_proveedor.grid(row=2,column=2,ipady=5,ipadx=5,pady=10,padx=5)

	label_nombre_proveedor=ttk.Label(frame_buscado_proveedores,text="Razón social",style="labelNavegacion.TLabel")
	label_nombre_proveedor.grid(row=3,column=1,pady=10,padx=5)
	entry_nombre_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate="key",validatecommand=vcmd2)
	entry_nombre_proveedor.grid(row=3,column=2,ipady=5,ipadx=5,pady=10,padx=5)

	label_categoria_proveedor=ttk.Label(frame_buscado_proveedores,text="Categoria",style="labelNavegacion.TLabel")
	label_categoria_proveedor.grid(row=4,column=1,pady=10,padx=5)
	entry_categoria_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel")
	entry_categoria_proveedor.grid(row=4,column=2,ipady=5,ipadx=5,pady=10,padx=5)


	label_telefono_proveedor=ttk.Label(frame_buscado_proveedores,text="Teléfono contacto",style="labelNavegacion.TLabel")
	label_telefono_proveedor.grid(row=2,column=3,pady=10,padx=5)
	entry_numero_proveedor.config(state="disabled")
	entry_telefono_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate= "key",validatecommand=vcmd)
	entry_telefono_proveedor.grid(row=2,column=4,ipady=5,ipadx=5,pady=10,padx=5)

	label_insumo_proveedor=ttk.Label(frame_buscado_proveedores,text="Insumos",style="labelNavegacion.TLabel")
	label_insumo_proveedor.grid(row=3,column=3,pady=10,padx=5)
	entry_insumo_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate="key",validatecommand=vcmd2)
	entry_insumo_proveedor.grid(row=3,column=4,ipady=5,ipadx=5,pady=10,padx=5)

	label_domicilio_proveedor=ttk.Label(frame_buscado_proveedores,text="Domicilio",style="labelNavegacion.TLabel")
	label_domicilio_proveedor.grid(row=4,column=3,pady=10,padx=5)
	entry_domicilio_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel")
	entry_domicilio_proveedor.grid(row=4,column=4,ipady=5,ipadx=5,pady=10,padx=5)

	label_cp_proveedor=ttk.Label(frame_buscado_proveedores,text="Código postal",style="labelNavegacion.TLabel")
	label_cp_proveedor.grid(row=2,column=5,pady=10,padx=5)
	entry_cp_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate= "key",validatecommand=vcmd)
	entry_cp_proveedor.grid(row=2,column=6,ipady=5,ipadx=5,pady=10,padx=5)

	label_mail_proveedor=ttk.Label(frame_buscado_proveedores,text="E-mail",style="labelNavegacion.TLabel")
	label_mail_proveedor.grid(row=3,column=5,pady=10,padx=5)
	entry_mail_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel")
	entry_mail_proveedor.grid(row=3,column=6,ipady=5,ipadx=5,pady=10,padx=5)

	label_iva_proveedor=ttk.Label(frame_buscado_proveedores,text="IVA",style="labelNavegacion.TLabel")
	label_iva_proveedor.grid(row=4,column=5,pady=10,padx=5)
	entry_iva_proveedor=ttk.Entry(frame_buscado_proveedores,width=35,style="entradasNavegacion.TLabel",validate="key",validatecommand=vcmd2)
	entry_iva_proveedor.grid(row=4,column=6,ipady=5,ipadx=5,pady=10,padx=5)


	def seleccionarComboProveedor(evento):
		frame_buscado_proveedores.pack()           
		indiceProveedor=combo.current()
		proveedor=datos[indiceProveedor]

		entry_numero_proveedor.config(state="normal")

		entry_numero_proveedor.delete(0,END)
		entry_cuit_proveedor.delete(0,END)
		entry_nombre_proveedor.delete(0,END)
		entry_categoria_proveedor.delete(0,END)
		entry_telefono_proveedor.delete(0,END)
		entry_insumo_proveedor.delete(0,END)
		entry_domicilio_proveedor.delete(0,END)
		entry_cp_proveedor.delete(0,END)
		entry_mail_proveedor.delete(0,END)
		entry_iva_proveedor.delete(0,END)

		entry_numero_proveedor.insert(END,proveedor[0])
		entry_cuit_proveedor.insert(END,proveedor[1])
		entry_nombre_proveedor.insert(END,proveedor[2])
		entry_categoria_proveedor.insert(END,proveedor[3])
		entry_telefono_proveedor.insert(END,proveedor[4])
		entry_insumo_proveedor.insert(END,proveedor[5])
		entry_domicilio_proveedor.insert(END,proveedor[6])
		entry_cp_proveedor.insert(END,proveedor[7])
		entry_mail_proveedor.insert(END,proveedor[8])
		entry_iva_proveedor.insert(END,proveedor[9])

	combo.bind("<<ComboboxSelected>>",seleccionarComboProveedor)
	
	def buscar_proveedor():
		boton_eliminar_proveedores.config(state="normal")
		boton_modificar_proveedores.config(state="normal")
		buscarProveedor=entry_busqueda_proveedores.get() 
		if(buscarProveedor !=""):
			try:
				ver=True
				for letra in buscarProveedor:
					if(letra.isdigit()):
						ver=False
						break
				if(ver):
					combo.pack_forget()
					buscarProveedor=(entry_busqueda_proveedores.get(),)
					tabla=conexion.cursor()
					tabla.execute("SELECT * FROM proveedores WHERE nombre LIKE ?",buscarProveedor)             
					global datos
					datos=tabla.fetchall()
					if(len(datos)>0):
						combo.pack(side=TOP,fill=X,padx=10,pady=10)
						lista=[]
						for dato in datos:
							lista.append("Nombre de proveedor:"+" "+dato[2])
						combo.config(values=lista)
						combo.current(0)
						boton_guardar_proveedor.config(state="disabled")
					else:
						messagebox.showerror("LifeHealth","No se ha encontrado proveedor")
						limpiar_proveedores()
						combo.pack_forget()
				else:
					messagebox.showwarning("LifeHealth","Buscar por nombre!")
					limpiar_proveedores()

			except sqlite3.Error as e:
				messagebox.showerror("Registro incorrecto",{e})

		else:
			messagebox.showwarning(title="LifeHealth",message="Ingrese algo que buscar")
			limpiar_proveedores()

	boton_buscar_proveedor=ttk.Button(frame_datos_proveedores,text="Buscar",style="botonNavegacion.TButton",command=buscar_proveedor)
	boton_buscar_proveedor.pack(side=LEFT,padx=60)

	def modificar_proveedores():

		idProveedor = entry_numero_proveedor.get()
		cuitProveedor = entry_cuit_proveedor.get()
		nombre = entry_nombre_proveedor.get()
		categoriaProveedor = entry_categoria_proveedor.get()
		telProveedor = entry_telefono_proveedor.get()
		insumosProveedor = entry_insumo_proveedor.get()
		domicilioProveedor = entry_domicilio_proveedor.get()
		cpProveedor = entry_cp_proveedor.get()
		emailProveedor = entry_mail_proveedor.get()
		ivaProveedor = entry_iva_proveedor.get()

		datos = (cuitProveedor,nombre,
			    categoriaProveedor,telProveedor,
			    insumosProveedor,domicilioProveedor,
			    cpProveedor,emailProveedor,
			    ivaProveedor,idProveedor)

		tabla=conexion.cursor()
		tabla.execute("UPDATE proveedores SET cuitProveedor=?,nombre=?,categoriaProveedor =?,telProveedor=?,insumosProveedor=?,domicilioProveedor=?,cpProveedor=?,emailProveedor=?,ivaProveedor=? WHERE idProveedor =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Modificado con éxito")
		combo.pack_forget()
		limpiar_proveedores()
		boton_guardar_proveedor.config(state="normal")
	boton_modificar_proveedores=ttk.Button(frame_proveedores,text="MODIFICAR",style="botonNavegacion.TButton",command=modificar_proveedores)                                   
	boton_modificar_proveedores.pack(side=LEFT,padx=20,pady=20)

	def guardar_proveedores():
		cuitProveedor = entry_cuit_proveedor.get()
		nombre = entry_nombre_proveedor.get()
		categoriaProveedor = entry_categoria_proveedor.get()
		telProveedor = entry_telefono_proveedor.get()
		insumosProveedor = entry_insumo_proveedor.get()
		domicilioProveedor = entry_domicilio_proveedor.get()
		cpProveedor = entry_cp_proveedor.get()
		emailProveedor = entry_mail_proveedor.get()
		ivaProveedor = entry_iva_proveedor.get()

		if(cuitProveedor != "" and nombre != "" and categoriaProveedor != "" and telProveedor != "" and 
			insumosProveedor != "" and domicilioProveedor != "" and cpProveedor !=""and emailProveedor!= ""and ivaProveedor!=""):
			boton_modificar_proveedores.config(state="disable")

			datos = (cuitProveedor,nombre,categoriaProveedor,telProveedor,insumosProveedor,
				      domicilioProveedor,cpProveedor,emailProveedor,ivaProveedor)

			tabla = conexion.cursor()
			tabla.execute("INSERT INTO proveedores(cuitProveedor,nombre,categoriaProveedor,telProveedor,insumosProveedor,domicilioProveedor,cpProveedor,emailProveedor,ivaProveedor)VALUES(?,?,?,?,?,?,?,?,?)",datos)
			conexion.commit()
			messagebox.showinfo("LifeHealth","Guardado con éxito")
			limpiar_proveedores()
			boton_modificar_proveedores.config(state="normal")
		else:
			messagebox.showwarning("LifeHealth","Complete todos los campos")
	boton_guardar_proveedor = ttk.Button(frame_proveedores,text="GUARDAR",style="botonNavegacion.TButton",command = guardar_proveedores)
	boton_guardar_proveedor.pack(side=LEFT,padx=20,pady=20)

	def eliminar_proveedores():
		boton_guardar_proveedor.config(state="normal")
		idProveedor = entry_numero_proveedor.get()
		datos = (idProveedor,)
		tabla=conexion.cursor()
		tabla.execute("DELETE FROM proveedores WHERE idProveedor =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Eliminado con éxito")
		combo.pack_forget()
		limpiar_proveedores()
	boton_eliminar_proveedores = ttk.Button(frame_proveedores,text="ELIMINAR",style="botonNavegacion.TButton",command = eliminar_proveedores)
	boton_eliminar_proveedores.pack(side=LEFT,padx=20,pady=20)
	boton_eliminar_proveedores.config(state="disabled")

	def limpiar_proveedores():
		entry_busqueda_proveedores.delete(0,END)
		entry_numero_proveedor.config(state="normal")
		entry_numero_proveedor.delete(0,END)
		entry_numero_proveedor.config(state="readonly")
		entry_cuit_proveedor.delete(0,END)
		entry_nombre_proveedor.delete(0,END)
		entry_categoria_proveedor.delete(0,END)
		entry_telefono_proveedor.delete(0,END)
		entry_insumo_proveedor.delete(0,END)
		entry_domicilio_proveedor.delete(0,END)
		entry_cp_proveedor.delete(0,END)
		entry_mail_proveedor.delete(0,END)
		entry_iva_proveedor.delete(0,END)
		
		boton_guardar_proveedor.config(state="normal")
		boton_modificar_proveedores.config(state="disable")
		boton_eliminar_proveedores.config(state="disable")
		combo.pack_forget()
	boton_limpiar_proveedores = ttk.Button(frame_proveedores,text="LIMPIAR",style="botonNavegacion.TButton",command = limpiar_proveedores)
	boton_limpiar_proveedores.pack(side=LEFT,padx=20,pady=20)

	def volverPrincipalProveedor():

		global imagen_pil_volver_proveedor
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_proveedor= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_proveedor = imagen_pil_volver_proveedor.resize((30,30))
	imagen_tk_volver_proveedor= ImageTk.PhotoImage(imagen_resize_volver_proveedor)

	boton_volver_proveedor = ttk.Button(frame_proveedores,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalProveedor)
	boton_volver_proveedor.config(image=imagen_tk_volver_proveedor,compound=LEFT)
	boton_volver_proveedor.image = imagen_tk_volver_proveedor
	boton_volver_proveedor.pack(side=LEFT,padx=20,pady=20)
	
def empleados(frame_contenido):
	global frame_empleados
	global combo
	frame_empleados = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_empleados.pack(fill=BOTH,expand=1)

	frame_buscador_empleados=ttk.Frame(frame_empleados,style="fondo.TFrame")
	frame_buscador_empleados.pack(fill=X,pady=40)
	frame_datos_empleados=ttk.Frame(frame_buscador_empleados,style="principal.TFrame")
	frame_datos_empleados.pack(fill=X,expand=1,padx=30)
	frame_buscado_empleados=ttk.Frame(frame_empleados,style="navegacion.TFrame")
	frame_buscado_empleados.pack(ipadx=150,ipady=30,padx=30,pady=40)
	
	label_busqueda_empleados=ttk.Label(frame_datos_empleados,text="Buscar por nombre",style="labelNavegacion.TLabel")
	label_busqueda_empleados.pack(side=LEFT,padx=20,pady=20)
	entry_busqueda_empleados=ttk.Entry(frame_datos_empleados,style="entradasNavegacion2.TLabel",width=35)
	entry_busqueda_empleados.pack(side=LEFT,padx=10,pady=20)

	combo = ttk.Combobox(frame_datos_empleados)

	label_datos_empleados=ttk.Label(frame_buscado_empleados,text="Datos del empleado",style="subTitulo.TLabel")
	label_datos_empleados.grid(row=1,column=1,pady=35,padx=10,sticky=W)

	label_legajo_empleados=ttk.Label(frame_buscado_empleados,text="N Legajo°",style="labelNavegacion.TLabel",)
	label_legajo_empleados.grid(row=1,column=2,pady=35,padx=5)
	entry_legajo_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=30)
	entry_legajo_empleados.grid(row=1,column=3,ipady=5,pady=35,padx=5,sticky=W)
	entry_legajo_empleados.config(state="readonly")

	label_cuit_empleados=ttk.Label(frame_buscado_empleados,text="CUIT",style="labelNavegacion.TLabel")
	label_cuit_empleados.grid(row=2,column=1,pady=5,padx=10,sticky=W)
	entry_cuit_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=20,validate= "key",validatecommand=vcmd)
	entry_cuit_empleados.grid(row=2,column=2,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)

	label_nombre_empleados=ttk.Label(frame_buscado_empleados,text="Nombre Completo",style="labelNavegacion.TLabel")
	label_nombre_empleados.grid(row=3,column=1,pady=5,padx=10,sticky=W)
	entry_nombre_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=35)
	entry_nombre_empleados.grid(row=3,column=2,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)

	label_dni_empleados=ttk.Label(frame_buscado_empleados,text="DNI",style="labelNavegacion.TLabel")
	label_dni_empleados.grid(row=4,column=1,pady=5,padx=10,sticky=W)
	entry_dni_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=15,validate= "key",validatecommand=vcmd)
	entry_dni_empleados.grid(row=4,column=2,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)

	label_civil_empleados=ttk.Label(frame_buscado_empleados,text="Estado Civil",style="labelNavegacion.TLabel")
	label_civil_empleados.grid(row=5,column=1,pady=5,padx=10,sticky=W)
	entry_civil_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=15)
	entry_civil_empleados.grid(row=5,column=2,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)

	label_hijos_empleados=ttk.Label(frame_buscado_empleados,text="Hijos:SI/NO",style="labelNavegacion.TLabel")
	label_hijos_empleados.grid(row=6,column=1,pady=5,padx=10,sticky=W)
	entry_hijos_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=5)
	entry_hijos_empleados.grid(row=6,column=2,ipady=5,ipadx=5,pady=10,padx=10,sticky=W)

	label_nacionalidad_empleados=ttk.Label(frame_buscado_empleados,text="Nacionalidad",style="labelNavegacion.TLabel")
	label_nacionalidad_empleados.grid(row=2,column=4,pady=5,padx=5,sticky=W)
	entry_nacionalidad_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=10)
	entry_nacionalidad_empleados.grid(row=2,column=5,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)
	
	label_telefono_empleados=ttk.Label(frame_buscado_empleados,text="Teléfono contacto:Prefijo sin 0 y 15",style="labelNavegacion.TLabel")
	label_telefono_empleados.grid(row=3,column=4,pady=5,padx=10,sticky=W)
	entry_legajo_empleados.config(state="disabled")
	entry_tel_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=15,validate= "key",validatecommand=vcmd)
	entry_tel_empleados.grid(row=3,column=5,ipady=5,ipadx=5,pady=5,padx=10,sticky=W)

	label_domicilio_empleados=ttk.Label(frame_buscado_empleados,text="Domicilio",style="labelNavegacion.TLabel")
	label_domicilio_empleados.grid(row=4,column=4,pady=5,padx=5,sticky=W)
	entry_domicilio_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=35)
	entry_domicilio_empleados.grid(row=4,column=5,ipady=5,ipadx=5,pady=10,padx=5,sticky=W)

	label_mail_empleados=ttk.Label(frame_buscado_empleados,text="E-mail",style="labelNavegacion.TLabel")
	label_mail_empleados.grid(row=5,column=4,pady=5,padx=5,sticky=W)
	entry_mail_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=30)
	entry_mail_empleados.grid(row=5,column=5,ipady=5,ipadx=5,pady=5,padx=5,sticky=W)

	label_contrato_empleados=ttk.Label(frame_buscado_empleados,text="Tipo de contratación",style="labelNavegacion.TLabel")
	label_contrato_empleados.grid(row=6,column=4,pady=5,padx=5,sticky=W)
	entry_contrato_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=20)
	entry_contrato_empleados.grid(row=6,column=5,ipady=5,ipadx=5,pady=5,padx=5,sticky=W)

	label_rol_empleados=ttk.Label(frame_buscado_empleados,text="Rol",style="labelNavegacion.TLabel")
	label_rol_empleados.grid(row=7,column=4,pady=5,padx=5,sticky=W)
	entry_rol_empleados=ttk.Entry(frame_buscado_empleados,style="entradasNavegacion.TLabel",width=20)
	entry_rol_empleados.grid(row=7,column=5,ipady=5,ipadx=5,pady=5,padx=5,sticky=W)



	def seleccionarComboEmpleado(evento):
		frame_buscado_empleados.pack()           
		indiceEmpleado=combo.current()
		empleado=datos[indiceEmpleado]

		entry_legajo_empleados.config(state="normal")

		entry_legajo_empleados.delete(0,END)
		entry_cuit_empleados.delete(0,END)
		entry_nombre_empleados.delete(0,END)
		entry_dni_empleados.delete(0,END)
		entry_civil_empleados.delete(0,END)
		entry_hijos_empleados.delete(0,END)
		entry_nacionalidad_empleados.delete(0,END)
		entry_tel_empleados.delete(0,END)
		entry_domicilio_empleados.delete(0,END)
		entry_mail_empleados.delete(0,END)
		entry_contrato_empleados.delete(0,END)
		entry_legajo_empleados.insert(END,empleado[0])
		entry_cuit_empleados.insert(END,empleado[1])
		entry_nombre_empleados.insert(END,empleado[2])
		entry_dni_empleados.insert(END,empleado[3])
		entry_civil_empleados.insert(END,empleado[4])
		entry_hijos_empleados.insert(END,empleado[5])
		entry_nacionalidad_empleados.insert(END,empleado[6])
		entry_tel_empleados.insert(END,empleado[7])
		entry_domicilio_empleados.insert(END,empleado[8])
		entry_mail_empleados.insert(END,empleado[9])
		entry_contrato_empleados.insert(END,empleado[10])
		entry_rol_empleados.insert(END,empleado[11])

	combo.bind("<<ComboboxSelected>>",seleccionarComboEmpleado)

	def buscar_empleado():

		global combo
		boton_eliminar_empleado.config(state="normal")
		boton_modificar_empleado.config(state="normal")

		busquedaEmpleado=entry_busqueda_empleados.get()

		if(busquedaEmpleado != ""):
			try:
				ver=True
				for letra in busquedaEmpleado:
					if(letra.isdigit()):
						ver=False
						break
				if(ver):
					combo.pack_forget()
					busquedaEmpleado=(entry_busqueda_empleados.get(),)
					tabla=conexion.cursor()
					tabla.execute("SELECT * FROM empleados WHERE nombreEmpleados=?",busquedaEmpleado)             
					global datos
					datos=tabla.fetchall()
					if(len(datos)>0):
						combo.pack(side=TOP,fill=X,padx=10,pady=10)
						lista=[]
						for dato in datos:
							lista.append("Nombre de empleado:"+" "+dato[2])
						combo.config(values=lista)
						combo.current(0)
						boton_guardar_empleado.config(state="disabled")
					else:
						messagebox.showerror("LifeHealth","No se ha encontrado empleado")
						limpiar_empleados()
						combo.pack_forget()
				else:
					messagebox.showwarning("LifeHealth","Buscar por nombre!")

			except sqlite3.Error as e:
				messagebox.showerror("Registro incorrecto",{e})

		else:
			messagebox.showwarning(title="LifeHealth",message="Ingrese algo que buscar")	
			
	boton_buscar_empleado=ttk.Button(frame_datos_empleados,text="Buscar",style="botonNavegacion.TButton",command=buscar_empleado)
	boton_buscar_empleado.pack(side=LEFT,padx=60)

	def modificar_empleados():
		legajoEmpleados = entry_legajo_empleados.get()
		cuitEmpleados = entry_cuit_empleados.get()
		nombreEmpleados = entry_nombre_empleados.get()
		dniEmpleados = entry_dni_empleados.get()
		civilEmpleados = entry_civil_empleados.get()
		hijosEmpleados = entry_hijos_empleados.get()
		nacionalidadEmpleados = entry_nacionalidad_empleados.get()
		telEmpleados = entry_tel_empleados.get()
		domicilioEmpleados = entry_domicilio_empleados.get()
		emailEmpleados = entry_mail_empleados.get()
		contratoEmpleados = entry_contrato_empleados.get()
		rolEmpleados = entry_rol_empleados.get()

		datos = (cuitEmpleados,nombreEmpleados,
			    dniEmpleados,civilEmpleados,
			    hijosEmpleados,nacionalidadEmpleados,
			    telEmpleados,domicilioEmpleados,
			    emailEmpleados,contratoEmpleados,rolEmpleados,legajoEmpleados)

		tabla=conexion.cursor()
		tabla.execute("UPDATE empleados SET cuitEmpleados=?,nombreEmpleados=?,dniEmpleados =?,civilEmpleados=?,hijosEmpleados=?,nacionalidadEmpleados=?,telEmpleados=?,domicilioEmpleados=?,emailEmpleados=?,contratoEmpleados=?,rolEmpleados=? WHERE legajoEmpleados =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Modificado con éxito")
		combo.pack_forget()
		limpiar_empleados()
		boton_guardar_empleado.config(state="normal")
		
	boton_modificar_empleado = ttk.Button(frame_empleados,text="MODIFICAR",style="botonNavegacion.TButton",command = modificar_empleados)
	boton_modificar_empleado.pack(side=LEFT,padx=20,pady=10)
	
		
	def guardar_empleados():
		cuitEmpleados = entry_cuit_empleados.get()
		nombreEmpleados = entry_nombre_empleados.get()
		dniEmpleados = entry_dni_empleados.get()
		civilEmpleados = entry_civil_empleados.get()
		hijosEmpleados = entry_hijos_empleados.get()
		nacionalidadEmpleados = entry_nacionalidad_empleados.get()
		telEmpleados = entry_tel_empleados.get()
		domicilioEmpleados = entry_domicilio_empleados.get()
		emailEmpleados = entry_mail_empleados.get()
		contratoEmpleados = entry_contrato_empleados.get()
		rolEmpleados = entry_rol_empleados.get()

		if(cuitEmpleados != "" and nombreEmpleados != "" and dniEmpleados != "" and civilEmpleados != "" and 
			hijosEmpleados != "" and nacionalidadEmpleados != "" and telEmpleados !=""and domicilioEmpleados!= ""and emailEmpleados!="" and contratoEmpleados != "" and rolEmpleados !=""):
			boton_modificar_empleado.config(state="disable")

			datos = (cuitEmpleados,nombreEmpleados,dniEmpleados,civilEmpleados,hijosEmpleados,
				      nacionalidadEmpleados,telEmpleados,domicilioEmpleados,emailEmpleados,contratoEmpleados,rolEmpleados)
			tabla = conexion.cursor()
			tabla.execute("INSERT INTO empleados(cuitEmpleados,nombreEmpleados,dniEmpleados,civilEmpleados,hijosEmpleados,nacionalidadEmpleados,telEmpleados,domicilioEmpleados,emailEmpleados,contratoEmpleados,rolEmpleados)VALUES(?,?,?,?,?,?,?,?,?,?,?)",datos)
			conexion.commit()
			messagebox.showinfo("LifeHealth","Guardado con éxito")
			limpiar_empleados()
			boton_modificar_empleado.config(state="normal")
		else:
			messagebox.showwarning("LifeHealth","Complete todos los campos")

	boton_guardar_empleado = ttk.Button(frame_empleados,text="GUARDAR",style="botonNavegacion.TButton",command = guardar_empleados)
	boton_guardar_empleado.pack(side=LEFT,padx=20,pady=10)

	def eliminar_empleados():
		boton_guardar_empleado.config(state="normal")
		legajoEmpleados = entry_legajo_empleados.get()
		datos = (legajoEmpleados,)
		tabla=conexion.cursor()
		tabla.execute("DELETE FROM empleados WHERE legajoEmpleados =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Eliminado con éxito")
		combo.pack_forget()
		limpiar_empleados()
		
	boton_eliminar_empleado = ttk.Button(frame_empleados,text="ELIMINAR",style="botonNavegacion.TButton",command = eliminar_empleados)
	boton_eliminar_empleado.pack(side=LEFT,padx=20,pady=10)
	boton_eliminar_empleado.config(state="disabled")

	def limpiar_empleados():
		entry_busqueda_empleados.delete(0,END)
		entry_legajo_empleados.config(state="normal")
		entry_legajo_empleados.delete(0,END)
		entry_legajo_empleados.config(state="readonly")
		entry_cuit_empleados.delete(0,END)
		entry_nombre_empleados.delete(0,END)
		entry_dni_empleados.delete(0,END)
		entry_civil_empleados.delete(0,END)
		entry_hijos_empleados.delete(0,END)
		entry_nacionalidad_empleados.delete(0,END)
		entry_tel_empleados.delete(0,END)
		entry_domicilio_empleados.delete(0,END)
		entry_mail_empleados.delete(0,END)
		entry_contrato_empleados.delete(0,END)
		entry_rol_empleados.delete(0,END)

		boton_guardar_empleado.config(state="normal")
		boton_modificar_empleado.config(state="disable")
		boton_eliminar_empleado.config(state="disable")
		combo.pack_forget()
	boton_limpiar_empleado = ttk.Button(frame_empleados,text="LIMPIAR",style="botonNavegacion.TButton",command = limpiar_empleados)
	boton_limpiar_empleado.pack(side=LEFT,padx=20,pady=10)

	def volverPrincipalEmpleados():
		global imagen_pil_volver_empleado
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		

	imagen_pil_volver_empleado= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_empleado = imagen_pil_volver_empleado.resize((30,30))
	imagen_tk_volver_empleado= ImageTk.PhotoImage(imagen_resize_volver_empleado)

	boton_volver_empleado = ttk.Button(frame_empleados,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalEmpleados)
	boton_volver_empleado.config(image=imagen_tk_volver_empleado,compound=LEFT)
	boton_volver_empleado.image = imagen_tk_volver_empleado
	boton_volver_empleado.pack(side=LEFT,padx=20,pady=10)
	
def pedidos(frame_contenido):
	#DateEntry(ventana_editar,font="Georgia 14 bold",date_pattern="yyyy-mm-dd"
	
	global proveedor
	global producto
	global cantidad
	
	db_nombre ="Bd/LifeHealth.db"	
	
	def rutas(ruta):
		try:
			rutabase=sys.__MEIPASS
		except Exception:
			rutabase=os.path.abspath(".")
		return os.path.join(rutabase,ruta)

	global label_hora
	global label_fecha
	
	#Frame:

	frame_pedidos = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_pedidos.pack(fill=BOTH,expand=1)

	frame_contenido_pedidos = ttk.Frame(frame_pedidos,style="navegacion.TFrame")
	frame_contenido_pedidos.pack(side=LEFT,fill=Y,ipadx=50)

	frame_tree_pedidos= ttk.Frame(frame_pedidos,style="navegacion.TFrame")
	frame_tree_pedidos.place(x=600,y=60,width=620,height=450)

	#Contenido:

	label_compras = LabelFrame(frame_contenido_pedidos,text="Registrar pedidos",bg="SkyBlue4",font="Georgia,Bold,15")
	label_compras.pack(anchor=NW,padx=10,pady=20)
	ruta=rutas(r"iconos/calendario.png")
	
	#Etiqueta para fecha y hora actual

	imagen_pil_calendario_pedidos = Image.open(ruta)
	imagen_resize_calendario_pedidos = imagen_pil_calendario_pedidos.resize((30, 30))
	imagen_tk_calendario_pedidos = ImageTk.PhotoImage(imagen_resize_calendario_pedidos)

	label_fecha = ttk.Label(label_compras,style="labelNavegacion.TLabel")
	label_fecha.config(image=imagen_tk_calendario_pedidos, compound=LEFT)
	label_fecha.image = imagen_tk_calendario_pedidos
	label_fecha.pack(anchor=NE,padx=10,pady=10)

	ruta=rutas(r"iconos/hora.png")
	imagen_pil_hora_pedido = Image.open(ruta)
	imagen_resize_hora_pedido = imagen_pil_hora_pedido.resize((30, 30))
	imagen_tk_hora_pedido = ImageTk.PhotoImage(imagen_resize_hora_pedido)

	label_hora = ttk.Label(label_compras, text="", style="labelNavegacion.TLabel")
	label_hora.config(image=imagen_tk_hora_pedido, compound=LEFT)
	label_hora.image = imagen_tk_hora_pedido
	label_hora.pack(anchor=NE,padx=10,pady=10)

	def actualizar_fecha_y_hora():

		#Obtener fecha y hora actual
		fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
		hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

		#Actualiza las etiquetas
		label_fecha.config(text=fecha_actual)
		label_hora.config(text=hora_actual)

		# Llamar a este método nuevamente después de 1000 ms (1 segundo)
		ventana_principal.after(1000, actualizar_fecha_y_hora)

	actualizar_fecha_y_hora()

	# Variable para mantener el número de pedido actual
 
	numero_pedido = 1

	lblpedido = ttk.Label(label_compras, text="N° Pedido: ",style="labelNavegacion.TLabel")
	lblpedido.pack(anchor=NW,padx=10,pady=5)
	entry_pedido = ttk.Label(label_compras, text="", style="labelNavegacion.TLabel",relief="groove",width=20)
	entry_pedido.pack(anchor=NW,padx=10,pady=5)
	entry_pedido.config(text=str(numero_pedido))
	
	def actualizar_numero_pedido():
		try:
		
			conexion = sqlite3.connect(db_nombre)
			cursor = conexion.cursor()# Obtener el último número de pedido registrado en la base de datos
			cursor.execute("SELECT MAX(numero_pedido) FROM pedidos")
			ultimo_pedido = cursor.fetchone()[0]
			return ultimo_pedido +1 if ultimo_pedido is not None else 1 
		except sqlite3.Error as e:
			messagebox.showerror("Error obteniendo el número de pedido actual:", e)
			return 1
		
		conexion.close() 
		
	actualizar_numero_pedido()  # Actualizar el número de pedido inicial

	lblproveedor = ttk.Label(label_compras,text="Proveedor:",style='labelNavegacion.TLabel')
	lblproveedor.pack(anchor=NW,padx=10,pady=5)
	entry_proveedor = ttk.Combobox(label_compras,style='labelNavegacion.TLabel',state="readonly")
	entry_proveedor.pack(anchor=NW,padx=10,pady=5)

	def cargar_proveedores():
		global proveedor
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT nombre FROM proveedores")
			proveedores = c.fetchall()
			nombres_proveedores = [proveedor[0] for proveedor in proveedores]
			entry_proveedor["values"] = nombres_proveedores
			conexion.close()
		except sqlite3.Error as e:
			messagebox.showerror("LifeHealth","Error cargando proveedores:", e)
	
	cargar_proveedores()

	lblproducto = ttk.Label(label_compras,text="Producto:",style='labelNavegacion.TLabel')
	lblproducto.pack(anchor=NW,padx=10,pady=5)
	entry_producto = ttk.Combobox(label_compras,style='labelNavegacion.TLabel',width=20,state="readonly")
	entry_producto.pack(anchor=NW,padx=10,pady=5)

	def cargar_productos():
		global producto
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT nombre FROM inventario")
			productos = c.fetchall()
			entry_producto["values"] = [producto[0] for producto in productos]
			conexion.close()
		except sqlite3.Error as e:
			messagebox.showerror("LifeHealth","Error cargando productos:", e)

	cargar_productos()

	lblcantidad = ttk.Label(label_compras,text="Cantidad:",style='labelNavegacion.TLabel')
	lblcantidad.pack(anchor=NW,padx=10,pady=5)
	entry_cantidad = ttk.Entry(label_compras,style='labelNavegacion.TLabel',width=20,validate= "key",validatecommand=vcmd)
	entry_cantidad.pack(anchor=NW,padx=10,pady=5)

	#Barras de desplazamiento vertical y horizontal

	scrol_y = ttk.Scrollbar(frame_tree_pedidos)
	scrol_y.pack(side=RIGHT, fill=Y)
	scrol_x = ttk.Scrollbar(frame_tree_pedidos, orient=HORIZONTAL)
	scrol_x.pack(side=BOTTOM, fill=X)

	#Treeview:

	treeview = ttk.Treeview(frame_tree_pedidos, columns=("N° Pedido", "Proveedor", "Producto", "Cantidad", "Fecha", "Hora"), show="headings")
	treeview.pack(expand=True, fill=BOTH)

	scrol_y.config(command=treeview.yview)
	scrol_x.config(command=treeview.xview)

	#Configuaracion de columnas:

	treeview.heading("N° Pedido", text="N° Pedido")
	treeview.heading("Proveedor", text="Proveedor")
	treeview.heading("Producto", text="Producto")
	treeview.heading("Cantidad", text="Cantidad")
	treeview.heading("Fecha", text="Fecha")
	treeview.heading("Hora", text="Hora")

	#Establecer ancho de columnas

	treeview.column("N° Pedido", width=80,anchor="center")
	treeview.column("Proveedor", width=100,anchor="center")
	treeview.column("Producto", width=100,anchor="center")
	treeview.column("Cantidad", width=100,anchor="center")
	treeview.column("Fecha", width=100,anchor="center")
	treeview.column("Hora", width=100,anchor="center")
	
	
	def agregar_pedido_a_treeview(proveedor, producto, cantidad):

		# Obtener el número de pedido actual
		n_pedido = numero_pedido  
		# Obtener la fecha y hora actual
		fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
		hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

		# Insertar los datos del pedido en el Treeview con el mismo número de pedido
		
		treeview.insert("", "end", values=(n_pedido, proveedor, producto, cantidad, fecha_actual, hora_actual))


	def agregar_pedido():# obtener los datos del pedido, como el proveedor, producto y cantidad
		global proveedor
		global producto
		global cantidad

		# Aquí  obtener los datos del pedido, como el proveedor, producto y cantidad
        
		proveedor =entry_proveedor.get()
		producto = entry_producto.get() 
		cantidad = entry_cantidad.get() 

		 # Verificar si se han ingresado todos los datos necesarios

		if proveedor  and producto and cantidad :

			# Llamar a la función para agregar el pedido al Treeview
			
			agregar_pedido_a_treeview(proveedor, producto, cantidad)

			# Limpiar los campos después de agregar el pedido
			
			entry_proveedor.set("")  # Limpiar el proveedor seleccionado
			entry_producto.set("")    # Limpiar el producto seleccionado
			entry_cantidad.delete(0, "end")  # Limpiar la cantidad ingresada
		else:
			messagebox.showerror("Error", "Por favor, complete todos los campos.")

	ruta=rutas(r"iconos/agregar.png")
	imagen_pil_agregar_pedidos = Image.open(ruta)
	imagen_resize_agregar_pedidos = imagen_pil_agregar_pedidos.resize((30, 30))
	imagen_tk_agregar_pedidos = ImageTk.PhotoImage(imagen_resize_agregar_pedidos)


	boton_agregar_pedido = ttk.Button(label_compras,text="AGREGAR",style="botonNavegacion.TButton",command = agregar_pedido)
	boton_agregar_pedido.config(image=imagen_tk_agregar_pedidos,compound=LEFT)
	boton_agregar_pedido.image = imagen_tk_agregar_pedidos
	boton_agregar_pedido.pack(anchor=NW,padx=10,pady=5)

	def registrar_pedido():

		#Conexion b.d

		conexion = sqlite3.connect(db_nombre)
		cursor = conexion.cursor()

		# Recorrer los elementos del Treeview y guardarlos en la base de datos
		
		for child in treeview.get_children():
			pedido = treeview.item(child)['values']
			numero_pedido, proveedor, producto, cantidad, fecha, hora = pedido # Insertar el pedido en la tabla 'pedidos'
			
			#Insertar pedido en la tabala "pedidos"

			cursor.execute("INSERT INTO pedidos (numero_pedido, proveedor, producto, cantidad, fecha, hora) VALUES (?, ?, ?, ?, ?, ?)", pedido)

			# Actualizar el stock en la tabla "inventario"
			
			cursor.execute("UPDATE inventario SET stock = stock + ? WHERE nombre = ?", (cantidad, producto))# Confirmar la transacción y cerrar la conexión
		
		#Confirmo y cierro conexion

		conexion.commit()
		conexion.close() 

		# Limpiar el Treeview
		for item in treeview.get_children():
			treeview.delete(item)
		
		#treeview.delete(treeview.get_children())

		# Mostrar un mensaje de confirmación
		
		messagebox.showinfo("Pedido registrado", "El pedido ha sido registrado exitosamente.") # Actualizar la visualización del número de pedido

		# Actualizar la visualización del número de pedido

		actualizar_numero_pedido()

	ruta=rutas(r"iconos/rpedido.png")
	imagen_pil_registrar_pedidos = Image.open(ruta)
	imagen_resize_registrar_pedidos = imagen_pil_registrar_pedidos.resize((30, 30))
	imagen_tk_registrar_pedidos = ImageTk.PhotoImage(imagen_resize_registrar_pedidos)

	boton_registrar_pedido = ttk.Button(label_compras,text="REGISTRAR",style="botonNavegacion.TButton",command = registrar_pedido)
	boton_registrar_pedido.config(image=imagen_tk_registrar_pedidos,compound=LEFT)
	boton_registrar_pedido.image = imagen_tk_registrar_pedidos
	boton_registrar_pedido.pack(anchor=NW,padx=10,pady=5)

	
	def ver_pedidos():

		# Crear el Toplevel(nueva ventana)
		
		top_pedidos = Toplevel()
		top_pedidos.title("Lista de Pedidos Registrados")
		top_pedidos.geometry("800x600")  # Definir el tamaño del Toplevel
		top_pedidos.config(bg="SkyBlue4")  # Configurar el color de fondo del Toplevel 

		# Crear el Label "Pedidos Registrados"
		
		label_pedidos = ttk.Label(top_pedidos, text="Pedidos Registrados",style="labelNavegacion.TLabel")
		label_pedidos.pack(pady=10) 

		# Crear el Treeview
		
		tree_pedidos = ttk.Treeview(top_pedidos, show="headings")
		tree_pedidos['columns'] = ('N° Pedido', 'Proveedor', 'Producto', 'Cantidad', 'Fecha', 'Hora')
		tree_pedidos.column("#0", anchor='center', width=100)
		tree_pedidos.column('#1', anchor='center', width=100)
		tree_pedidos.column('#2', anchor='center', width=100)
		tree_pedidos.column('#3', anchor='center', width=100)
		tree_pedidos.column('#4', anchor='center', width=100)
		tree_pedidos.column('#5', anchor='center', width=150)
		tree_pedidos.column('#6', anchor='center', width=150)#tree_pedidos.heading("#0", text='ID')
		
		tree_pedidos.heading('#1', text='N° Pedido')
		tree_pedidos.heading('#2', text='Proveedor')
		tree_pedidos.heading('#3', text='Producto')
		tree_pedidos.heading('#4', text='Cantidad')
		tree_pedidos.heading('#5', text='Fecha')
		tree_pedidos.heading('#6', text='Hora')# Obtener datos de la base de datos

		#Obtener datos de b.d

		conexion = sqlite3.connect(db_nombre)
		cursor = conexion.cursor()
		cursor.execute("SELECT * FROM pedidos")
		filas = cursor.fetchall()
		
		for fila in filas:
			tree_pedidos.insert('', 'end', text=fila[0], values=fila[1:])
		conexion.close()

		# Ubicar el Treeview en el Toplevel usando place 

		tree_pedidos.place(x=50, y=100, width=700, height=450)  

		# configurar Treeview con barras de desplazamiento vertical
		
		scroll_y_pedidos = ttk.Scrollbar(top_pedidos, orient='vertical', command=tree_pedidos.yview)
		scroll_y_pedidos.place(x=750, y=100, height=450)  # Ubicar la barra de desplazamiento vertical
		tree_pedidos.config(yscrollcommand=scroll_y_pedidos.set)
	
	ruta=rutas(r"iconos/verpedidos.png")
	imagen_pil_ver_pedidos = Image.open(ruta)
	imagen_resize_ver_pedidos = imagen_pil_ver_pedidos.resize((30, 30))
	imagen_tk_ver_pedidos = ImageTk.PhotoImage(imagen_resize_ver_pedidos)

	
	boton_ver_pedido = ttk.Button(label_compras,text="Ver pedidos",style="botonNavegacion.TButton",command = ver_pedidos)
	boton_ver_pedido.config(image=imagen_tk_ver_pedidos,compound=LEFT)
	boton_ver_pedido.image = imagen_tk_ver_pedidos
	boton_ver_pedido.pack(anchor=NW,padx=10,pady=5)
	
	
	def volverPrincipalCompras():

		global imagen_pil_volver_compras
		borrarFrames()
		frame_pedidos.pack_forget()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_compras= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_compras = imagen_pil_volver_compras.resize((30,30))
	imagen_tk_volver_compras= ImageTk.PhotoImage(imagen_resize_volver_compras)

	boton_volver_compras = ttk.Button(label_compras,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalCompras)
	boton_volver_compras.config(image=imagen_tk_volver_compras,compound=LEFT)
	boton_volver_compras.image = imagen_tk_volver_compras
	boton_volver_compras.pack(anchor=NW,padx=10,pady=5)
	
def ventas(frame_contenido):
	
	db_nombre= "Bd/LifeHealth.db"
	
	global frame_ventas
	global label_fecha
	global label_hora
	global label_fecha
	global label_hora
	global numero_factura
	global entry_cliente
	global fecha_actual
	global hora_actual
	global numero_factura
	
	global productos_seleccionados
	productos_seleccionados=[]

	#Ruta imagenes:
	
	def rutas(ruta):
		try:
			rutabase=sys.__MEIPASS
		except Exception:
			rutabase=os.path.abspath(".")
		return os.path.join(rutabase,ruta)	

	#Frames:	


	frame_ventas = ttk.Frame(frame_contenido,style="frameSecundarios.TFrame")#Frame de contrenido Label y Entry
	frame_ventas.pack(fill=BOTH,expand=1)

	frame_contenido_ventas2 = ttk.Frame(frame_ventas,style="frameSecundarios.TFrame")#Frame de contrenido Label y Entry
	frame_contenido_ventas2.pack(fill=BOTH,expand=1)

	frame_contenido_ventas = ttk.Frame(frame_ventas,style="frameSecundarios.TFrame")#Frame de contrenido Label y Entry
	frame_contenido_ventas.pack(fill=BOTH,expand=1)

	#Hora y fecha

	global label_hora
	global label_fecha

	ruta=rutas(r"iconos/calendario.png")# Crear etiqueta para mostrar la fecha actual
	imagen_pil_ventas2 = Image.open(ruta)
	imagen_resize_ventas2 = imagen_pil_ventas2.resize((30, 30))
	imagen_tk_ventas2 = ImageTk.PhotoImage(imagen_resize_ventas2)
	
	label_fecha = ttk.Label(frame_contenido_ventas2, style="labelNavegacion.TLabel")
	label_fecha.config(image=imagen_tk_ventas2, compound=LEFT)
	label_fecha.image = imagen_tk_ventas2
	label_fecha.place(x=900, y=15)
	
	ruta=rutas(r"iconos/hora.png")# Crear etiqueta para mostrar la hora actualizada
	imagen_pil_ventas3 = Image.open(ruta)
	imagen_resize_ventas3 = imagen_pil_ventas3.resize((30, 30))
	imagen_tk_ventas3 = ImageTk.PhotoImage(imagen_resize_ventas3)

	label_hora = ttk.Label(frame_contenido_ventas2, text="",style="labelNavegacion.TLabel")
	label_hora.config(image=imagen_tk_ventas3, compound=LEFT)
	label_hora.image = imagen_tk_ventas3
	label_hora.place(x=1150, y=15)

	def actualizar_fecha_y_hora():

		fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")# Obtener la fecha y hora actual
		hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
		label_fecha.config(text=fecha_actual)# Actualizar las etiquetas de fecha y hora
		label_hora.config(text=hora_actual)
		ventana_principal.after(1000, actualizar_fecha_y_hora)# Llamar a este método nuevamente después de 1000 ms (1 segundo)


	actualizar_fecha_y_hora()# Actualizar la fecha y la hora cada segundo


	#Datos

	labelFrame = LabelFrame(frame_contenido_ventas2,text="Ventas de productos",bg="SkyBlue4",font="Georgia 20 bold")  
	labelFrame.place(x=35,y=100, width=1300, height=200)

	global entry_cliente

	label_cliente = ttk.Label(labelFrame, text="Cliente:", style="labelNavegacion.TLabel")
	label_cliente.place(x=10, y=11)
	entry_cliente = ttk.Combobox(labelFrame, style="labelNavegacion.TLabel", state="readonly")
	entry_cliente.place(x=120, y=8, width=240, height=40)

	#Carga cliente

	def cargar_clientes():
		global entry_cliente
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT nombre FROM clientes")
			clientes = c.fetchall()
			nombres_clientes = [cliente[0] for cliente in clientes]
			entry_cliente["values"] = nombres_clientes
			conexion.close()
		except sqlite3.Error as e:
			messagebox.showerror("Error cargando clientes:", e)

	cargar_clientes()

	label_nombre = ttk.Label(labelFrame, text="Producto:",style="labelNavegacion.TLabel")
	label_nombre.place(x=10, y=70)
	entry_nombre = ttk.Combobox(labelFrame, style="labelNavegacion.TLabel", state="readonly")
	entry_nombre.place(x=120, y=66, width=240, height=40)

	#Carga producto

	def cargar_productos():
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT nombre FROM inventario")
			productos = c.fetchall()
			entry_nombre["values"] = [producto[0] for producto in productos]
			conexion.close()
		except sqlite3.Error as e:
			messagebox.showerror("Error cargando productos:", e)
	
	cargar_productos()

	label_cantidad = ttk.Label(labelFrame, text="Cantidad:",style="labelNavegacion.TLabel")
	label_cantidad.place(x=400, y=11)
	entry_cantidad = ttk.Entry(labelFrame, style="entradasNavegacion2.TLabel",validate= "key",validatecommand=vcmd)
	entry_cantidad.place(x=510, y=8, width=80, height=40)

	label_stock = ttk.Label(labelFrame, text="Stock:",style="labelNavegacion.TLabel")#Label para mostrar el stock del producto seleccionado
	label_stock.place(x=400, y=70)

	#Actualiza stock

	def actualizar_stock(event=None):
		global numero_factura
		global productos_seleccionados

		producto_seleccionado = entry_nombre.get()
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT stock FROM inventario WHERE nombre=?", (producto_seleccionado,))
			stock= c.fetchone()[0]
			conexion.close()
			label_stock.config(text=f"Stock: {stock}")
		except sqlite3.Error as e:
			messagebox.showerror("Error al obtener el stock del producto:", e)

	entry_nombre.bind("<<ComboboxSelected>>", actualizar_stock)  # Llamar a actualizar_stock cuando se seleccione un producto

	label_factura = ttk.Label(labelFrame, text="Número de Factura:",style="labelNavegacion.TLabel")
	label_factura.place(x=800, y=70)

	numero_factura=1

	#Actualiza n de factura

	def obtener_numero_factura_actual():
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT MAX(factura) FROM ventas")
			ultimo_numero_factura = c.fetchone()[0]
			conexion.close()
			return ultimo_numero_factura + 1 if ultimo_numero_factura is not None else 1
		except sqlite3.Error as e:
			messagebox.showerror("Error obteniendo el número de factura actual:", e)
			return 1
	numero_factura = obtener_numero_factura_actual()


	label_numero_factura = ttk.Label(labelFrame, text=f"{numero_factura}", style="labelNavegacion.TLabel")
	label_numero_factura.place(x=1010, y=70)

	label_precio_total = ttk.Label(frame_contenido_ventas, text="Precio a Pagar: $ 0 ",style="labelNavegacion.TLabel")
	label_precio_total.place(x=800, y=280)

	#crear Treeview

	treeFrame = ttk.Frame(frame_contenido_ventas, style="frameSecundarios.TFrame") 
	treeFrame.place(x=110, y=10, width=1100, height=250)
	
	tree = ttk.Treeview(treeFrame, columns=("Factura", "Cliente", "Producto", "Precio", "Cantidad", "Total"), show="headings")
	tree.heading("Factura", text="Factura")
	tree.heading("Cliente", text="Cliente")
	tree.heading("Producto", text="Producto")
	tree.heading("Precio", text="Precio")
	tree.heading("Cantidad", text="Cantidad")
	tree.heading("Total", text="Total")
	
	tree.column("Factura", width=70, anchor="center")
	tree.column("Cliente", width=300, anchor="center")
	tree.column("Producto", width=300, anchor="center")
	tree.column("Precio", width=120, anchor="center")
	tree.column("Cantidad", width=120, anchor="center")
	tree.column("Total", width=150, anchor="center")
	
	tree.config(height=25) 
	scrollbar = ttk.Scrollbar(treeFrame, orient="vertical", command=tree.yview)
	scrollbar.pack(side="right", fill="y")
	
	tree.configure(yscrollcommand=scrollbar.set)
	tree.pack()

	def agregar_articulo():
		global productos_seleccionados
		global cliente
		
		cliente = entry_cliente.get()
		producto =entry_nombre.get()
		cantidad = entry_cantidad.get()

		if not cliente:
			messagebox.showerror("Error", "Por favor seleccione un cliente.")
			return

		if not producto:
			messagebox.showerror("Error", "Por favor seleccione un producto.")
			return

		if not cantidad.isdigit() or int(cantidad) <= 0:
			messagebox.showerror("Error", "Por favor ingrese una cantidad válida.")
			return

		cantidad = int(cantidad)
		cliente = entry_cliente.get()

		try:
			conn = sqlite3.connect(db_nombre)
			c = conn.cursor()
			c.execute("SELECT precio, costo, stock FROM inventario WHERE nombre=?", (producto,))
			resultado = c.fetchone()

			if resultado is None:
				messagebox.showerror("Error", "Producto no encontrado.")
				return

			precio, costo, stock = resultado

			if cantidad > stock:
				messagebox.showerror("Error", f"Stock insuficiente. Solo hay {stock} unidades disponibles.")
				return

			total = precio * cantidad
			total_cop = "{:,.0f}  ".format(total)

			# Insertar el artículo en el Treeview con el número de factura actual
			tree.insert("", "end", values=(numero_factura, cliente, producto, "{:,.0f} ".format(precio), cantidad, total_cop))
			productos_seleccionados.append((numero_factura, cliente, producto, precio, cantidad, total_cop, costo))

			conn.close()
			# Limpiar Entry de cantidad y deseleccionar Combobox
			entry_cantidad.delete(0, 'end')
			entry_nombre.set('')
			# self.entry_cliente.set('')  # Limpiar la selección del cliente
		except sqlite3.Error as e:
			messagebox.showerror("Error al agregar artículo:", e)

		def calcular_precio_total():
			total_pagar = sum(float(tree.item(item)["values"][-1].replace(" ", "").replace(",", "")) for item in tree.get_children())
			total_pagar_arg = "{:,.0f}  ".format(total_pagar)
			label_precio_total.config(text=f"Precio a Pagar: $ {total_pagar_arg}")

		calcular_precio_total()  # Calcular el precio total después de agregar un artículo
	
	ruta=rutas(r"iconos/agregar.png")
	imagen_pil_ventas_agregar = Image.open(ruta)
	imagen_resize_ventas_agregar = imagen_pil_ventas_agregar.resize((30, 30))
	imagen_tk_ventas_agregar = ImageTk.PhotoImage(imagen_resize_ventas_agregar)
	boton_agregar = ttk.Button(labelFrame, text="Agregar Artículo",style="botonNavegacion.TButton", command=agregar_articulo)
	boton_agregar.config(image=imagen_tk_ventas_agregar, compound=LEFT)
	boton_agregar.image = imagen_tk_ventas_agregar
	boton_agregar.place(x=650, y=8,width=220, height=40)
	
	def realizar_pago():
		global productos_seleccionados
		if not tree.get_children():
			messagebox.showerror("Error", "No hay productos seleccionados para realizar el pago.")
			return
		total_venta = sum(float(item[5].replace(" ", "").replace(",", "")) for item in productos_seleccionados)

		# Formatear el total para agregar puntos en los miles
		total_formateado = "{:,.0f}".format(total_venta)
		
		# Crear una nueva ventana TopLevel para que el usuario ingrese el monto pagado
		ventana_pago = Toplevel()
		ventana_pago.title("Realizar pago")
		ventana_pago.geometry("400x400")
		ventana_pago.config(bg="SkyBlue4")
		ventana_pago.resizable(False, False)

		label_titulo = ttk.Label(ventana_pago, text="Realizar pago", style="labelNavegacion.TLabel")
		label_titulo.place(x=70, y=10)
		label_total = ttk.Label(ventana_pago, text=f"Total a pagar: $ {total_formateado} ", style="labelNavegacion.TLabel")
		label_total.place(x=80, y=100)
		label_monto = ttk.Label(ventana_pago, text="Ingrese el monto pagado:", style="labelNavegacion.TLabel")
		label_monto.place(x=80, y=160)
		entry_monto = ttk.Entry(ventana_pago, style="entradasNavegacion.TLabel",validate= "key",validatecommand=vcmd)
		entry_monto.place(x=80, y=210, width=240, height=40)

		def procesar_pago(cantidad_pagada, ventana_pago, total_venta):
			global productos_seleccionados
			cantidad_pagada =float(cantidad_pagada)
			cliente = entry_cliente.get()  # Obtener el cliente seleccionado
			
			if cantidad_pagada < total_venta:
				messagebox.showerror("Error", "La cantidad pagada es insuficiente.")
				return
			cambio = cantidad_pagada - total_venta

			# Formatear el total para agregar puntos en los miles
			total_formateado = "{:,.0f}".format(total_venta)

			mensaje = f"Total: $ {total_formateado} \nCantidad pagada: $ {cantidad_pagada:,.0f} \nCambio: $ {cambio:,.0f} "
			messagebox.showinfo("Pago Realizado", mensaje)
			try:
				conn = sqlite3.connect(db_nombre)
				c = conn.cursor()
				# Obtener la fecha y hora actual
				fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
				hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

				# Insertar las ventas en la tabla 'ventas' usando el número de factura actual
				for item in productos_seleccionados:
					factura, cliente, producto, precio, cantidad, total, costo = item
					c.execute("INSERT INTO ventas (factura, cliente, producto, precio, cantidad, total, costo, fecha, hora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
						(factura, cliente, producto, precio, cantidad, total.replace(" ", "").replace(",", ""), costo * cantidad, fecha_actual, hora_actual))

					#Restar la cantidad de productos vendidos del stock en la tabla 'inventario'
					c.execute("UPDATE inventario SET stock = stock - ? WHERE nombre = ?", (cantidad, producto))
				conn.commit()

				# Generar factura en PDF
				generar_factura_pdf(total_venta, cliente)
			except sqlite3.Error as e:
				messagebox.showerror("Error", f"Error al registrar la venta: {e}")
			global numero_factura
			numero_factura += 1
			label_numero_factura.config(text=str(numero_factura))
			productos_seleccionados = []
			limpiar_campos()
			# Cerrar la ventana de pago después de procesar el pago
			ventana_pago.destroy()
		
		ruta=rutas(r"iconos/pago.png")
		imagen_pil_pago_venta = Image.open(ruta)
		imagen_resize_pago_venta = imagen_pil_pago_venta.resize((30, 30))
		imagen_tk_pago_venta = ImageTk.PhotoImage(imagen_resize_pago_venta)
		button_confirmar_pago = ttk.Button(ventana_pago, text="Confirmar Pago",style="botonNavegacion.TButton", command=lambda: procesar_pago(entry_monto.get(), ventana_pago, total_venta))
		button_confirmar_pago.config(image=imagen_tk_pago_venta, compound=LEFT)
		button_confirmar_pago.image = imagen_tk_pago_venta
		button_confirmar_pago.place(x=80, y=270, width=240, height=40)

	ruta=rutas(r"iconos/pago.png")
	imagen_pil_ventas_pagos = Image.open(ruta)
	imagen_resize_ventas_pagos = imagen_pil_ventas_pagos.resize((30, 30))
	imagen_tk_ventas_pagos = ImageTk.PhotoImage(imagen_resize_ventas_pagos)
			
	boton_pagar = ttk.Button(frame_contenido_ventas, text="Pagar", style="botonNavegacion.TButton", command=realizar_pago)
	boton_pagar.config(image=imagen_tk_ventas_pagos, compound=LEFT)
	boton_pagar.image = imagen_tk_ventas_pagos
	boton_pagar.place(x=20, y=280)

	
	
	def limpiar_campos():
		# Limpiar TreeView y Label de precio total
		for item in tree.get_children():
			tree.delete(item)
		label_precio_total.config(text="Precio a Pagar: $ 0 ")
		entry_nombre.set('')
		entry_cantidad.delete(0, 'end')
	
	def generar_factura_pdf(total_venta, cliente):
	        try:
	            # Crear un lienzo para el PDF
	            factura_path = f"facturas/Factura_{numero_factura}.pdf"
	            c = canvas.Canvas(factura_path, pagesize=letter)

	            # Información de la empresa
	            empresa_nombre = "LifeHealth"
	            empresa_direccion = "Mitre 2451- Ciudad de Mendoza-Argentina"
	            empresa_telefono = "+59 2615534872 / 2615487219"
	            empresa_logo_path = rutas("imagenes/imagenLogo.png")

	            # Agregar logo de la empresa
	            c.drawImage(empresa_logo_path, 50, 700, width=140, height=80)

	            # Agregar contenido a la factura
	            c.setFont("Helvetica-Bold", 18)
	            c.drawString(250, 750, "FACTURA DE VENTA")

	            c.setFont("Helvetica-Bold", 12)
	            c.drawString(50, 680, f"{empresa_nombre}")
	            c.setFont("Helvetica", 12)
	            c.drawString(50, 660, f"Dirección: {empresa_direccion}")
	            c.drawString(50, 640, f"Teléfono: {empresa_telefono}")
	            c.drawString(50, 620, "----------------------------------------------------------------------------------------------------------------------------------")
	            c.drawString(50, 600, f"Número de Factura: {numero_factura}")
	            c.drawString(50, 580, f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	            c.drawString(50, 560, "----------------------------------------------------------------------------------------------------------------------------------")
	            c.drawString(50, 540, f"Cliente: {cliente}")
	            c.drawString(50, 520, "Descripción de Productos:")

	            # Crear una tabla para los productos
	            y_offset = 500
	            c.setFont("Helvetica-Bold", 12)
	            c.drawString(70, y_offset, "Producto")
	            c.drawString(270, y_offset, "Cantidad")
	            c.drawString(370, y_offset, "Precio")
	            c.drawString(470, y_offset, "Total")

	            y_offset -= 20
	            c.setFont("Helvetica", 12)
	            for item in productos_seleccionados:
	                factura, cliente, producto, precio, cantidad, total, costo = item
	                c.drawString(70, y_offset, producto)
	                c.drawString(270, y_offset, str(cantidad))
	                c.drawString(370, y_offset, "{:,.0f} ".format(precio))
	                c.drawString(470, y_offset, total)
	                y_offset -= 20

	            c.drawString(50, y_offset, "----------------------------------------------------------------------------------------------------------------------------------")
	            y_offset -= 20
	            c.drawString(50, y_offset, f"Total a Pagar: $ {total_venta:,.0f} ")
	            c.drawString(50, y_offset - 40, "----------------------------------------------------------------------------------------------------------------------------------")

	            # Mensaje de agradecimiento
	            c.setFont("Helvetica-Bold", 16)
	            c.drawString(150, y_offset - 100, "¡Gracias por tu compra, vuelve pronto!")

	            # Términos y condiciones
	            y_offset -= 140
	            c.setFont("Helvetica", 10)
	            c.drawString(50, y_offset, "Términos y Condiciones:")
	            c.drawString(50, y_offset - 20, "1. Los productos comprados no tienen devolución.")
	            c.drawString(50, y_offset - 40, "2. Conserve esta factura como comprobante de su compra.")
	            c.drawString(50, y_offset - 60, "3. Para más información, visite nuestro sitio web o contacte a servicio al cliente.")

	            # Pie de página con información de contacto y redes sociales

	            c.setFont("Helvetica", 10)
	            c.drawString(100, 50, "Para más información, visite nuestro sitio web o síganos en nuestras redes sociales:")
	            c.drawString(100, 40, "www.LifeHealth.com | Facebook: /LifeHealth.SA | Twitter: @LifeHealth.SA | Instagram: @LifeHealth.SA")
	            c.save()

	            messagebox.showinfo("Factura Generada", f"Se ha generado la factura en: {factura_path}")
	            
	            # Abrir el archivo PDF
	            os.startfile(os.path.abspath(factura_path))

	        except Exception as e:
	            messagebox.showerror("Error", f"No se pudo generar la factura: {e}")

	def ver_ventas_realizadas():
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT * FROM ventas")
			ventas = c.fetchall()
			conexion.close()

			ventana_ventas = Toplevel()
			ventana_ventas.title("Ventas Realizadas")
			ventana_ventas.geometry("1100x450")  # Establecer el tamaño del Toplevel
			ventana_ventas.configure(bg="SkyBlue4")  # Establecer el color de fondo del Toplevel

			# Función para filtrar las ventas por factura		
			def filtrar_ventas():
				factura_a_buscar = entry_factura.get()
				if factura_a_buscar:
					ventas_filtradas = [venta for venta in ventas if str(venta[0]) == factura_a_buscar]
				else:
					ventas_filtradas = ventas

				# Limpiar el Treeview antes de insertar los nuevos datos
				for item in tree.get_children():
					tree.delete(item)

				# Insertar las ventas filtradas en el Treeview		
				for venta in ventas_filtradas:
					venta = list(venta)
					venta[3] = "$ {:,.2f}".format(venta[3])  # Precio
					venta[5] = "$ {:,.2f}".format(venta[5])  # Total
					venta[6] = datetime.datetime.strptime(venta[6], "%Y-%m-%d").strftime("%d-%m-%Y")  # Fecha
					tree.insert("", "end", values=venta)

			label_ventas_realizadas = ttk.Label(ventana_ventas, text="Ventas Realizadas",style="labelNavegacion.TLabel")
			label_ventas_realizadas.pack(pady=10)# Agregar el Label "Ventas Realizadas"

			filtro_frame = ttk.Frame(ventana_ventas, style="Frame.TFrame")# Frame para el filtro por factura
			filtro_frame.pack(pady=5)

			label_factura = ttk.Label(filtro_frame, text="Número de Factura:", style="labelNavegacion.TLabel")# Entry para ingresar el número de factura a filtrar
			label_factura.grid(row=0, column=0)
			entry_factura = ttk.Entry(filtro_frame, style="entradasNavegacion.TLabel")
			entry_factura.grid(row=0, column=1, pady=5, ipady=5)  # Ajusta ipady para aumentar la altura vertical del Entry

			ruta=rutas(r"iconos/filtrar.png")
			imagen_pil_ventas_filtro = Image.open(ruta)
			imagen_resize_ventas_filtro = imagen_pil_ventas_filtro.resize((30, 30))
			imagen_tk_ventas_filtro = ImageTk.PhotoImage(imagen_resize_ventas_filtro)
			btn_filtrar = ttk.Button(filtro_frame, text="Filtrar", style="botonNavegacion.TButton", command=filtrar_ventas)  # Cambiar el tamaño de la fuente del botón
			btn_filtrar.config(image=imagen_tk_ventas_filtro, compound=LEFT)# Botón para aplicar el filtro
			btn_filtrar.image = imagen_tk_ventas_filtro
			btn_filtrar.grid(row=0, column=2, padx=5)

			tree_frame = ttk.Frame(ventana_ventas, style="frameTerciarios.TFrame")  # Establecer el color de fondo del Frame dentro del Toplevel
			tree_frame.pack(padx=10, pady=10)
			
			tree = ttk.Treeview(tree_frame, columns=("Factura", "Cliente", "Producto", "Precio", "Cantidad", "Total", "Fecha", "Hora"), show="headings")
			tree.heading("Factura", text="Factura")
			tree.heading("Cliente", text="Cliente")
			tree.heading("Producto", text="Producto")
			tree.heading("Precio", text="Precio")
			tree.heading("Cantidad", text="Cantidad")
			tree.heading("Total", text="Total")
			tree.heading("Fecha", text="Fecha")
			tree.heading("Hora", text="Hora")
			
			for col in ("Factura", "Cliente", "Producto", "Precio", "Cantidad", "Total", "Fecha", "Hora"):
				tree.column(col, width=150)
				tree.column(col, anchor="center")  # Alinear al centro
			scrollbar_y = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
			scrollbar_y.pack(side="right", fill="y")
			
			scrollbar_x = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
			scrollbar_x.pack(side="bottom", fill="x")
			
			tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
			
			for venta in ventas:# Mostrar todas las ventas al inicio
				venta = list(venta)
				venta[3] = "{:,.2f} $".format(venta[3])  # Precio
				venta[5] = "{:,.2f} $".format(venta[5])  # Total
				venta[6] = datetime.datetime.strptime(venta[6], "%Y-%m-%d").strftime("%d-%m-%Y")  # Fecha
				tree.insert("", "end", values=venta)
			tree.pack()
		except sqlite3.Error as e:
			messagebox.showerror("Error al obtener las ventas:", e)

	ruta=rutas(r"iconos/ver.png")
	imagen_pil_ventas_ver = Image.open(ruta)
	imagen_resize_ventas_ver = imagen_pil_ventas_ver.resize((30, 30))
	imagen_tk_ventas_ver = ImageTk.PhotoImage(imagen_resize_ventas_ver)

	boton_ver_ventas = ttk.Button(frame_contenido_ventas, text="Ver Ventas Realizadas", style="botonNavegacion.TButton", command=ver_ventas_realizadas)
	boton_ver_ventas.config(image=imagen_tk_ventas_ver, compound=LEFT)
	boton_ver_ventas.image = imagen_tk_ventas_ver
	boton_ver_ventas.place(x=200, y=280)


	def volverPrincipalVentas():
		global imagen_pil_volver_gastos
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
			
	imagen_pil_volver_ventas= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_ventas = imagen_pil_volver_ventas.resize((30,30))
	imagen_tk_volver_ventas= ImageTk.PhotoImage(imagen_resize_volver_ventas)

	boton_volver_ventas = ttk.Button(labelFrame,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalVentas)
	boton_volver_ventas.config(image=imagen_tk_volver_ventas,compound=LEFT)
	boton_volver_ventas.image = imagen_tk_volver_ventas
	boton_volver_ventas.place(x=910, y=8)	
				
def inventario(frame_contenido):
	
	db_nombre="Bd/LifeHealth.db"

	global principal_inventario
	global cargar_proveedores
	global tre
	global principal_inventario
	global mostrar
	global tre
	global frame_inventario
	global imagen_pil_calendario_articulo
	global imagen_pil_calendario_hora
	global nombre
       
	
	def rutas(ruta):
		global rutas
		try:
			rutabase=sys.__MEIPASS #Ruta base del archivo ejecutable empaquetado "Memoria ejecutable" Permite acceder a archivops ejecutables,datos e imagenes PyInstaller
		except Exception:
			rutabase=os.path.abspath(".")#Asigna ruta absoluta del directorio actual . El "." es el directorio actual de trabajo
		return os.path.join(rutabase,ruta)#Devuelve la ruta completa y absoluta de un archivo o directorio mediante la unión de la rutabase y la ruta relativa

	def eje_consulta(consulta,parametros=()):
		global eje_consulta
		with sqlite3.connect(db_nombre) as conexion:#with clave  que asegura que se cierre automáticamente la conexion cuando se termine de usar y hacer la consulta a la base de datos
			cursor = conexion.cursor()
			resultado = cursor.execute(consulta,parametros)
			conexion.commit()
		return resultado
	
	def validacion(nombre,proveedor,precio,costo,stock):
		global validacion
		return len(nombre)>0 and len(proveedor)>0 and len(precio)>0 and len(costo)>0 and len(stock)>0 # validar los datos recuperados
	
	def mostrar():
		global mostrar
		consulta = "SELECT * FROM inventario ORDER BY id DESC" # mostrar en el Treeview
		resultado = eje_consulta(consulta)
		
		for elemento in resultado:
			precio=elemento[3]
			precio_arg = "{:,.0f}".format(precio)  # Formatear el precio a peso argentino
			costo=elemento[4]
			costo_arg = "{:,.0f}".format(costo)   # Formatear el costo a peso argentino
			tre.insert("", 0, text=elemento[0], values=(elemento[0], elemento[1], elemento[2],precio_arg, costo_arg, elemento[5]))#Se insertan valores en la tabla
			
			
	global entry_nombre
	global entry_precio
	global entry_proveedor
	global entry_costo
	global entry_stock


	frame_inventario = ttk.Frame(frame_contenido,style='frameSecundarios.TFrame')
	frame_inventario.pack(fill=BOTH,expand=1)

	frame_contenido_inventario =ttk.Frame(frame_inventario,style="frameTerciarios.TFrame")
	frame_contenido_inventario.pack(side=LEFT,fill=Y)

	frame_botones_inventario =ttk.Frame(frame_inventario,style="frameSecundarios.TFrame")
	frame_botones_inventario.pack(fill=BOTH,expand=1)
		
	label_registrar_producto = LabelFrame(frame_contenido_inventario,text="Registrar producto",bg="SkyBlue4",font="Georgia 20 bold")
	label_registrar_producto.grid(row=0,column=0,ipady=5,ipadx=5,pady=20,padx=10,sticky=NW)

		
	lblname = ttk.Label(label_registrar_producto,text="Nombre: ",style="labelNavegacion.TLabel")
	lblname.grid(row=2,column=0,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
	entry_nombre = ttk.Entry(label_registrar_producto,style="entradasNavegacion.TLabel",width=35)
	entry_nombre.grid(row=2,column=1,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
		
	lblproveedor = ttk.Label(label_registrar_producto,text="Proveedor: ",style="labelNavegacion.TLabel")
	lblproveedor.grid(row=3,column=0,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
	entry_proveedor = ttk.Combobox(label_registrar_producto,style="entradasNavegacion.TLabel",state="readonly",width=35)
	entry_proveedor.grid(row=3,column=1,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)

	def cargar_proveedores():
		global cargar_proveedores

		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT nombre FROM proveedores")
			proveedores = c.fetchall()
			nombre_proveedores = [proveedor[0] for proveedor in proveedores]
			entry_proveedor["values"] = nombre_proveedores
			conexion.close()
		except sqlite3.Error as e:
			messagebox.showerror("Error cargando proveedores:", e)
	cargar_proveedores()
	
		
	lblprecio = ttk.Label(label_registrar_producto,text="Precio: ",style="labelNavegacion.TLabel")
	lblprecio.grid(row=4,column=0,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
	entry_precio = ttk.Entry(label_registrar_producto,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_precio.grid(row=4,column=1,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)

	lblcosto = ttk.Label(label_registrar_producto,text="Costo: ",style="labelNavegacion.TLabel")
	lblcosto.grid(row=5,column=0,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
	entry_costo = ttk.Entry(label_registrar_producto,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_costo.grid(row=5,column=1,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)

	lblstock = ttk.Label(label_registrar_producto,text="Stock: ",style="labelNavegacion.TLabel")
	lblstock.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)
	entry_stock = ttk.Entry(label_registrar_producto,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_stock.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,padx=10,sticky=NW)

	def registrar():

		global tre
		global registrar
		global entry_nombre
		global entry_precio
		global entry_proveedor
		global entry_costo
		global entry_stock

		#nombre=StringVar()
		#proveedor=StringVar()
		#precio=StringVar()
		#costo=StringVar()
		#stock=StringVar()
			
		resultado = tre.get_children()#Obtener los elementos hijos de un objeto Devuelve una lista de items hijos de un item seleccionado

		for i in resultado:
			tre.delete(i)
		
		nombre = entry_nombre.get()  # recuperar o agarrar los datos de los entry
		proveedor = entry_proveedor.get()
		precio = entry_precio.get()
		costo = entry_costo.get()
		stock = entry_stock.get()

		if validacion(nombre, proveedor, precio, costo, stock):
			consulta = "INSERT INTO inventario VALUES(?,?,?,?,?,?)"
			parametros = (None,nombre, proveedor, precio, costo, stock)
			eje_consulta(consulta, parametros)    
			mostrar()
			calcular_costo_total()  # Actualizar el costo total después de registrar un nuevo producto
			messagebox.showinfo("LifeHealth","Éxito,Producto agregado al inventario correctamente")# Mostrar mensaje de confirmacion

			entry_nombre.delete(0, END)
			entry_proveedor.delete(0, END)
			entry_precio.delete(0, END)
			entry_costo.delete(0, END)
			entry_stock.delete(0, END)
		else:
			messagebox.showwarning(title="Error", message="Rellene todos los campos")
			mostrar()

	ruta=rutas(r"iconos/ingresara.png")
	imagen_pil_ingresara = Image.open(ruta)
	imagen_resize_ingresara = imagen_pil_ingresara.resize((20, 20))
	imagen_tk_ingresara = ImageTk.PhotoImage(imagen_resize_ingresara)

	boton_agregar_articulo = ttk.Button( label_registrar_producto,text="INGRESAR",style="botonNavegacion.TButton",command = registrar)
	boton_agregar_articulo.config(image=imagen_tk_ingresara, compound=LEFT)
	boton_agregar_articulo.image = imagen_tk_ingresara
	boton_agregar_articulo.grid(row=12,column=0,pady=10)

		
	#Treviw

	treFrame=ttk.Frame(frame_inventario,style="navegacion.TFrame")
	treFrame.place(x=550,y=20,width=800,height=250)

	scrol_y_i = ttk.Scrollbar(treFrame,orient=VERTICAL)
	scrol_y_i.pack(side=RIGHT,fill=Y)
	scrol_x_i = ttk.Scrollbar(treFrame,orient=HORIZONTAL)
	scrol_x_i.pack(side=BOTTOM,fill=X)
		
	tre= ttk.Treeview(treFrame,columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"),show="headings",height=10,yscrollcommand=scrol_y_i.set,xscrollcommand=scrol_x_i.set)
	tre.pack(expand=True,fill=BOTH)

	scrol_y_i.config(command=tre.yview)
	scrol_x_i.config(command=tre.xview)

	tre.heading("ID",text="Id")
	tre.heading("PRODUCTO",text="Producto")    
	tre.heading("PROVEEDOR",text="Proveedor")
	tre.heading("PRECIO",text="Precio")
	tre.heading("COSTO",text="Costo")
	tre.heading("STOCK",text="Stock")

	tre.column("ID",width=50, anchor="center")
	tre.column("PRODUCTO",width=140, anchor="center")    
	tre.column("PROVEEDOR",width=70, anchor="center")
	tre.column("PRECIO",width=70, anchor="center")
	tre.column("COSTO",width=70, anchor="center")
	tre.column("STOCK",width=70, anchor="center")

	label_costo_total = ttk.Label(frame_botones_inventario, text="Total en Inventario: ", style="labelNavegacion.TLabel")
	label_costo_total.place(x=400,y=650)

		
	

	def calcular_costo_total():
		global calcular_costo_total

		consulta = "SELECT SUM(costo * stock) FROM inventario"
		resultado = eje_consulta(consulta)
		costo_total = resultado.fetchone()[0]
		costo_total_arg = "{:,.2f}".format(costo_total) if costo_total else "$ 0 "
		label_costo_total.config(text=f"Total en Inventario: {costo_total_arg}")
		

	def actualizar_inventario():
		global actualizar_inventario

		for item in tre.get_children():# Limpiar el Treeview antes de mostrar los datos actualizados
			tre.delete(item)

		mostrar()# Mostrar los datos actualizados en el Treeview
		calcular_costo_total()
		messagebox.showinfo("Actualización", "El inventario ha sido actualizado exitosamente.")

	ruta=rutas(r"iconos/actualizar.png")
	imagen_pil_actualizar = Image.open(ruta)
	imagen_resize_actualizar = imagen_pil_actualizar.resize((20, 20))
	imagen_tk_actualizar = ImageTk.PhotoImage(imagen_resize_actualizar)

	btn_actualizar_producto = ttk.Button(label_registrar_producto,text="ACTUALIZAR",style="botonNavegacion.TButton",command = actualizar_inventario)
	btn_actualizar_producto.config(image=imagen_tk_actualizar, compound=LEFT)
	btn_actualizar_producto.image = imagen_tk_actualizar
	btn_actualizar_producto.grid(row=12,column=1,pady=10)

		
	def editar_producto():
		global editar_producto

		seleccion = tre.selection()# Obtener el ítem seleccionado en el Treeview
		if not seleccion:
			messagebox.showwarning("Editar Producto", "Seleccione un producto para editar.")
			return
			
		item_id = tre.item(seleccion)["text"]# Obtener los datos del ítem seleccionado
		item_values = tre.item(seleccion)["values"]
				

		ventana_editar = Toplevel()#Ventana para editar el producto
		ventana_editar.title("Editar Producto")
		ventana_editar.geometry("600x600")
		ventana_editar.config(bg="black")

		lbl_nombre = ttk.Label(ventana_editar, text="Nombre:", style="labelNavegacion.TLabel")
		lbl_nombre.grid(row=0, column=0, padx=10, pady=10)
		entry_nombre = ttk.Entry(ventana_editar, style="entradasNavegacion.TLabel",width=35)
		entry_nombre.grid(row=0, column=1, padx=10, pady=10)
		entry_nombre.insert(0, item_values[1])

		lbl_proveedor = ttk.Label(ventana_editar, text="Proveedor :", style="labelNavegacion.TLabel")
		lbl_proveedor.grid(row=1, column=0, padx=10, pady=10)
		entry_proveedor = ttk.Entry(ventana_editar,style="entradasNavegacion.TLabel",width=35)
		entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
		entry_proveedor.insert(0, item_values[2])


		lbl_precio = ttk.Label(ventana_editar, text="Precio :", style="labelNavegacion.TLabel")
		lbl_precio.grid(row=2, column=0, padx=10, pady=10)
		entry_precio = ttk.Entry(ventana_editar, style="entradasNavegacion.TLabel",width=35)
		entry_precio.grid(row=2, column=1, padx=10, pady=10)
		entry_precio.insert(0, item_values[3])

		lbl_costo = ttk.Label(ventana_editar, text="Costo :", style="labelNavegacion.TLabel")
		lbl_costo.grid(row=3, column=0, padx=10, pady=10)
		entry_costo = ttk.Entry(ventana_editar, style="entradasNavegacion.TLabel",width=35)
		entry_costo.grid(row=3, column=1, padx=10, pady=10)
		entry_costo.insert(0, item_values[4])

		lbl_stock = ttk.Label(ventana_editar, text="Stock :", style="labelNavegacion.TLabel")
		lbl_stock.grid(row=4, column=0, padx=10, pady=10)
		entry_stock= ttk.Entry(ventana_editar, style="entradasNavegacion.TLabel",width=35)
		entry_stock.grid(row=4, column=1, padx=10, pady=10)
		entry_stock.insert(0, item_values[5])

		def guardar_cambios():
			global guardar_cambios

			nombre = entry_nombre.get()
			proveedor = entry_proveedor.get()
			precio = entry_precio.get()
			costo = entry_costo.get()
			stock = entry_stock.get()

			if not (nombre  and proveedor and precio  and costo  and stock):
				messagebox.showwarning("Guardar Cambios", "Rellene todos los campos.")
				return
			try:
				precio = float(precio.replace(",", ""))
				costo = float(costo.replace(",", ""))	
			except ValueError:
				messagebox.showwarning("Guardar Cambios", "Ingrese valores numéricos válidos para precio y costo.")
				return

			consulta = "UPDATE inventario SET nombre=?, proveedor=?, precio=?, costo=?, stock=? WHERE id=?"
			parametros = (nombre, proveedor, precio, costo, stock, item_id)
			eje_consulta(consulta, parametros)
			actualizar_inventario() # Actualizar el Treeview y el costo total
			ventana_editar.destroy()# Cerrar la ventana de edición

		ruta=rutas(r"iconos/guardarArt.png")
		imagen_pil_guardar_articulos = Image.open(ruta)
		imagen_resize_guardar_articulos = imagen_pil_guardar_articulos.resize((30, 30))
		imagen_tk_guardar_articulos = ImageTk.PhotoImage(imagen_resize_guardar_articulos)

		btn_guardar_articulos = ttk.Button(ventana_editar, text="GUARDAR",style="botonNavegacion.TButton",command = guardar_cambios)
		btn_guardar_articulos.config(image=imagen_tk_guardar_articulos, compound=LEFT)
		btn_guardar_articulos.image = imagen_tk_guardar_articulos
		btn_guardar_articulos.grid(row=6, column=1)
		
	ruta=rutas(r"iconos/editar.png")
	imagen_pil_editar = Image.open(ruta)
	imagen_resize_editar = imagen_pil_editar.resize((20, 20))
	imagen_tk_editar =ImageTk .PhotoImage(imagen_resize_editar)

	boton_editar_articulo = ttk.Button(label_registrar_producto,text="EDITAR",style="botonNavegacion.TButton",command = editar_producto)
	boton_editar_articulo.config(image=imagen_tk_editar, compound=LEFT)
	boton_editar_articulo.image = imagen_tk_editar
	boton_editar_articulo.grid(row=13,column=1,pady=10)

	label_aclaracion=ttk.Label(label_registrar_producto,text="Aclaración:",font="Georgia 10 bold")
	label_aclaracion.grid(row=14,column=0,pady=10)		
	label_aclaracion1=ttk.Label(label_registrar_producto,text="Solo usar en precio y costo:",font="Georgia 10 bold")
	label_aclaracion1.grid(row=15,column=0,pady=10)		
	label_aclaracion2=ttk.Label(label_registrar_producto,text="aproximacion sin . ni ,",font="Georgia 10 bold")
	label_aclaracion2.grid(row=16,column=0,pady=10)		
	label_aclaracion3=ttk.Label(label_registrar_producto,text="STOCK siempre en 0 ",font="Georgia 12 bold")
	label_aclaracion3.grid(row=17,column=0,pady=10)		
	

		
	def volverPrincipalInventario():
		global imagen_pil_volver_productos
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
			
			
	imagen_pil_volver_productos= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_productos = imagen_pil_volver_productos.resize((20,20))
	imagen_tk_volver_productos= ImageTk.PhotoImage(imagen_resize_volver_productos)

	boton_volver_producto = ttk.Button(label_registrar_producto,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalInventario)
	boton_volver_producto.config(image=imagen_tk_volver_productos,compound=LEFT)
	boton_volver_producto.image = imagen_tk_volver_productos
	boton_volver_producto.grid(row=13,column=0,pady=10)			

def reportes(frame_contenido):
	db_nombre="Bd/LifeHealth.db"
	0
	global frame_reportes
	global generar_reporte
	global generar_reporte_ganancias_totales

	frame_reportes = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_reportes.pack(fill=BOTH,expand=1)
	#label_reportes = ttk.Label(frame_reportes,text="Reportes",style='titulo.TLabel')
	#label_reportes.pack()

	frame_ventas_totales =ttk.Frame(frame_reportes,style="navegacion.TFrame")
	frame_ventas_totales.place(x=20,y=20,width=650,height=650)

	frame_ganancias =ttk.Frame(frame_reportes,style="navegacion.TFrame")
	frame_ganancias.place(x=700,y=20,width=650,height=650)	


	
	frame_contenido_ventas = ttk.Frame(frame_ventas_totales,style="fondo.TFrame")
	frame_contenido_ventas.place(x=22,y=10,width=600,height=300)

	frame_contenido_ganancias = ttk.Frame(frame_ganancias,style="fondo.TFrame")
	frame_contenido_ganancias.place(x=22,y=10,width=600,height=300)


	frame_tabla_ventas = Frame(frame_ventas_totales)
	frame_tabla_ventas.place(x=20,y=330,width=600,height=300)

	frame_tabla_ganancias = Frame(frame_ganancias)
	frame_tabla_ganancias.place(x=20,y=330,width=600,height=300)



	label_reporte = ttk.Label(frame_contenido_ventas, text="Reporte de ventas",style="labelNavegacion.TLabel")
	label_reporte.place(x=200, y=10, height=40)


	label_desde = ttk.Label(frame_contenido_ventas, text="Desde:", style="labelNavegacion.TLabel")
	label_desde.place(x=30, y=60, width=100, height=40)
	entry_desde = DateEntry(frame_contenido_ventas, font="Georgia 14 bold",date_pattern="yyyy-mm-dd")
	entry_desde.place(x=30, y=110, width=130, height=40)

	label_hasta = ttk.Label(frame_contenido_ventas, text="Hasta:", style="labelNavegacion.TLabel")
	label_hasta.place(x=30, y=180, width=100, height=40)
	entry_hasta = DateEntry(frame_contenido_ventas, font="Georgia 14 bold",date_pattern="yyyy-mm-dd")
	entry_hasta.place(x=30, y=230, width=130, height=40)

	
	tabla_reporte = ttk.Treeview(frame_tabla_ventas, columns=("Cantidad de Ventas", "Total de Ventas"), show="headings", height=5) 
	tabla_reporte.heading("Cantidad de Ventas", text="Cantidad de productos vendidos", anchor="center")
	tabla_reporte.heading("Total de Ventas", text="Total de Ventas", anchor="center")
	tabla_reporte.column("Cantidad de Ventas", width=200, anchor="center")
	tabla_reporte.column("Total de Ventas", width=200, anchor="center")
	tabla_reporte.place(x=0, y=0, width=600, height=300)  

	tabla_reporte.tag_configure("money", font="sans 10")
	tabla_reporte.tag_configure("money", foreground="black")
	tabla_reporte.tag_configure("money", background="#D9D2E9")
	tabla_reporte.tag_configure("money", anchor="center")

	label_nota = Label(frame_ventas_totales, text="El reporte de ventas totales equivale al total de las ventas de los \nproductos incluyendo costo y ganancia",font="Georgia 10 bold")
	label_nota.place(x=70, y=590, height=80) 

	label_reporte1 = ttk.Label(frame_contenido_ganancias, text="Reporte de ganancias",style="labelNavegacion.TLabel")
	label_reporte1.place(x=200, y=10, height=40)

	
	label_desde1 = ttk.Label(frame_contenido_ganancias, text="Desde:",style="labelNavegacion.TLabel")
	label_desde1.place(x=30, y=60, width=100, height=40)
	entry_desde1 = DateEntry(frame_contenido_ganancias, font="Georgia 14 bold",date_pattern="yyyy-mm-dd")
	entry_desde1.place(x=30, y=110, width=130, height=40)

	label_hasta1 = ttk.Label(frame_contenido_ganancias, text="Hasta:",style="labelNavegacion.TLabel")
	label_hasta1.place(x=30, y=180, width=100, height=40)
	entry_hasta1 = DateEntry(frame_contenido_ganancias, font="Georgia 14 bold",date_pattern="yyyy-mm-dd")
	entry_hasta1.place(x=30, y=230, width=130, height=40)

	tabla_ganancias = ttk.Treeview(frame_tabla_ganancias, columns=("Ganancias Totales",), show="headings",height=5)
	tabla_ganancias.heading("Ganancias Totales", text="Ganancias Totales", anchor="center")
	tabla_ganancias.column("Ganancias Totales", width=200,anchor="center")
	tabla_ganancias.place(x=300, y=100, width=700, height=200, anchor="center")


	label_nota2 = Label(frame_ganancias, text="El reporte de ganancias equivale a las ventas totales menos el costo \nde los productos",font="Georgia 10 bold")
	label_nota2.place(x=160, y=590, height=80) 

	def formato_moneda (cantidad):
		
		return f' {cantidad}'

	def generar_reporte():
		fecha_desde = entry_desde.get()
		fecha_hasta = entry_hasta.get()
		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT COUNT(*), SUM(total) FROM ventas WHERE fecha BETWEEN ? AND ?", (fecha_desde, fecha_hasta))
			resultado = c.fetchone()
			conexion.close()

			cantidad_ventas = resultado[0]
			total_ventas = resultado[1]

			for item in tabla_reporte.get_children():
				tabla_reporte.delete(item)

			formatear_total = formato_moneda(total_ventas)

			tabla_reporte.insert("", "end", values=(cantidad_ventas, formatear_total))

		except sqlite3.Error as e:
			messagebox.showerror("Error", f"Error al generar el reporte: {e}")
			
	imagen_pil_filtrar= Image.open("iconos/filtrar.png")
	imagen_resize_filtrar = imagen_pil_filtrar.resize((30,30))
	imagen_tk_filtrar= ImageTk.PhotoImage(imagen_resize_filtrar)

	boton_filtrar = ttk.Button(frame_contenido_ventas, text="Filtrar", style="botonNavegacion.TButton", command=generar_reporte)
	boton_filtrar.config(image=imagen_tk_filtrar, compound=LEFT)
	boton_filtrar.image = imagen_tk_filtrar
	boton_filtrar.pack(pady=110)


	def generar_reporte_ganancias_totales():
		fecha_desde1 = entry_desde1.get()
		fecha_hasta1 = entry_hasta1.get()

		try:
			conexion = sqlite3.connect(db_nombre)
			c = conexion.cursor()
			c.execute("SELECT SUM(total) FROM ventas WHERE fecha BETWEEN ? AND ?", (fecha_desde1, fecha_hasta1))
			total_ventas = c.fetchone()[0] or 0
			c.execute("SELECT SUM(costo) FROM ventas WHERE fecha BETWEEN ? AND ?", (fecha_desde1, fecha_hasta1))
			total_costos = c.fetchone()[0] or 0
			ganancias_totales = total_ventas - total_costos
			conexion.close()
			for item in tabla_ganancias.get_children():
				tabla_ganancias.delete(item)
			tabla_ganancias.insert("", "end", values=(f" {ganancias_totales}",))
		except sqlite3.Error as e:
			messagebox.showerror("Error", f"Error al generar el reporte de ganancias totales: {e}")
 
	imagen_pil_filtrar2= Image.open("iconos/filtrar.png")
	imagen_resize_filtrar2 = imagen_pil_filtrar2.resize((30,30))
	imagen_tk_filtrar2= ImageTk.PhotoImage(imagen_resize_filtrar2)

	boton_filtrar2 = ttk.Button(frame_contenido_ganancias, text="Filtrar", style="botonNavegacion.TButton", command=generar_reporte_ganancias_totales)
	boton_filtrar2.config(image=imagen_tk_filtrar2, compound=LEFT)
	boton_filtrar2.image = imagen_tk_filtrar2
	boton_filtrar2.pack(pady=110)

	def volverPrincipalReporte():
		global imagen_pil_volver_reporte
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_reporte= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_reporte = imagen_pil_volver_reporte.resize((30,30))
	imagen_tk_volver_reporte= ImageTk.PhotoImage(imagen_resize_volver_reporte)

	boton_volver_reporte = ttk.Button(frame_ganancias,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalReporte)
	boton_volver_reporte.config(image=imagen_tk_volver_reporte,compound=RIGHT)
	boton_volver_reporte.image = imagen_tk_volver_reporte
	boton_volver_reporte.place(x=00,y=610)	

def usuarios(frame_contenido):
	db_nombre = "Bd/LifeHealth.db"
	global frame_usuarios

	frame_usuarios = ttk.Frame(frame_contenido,style='frameSecundarios.TFrame')
	frame_usuarios.pack(fill=BOTH,expand=1)


	frame_botones_usuarios = ttk.Frame(frame_usuarios,style='frameTerciarios.TFrame')
	frame_botones_usuarios.pack(side=RIGHT,fill=Y)

	
	imagen_pil_fecha = Image.open("iconos/calendario.png")
	imagen_resize_fecha = imagen_pil_fecha.resize((30, 30))
	imagen_tk_fecha = ImageTk.PhotoImage(imagen_resize_fecha)

	label_fecha = ttk.Label(frame_botones_usuarios, style="labelNavegacion.TLabel")
	label_fecha.config(image=imagen_tk_fecha, compound=LEFT)
	label_fecha.image = imagen_tk_fecha
	label_fecha.pack(padx=10,pady=10)

	imagen_pil_hora = Image.open("iconos/hora.png")
	imagen_resize_hora = imagen_pil_hora.resize((30, 30))
	imagen_tk_hora = ImageTk.PhotoImage(imagen_resize_hora)

	label_hora = ttk.Label(frame_botones_usuarios, style="labelNavegacion.TLabel")
	label_hora.config(image=imagen_tk_hora, compound=LEFT)
	label_hora.image = imagen_tk_hora
	label_hora.pack(padx=10,pady=10)

	frame_tabla_usuarios=ttk.Frame(frame_usuarios) 
	frame_tabla_usuarios.place(x=160,y=50,width=650,height=450)
	scrol_y_u = ttk.Scrollbar(frame_tabla_usuarios)
	scrol_y_u.pack(side=RIGHT, fill=Y)

	scrol_x_u = ttk.Scrollbar(frame_tabla_usuarios, orient=HORIZONTAL)
	scrol_x_u.pack(side=BOTTOM, fill=X)

	lista_usuarios = ttk.Treeview(frame_tabla_usuarios, yscrollcommand=scrol_y_u.set, xscrollcommand=scrol_x_u.set, height=40)
	lista_usuarios["columns"] = ("Usuario", "Contraseña")

	lista_usuarios.pack(expand=True, fill=BOTH)
	lista_usuarios.heading("#0", text="ID")
	lista_usuarios.heading("Usuario", text="Usuario")
	lista_usuarios.heading("Contraseña", text="Contraseña")

	lista_usuarios.column("#0", width=50, anchor="center")
	lista_usuarios.column("Usuario", width=150, anchor="center")
	lista_usuarios.column("Contraseña", width=150, anchor="center")

	def buscar_usuarios():
		try:
			conexion = sqlite3.connect(db_nombre)
			cursor = conexion.cursor()
			cursor.execute("SELECT * FROM usuarios")
			usuarios = cursor.fetchall()
			return usuarios
		except sqlite3.Error as e:
			messagebox.showerror("Error", f"No se pudieron leer los usuarios: {e}")
			return []

	def actualizar_usuario(idUsuario, usuario_info, clave_info):
		try:
			conexion = sqlite3.connect(db_nombre)
			cursor = conexion.cursor()
			cursor.execute("UPDATE usuarios SET usuario_info=?, clave_info=? WHERE idUsuario=?", (usuario_info,clave_info, idUsuario))
			conexion.commit()
			messagebox.showinfo("Éxito", "Usuario actualizado exitosamente")
		except sqlite3.Error as e:
			messagebox.showerror("Error", f"No se pudo actualizar el usuario: {e}")
		finally:
			if conexion:
				conexion.close()
	

	def cargar_usuarios():

		for row in lista_usuarios.get_children():
			lista_usuarios.delete(row)

		usuarios = buscar_usuarios()

		for usuario in usuarios:
			lista_usuarios.insert("", "end", text=usuario[0], values=(usuario[1], "*" * len(usuario[2])))

	cargar_usuarios()

	def actualizar_usuario_seleccionado():

		item_seleccionado = lista_usuarios.selection()

		if item_seleccionado:
			idUsuario = lista_usuarios.item(item_seleccionado, "text")
			usuario_info = lista_usuarios.item(item_seleccionado, "values")[0]
			clave_info = lista_usuarios.item(item_seleccionado, "values")[1]

			ventana_modificar_usuario = Toplevel()
			ventana_modificar_usuario.title("Modificar Usuario")
			ventana_modificar_usuario.geometry("400x400") 
			ventana_modificar_usuario.config(bg="SkyBlue4")

			label_username = ttk.Label(ventana_modificar_usuario, text="Nuevo nombre de usuario:",style="labelNavegacion.TLabel")
			label_username.place(x=70, y=20)
			entry_username = ttk.Entry(ventana_modificar_usuario,style="entradasNavegacion.TLabel")
			entry_username.insert(0, usuario_info)
			entry_username.place(x=70, y=60, width=240,height=40)

			label_password = ttk.Label(ventana_modificar_usuario, text="Nueva contraseña:",style="labelNavegacion.TLabel")
			label_password.place(x=70, y=110)
			entry_password = ttk.Entry(ventana_modificar_usuario, show="*",style="entradasNavegacion.TLabel")
			entry_password.insert(0, clave_info)
			entry_password.place(x=75, y=150, width=240,height=40)

			imagen_pil_guardar2 = Image.open("iconos/guardar.png")
			imagen_resize_guardar2 = imagen_pil_guardar2.resize((30, 30))
			imagen_tk_guardar2 = ImageTk.PhotoImage(imagen_resize_guardar2)

			btn_actualizar_usuario = ttk.Button(ventana_modificar_usuario, text="Actualizar",style="botonNavegacion.TButton", command=lambda: actualizar_usuario(idUsuario, entry_username.get(), entry_password.get()))
			btn_actualizar_usuario.config(image=imagen_tk_guardar2, compound=LEFT)
			btn_actualizar_usuario.image = imagen_tk_guardar2
			btn_actualizar_usuario.place(x=110, y=210,width=170,height=40)
		else:
			messagebox.showwarning("Advertencia", "Por favor, seleccione un usuario para actualizar.")

	#imagen_pil_guardar = Image.open("iconos/guardar.png")
	#imagen_resize_guardar = imagen_pil_guardar.resize((30, 30))
	#imagen_tk_guardar = ImageTk.PhotoImage(imagen_resize_guardar)

	#btn_actualizar = ttk.Button(frame_botones_usuarios, text="Actualizar Usuario",style="botonNavegacion.TButton",command=actualizar_usuario_seleccionado)
	#btn_actualizar.config(image=imagen_tk_guardar, compound=LEFT)
	#btn_actualizar.image = imagen_tk_guardar
	#btn_actualizar.pack(padx=10,pady=20)
	

	def actualizar_fecha_y_hora(self): 

		fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
		hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

		label_fecha.config(text=fecha_actual)
		label_hora.config(text=hora_actual)
		ventana_principal.after(1000, actualizar_fecha_y_hora)

	def volverUsuario():
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_usuario = Image.open("iconos/btnVolver.png")
	imagen_resize_volver_usuario = imagen_pil_volver_usuario.resize((30, 30))
	imagen_tk_volver_ususario = ImageTk.PhotoImage(imagen_resize_volver_usuario)

	btn_volver_usuario = ttk.Button(frame_botones_usuarios, text="Volver",style="botonNavegacion.TButton",command=volverUsuario)
	btn_volver_usuario.config(image=imagen_tk_volver_ususario, compound=LEFT)
	btn_volver_usuario.image = imagen_tk_volver_ususario
	btn_volver_usuario.pack(padx=10,pady=20)
	
def gastos(frame_contenido):
	global frame_gastos
	frame_gastos = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_gastos.pack(fill=BOTH,expand=1)

	frame_contenido_gastos =ttk.Frame(frame_gastos,style="navegacion.TFrame")
	frame_contenido_gastos.pack(side=LEFT,fill=Y)

	frame_botones_gastos =ttk.Frame(frame_gastos,style="navegacion.TFrame")
	frame_botones_gastos.pack(fill=Y,side=RIGHT,ipadx=50)

	listbox_gastos = Listbox(frame_gastos)
	listbox_gastos.place(x=340,y=100,width=700,height=400)

	scrol_y_g= ttk.Scrollbar(listbox_gastos,orient=VERTICAL)
	scrol_y_g.pack(side=RIGHT,fill=Y)
	scrol_x_g = ttk.Scrollbar(listbox_gastos,orient=HORIZONTAL)
	scrol_x_g.pack(side=BOTTOM,fill=X)

	
	#Evento mostrar en listbox
	def mostrarGastos(evento):
		indiceGastos=listbox_gastos.curselection()[0]
		mensajeGastos=listbox_gastos.get(indiceGastos)
		messagebox.showinfo("LifeHealth",mensajeGastos)
	listbox_gastos.bind("<<ListboxSelect>>",mostrarGastos)


	label_gastos = ttk.Label(frame_contenido_gastos,text="Registrar gastos",style="subTitulo.TLabel")
	label_gastos.pack(padx=15,pady=15)

	label_buscar_gastos =ttk.Label(frame_contenido_gastos,text="Buscar Gastos",style="labelNavegacion.TLabel")
	label_buscar_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_buscar_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35)
	entry_buscar_gastos.pack(anchor=NW,padx=15,pady=15)
	
	label_id_gastos = ttk.Label(frame_contenido_gastos,text="N° de gasto",style="labelNavegacion.TLabel")
	label_id_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_id_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35)
	entry_id_gastos.pack(anchor=NW,padx=15,pady=15)

	entry_id_gastos.config(state="readonly")

	label_concepto_gastos = ttk.Label(frame_contenido_gastos,text="Concepto",style="labelNavegacion.TLabel")
	label_concepto_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_concepto_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd2)
	entry_concepto_gastos.pack(anchor=NW,padx=15,pady=15)

	label_valor_gastos = ttk.Label(frame_contenido_gastos,text="Valor",style="labelNavegacion.TLabel")
	label_valor_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_valor_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35,validate= "key",validatecommand=vcmd)
	entry_valor_gastos.pack(anchor=NW,padx=15,pady=15)

	label_entidad_gastos = ttk.Label(frame_contenido_gastos,text="Entidad",style="labelNavegacion.TLabel")
	label_entidad_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_entidad_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35)
	entry_entidad_gastos.pack(anchor=NW,padx=15,pady=15)

	label_fecha_gastos = ttk.Label(frame_contenido_gastos,text="Fecha",style="labelNavegacion.TLabel")
	label_fecha_gastos.pack(anchor=NW,pady=15,padx=15)
	entry_fecha_gastos = ttk.Entry(frame_contenido_gastos,style="entradasNavegacion.TLabel",width=35)
	entry_fecha_gastos.pack(anchor=NW,padx=15,pady=15)
	
	def buscarGasto():
		global datos
		buscarGastos=entry_buscar_gastos.get() 
		if(buscarGastos !=""):
			try:
				ver=True
				for letra in buscarGastos:
					if(not(letra.isdigit())):
						ver=False
						break
				if(ver):
					buscarGastos = (entry_buscar_gastos.get(),)
					conexion = sqlite3.connect("Bd/LifeHealth.db")
					tabla=conexion.cursor()
					tabla.execute("SELECT * FROM gastos WHERE idGastos=?",buscarGastos)
					datos = tabla.fetchall()
					entry_id_gastos.config(state="normal")
					entry_id_gastos.delete(0,END)
					entry_concepto_gastos.delete(0,END)
					entry_valor_gastos.delete(0,END)
					entry_entidad_gastos.delete(0,END)
					entry_fecha_gastos.delete(0,END)
					boton_eliminar_gastos.config(state="normal")
					boton_modificar_gastos.config(state="normal")
					
					if(len(datos)>0):
						boton_guardar_gastos.config(state="disabled")
						for dato in datos:
							idGastos=dato[0]
							conceptoGastos=dato[1]
							valorGastos=dato[2]
							entidadGastos=dato[3]
							fechaGastos=dato[4]
							
							entry_id_gastos.insert(END,idGastos)
							entry_concepto_gastos.insert(END,conceptoGastos)
							entry_valor_gastos.insert(END,valorGastos)
							entry_entidad_gastos.insert(END,entidadGastos)
							entry_fecha_gastos.insert(END,fechaGastos)

					else:
						messagebox.showwarning("LifeHealth","No se encrontró registro")
						entry_id_gastos.config(state="readonly")
						limpiarGasto()
				else:
					messagebox.showwarning(title="LifeHealth",message="Ingrese solo números!")
			except ValueError:
				messagebox.showwarning(title="LifeHealth",message="Registro incorrecto")
		else:
			messagebox.showwarning(title="LifeHealth",message="Ingrese algo que buscar")		
	
	boton_buscar_gastos = ttk.Button(frame_botones_gastos,text="BUSCAR",style="botonNavegacion.TButton",command = buscarGasto)
	boton_buscar_gastos.pack(padx=10,pady=50)

	def ingresarGasto():
		try:
			boton_guardar_gastos.config(state="normal")
			conceptoGastos = entry_concepto_gastos.get()
			valorGastos = entry_valor_gastos.get()
			entidadGastos = entry_entidad_gastos.get()
			fechaGastos = entry_fecha_gastos.get()
			
			if(conceptoGastos != "" and valorGastos != "" and entidadGastos != "" and fechaGastos  !=""):
				datos = (conceptoGastos,valorGastos,entidadGastos,fechaGastos)
				conexion = sqlite3.connect("Bd/LifeHealth.db")				
				tabla = conexion.cursor()
				tabla.execute("INSERT INTO gastos(conceptoGastos,valorGastos,entidadGastos,fechaGastos)VALUES(?,?,?,?)",datos)
				conexion.commit()
				messagebox.showinfo("LifeHealth","Guardado con éxito")
				
				limpiarGasto()
				listarGasto()
				
			else:
				messagebox.showwarning("LifeHealth","Complete todos los campos")

		except ValueError   as e:
			messagebox.showerror("Error","Error datos de la base de datos, {e}")

	boton_guardar_gastos = ttk.Button(frame_botones_gastos,text="INGRESAR",style="botonNavegacion.TButton",command = ingresarGasto)
	boton_guardar_gastos.pack(padx=10,pady=30)
	def modificarGasto():
		boton_guardar_gastos.config(state="normal")

		idGastos = entry_id_gastos.get()
		conceptoGastos = entry_concepto_gastos.get()
		valorGastos = entry_valor_gastos.get()
		entidadGastos = entry_entidad_gastos.get()
		fechaGastos = entry_fecha_gastos.get()
		datos = (conceptoGastos,valorGastos,entidadGastos,fechaGastos,idGastos)
		conexion = sqlite3.connect("Bd/LifeHealth.db")
		tabla=conexion.cursor()
		tabla.execute("UPDATE gastos SET conceptoGastos=?,valorGastos=?,entidadGastos=?,fechaGastos=? WHERE idGastos =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Modificado con éxito")
		limpiarGasto()
		listarGasto()
	boton_modificar_gastos = ttk.Button(frame_botones_gastos,text="MODIFICAR",style="botonNavegacion.TButton",command = modificarGasto)
	boton_modificar_gastos.pack(padx=10,pady=30)
	boton_modificar_gastos.config(state="disabled")

	def eliminarGasto():
		boton_guardar_gastos.config(state="normal")
		idGastos = entry_id_gastos.get()
		datos = (idGastos,)
		conexion = sqlite3.connect("Bd/LifeHealth.db")
		tabla=conexion.cursor()
		tabla.execute("DELETE FROM gastos WHERE idGastos =?",datos)
		conexion.commit()
		messagebox.showinfo("LifeHealth","Eliminado con éxito")	
		limpiarGasto()
		listarGasto()

	boton_eliminar_gastos = ttk.Button(frame_botones_gastos,text="ELIMINAR",style="botonNavegacion.TButton",command = eliminarGasto)
	boton_eliminar_gastos.pack(padx=10,pady=30)
	boton_eliminar_gastos.config(state="disable")
	
	def limpiarGasto():
		boton_guardar_gastos.config(state="normal")
		entry_buscar_gastos.delete(0,END)
		entry_id_gastos.config(state="normal")
		entry_id_gastos.delete(0,END)
		entry_id_gastos.config(state="readonly")
		entry_concepto_gastos.delete(0,END)
		entry_valor_gastos.delete(0,END)
		entry_entidad_gastos.delete(0,END)
		entry_fecha_gastos.delete(0,END)
		
		boton_modificar_gastos.config(state="disable")
		boton_eliminar_gastos.config(state="disable")

	boton_limpiar_gastos = ttk.Button(frame_botones_gastos,text="LIMPIAR",style="botonNavegacion.TButton",command = limpiarGasto)
	boton_limpiar_gastos.pack(padx=10,pady=30)

	def listarGasto():
		conexion = sqlite3.connect("Bd/LifeHealth.db")

		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM gastos")
		listado = tabla.fetchall()
		listbox_gastos.delete(0,END)

		for elemento in listado:
			informacionGastos = "ID:"+"  "+str(elemento[0])+"  "+"CONCEPTO:"+"  "+elemento[1]+"  "+"VALOR:"+"  "+str(elemento[2])+"  "+"ENTIDAD"+"  "+elemento[3]+" "+"FECHA"+" "+str(elemento[4])   
			listbox_gastos.insert(END,informacionGastos)
	
	boton_listar_gastos = ttk.Button(frame_botones_gastos,text="LISTAR",style="botonNavegacion.TButton",command = listarGasto())
	boton_listar_gastos.pack(padx=20,pady=30)	

	def volverPrincipalGastos():
		global imagen_pil_volver_gastos
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_gastos= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_gastos = imagen_pil_volver_gastos.resize((30,30))
	imagen_tk_volver_gastos= ImageTk.PhotoImage(imagen_resize_volver_gastos)

	boton_volver_gastos = ttk.Button(frame_botones_gastos,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalGastos)
	boton_volver_gastos.config(image=imagen_tk_volver_gastos,compound=LEFT)
	boton_volver_gastos.image = imagen_tk_volver_gastos
	boton_volver_gastos.pack(padx=10,pady=30)
	
def acerca(frame_contenido):
	global frame_acerca
	global imagenLogo
	frame_acerca = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_acerca.pack(fill=BOTH,expand=1)
	frame_contenido_acerca=ttk.Frame(frame_acerca,style="navegacion.TFrame")
	frame_contenido_acerca.pack(fill=Y,side=LEFT,padx=300,pady=20)

	imagenLogo=PhotoImage(file="imagenes/imagenLogo.png")
	label_Logo = Label(frame_contenido_acerca,image=imagenLogo)
	label_Logo.pack(padx=90,pady=20)
	label_acerca = ttk.Label(frame_contenido_acerca,text="Comprometidos en soluciones tecnológicas innovadoras,",anchor="c",justify=RIGHT,style="subTitulo.TLabel")
	label_acerca.pack(pady=5,padx=50)
	label_acerca2 = ttk.Label(frame_contenido_acerca,text="que sastifacen las necesidades de nuestros clientes.",anchor="c",justify=RIGHT,style='subTitulo.TLabel')
	label_acerca2.pack(pady=5,padx=50)
	label_acerca3 = ttk.Label(frame_contenido_acerca,text="Proyecto LifeHealth",anchor="c",justify=RIGHT,style="labelNavegacion.TLabel")
	label_acerca3.pack(pady=5,padx=50)
	label_acerca4 = ttk.Label(frame_contenido_acerca,text="Versión 2.00",anchor="c",justify=RIGHT,style="labelNavegacion.TLabel")
	label_acerca4.pack(pady=5,padx=50)
	label_acerca5 = ttk.Label(frame_contenido_acerca,text="Última actualización: 22-07-2024",anchor="c",justify=RIGHT,style="labelNavegacion.TLabel")
	label_acerca5.pack(pady=5,padx=50)
	label_acerca6 = ttk.Label(frame_contenido_acerca,text="Soporte: ",anchor="c",justify=RIGHT,style="subTitulo.TLabel")
	label_acerca6.pack(pady=5,padx=50)
	
	label_direccion_acerca = ttk.Label(frame_contenido_acerca,text="DIRECCIÓN: Mitre 2451- Ciudad de Mendoza",anchor="c",justify=RIGHT,style='labelNavegacion.TLabel')
	label_direccion_acerca.pack(pady=5)

	label_contacto_acerca = ttk.Label(frame_contenido_acerca,text="CONTACTO: 2615534872 / 2615487219",anchor="c",justify=RIGHT,style='labelNavegacion.TLabel')
	label_contacto_acerca.pack(pady=5)

	label_mail_acerca = ttk.Label(frame_contenido_acerca,text="E-MAIL: LifeHealth2024@gmail.com",anchor="c",justify=RIGHT,style='labelNavegacion.TLabel')
	label_mail_acerca.pack(pady=5)
	
	label_derechos_acerca = Label(frame_contenido_acerca,text="Copyright 2024 - Todos los derechos reservados",font=("Calibri",12),bg="SkyBlue4",fg="black")
	label_derechos_acerca.pack(pady=5)
	
	def volverPrincipalAcerca():
		global imagen_pil_volver_acerca
		borrarFrames()
		frame_contenido.pack_forget()
		frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)
		frame_inicio.pack(fill=BOTH,expand=1)
		
	imagen_pil_volver_acerca= Image.open("iconos/btnVolver.png")
	imagen_resize_volver_acerca = imagen_pil_volver_acerca.resize((30,30))
	imagen_tk_volver_acerca= ImageTk.PhotoImage(imagen_resize_volver_acerca)

	boton_volver_acerca = ttk.Button(frame_contenido_acerca,text="VOLVER",style="botonNavegacion.TButton",command = volverPrincipalAcerca)
	boton_volver_acerca.config(image=imagen_tk_volver_acerca,compound=LEFT)
	boton_volver_acerca.image = imagen_tk_volver_acerca
	boton_volver_acerca.pack(side=RIGHT,padx=5)
	
ventana_principal = Tk()
misEstilos()
login_principal()
ventana_principal.mainloop()

