import socket   
import threading
import datetime

fecha = datetime.datetime.now()
hora = fecha.strftime('%d/%m/%Y %H:%M:%S')


host = '127.0.0.1'
puerto = 65432

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((host, puerto))
servidor.listen()
print(f"Servidor funcionando en: {host} puerto: {puerto}")


clientes = []
nombredeusuarios = []

def controldemensajes(mensaje, cCliente):
    for cliente in clientes:
        if cliente != cCliente:
            cliente.send(mensaje)

def desconectarcliente(cliente):
    indice = clientes.index(cliente)
    nombreusuario = nombredeusuarios[indice]
    controldemensajes(f"Chat: {nombreusuario} se ha desconectado".encode('utf-8'), cliente)
    clientes.remove(cliente)
    nombredeusuarios.remove(nombreusuario)
    cliente.close()
    print(f"{nombreusuario} Desconectado")

def manejodemensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            controldemensajes(mensaje, cliente)
        except:
            desconectarcliente(cliente)
            break


def recibirconexiones():
    while True:
        cliente, direccion = servidor.accept()

        
        nombreu = cliente.recv(1024).decode('utf-8')

        clientes.append(cliente)
        nombredeusuarios.append(nombreu)

        print(f"{hora}{nombreu} se conecto con: {str(direccion)}")

        mensaje = f"ChatBot: {nombreu} Se unio al chat!".encode("utf-8")
        controldemensajes(mensaje, cliente)
        cliente.send("Conectado al servidor".encode("utf-8"))

        h = threading.Thread(target=manejodemensajes, args=(cliente,))
        h.start()

recibirconexiones()