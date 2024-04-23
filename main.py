import sys
from datetime import timedelta

from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.setWindowTitle("Kalkulator kalorii")
        self.ui.setupUi(self)
        self.show()
        self.ui.dodaj.clicked.connect(self.dodawanie_posilku)




    def plec(self):
        kobieta = self.ui.kobieta.text()
        mezczyzna = self.ui.mezczyzna.text()



        if mezczyzna == 1:
            jaka_plec = mezczyzna
        elif mezczyzna == 0:
            jaka_plec = kobieta

            print(jaka_plec)



    def aktywnosc(self):
        if self.ui.mala_aktywnosc.isChecked():
            return 'niska'
        elif self.ui.srednia_aktywnosc.isChecked():
            return 'srednia'
        elif self.ui.duza_aktywnosc.isChecked():
            return 'duza'






    def dodawanie_posilku(self):

        nazwa = self.ui.nazwa_posilku.text()
        kaloriie = self.ui.kaloriie_jedzenie.text()

        print(kaloriie + nazwa)
        lista_kalorii = [kaloriie]
        lista_kalorii.append(kaloriie)
        self.ui.liczba_kalorii.setText(lista_kalorii[0])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec())


