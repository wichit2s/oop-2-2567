from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QTextEdit, QPlainTextEdit, QCheckBox, QPushButton, \
    QLabel, QDial


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.create_menubar()
        self.create_central_widget()
        self.create_statusbar()
        self.show()

    def create_menubar(self):
        pass

    def create_statusbar(self):
        pass

    def create_central_widget(self):
        # center = QLineEdit() # single line input
        # center = QTextEdit() # multi-line input
        # center = QPlainTextEdit()
        # center = QCheckBox("Pick me I'm green!!!")
        # center = QPushButton('Click meee')
        image = QPixmap('anime.jpg')
        center = QLabel('QLabel', pixmap=image)
        center = QDial()
        # center.setStyleSheet('font-size: 72px; color: green;')
        self.setCentralWidget(center)


app = QApplication([])
window = MyWindow()
app.exec()