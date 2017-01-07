# 235 строк | 211 строк на шарпах
# Библиотеки
import sys
import Game

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSpinBox
from PyQt5.QtGui import QPainter, QBrush


class FormGame(QMainWindow):

    # Поля класса
    __start_game = object
    __rowsCount = object
    __colsCount = object
    __colorsCount = object
    __scoreLabel = object
    __game = object
    # Набор цветов для кружков
    __colors = [Qt.white, Qt.blue, Qt.red, Qt.yellow, Qt.green, Qt.magenta]

    # Конструктор класса
    def __init__(self):
        super().__init__()
        # Характеристика окна
        self.title = "Game"
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        # Мне нужна эта переменная для нормальной работы графиик, почему-то как в шарпах не пашет, вылетает
        self.helpIndex = 0
        # Вызов отрисовки UI
        self.init_ui()

    # Метод отрисовки UI
    def init_ui(self):
        # Создаем окошко с параметрами из init
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Создаем кнопку начала игры
        self.__start_game = QPushButton('Start', self)
        self.__start_game.move(400, 0)

        # Создаем текст боксы для количества rows, cols, colors
        self.__rowsCount = QSpinBox(self)
        self.__rowsCount.move(400, 50)
        self.__rowsCount.setValue(15)
        self.__colsCount = QSpinBox(self)
        self.__colsCount.move(400, 90)
        self.__colsCount.setValue(15)
        self.__colorsCount = QSpinBox(self)
        self.__colorsCount.move(400, 130)

        # Создаем label для очков
        self.__scoreLabel = QLabel(self)
        self.__scoreLabel.setText("Score")
        self.__scoreLabel.move(400, 160)

        # Привязка метода к нажатию кнопки
        self.__start_game.clicked.connect(self.click_on_button)

        self.show()

    # Нажатие мышки на поле
    def mousePressEvent(self, QMouseEvent):
        if self.__game.click(QMouseEvent.pos().x(), QMouseEvent.pos().y()):
            self.repaint()

    # Реакция на клик по кнопке
    def click_on_button(self):
        self.helpIndex = 1
        self.__game = Game.Game(self.__rowsCount.value(), self.__colsCount.value(), self.__colorsCount.value())
        # Перерисуем графику
        self.repaint()

    # Отрисовка графики
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.paint(qp)
        qp.end()

    # Метод отрисовке всего поля с шарами
    def paint(self, qp):
        # Выходит из метода если игра не создана
        if self.helpIndex == 0:
            return

        # Рисует поле шаров, если игра создана
        brush = QBrush(Qt.SolidPattern)
        self.__scoreLabel.setText(str(self.__game.score))
        for y in range(self.__game.rowCounts):
            for x in range(self.__game.columnCounts):
                brush.setColor(self.__colors[self.__game.field[y][x]])
                qp.setBrush(brush)
                qp.drawEllipse(x * 25, y * 25, 25, 25)

# Запуск как main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FormGame()
    sys.exit(app.exec_())