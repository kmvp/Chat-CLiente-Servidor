from tkinter import *
import socket
import threading
from tkinter import ttk, font, messagebox
from tkinter.scrolledtext import ScrolledText

localIP     = "127.0.0.1"
localPort   = 20002
bufferSize  = 1024
condir		= ("127.0.0.1", 20001)

msgFromServer   = ""
clientMsg 		= ""
clientIP		= ""

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def main():
	global msgFromServer
	global UDPServerSocket
	global clientMsg
	global condir

	def f_salir():
		ventana_principal.destroy()

	def funcion_enviar():
		texto=campo_enviar_texto.get()
		tx=str.encode(texto)
		add=str.encode(clientIP)
		muestra.tag_config("yo", foreground='midnight blue', font='Fixedsys 14')
		muestra.insert(END, "Cliente  >> {} \n".format(texto),"yo")
		UDPServerSocket.sendto(tx, condir)

	def iniciar_server():
		global clientMsg
		while(True):
			bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
			message = bytesAddressPair[0]
			muestra_mensaje.tag_config("el", foreground='black', font='Fixedsys 14')
			muestra_mensaje.insert(END, "Servidor >> {} \n".format(message),"el")

	print("Funcion principal")
	ventana_principal = Tk()
	muestra_mensaje = Text(ventana_principal, height=10, width=80, bg='floral white' )
	muestra = Text(ventana_principal, height=10, width=80, bg='mint cream')
	muestra_mensaje.pack()
	muestra.pack()
	
	print(" ")
	campo_enviar_texto = Entry(ventana_principal, width=75)
	campo_enviar_texto.pack()
	print(" ")
	boton_enviar_texto = Button(ventana_principal,text="Enviar mensaje", command=funcion_enviar, height=2, width=20, bg="dark slate blue")
	boton_enviar_texto.pack()
	boton = Button(text="Cerrar", command = ventana_principal.destroy, height=2, width=10, bg="MistyRose3")
	boton.pack(side=RIGHT)

	t = threading.Thread(target=iniciar_server)
	t.start()

	ventana_principal.title('Chat del Cliente')
	ventana_principal.mainloop()

if __name__ == "__main__":
	main()