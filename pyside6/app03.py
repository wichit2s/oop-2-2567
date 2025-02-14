from PySide6.QtWidgets import QMainWindow, QApplication


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.show()

app = QApplication([])
window = MyWindow()
app.exec()
