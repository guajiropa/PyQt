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

        layout = QVBoxLayout()
        label = QLabel("Hello Qt World!!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

#------------------------------------------------------------------------------------------------------


app = QApplication(sys.argv)
dialog = HelloWorld()
#dialog.resize(250, 150)
#dialog.move(300, 300)
dialog.setWindowTitle("Python for GUI")
dialog.show()
sys.exit(app.exec_())
