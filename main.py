import random

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QSystemTrayIcon,
    QMenu)
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtCore import QTimer, Qt, QPoint

app = QApplication()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 定义宠物的默认大小和位置
        self.mouse_pos = None
        self.setGeometry(1000, 500, 200, 200)
        # 设置窗口标志为置顶显示
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 将 QWidget 的背景设置为半透明

        # 设置后台托盘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("static/meditation.png"))  # 使用自己的图标
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
        """)

        self.tray_icon.setContextMenu(self.menu)

        # 加载图片资源
        self.meditation_img = QPixmap("static/meditation.png")
        self.meditation_img = self.meditation_img.scaled(120, 120, Qt.KeepAspectRatio)
        self.stand_img = QPixmap("static/stand.png")
        self.stand_img = self.stand_img.scaled(120, 120, Qt.KeepAspectRatio)

        # 创建显示控件
        self.pet_label = QLabel(self)
        self.pet_label.setPixmap(self.meditation_img)
        # self.pet_label.setAttribute(Qt.WA_TranslucentBackground)  # 将 QWidget 的背景设置为半透明
        self.pet_label.show()
        self.increase_text = QLabel(self)
        self.increase_text.setGeometry(30, 0, 20, 15)
        self.increase_text.setText('hello')
        self.increase_text.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_text)

    def update_text(self) -> None:
        x, y = self.increase_text.pos().x(), self.increase_text.pos().y()
        if y < 10:
            self.increase_text.move(x, y + 20)
            increase = str(int(random.uniform(0.7, 1.3) * 20))
            self.increase_text.setText(increase)
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
            if not self.timer.isActive():
                self.timer.start(1000 // 10)  # 每秒30帧
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
