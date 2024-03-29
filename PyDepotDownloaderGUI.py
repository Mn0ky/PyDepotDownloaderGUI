from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QMovie
import sys
import webbrowser, os
import os, signal
from os import path
from subprocess import call

os.path.join(os.getcwd())
#uncomment line below if compiling
#os.chdir(os.path.dirname(sys.executable))

fileName1 = ""
manlist = []

if os.path.isfile('manidlistpath.txt'):
	with open('manidlistpath.txt', 'r') as f:
		fileName1 = f.read()

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uipath = os.path.normpath("Resources/depotdownloadergui.ui")
		# uncomment line below if compiling
		# uipath = os.path.join(os.path.dirname(sys.executable), 'Resources/depotdownloadergui.ui')
		uic.loadUi(uipath, self)

		self.outputedit = self.findChild(QtWidgets.QTextEdit, 'outputedit')
		self.output = self.outputedit
		self.runButton = self.findChild(QtWidgets.QPushButton, 'runpushbutton')
		self.runButton.clicked.connect(self.callProgram)

		layout = self.findChild(QtWidgets.QHBoxLayout, 'horizontalLayout')

		self.buttonopenmanid = self.findChild(QtWidgets.QPushButton, 'openmanidpushbutton')
		self.buttonopenmanid.clicked.connect(self.openmanidpushbuttonPressed)

		self.buttonbrsdl = self.findChild(QtWidgets.QPushButton, 'brsdlpushbutton')
		self.buttonbrsdl.clicked.connect(self.brsdlpushbuttonPressed)

		self.buttonformat = self.findChild(QtWidgets.QPushButton, 'formatpushbutton')
		self.buttonformat.clicked.connect(self.formatpushbuttonPressed)

		self.cb = self.findChild(QtWidgets.QPushButton, 'cb')
		self.cb.clicked.connect(self.cbPressed)

		self.killbutton = self.findChild(QtWidgets.QPushButton, 'candown')

		self.manpathedit = self.findChild(QtWidgets.QPlainTextEdit, 'manedit')
		self.manpathedit.insertPlainText(fileName1)

		self.progress = self.findChild(QtWidgets.QLabel, 'loader')
		ldico = os.path.normpath("Resources/loading_icon.gif")
		self.movie = QMovie(ldico)
		self.progress.setMovie(self.movie)

		radiobutton = QRadioButton("Auto")
		radiobutton.setChecked(True)
		radiobutton.country = "Auto"
		radiobutton.toggled.connect(self.onClicked)
		layout.addWidget(radiobutton)

		radiobutton = QRadioButton("Windows")
		radiobutton.country = "Windows"
		radiobutton.toggled.connect(self.onClicked)
		layout.addWidget(radiobutton)

		radiobutton = QRadioButton("MacOS")
		radiobutton.country = "MacOS"
		radiobutton.toggled.connect(self.onClicked)
		layout.addWidget(radiobutton)

		radiobutton = QRadioButton("Linux")
		radiobutton.country = "Linux"
		radiobutton.toggled.connect(self.onClicked)
		layout.addWidget(radiobutton)
		self.rbv = "Auto"
		self.show()

	def onClicked(self):
		radioButton = self.sender()
		if radioButton.isChecked():
			self.rbv = radioButton.country
			if self.rbv == "Auto":
				self.depotid = self.findChild(QtWidgets.QPlainTextEdit, 'depidtextedit')
				self.depotid.setEnabled(True)
			else:
				self.depotid = self.findChild(QtWidgets.QPlainTextEdit, 'depidtextedit')
				self.depotid.setEnabled(False)
				self.depotid.setPlainText("")	

	def openmanidpushbuttonPressed(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		oldfileName = self.manpathedit.toPlainText()
		
		global fileName1

		fileName1, _ = QFileDialog.getOpenFileName(self,"Select ManifestID List", "","Text Files (*.txt)", options=options)
		if fileName1 == "":
			fileName1 = oldfileName
		self.manpathedit = self.findChild(QtWidgets.QPlainTextEdit, 'manedit')
		self.manpathedit.setPlainText(fileName1)
			
	def brsdlpushbuttonPressed(self):
		if not os.path.isdir('Downloads'):
			os.mkdir('Downloads')
		if os.name == 'nt':
			webbrowser.open(os.path.realpath('Downloads'))
		else:
			call(["open", "Downloads"])

	def formatpushbuttonPressed(self):
		if os.path.isfile(fileName1):
			try:
				my_file = open(fileName1, "r")
				content_list = my_file.readlines()
				for i in content_list:
					manlist.append(i.split('\t')[2])
				with open(fileName1, "w") as output:
					for a in manlist:
						output.write(str(a))
				if os.name == 'nt':
					SuccessText = "<span style=\" font-size:9pt; font-weight:1200; color:#00e600;\" >"
					SuccessText += ("Success: Formatted Manifest List!")
					SuccessText += ("</span>")
				else:
					SuccessText = "<span style=\" font-size:12pt; font-weight:1200; color:#00e600;\" >"
					SuccessText += ("Success: Formatted Manifest List!")
					SuccessText += ("</span>")
				self.output.append(SuccessText)			

			except Exception:
				if os.name == "nt":
					ErrorText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Manifest List Not Specified Or Not Formattable!")
					ErrorText += ("</span>")
				else:
					ErrorText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Manifest List Not Specified Or Not Formattable!")
					ErrorText += ("</span>")
				self.output.append(ErrorText)
		
		else:
			if os.name == "nt":
				ErrorText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff0000;\" >"
				ErrorText += ("Error: Manifest List Not Specified!")
				ErrorText += ("</span>")
			else:
				ErrorText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff0000;\" >"
				ErrorText += ("Error: Manifest List Not Specified!")
				ErrorText += ("</span>")
			self.output.append(ErrorText)	

	def callProgram(self):

		dllpath = str(os.getcwd() + "/Resources/depotdownloader-2.3.6/DepotDownloader.dll")
		# uncomment line below if compiling
		#dllpath = str(os.path.dirname(sys.executable) + "/Resources/depotdownloader-2.3.6/DepotDownloader.dll")
		fileName2 = os.path.normpath(dllpath)
		self.username = self.findChild(QtWidgets.QPlainTextEdit, 'usertextedit')
		self.username = self.username.toPlainText()
		self.password = self.findChild(QtWidgets.QLineEdit, 'passtextedit')
		self.password = self.password.text()
		self.depotid = self.findChild(QtWidgets.QPlainTextEdit, 'depidtextedit')
		self.depotid = self.depotid.toPlainText()
		appid = self.findChild(QtWidgets.QPlainTextEdit, 'appidtextedit')
		appid = appid.toPlainText()
		downloadpath = os.path.normpath("Downloads/" + appid)
		# uncomment lines below if compiling
		# downloadpath = str(os.path.dirname(sys.executable)) + "/Downloads/" + appid
		# downloadpath = os.path.normpath(downloadpath)
		big_command_list =[]
		big_command = str("dotnet " + fileName2 +" -app " + appid + " -username " + self.username + " -password " + self.password + " -dir " + downloadpath +  " -os ")
		if fileName1 != "":
			with open(fileName1) as f:
				manifestcontent = f.readlines()
			manifestcontent = [x.strip() for x in manifestcontent]			

			index = 1

			if appid == "":
				if os.name == 'nt':
					ErrorText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Must specify AppID!")
					ErrorText += ("</span>")
				else:
					ErrorText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Must specify AppID!")
					ErrorText += ("</span>")
				self.output.append(ErrorText)
				return

			if self.depotid =="" :
				if self.rbv == "Windows" :
					big_command_list.append(big_command + "windows")
				elif self.rbv == "MacOS" :
					big_command_list.append(big_command + "macos")
				elif self.rbv == "Linux" :
					big_command_list.append(big_command + "linux")
				else:
					big_command_list.append(str("dotnet " + fileName2 +" -app " + appid + " -username " + self.username + " -password " + self.password + " -dir " + downloadpath))
					if self.username == "" and self.password == "":
						big_command_list = [x.replace(' -username ', '') for x in big_command_list]
						big_command_list = [x.replace(' -password ', '') for x in big_command_list]
			else:
				for a in manifestcontent:
					downloadpath=os.path.normpath("Downloads/" + a + " " + str(index)+ ")")	
					big_command_list.append(str("dotnet " + fileName2 +" -app " + appid + " -username " + self.username + " -password " + self.password + " -depot " + self.depotid + " -manifest " + a + " -dir " + "\""+downloadpath+"\""))
					index = index + 1
					if self.username == "" and self.password == "":
						big_command_list = [x.replace(' -username ', '') for x in big_command_list]
						big_command_list = [x.replace(' -password ', '') for x in big_command_list]
		else:
			if not self.depotid == "":
				if os.name == 'nt':
					ErrorText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Manifest List Not Specified!")
					ErrorText += ("</span>")
				else:
					ErrorText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff0000;\" >"
					ErrorText += ("Error: Manifest List Not Specified!")
					ErrorText += ("</span>")
				self.output.append(ErrorText)
				return
			else:
				if self.rbv == "Windows" :
					big_command_list.append(big_command + "windows")
				elif self.rbv == "MacOS" :
					big_command_list.append(big_command + "macos")
				elif self.rbv == "Linux" :
					big_command_list.append(big_command + "linux")
				else:
					big_command_list.append(str("dotnet " + fileName2 +" -app " + appid + " -username " + self.username + " -password " + self.password + " -dir " + downloadpath))
					if self.username == "" and self.password == "":
						big_command_list = [x.replace(' -username ', '') for x in big_command_list]
						big_command_list = [x.replace(' -password ', '') for x in big_command_list]	

		manager = SequentialManager(self)
		manager.resultsChanged.connect(self.onResultsChanged)
		manager.start(big_command_list)
		self.runpushbutton.setEnabled(False)
		self.movie.start()
		self.progress.show()

	def cbPressed(self):
		self.output.setPlainText('')
		if os.name == 'nt':
			WarningText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff7733;\" >"
			WarningText += ("Warning: Output Cleared!")
			WarningText += ("</span>")
		else:
			WarningText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff7733;\" >"
			WarningText += ("Warning: Output Cleared!")
			WarningText += ("</span>")
		self.output.append(WarningText)
				

	def onResultsChanged(self, result):
		result = str(result).replace("b' ", "")
		result = str(result).replace("b'","")
		result = str(result).replace("\\n'", "")
		result = str(result).replace('b"', '"')
		result = str(result).replace('\\n ', '\n')
		result = str(result).replace('\\n'," ")
		if os.name == 'nt':
			result = str(result).replace('\\r'," ")
		# uncomment line below for output in terminal (for debugging)
		# print("result= ", result)
		self.output.append(str(result))

class SequentialManager(QtCore.QObject):
	finished = QtCore.pyqtSignal()
	resultsChanged = QtCore.pyqtSignal(QtCore.QByteArray)

	def __init__(self, parent=MainWindow):
		super(SequentialManager, self).__init__(parent)
		self.cancel = "false"
		self.process = QtCore.QProcess(self)
		self.process.finished.connect(self.handleFinished)
		self.process.readyReadStandardOutput.connect(self.onReadyReadStandardOutput)
		self.parent().killbutton.clicked.connect(self.candownPressed)

	def candownPressed(self):
		self.process.kill()
		self.cancel = "true"
		if os.name == 'nt':
			WarningText = "<span style=\" font-size:9pt; font-weight:1200; color:#ff7733;\" >"
			WarningText += ("Warning: Download(s) Canceled!")
			WarningText += ("</span>")
		else:
			WarningText = "<span style=\" font-size:12pt; font-weight:1200; color:#ff7733;\" >"
			WarningText += ("Warning: Download(s) Canceled!")
			WarningText += ("</span>")
		self.parent().output.append(WarningText)

	def start(self, commands):
		self._commands = iter(commands)
		self.fetchNext()

	def fetchNext(self):
		if self.cancel == "true":
			self.parent().killbutton.clicked.disconnect()
			return False
		try:
			command = next(self._commands)
		except StopIteration:
			return False
		else:
			self.process.start(command)
		return True

	def onReadyReadStandardOutput(self):
		result = self.process.readAllStandardOutput()
		if "This account is protected by Steam Guard" in str(result):
			code, done1 = QtWidgets.QInputDialog.getText( 
			None, 'Input Dialog', 'Enter SteamGuard/2FA Code:')
			code = code + "\n"
			self.process.write(code.encode('utf-8'))
		self.resultsChanged.emit(result)

	def handleFinished(self):
		if not self.fetchNext():
			if self.cancel == "false":
				self.finished.emit()
				self.parent().killbutton.clicked.disconnect()
				self.parent().runpushbutton.setEnabled(True)
				if os.name == 'nt':
					SuccessText = "<span style=\" font-size:9pt; font-weight:1200; color:#00e600;\" >"
					SuccessText += ("Success: Download(s) Complete!")
					SuccessText += ("</span>")
				else:
					SuccessText = "<span style=\" font-size:12pt; font-weight:1200; color:#00e600;\" >"
					SuccessText += ("Success: Download(s) Complete!")
					SuccessText += ("</span>")
				self.parent().output.append(SuccessText)
				self.parent().progress.hide()
			else:
				self.finished.emit()
				self.parent().runpushbutton.setEnabled(True)
				self.parent().movie.stop()
				self.parent().progress.hide()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()

with open('manidlistpath.txt', "w") as f:
	f.write(fileName1)