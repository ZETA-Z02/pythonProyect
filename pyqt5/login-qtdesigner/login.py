from PyQt5 import QtWidgets, uic
# iniciar la aplicacion
app = QtWidgets.QApplication([])

# Cargar archivos .ui
login = uic.loadUi("login1.ui")
entrar = uic.loadUi("login2.ui")
error = uic.loadUi("login3.ui")


def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()
    if len(name) == 0 or len(password) == 0:
        login.label_5.setText("Ingrese todos los datos")
    elif name == "zeta" and password == "zeta":
        gui_entrar()
    else:
        gui_error()


def gui_entrar():
    login.hide()
    entrar.show()


def gui_error():
    login.hide()
    error.show()


def salir():
    app.exit()


def regresar():
    entrar.hide()
    error.hide()
    login.label_5.setText("")
    login.show()


# Bottons
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)
entrar.regresar.clicked.connect(regresar)
error.regresar.clicked.connect(regresar)
entrar.pushButton_2.clicked.connect(salir)
error.pushButton_2.clicked.connect(salir)


# Ejecutable
login.show()
app.exec()
