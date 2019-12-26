import sys
from PyQt5 import uic, QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


# Проект по pygame должен включать:
# наличие двух уровней
# наличие текстур
# Анимация героя
# меню игры
# инструкция по клавишам
# скрин конца игры


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('piano.ui', self)

        self.butts = [self.C_1, self.D_1, self.E_1, self.F_1, self.G_1, self.A_1, self.H_1,
                      self.C_1d, self.D_1d, self.F_1d, self.G_1d, self.A_1d]
        self.sounds = ['sounds/violin_C4_025_forte_arco-normal.mp3',
                       'sounds/violin_D4_025_forte_arco-normal.mp3',
                       'sounds/violin_E4_025_forte_arco-normal.mp3',
                       'sounds/violin_F4_025_forte_arco-normal.mp3',
                       'sounds/violin_G4_025_forte_arco-normal.mp3',
                       'sounds/violin_A4_025_forte_arco-normal.mp3',
                       'sounds/violin_B4_025_forte_arco-normal.mp3',
                       'sounds/violin_Cs4_025_forte_arco-normal.mp3',
                       'sounds/violin_Ds4_025_forte_arco-normal.mp3',
                       'sounds/violin_Fs4_025_forte_arco-normal.mp3',
                       'sounds/violin_Gs4_025_forte_arco-normal.mp3',
                       'sounds/violin_As4_025_forte_arco-normal.mp3']
        for i in self.butts:
            i.clicked.connect(self.playSound)

    def keyPressEvent(self, event):
        indx = -1
        if event.key() == Qt.Key_A:
            indx = 0
        elif event.key() == Qt.Key_S:
            indx = 1
        elif event.key() == Qt.Key_D:
            indx = 2
        elif event.key() == Qt.Key_F:
            indx = 3
        elif event.key() == Qt.Key_G:
            indx = 4
        elif event.key() == Qt.Key_H:
            indx = 5
        elif event.key() == Qt.Key_J:
            indx = 6
        elif event.key() == Qt.Key_W:
            indx = 7
        elif event.key() == Qt.Key_E:
            indx = 8
        elif event.key() == Qt.Key_T:
            indx = 9
        elif event.key() == Qt.Key_Y:
            indx = 10
        elif event.key() == Qt.Key_U:
            indx = 11
        print(indx)
        if indx != -1:
            self.playSoundByKey(indx)

    def playSound(self):
        filename = self.sounds[self.butts.index(self.sender())]
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def playSoundByKey(self, indx):
        filename = self.sounds[indx]
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
