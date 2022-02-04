from PySide2.QtWidgets import QWidget
from views.ui_files.Ui_login import LoginForm

from pys2_msgboxes import msgboxes

class VentanaIngreso(QWidget, LoginForm):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.joinButton.clicked.connect(self.uniralchat)

    def uniralchat(self):
        username = self.usernameLineEdit.text()

        if username != '':
            from controllers.chat import VentanaChat
            self.chat_window = VentanaChat(username)
            self.chat_window.show()
            self.close()
        else:
            msgboxes.input_error_msgbox('Dato requerido', 'Debe introducir un nombre de usuario!')
