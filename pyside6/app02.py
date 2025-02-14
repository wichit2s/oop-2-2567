from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication([])
window = QMainWindow()
# window = QWidget()
window.resize(600, 400)
window.show()
app.exec()
