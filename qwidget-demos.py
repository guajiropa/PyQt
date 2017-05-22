"""
#   Author      :   Robert James Patterson
#   Created     :   5/22/2017
#   Modified    :   5/22/2017
#   Project     :   qwigets-demos.py
#   Synopsis    :   Basic Qt widgets demo application, just to play around with
#                    some of the different widgets available from the Qt widgets
#                    library.
#
"""
# Import supporting modules for the QWidgetsDemos() class.
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")
        self.setWindowIcon(QIcon("downloader.png"))

        self.line_edit = QLineEdit()
        self.label = QLabel()
        self.checkbox = QCheckBox()
        self.combobox = QComboBox()
        close_button = QPushButton("Close")
        self.checkbox.setText("Check me out!")

        self.combobox.addItems(["PyQt", "PyTkinter",
                                "PyGtk", "PySimpleGui"])

        self.label.setText("<b>Hello PyQt</b>")

        self.line_edit.setPlaceholderText("Type some text here . . .")
        text = self.line_edit.text()
        #print("You typed : {0}".format(text))

        # This section is for our event handlers.
        close_button.clicked.connect(self.close)
        self.checkbox.clicked.connect(self.selected)
        self.combobox.currentIndexChanged.connect(self.combo_selected)
        # Put the dialog window together.
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

    def combo_selected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_text + " is at index : " + current_index)

    def selected(self):
        if self.checkbox.isChecked():
            self.label.setText("<b><em>You checked the checkbox!</em></b>")
        else:
            self.label.setText("The checkbox was unchecked.")


def main():
    app = QApplication(sys.argv)
    dialog = QWidgetDemos()
    dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

