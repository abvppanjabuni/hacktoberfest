# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# width of window
		self.w_width = 400

		# height of window
		self.w_height = 450

		# setting geometry
		self.setGeometry(100, 100,
						self.w_width,
						self.w_height)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating head label
		head = QLabel("1/4 Mile Calculator",
					self)

		# setting geometry to the head
		head.setGeometry(0, 10, 400, 60)

		# setting font
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
		e_label = QLabel("Equation", self)

		# setting properties label
		e_label.setAlignment(Qt.AlignCenter)
		e_label.setGeometry(20, 100, 170, 40)
		e_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		e_label.setFont(QFont('Times', 9))

		# creating a combo box to selected equation
		self.equation = QComboBox(self)

		# adding items to the combo box
		items = ["Huntington", "Fox", "Hale"]
		self.equation.addItems(items)

		# setting properties to the combo box
		self.equation.setFont(QFont('Times', 9))
		self.equation.setGeometry(200, 100, 180, 40)
		self.equation.setEditable(False)


		# creating a label
		w_label = QLabel("Car Weight (lb)", self)

		# setting properties to the label
		w_label.setAlignment(Qt.AlignCenter)
		w_label.setGeometry(20, 150, 170, 40)
		w_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		w_label.setFont(QFont('Times', 9))

		# creating a QLineEdit object
		self.weight = QLineEdit(self)

		# accepting only number as input
		onlyInt = QIntValidator()
		self.weight.setValidator(onlyInt)

		# setting properties to the line edit
		self.weight.setGeometry(200, 150, 180, 40)
		self.weight.setAlignment(Qt.AlignCenter)
		self.weight.setFont(QFont('Times', 9))

		# creating a label
		p_label = QLabel("Engine Power (hp) ", self)

		# setting properties to the years label
		p_label.setAlignment(Qt.AlignCenter)
		p_label.setGeometry(20, 200, 170, 40)
		p_label.setStyleSheet("QLabel"
							"{"
							"border : 2px solid black;"
							"background : rgba(70, 70, 70, 35);"
							"}")
		p_label.setFont(QFont('Times', 9))

		# creating a QLineEdit object
		self.power = QLineEdit(self)

		# accepting only number as input
		onlyInt = QIntValidator()
		self.power.setValidator(onlyInt)

		# setting properties to the line edit
		self.power.setGeometry(200, 200, 180, 40)
		self.power.setAlignment(Qt.AlignCenter)
		self.power.setFont(QFont('Times', 9))


		# creating a push button
		calculate = QPushButton("Calculate Time", self)

		# setting geometry to the push button
		calculate.setGeometry(125, 270, 150, 40)

		# adding action to the calculate button
		calculate.clicked.connect(self.calculate_action)

		# creating a label to show percentile
		self.result = QLabel(self)

		# setting properties to result label
		self.result.setAlignment(Qt.AlignCenter)
		self.result.setGeometry(30, 340, 340, 80)
		self.result.setWordWrap(True)
		self.result.setStyleSheet("QLabel"
								"{"
								"border : 3px solid black;"
								"background : white;"
								"}")
		self.result.setFont(QFont('Arial', 11))

	# method for calculating the
	# quarter-mile elapsed time (ET)
	def calculate_action(self):


		# getting weight of car
		weight = self.weight.text()

		# getting power of engine
		power = self.power.text()

		# if no input is given close the function
		if len(weight) == 0 or len(power) == 0:
			return

		# converting weight into integer
		weight = int(weight)

		# converting power into integer
		power = int(power)

		# if user enter total value as 0
		# return the function
		if power == 0 or weight == 0:
			return

		# getting the selected equation index
		equation = self.equation.currentIndex()

		# setting constant value according to the equation
		# Roger Huntington's constant
		if equation == 0:
			constant = 6.290

		# Geoffrey Fox's constant
		elif equation == 1:
			constant = 6.269

		# Patrick Hale's constant
		else:
			constant = 5.825

		# calculating the time
		result = constant * ((weight/power)**(1/3))

		# formatting the time
		result = "{:.2f}".format(result)

		# setting text to the result label
		self.result.setText("1/4 Mile Elapsed Time : "
							+ str(result) + " seconds")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
