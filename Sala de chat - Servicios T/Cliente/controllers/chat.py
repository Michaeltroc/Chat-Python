from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.ui_files.Ui_chat import ChatForm
from controllers.login import VentanaIngreso

import socket
import threading
import datetime

fecha = datetime.datetime.now()
hora = fecha.strftime('%d/%m/%Y %H:%M:%S')



class VentanaChat(QWidget, ChatForm):

    def __init__(self, nombreu):
        super().__init__()
        self.nombreu = nombreu
        self.setupUi(self)

        self.conectar()

        self.sendButton.clicked.connect(self.enviarmensajes)

    def conectar(self):
        conectardatos = ('127.0.0.1', 65432)
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM

        self.cliente = socket.socket(af_inet, sock_stream)
        self.cliente.connect(conectardatos)

        recibirh = threading.Thread(target=self.recibirmensajes)
        recibirh.daemon = True
        recibirh.start()

        self.cliente.send(self.nombreu.encode('utf-8'))
        self.logoutButton.clicked.connect(self.salir)
    
    def salir(self):
        self.ingresoventana = VentanaIngreso()
        self.ingresoventana.show()
        self.cliente.close()
        self.close()

    def recibirmensajes(self):
        while True:
            try:
                mensaje = self.cliente.recv(1024).decode('utf-8')
                self.chatTextEdit.append(mensaje)
                self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.cliente.close()
                break
    
    def enviarmensajes(self):
        mensaje = self.messageLineEdit.text()

        mensaje = f"{hora}->{self.nombreu}: {mensaje}"
        self.cliente.send(mensaje.encode('utf-8'))
        self.chatTextEdit.append(mensaje)
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        self.messageLineEdit.clear()