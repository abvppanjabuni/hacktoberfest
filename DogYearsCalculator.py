# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
import sys

# window class
class Window(QMainWindow):
	
	# Constructor
	def __init__(self):
		super().__init__()

		# setting title of the window
		self.setWindowTitle("Python ")

		# width of the window
		self.w_width = 400

		# height of the window
		self.w_height = 400

		# setting geometry of the window
		self.setGeometry(100, 100, self.w_width, self.w_height)

		# method calling
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components creation
	def UiComponents(self):
		# creating head label
		head = QLabel("Dog Age Calculator", self)

		head.setWordWrap(True)

		# setting geometry of the head
		head.setGeometry(0, 10, 400, 60)

		# font work
		font = QFont('Times', 15)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)

		# setting color effect to the head
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.darkCyan)
		head.setGraphicsEffect(color)


		# creating a label
		age_label = QLabel("Age of Dog ", self)

		# setting geometry to the label
		age_label.setGeometry(50, 120, 147, 40)

		# setting alignment
		age_label.setAlignment(Qt.AlignCenter)

		# setting stylesheet
		age_label.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : rgba(70, 70, 70, 35);"
								"}")

		age_label.setFont(QFont('Times', 9))

		# creating a spin box
		self.age = QSpinBox(self)

		# setting geometry to the spin box
		self.age.setGeometry(203, 120, 147, 40)

		# setting maximum value of spin box
		self.age.setMaximum(20)

		# setting minimum value of spin box
		self.age.setMinimum(1)

		# setting suffix to the spin box
		self.age.setSuffix(" year(s)")

		# setting font and alignment
		self.age.setFont(QFont('Times', 9))
		self.age.setAlignment(Qt.AlignCenter)



		# creating a push button
		calculate = QPushButton("Calculate Age", self)

		# setting geometry to the push button
		calculate.setGeometry(100, 200, 200, 40)

		# adding action to the button
		calculate.clicked.connect(self.calculate)

		# adding color effect to the push button
		color = QGraphicsColorizeEffect()
		color.setColor(Qt.blue)
		calculate.setGraphicsEffect(color)


		# creating a label to show result
		self.result = QLabel(self)

		# setting properties to result label
		self.result.setAlignment(Qt.AlignCenter)

		# setting geometry
		self.result.setGeometry(50, 280, 300, 70)

		# making it multi line
		self.result.setWordWrap(True)

		# setting stylesheet
		# adding border and background
		self.result.setStyleSheet("QLabel"
								"{"
								"border : 3px solid black;"
								"background : white;"
								"}")

		# setting font
		self.result.setFont(QFont('Arial', 11))


	# method for calculating the dog's age
	def calculate(self):

		# getting the spin box value
		value = self.age.value()

		# if value is 1
		if value == 1:

			# dog age is 15
			d_age = 15

		# if value is 2
		elif value == 2:

			# dog age is 24
			d_age = 24

		# else dog age get incremented by 4
		else:
			d_age = 24 + (value - 2) * 4


		# showing age through label
		self.result.setText("If your dog were a human, it would be : " +str(d_age) + " years old !")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
