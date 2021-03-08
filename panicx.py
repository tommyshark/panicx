import sys, os
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import *

import design

version = '0.1.1'

class PanicX(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.path = ""
		self.btnBrowse.clicked.connect(self.BrowseFile)
		self.btnDelete.clicked.connect(self.deleteFile)
		self.lineEdit.setPlaceholderText("Путь")
		self.label_3.setText("Version " + version)
	def showCriticalIfNone(self):
		msgbox = QtWidgets.QMessageBox()
		msgbox.setText("Path is wrong!")
		msgbox.setIcon(QtWidgets.QMessageBox.Critical)
		msgbox.setWindowTitle("Wrong!")
		msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		returnValue = msgbox.exec()
	def showCriticalIfNone2(self):
		msgbox = QtWidgets.QMessageBox()
		msgbox.setText("Something is wrong! Такого файла не существует. \nВозможно у вас в пути к файлу есть пробелы, перед пробелом сразу после слова нужно поставить символ \\")
		msgbox.setIcon(QtWidgets.QMessageBox.Critical)
		msgbox.setWindowTitle("Wrong!")
		msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		returnValue = msgbox.exec()
	def showGoodIfOk(self):
		msgbox = QtWidgets.QMessageBox()
		msgbox.setText("Файл успешно удален!")
		msgbox.setIcon(QtWidgets.QMessageBox.Information)
		msgbox.setWindowTitle("Success!")
		msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		returnValue = msgbox.exec()
	def BrowseFile(self):
		bfile = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
		if bfile:
			bfile = str(bfile)
			path = bfile[2 : -19]
			self.lineEdit.setText(path)
	def deleteFile(self):
		# Deleting file at all with shred
		self.path = self.lineEdit.text()
		if self.path == "":
			msg = self.showCriticalIfNone()
		else:
			if os.system("shred -u -z " + self.path) == 0:
				msg3 = self.showGoodIfOk()
			else:
				msg2 = self.showCriticalIfNone2()
		

def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("Fusion")

	dark_palette = QPalette()

	dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.WindowText, Qt.white)
	dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
	dark_palette.setColor(QPalette.ToolTipText, Qt.white)
	dark_palette.setColor(QPalette.Text, Qt.white)
	dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ButtonText, Qt.white)
	dark_palette.setColor(QPalette.BrightText, Qt.red)
	dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.HighlightedText, Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
	window = PanicX()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()
