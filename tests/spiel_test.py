import unittest

from spiel import spiel


class VierGewinntTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.spieler = spiel.spieler
        self.feld = spiel.Spielfeld()
        self.end = spiel.Spielablauf()

        self.spielerAusgabetest = spiel.Spieler.spielerAusgabe(self.spieler)

    def test_SpielerAusgabe(self):
        self.assertEqual(self.spielerAusgabetest, "Spieler 1 ist dran")

    def test_setSpielfeld(self):
        spiel.spieler = 1
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.assertEqual(self.feld.spielfeld[5][0], 1)
        self.assertEqual(self.feld.spielfeld[4][0], 1)
        self.assertEqual(self.feld.spielfeld[3][0], 1)
        self.assertEqual(self.feld.spielfeld[2][0], 1)
        spiel.spieler = -1
        self.feld.setSpielfeld('2')
        self.feld.setSpielfeld('2')
        self.feld.setSpielfeld('2')
        self.feld.setSpielfeld('2')
        self.assertEqual(self.feld.spielfeld[5][1], -1)
        self.assertEqual(self.feld.spielfeld[4][1], -1)
        self.assertEqual(self.feld.spielfeld[3][1], -1)
        self.assertEqual(self.feld.spielfeld[2][1], -1)



    def test_falscheEingabe1(self):
        falsche_eingabe1 = str(8)
        self.feld.setSpielfeld(falsche_eingabe1)
        self.assertTrue(spiel.fehler)

    def test_falscheEingabe2(self):
        falsche_eingabe2 = "hallo"
        self.feld.setSpielfeld(falsche_eingabe2)
        self.assertTrue(spiel.fehler)

    def test_vertikaleAbfrage_Spieler1(self):
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.vertikaleAbfrage()
        self.assertTrue(self.end)

    def test_horizontaleAbfrage_Spieler1(self):
        self.feld.setSpielfeld("1")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("4")
        self.feld.horizontaleAbfrage()
        self.assertTrue(self.end)

    def test_diagonalRechtsAbfrage_Spieler1(self):
        self.feld.setSpielfeld("1")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.diagonalRechtsAbfrage()
        self.assertTrue(self.end)

    def test_diagonalLinksAbfrage_Spieler1(self):
        self.feld.setSpielfeld("7")
        self.feld.setSpielfeld("6")
        self.feld.setSpielfeld("6")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.diagonalLinksAbfrage()
        self.assertTrue(self.end)

    def test_vertikaleAbfrage_Spieler2(self):
        spiel.spieler = -1
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.setSpielfeld('1')
        self.feld.vertikaleAbfrage()
        self.assertTrue(self.end)

    def test_horizontaleAbfrage_Spieler2(self):
        spiel.spieler = -1
        self.feld.setSpielfeld("1")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("4")
        self.feld.horizontaleAbfrage()
        self.assertTrue(self.end)

    def test_diagonalRechtsAbfrage_Spieler2(self):
        spiel.spieler = -1
        self.feld.setSpielfeld("1")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("2")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("3")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.diagonalRechtsAbfrage()
        self.assertTrue(self.end)

    def test_diagonalLinksAbfrage_Spieler2(self):
        spiel.spieler = -1
        self.feld.setSpielfeld("7")
        self.feld.setSpielfeld("6")
        self.feld.setSpielfeld("6")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("5")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.setSpielfeld("4")
        self.feld.diagonalLinksAbfrage()
        self.assertTrue(self.end)

if __name__ == '__main__':
    unittest.main()
