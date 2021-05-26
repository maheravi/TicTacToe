# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui")

        self.game = [[None for i in range(3)] for j in range(3)]

        self.game[0][0] = self.ui.btn_00
        self.game[0][1] = self.ui.btn_01
        self.game[0][2] = self.ui.btn_02
        self.game[1][0] = self.ui.btn_10
        self.game[1][1] = self.ui.btn_11
        self.game[1][2] = self.ui.btn_12
        self.game[2][0] = self.ui.btn_20
        self.game[2][1] = self.ui.btn_21
        self.game[2][2] = self.ui.btn_22
        self.game[2][2] = self.ui.btn_22
        self.ui.newgame.clicked.connect(self.NewGame)

        self.ui.show()

        self.player = 1
        self.player1_wins = 0
        self.player2_wins = 0
        self.draw = 0

        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play, i, j))

    def play(self, i, j):

        if self.game[i][j].text() == "":
            if self.player == 1:
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet('color: blue; background-color: #CCFFFF')
                self.player = 2
                if self.player == 2 and self.ui.rb_p_vs_cpu.isChecked():
                    while True:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.game[i][j].text() == "":
                            self.game[i][j].setText('O')
                            self.game[i][j].setStyleSheet('color: red; background-color: #FFCCCC')
                            self.player = 1
                            break

            elif self.player == 2 and self.ui.rb_p_vs_p.isChecked():
                self.game[i][j].setText('O')
                self.game[i][j].setStyleSheet('color: red; background-color: #FFCCCC')
                self.player = 1

        self.check()

    def Reset(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet('color: white; background-color: #e2e2e2')

    def NewGame(self):
        self.player = 1
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet('color: white; background-color: #e2e2e2')
                self.player1_wins = 0
                self.player2_wins = 0
                self.draw = 0
                self.ui.lbl_player1.setText(str(self.player1_wins))
                self.ui.lbl_player2.setText(str(self.player2_wins))
                self.ui.lbl_draw.setText(str(self.draw))

    def check(self):
        for j in range(3):
            if all(self.game[j][i].text() == 'X' for i in range(3)) or all(self.game[i][j].text() == 'X' for i in range(
                    3)):
                self.player1_wins += 1
                self.ui.lbl_player1.setText(str(self.player1_wins))
                msg_box = QMessageBox()
                msg_box.setText("بازیکن شماره یک برنده شد")
                msg_box.exec_()
                self.Reset()
            elif all(self.game[j][i].text() == 'O' for i in range(3)) or all(
                    self.game[i][j].text() == 'O' for i in range(3)):
                self.player2_wins += 1
                self.ui.lbl_player2.setText(str(self.player2_wins))
                msg_box = QMessageBox()
                msg_box.setText("بازیکن شماره دو برنده شد")
                msg_box.exec_()
                self.Reset()

        if self.game[2][0].text() == self.game[1][1].text() == self.game[0][2].text():
            if self.game[2][0].text() == 'X':
                self.player1_wins += 1
                self.ui.lbl_player1.setText(str(self.player1_wins))
                msg_box = QMessageBox()
                msg_box.setText("بازیکن شماره یک برنده شد")
                msg_box.exec_()
                self.Reset()

            elif self.game[2][0].text() == 'O':
                self.player2_wins += 1
                self.ui.lbl_player2.setText(str(self.player2_wins))
                msg_box = QMessageBox()
                msg_box.setText("بازیکن شماره دو برنده شد")
                msg_box.exec_()
                self.Reset()

        if all(self.game[i][i].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg_box = QMessageBox()
            msg_box.setText("بازیکن شماره یک برنده شد")
            msg_box.exec_()
            self.Reset()

        if all(self.game[i][i].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg_box = QMessageBox()
            msg_box.setText("بازیکن شماره دو برنده شد")
            msg_box.exec_()
            self.Reset()

        if all(self.game[i][0].text() is not "" for i in range(3)) and all(self.game[i][1].text() is not "" for i in range(3)) and all(self.game[i][2].text() is not "" for i in range(3)):
            self.draw += 1
            self.ui.lbl_draw.setText(str(self.draw))
            msg_box = QMessageBox()
            msg_box.setText("بازی مساوی شد")
            msg_box.exec_()
            self.Reset()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
