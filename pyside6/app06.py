from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.typed = ''
        self.button = QPushButton('Click me')
        self.setCentralWidget(self.button)
        self.show()
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print('button click แล่วเด้อ')

    def keyPressEvent(self, event):
        self.typed += event.text()
        self.statusBar().showMessage(self.typed)

    def mouseMoveEvent(self, event):
        message = f'Moved {event.pos()}'
        self.statusBar().showMessage(message)

    def mousePressEvent(self, event):
        message = f'Pressed {event.pos()}'
        self.statusBar().showMessage(message)

app = QApplication([])
window = MyApp()
app.exec()