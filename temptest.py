from PySide6.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication()
    widget = MyWidget()
    widget.show()
    app.exec()