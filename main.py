import random

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QSystemTrayIcon,
    QMenu, QSizePolicy, QPushButton)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve, \
    QParallelAnimationGroup

from object.PersonClass.Character import Character

app = QApplication()


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.animate = None
        self.animation = None
        self.character = Character('kegehe')

        # self.setStyleSheet("""
        #     QWidget{
        #         border:1px solid black;
        #     }
        # """)

        # 定义窗体默认大小和位置
        self.mouse_pos = None
        self.setGeometry(1000, 500, 200, 200)
        # 设置窗口标志为置顶显示
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 将 QWidget 的背景设置为半透明

        # 设置后台托盘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("static/meditation.png"))  # 使用图标
        self.tray_icon.show()

        # 设置托盘菜单
        self.menu = QMenu()

        self.exit_action = QAction('隐藏', self.menu)
        self.exit_action.triggered.connect(lambda: self.setVisible(False))
        self.menu.addAction(self.exit_action)

        self.exit_action = QAction('显示', self.menu)
        self.exit_action.triggered.connect(lambda: self.setVisible(True))
        self.menu.addAction(self.exit_action)

        self.exit_action = QAction('退出', self.menu)
        self.exit_action.triggered.connect(lambda: QApplication.quit())
        self.menu.addAction(self.exit_action)

        self.menu.setStyleSheet("""
            QMenu{
                background-clip: padding-box;
                font-size: 12px;
                border-radius: 10px;
            }
            QMenu::item:selected {  
                background-color: #007bff;  
                color: white;  
            }
        """)  # 设置托盘菜单样式

        self.tray_icon.setContextMenu(self.menu)

        # 加载图片资源
        self.meditation_img = QPixmap("static/meditation.png")
        self.meditation_img = self.meditation_img.scaled(120, 120, Qt.KeepAspectRatio)
        self.stand_img = QPixmap("static/stand.png")
        self.stand_img = self.stand_img.scaled(120, 120, Qt.KeepAspectRatio)

        # 创建显示控件
        self.name_text = QLabel(self)
        self.name_text.setGeometry(0, 0, 50, 20)
        self.name_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.name_text.setText(f'名称：{self.character.name}')

        self.lv_text = QLabel(self)
        self.lv_text.setGeometry(0, 20, 50, 20)
        self.lv_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lv_text.setText(f'lv: {self.character.lv}')

        self.cultivation_text = QLabel(self)
        self.cultivation_text.setGeometry(0, 40, 50, 20)
        self.cultivation_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.cultivation_text.setText(f'总: {self.character.cultivation}')

        self.pet_label = QLabel(self)
        self.pet_label.setPixmap(self.meditation_img)
        # self.pet_label.setAttribute(Qt.WA_TranslucentBackground)  # 将 QWidget 的背景设置为半透明
        self.pet_label.show()

        self.increase_text = QLabel(self)
        self.increase_text.setGeometry(60, 0, 20, 15)
        self.increase_text.setAlignment(Qt.AlignCenter)
        self.increase_text.setStyleSheet("""
            QLabel{
                color: green;
            }
        """)

        self.breakthrough_button = QPushButton(self)
        self.breakthrough_button.setText('突破')
        self.breakthrough_button.setGeometry(55, 60, 30, 20)
        self.breakthrough_button.hide()
        self.breakthrough_button.clicked.connect(self.breakthrough)

        self.meditate_timer = QTimer(self)
        self.meditate_timer.timeout.connect(self.increase_meditate)

        self.text_move_timer = QTimer(self)
        self.text_move_timer.timeout.connect(self.update_text)

    def breakthrough(self):
        self.character.breakthrough()

    def increase_meditate(self):
        increase = self.character.meditate()
        # if self.character.cultivation >= 10000:
        #     increase_text = f'{self.character.cultivation / 10000}万'
        # elif self.character.cultivation >= 1000:
        #     increase_text = f'{self.character.cultivation / 1000}千'
        # elif self.character.cultivation >= 100:
        #     increase_text = f'{self.character.cultivation / 100}百'
        # elif self.character.cultivation >= 10:
        #     increase_text = f'{self.character.cultivation / 10}十'
        self.cultivation_text.setText(f'总: {self.character.cultivation}')

        self.increase_text.show()
        self.increase_text.setText(str(increase))

        self.animate = QPropertyAnimation(self.increase_text, b'pos')
        self.animate.setStartValue(QPoint(50, 100))
        self.animate.setEndValue(QPoint(50, 0))
        self.animate.setDuration(2000)
        self.animate.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation = QParallelAnimationGroup()
        self.animation.addAnimation(self.animate)
        self.animation.finished.connect(lambda: self.increase_text.hide())
        self.animation.start()

    def update_text(self) -> None:
        x, y = self.increase_text.pos().x(), self.increase_text.pos().y()
        if y < 10:
            self.increase_text.move(x, y + 20)
        else:
            self.increase_text.move(x, y - 1)

    def mousePressEvent(self, event) -> None:
        """
        鼠标点击事件
        Args:
            event: 鼠标事件
        Returns:
            None
        """
        if event.button() == Qt.LeftButton:
            # 记录点击位置，用于移动
            self.mouse_pos = event.globalPosition().toPoint() - self.pos()
            # 图片互动
            if not self.meditate_timer.isActive():
                self.meditate_timer.start(5000)  # 5秒增加一次
        if event.button() == Qt.RightButton:
            # 退出
            ...

        event.accept()

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件
        Args:
            event: 鼠标事件
        Returns:
            None
        """
        self.move(event.globalPosition().toPoint() - self.mouse_pos)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.mouse_pos = QPoint()
        event.accept()

    def enterEvent(self, event) -> None:
        """
        鼠标进入事件
        Args:
            event: 鼠标事件
        Returns:
            None
        """
        self.pet_label.setPixmap(self.stand_img)

    def leaveEvent(self, event) -> None:
        """
        鼠标离开事件
        Args:
            event: 鼠标事件
        Returns:
            None
        """
        self.pet_label.setPixmap(self.meditation_img)


if __name__ == "__main__":
    window = MyWindow()
    window.show()
    app.exec()
