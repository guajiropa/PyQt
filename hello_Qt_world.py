"""
#   Author      :   Robert James Patterson
#   Date        :   5/21/2017
#   Project     :   Pluralsite
#   Synopsis    :   Trying out GUI development with Python and Qt
#
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

#------------------------------------------------------------------------------------------------------


class HelloWorld(QDialog):
    """
    Create our own class from QDialog so that we may override
    some of it's methods
    """
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        self.label = QLabel("Hello Qt World!!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

#------------------------------------------------------------------------------------------------------


app = QApplication(sys.argv)

dialog = HelloWorld()
dialog.setWindowTitle("Python for GUI")
dialog.show()
sys.exit(app.exec_())
