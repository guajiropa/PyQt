"""
#   Author      :   Robert James Patterson
#   Created     :   5/21/2017
#   Modified    :   5/22/2017
#   Project     :   pydownloader.py
#   Synopsis    :   Downloads files from a URL provided by the end user using Python and Qt5
#
"""
# Import supporting modules for the Downloader() class.
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import urllib.request


class Downloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        # Declare the layout style.
        layout = QVBoxLayout()

        # Declare components used.
        # NOTE: the 'self' declaration makes these
        #       instance wide variables.
        self.url_text = QLineEdit()
        self.save_location_text = QLineEdit()
        self.progress_bar = QProgressBar()
        download_button = QPushButton("Download")
        browse_button = QPushButton("Browse")
        quit_button = QPushButton("Close")

        # Set the placeholder text for the text boxes.
        self.url_text.setPlaceholderText("URL")
        self.save_location_text.setPlaceholderText("File save location")

        # Set up the progress bar to list the progress
        # as a value on the graphic on this control.
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignHCenter)

        # Add the widgets to the layout.
        layout.addWidget(self.url_text)
        layout.addWidget(self.save_location_text)
        layout.addWidget(browse_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(download_button)
        layout.addWidget(quit_button)

        # Bring it all together to create the app window.
        self.setLayout(layout)
        self.setWindowIcon(QIcon("downloader.png"))
        self.setWindowTitle("PyDownloader")
        self.setFocus()

        # Event handler for the quit_button click event.
        quit_button.clicked.connect(self.close)

        # Event handler for the download_button click event.
        download_button.clicked.connect(self.download)

        # Event handler for browse_button click event.
        browse_button.clicked.connect(self.browse_file)

    def browse_file(self):
        """ This is the method to allow us to browse the local
            device and set the location to download the file to.
        """
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As",
                                                directory=".",
                                                filter="All Files (*.*)")

        self.save_location_text.setText(QDir.toNativeSeparators(str(save_file[0])))

    def download(self):
        """ This is the method that does the actual downloading of 
            and the saving of the file specified by the end user.
        """
        url = self.url_text.text()
        save_location = self.save_location_text.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Download failed : {0}".format(e))
            return

        QMessageBox.information(self, "Information", "Your download is complete.")
        # Reset the widgets on the form to their default values.
        self.progress_bar.setValue(0)
        self.url_text.setText("")
        self.save_location_text.setText("")

    def report(self, blocknum, blocksize, totalsize):
        """ This is the method that drives the reporting done by 
            the progress_bar widget.
        """
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress_bar.setValue(int(percent))


def main():
    app = QApplication(sys.argv)
    dl = Downloader()
    dl.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
