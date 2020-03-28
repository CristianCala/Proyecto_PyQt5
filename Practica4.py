#POR FIN NOJODASSSSS!!!!



import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("Practica4.ui", self)
		self.NombreA.textChanged.connect(self.Validar_nombre)
		self.ApellidoA.textChanged.connect(self.Validar_apellido)
		self.EmailA.textChanged.connect(self.Validar_email)
		self.BotonA.clicked.connect(self.Validar_formulario)

	def Validar_nombre(self):
		NombreA = self.NombreA.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', NombreA, re.I)
		if NombreA == "":
			self.NombreA.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validar:
			self.NombreA.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.NombreA.setStyleSheet("border: 1px solid green;")
			return True

	def Validar_apellido(self):
		ApellidoA = self.ApellidoA.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', ApellidoA, re.I)
		if ApellidoA == "":
			self.ApellidoA.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validar:
			self.ApellidoA.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.ApellidoA.setStyleSheet("border: 1px solid green;")
			return True

	def Validar_email(self):
		EmailA = self.EmailA.text()
		validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', EmailA, re.I)
		if EmailA == "":
			self.EmailA.setStyleSheet("border: 1px solid yellow;")
			return False
		elif not validar:
			self.EmailA.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.EmailA.setStyleSheet("border: 1px solid green;")
			return True

	def Validar_formulario(self):
		if self.Validar_nombre() and self.Validar_apellido() and self.Validar_email():
			QMessageBox.information(self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
		else:
			QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)
		
		
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()

