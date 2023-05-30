from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Slot

from object.PersonClass.Character import Character
from static.form import Ui_Form


def init_character():
    return Character('kegehe')


@Slot()
def on_exit():
    ...


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化角色信息
        self.character = init_character()
        # 初始化窗口属性
        self.setWindowTitle('text')  # 设置窗口标题
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.start_1)

    # @Slot()
    # def start_timer(self):
    #     if not self.timer1.isActive():
    #         self.timer1.start(1000)
    #
    # @Slot()
    # def breakthrough(self):
    #     di = []
    #     if int(self.character.exp) <= 1:
    #         print('not e')
    #     else:
    #         self.character.breakthrough()
    #
    @Slot()
    def start_1(self):
        self.character.exp += self.character.efficiency
        # self.label1.setText(str(self.character.exp))


if __name__ == '__main__':
    app = QApplication()
    app.aboutToQuit.connect(on_exit)
    widget = MainWidget()
    widget.show()
    app.exec()
