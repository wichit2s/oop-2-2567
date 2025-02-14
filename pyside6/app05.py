#### layouts
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLabel


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        anime = QPixmap('anime.jpg')
        self.setWindowIcon(anime)
        self.setWindowTitle('Anime Calculator')
        self.resize(400, 600)
        self.create_menubar()
        self.create_central_widget()
        self.create_statusbar()
        self.show()

    def create_central_widget(self):
        center = QWidget()
        layout = QGridLayout()
        center.setLayout(layout)
        led = QLabel('DISPLAY AREA')
        led.setStyleSheet('background-color: white;')
        layout.addWidget(led, 1, 1, 1, 4)
        labels = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
        ]
        for r in range(2, 6): # 2 3 4 5 6
            for c in range(1, 5): # 1 2 3 4
                widget = QPushButton(labels[r-2][c-1])
                widget.setStyleSheet('font-size: 60px;')
                layout.addWidget(widget, r, c)
        eq = QPushButton('=')
        eq.setStyleSheet('font-size: 60px;')
        layout.addWidget(eq, 6, 1, 1, 4)
        self.setCentralWidget(center)

    def create_statusbar(self):
        statusbar = self.statusBar()
        statusbar.showMessage('Calculator ready!!')

    def create_menubar(self):
        menubar = self.menuBar()
        menubar.addMenu('&File')
        menubar.addMenu('&Edit')
        menubar.addMenu('&Help')


app = QApplication([])
calc = Calculator()
app.exec()