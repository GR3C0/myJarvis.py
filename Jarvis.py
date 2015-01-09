import os
import sys
import time 
import base_de_datos 
import random
import smtplib

#variables que hacen funcionar los condicionales
hola = str("Hola Jarvis")
hola2 = str(" Hola Jarvis")
adios = str("Adios")
Fecha = str("Fecha y Hora")
Mayuscula = str("Todo en mayuscula")
Minuscula = str("Todo en minuscula")
Calculadora = str("Calculadora")
Importado = str("Que he importado")
tipo_ordenador = str("Que tipo de ordenador tengo")
ip_usuario = str("Cual es mi ip")
nano = str("nano")
archivo = str("Abre" + "file_name")#En fase de pruebas
Cerrar_archivo = str("Cerrar")
Salir = str("Salir")
Read = str("Read")
Enviar_correo = str("Envia un correo")

print "		Buenos dias Diego" #lo que imprime nada mas ejecutarlo

accion = raw_input("Escribe: ") #variable donde se almacena lo que el usuario escribe

#todas las funciones se declaran antes de la funcion saludar ya que necesita tener las funciones declaras antes para leerlass
def enviar_correo():

	fromaddr = 'diegomorellmasip@gmail.com'
	print ""
 	toaddrs = raw_input("pon el destinatario: ")
 	print ""
	msg = raw_input("Pon el mensaje: \n")
	print ""
		 
	# Datos
	username = 'diegomorellmasip@gmail.com'
	password = 'pupulado8'
	
	print ""
	print "Enviando correo"
	print ""
	# Enviando el correo
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	print "Correo enviado"
pass


def read():
	os.system("read()")
pass

def salir():
	os.system("exit()")
pass

def Abre_archivo(): #En fase de pruebas
	accion3 = str("Cerrar")
	objecto_archivo = open(Python [, wb][, wb])
	# Abrimos el archivo codehero.txt
	fo = open("codehero.txt", "wb")
	print "Nombre del archivo : ", fo.name
	print "Cerrado o no : ", fo.closed
	print "Modo de apertura : ", fo.mode

	accion4 = raw_input("que quieres hacer con el archivo")

	if accion4 == Cerrar_archivo:

		fo.close()
	pass	
pass

def nano():
	print ""
	os.system("nano")
	print ""
pass

def ip():
	print ""
	ip = os.system("ifconfig")
	print ip
	print ""
pass

def tipo_ordenador():
	print ""
	return hack.py 
	print ""
pass

def he_importado():
	print ""
	accion_ = raw_input ("Cual quieres saber: ")
	os = "os"
	sys = "sys"
	time = "time"
	base_de_datos = "La base de datos"
	random = "random"
	if accion_ == os:
		print dir(os)
		print help(os)

	elif accion_ == sys:
		print dir(sys)
		print help(sys)

	elif accion_ == time:
		print dir(time)
		print help(time)

	elif accion_ == base_de_datos:
		print dir(base_de_datos)

	elif accion_ == random:
		print dir(random)
		print help(random)
	pass
pass

def despedirse():
	print "" #Esto es un enter
	print "		Hasta luego Diego"
	print ""
pass


def texto_en_mayuscula(n):
	texto = raw_input("Pon lo que quieres en mayuscula: ")
	print ""
	print texto.upper() # imprime la variable texto que contiene lo que ha escrito el usuario y lo pone en mayuscula
	print "" 
pass


def texto_en_minuscula(n):
	texto = raw_input("Pon lo que quieres en minuscula: ")
	print ""
	print texto.lower() # imprime la variable texto que contiene lo que ha escrito el usuario y lo pone en minuscula
	print ""
pass

def extranjero(n):
		print ""
		print "	No estas en mi base de datos;"
		print "	Adios"
		print ""
pass

def hora_fecha():

		print ""

		ahora = time.strftime("%c")
		## representacion del tiempo
		print "	Fecha "  + time.strftime("%x")

		## representacion de la hora
		print "	Hora " + time.strftime("%X")

		print ""
pass

def calculadora(n):
		os.math
pass

def saludar(n): #Esta es la funcion que ejecuta jarvis nada mas empezar y contiene todos los condicionales 
	if accion == hola or accion == hola2:
		print "		Buenas Diego"
		accion2 = raw_input("Que quieres hacer: ")
		if accion2 == Fecha: 
			hora_fecha()

		elif accion2 == adios:
				despedirse()

		elif accion2 == Fecha:
				hora_fecha()

		elif accion2 == Mayuscula:
				texto_en_mayuscula(n)

		elif accion2 == Minuscula:
				texto_en_minuscula(n)

		elif accion2 == Importado:
				he_importado()

		elif accion2 == tipo_ordenador:
				tipo_ordenador()

		elif accion2 == ip_usuario:
				ip()

		elif accion2 == nano:
				nano()

		elif accion2 == Salir:
				salir()

		elif accion2 == Read:
				read()	

		elif accion2 == Enviar_correo:
				enviar_correo()

		else:
			print ""
			print "	Esa accion no esta en mi base de datos"
			print ""
		pass
	else:
		return extranjero(n)
	pass
pass

#cada condicional si se cumple ejecuta una funcion y si no ejecuta la funcion extranjero, eso quiere decir que el usuario que esta 
#escribiendo no lo tiene en la base de datos


saludar(hola)


