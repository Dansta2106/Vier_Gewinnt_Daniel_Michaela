import random, time

# Spielfeld wird als Listen in Listen erstellt
zeile1 = [0, 0, 0, 0, 0, 0, 0]
zeile2 = [0, 0, 0, 0, 0, 0, 0]
zeile3 = [0, 0, 0, 0, 0, 0, 0]
zeile4 = [0, 0, 0, 0, 0, 0, 0]
zeile5 = [0, 0, 0, 0, 0, 0, 0]
zeile6 = [0, 0, 0, 0, 0, 0, 0]

# Das Spielfeld besteht aus 6 Zeilen und 7 Spalten
spielfeld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6]

spieler = 1
runden_zaehler = 0
end = False
win = "Niemand"
fehler = False
ki = False
pseudo_runde = 0

# Test

class Spieler():

    def spielerWechsel(self):
        """ Spieler wird gewechselt

        Diese Methode setzt die globale Variable Spieler auf 1 oder -1
        und bestimmt dadurch, welcher Spieler am Zug ist.

        Returns
        -------
        int
            Zahl des Spielers, welche -1 oder 1 sein kann
        """
        global spieler
        if spieler == 1:
            spieler -= 2
        else:
            spieler += 2
        return spieler

    def spielerAusgabe(self):
        message = "Niemand"
        """ Aktueller Spieler wird ausgegeben

        Diese Methode gibt den aktuellen Spieler
        am Bildschirm aus.
        """
        if spieler == 1:
            if ki:
                message = "Sie sind dran"
            else:
                message = "Spieler 1 ist dran"
        if spieler == -1:
            message = "Spieler 2 ist dran"
        print(message)
        return message


class Spielfeld(Spieler):

    def setSpielfeld(self, eingabe_start: str):
        """ Das Spielfeld wird mit Spielzügen erweitert

        Diese Methode überprüft die Korrektheit der Eingabe
        und ändert den untersten nicht besetzten Wert in der
        eingegebenen Spalte in den Wert des aktuellen Spielers.
        Gibt bei falscher Eingabe einen Fehlertext aus.

        Parameters
        ----------
        eingabe_start : str
            Spielerwert wird in Spalte 'eingabe_start' gesetzt
        """
        global fehler
        global spielfeld
        try:
            eingabe = int(eingabe_start)
            if 1 <= eingabe <= 7 and spielfeld[0][eingabe - 1] == 0:
                for reihe in spielfeld[::-1]:
                    if reihe[eingabe - 1] == 0:
                        reihe[eingabe - 1] = spieler
                        break
            else:
                print("Fehler, falsche Eingabe")
                fehler = True
        except ValueError:
            print("Fehler, falsche Eingabe")
            fehler = True
            Spieler().spielerWechsel()

    def printSpielfeld(self):
        """ Gibt Spielfeld aus

        Diese Methode zeigt dem Spieler das aktuelles Spielfeld
        und gibt es am Bildschirm aus.
        """
        zeile_ausgabe = 0
        if (ki and spieler == 1 and fehler == False) or ki == False:
            while zeile_ausgabe < 6:
                print(spielfeld[zeile_ausgabe])
                zeile_ausgabe += 1


class KI(Spielfeld):

    def kiAbfrage(self, ki_abfrage: str):
        """ KI als Gegner auswählen

        Diese Methode fragt mittels Texteingabe ab, ob gegen die KI
        gespielt werden soll. Falls die KI zum Gegenspieler wird, wird
        die globale Variable 'ki' auf True gesetzt. Falls nicht gegen
        die KI gespielt wird, bleibt der Initialwert auf False.

        Parameters
        ----------
        ki_abfrage : str
            'ki_abfrage' wird auf unterschiedliche Schreibweisen
            des Wortes 'ja' überprüft
        """
        global ki

        if ki_abfrage == "Ja" or ki_abfrage == "J" or ki_abfrage == "j" or ki_abfrage == "ja" or ki_abfrage == "yes" or ki_abfrage == "Yes" or ki_abfrage == "y" or ki_abfrage == "Y":
            ki = True

    def kiZug(self, sleep: float):
        """ Die KI tätigt einen Zug

        Diese Methode erezeugt eine Zufallszahl zwischen 1 und 7
        und setzt diese auf einen den Spielregeln entsprechend
        gültigen Platz in der Spalte.

        Parameters
        ----------
        sleep : float
            Dieser Parameter verzögert den Zug der KI um 1.5 Sekunden,
            um den Anschein zu erwecken, dass diese 'nachdenkt'
        """
        if ki and spieler == -1:
            time.sleep(sleep)
            random_number = random.randint(1, 7)
            if 1 <= random_number <= 7 and spielfeld[0][random_number - 1] == 0:
                for reihe in spielfeld[::-1]:
                    if reihe[random_number - 1] == 0:
                        reihe[random_number - 1] = spieler
                        break
                print(f'Die KI hat in der Spalte {random_number} gespielt')


class Gewinnabfrage(KI):

    def erhoeheRunde(self):
        """ Rundenzähler

        Diese Methode zählt die Anzahl der Runden mit.
        """
        global runden_zaehler
        runden_zaehler += 1
        return runden_zaehler

    def horizontaleAbfrage(self):
        """ Horizontale Gewinnabfrage

        Diese Methode überprüft, ob vier Werte des gleichen Spielers in
        derselben Zeile direkt nebeneinander liegen.

        Returns
        -------
        condition_horizontal : int
            zählt die Anzahl der gleichen Spielerwerte nebeneinander mit
        """
        global spieler
        global end
        global win
        global spielfeld
        condition_horizontal = 0
        zeilenzahl = 0
        while zeilenzahl <= 5:
            condition_horizontal = 0
            spaltenzahl = 0
            while spaltenzahl <= 6:
                if spieler == 1:
                    if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                        win = "Spieler 2"
                        condition_horizontal += 1
                        if condition_horizontal >= 4:
                            end = True
                            break
                    else:
                        condition_horizontal = 0
                if spieler == -1:
                    if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                        win = "Spieler 1"
                        condition_horizontal += 1
                        if condition_horizontal >= 4:
                            end = True
                            print("horizontal")
                            break
                    else:
                        condition_horizontal = 0
                spaltenzahl += 1
            if end:
                break
            zeilenzahl += 1
        return condition_horizontal

    def vertikaleAbfrage(self):
        """ Vertikale Gewinnabfrage

        Diese Methode überprüft, ob vier Werte des gleichen Spielers in
        derselben Spalte direkt übereinander liegen.

        Returns
        -------
        condition_vertikal : int
            zählt die Anzahl der gleichen Spielerwerte übereinander mit
        """
        global end
        global spieler
        global win
        global spielfeld
        condition_vertikal = 0
        runde_spalte = 0
        while runde_spalte <= 6:
            runde_zeile = 0
            condition_vertikal = 0
            while runde_zeile <= 5:
                spaltenzahl = 0 + runde_spalte
                zeilenzahl = 0 + runde_zeile
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_vertikal += 1
                            if condition_vertikal >= 4:
                                end = True
                        else:
                            if zeilenzahl == 7:
                                spaltenzahl += 1
                                if spaltenzahl != 7:
                                    zeilenzahl = -1
                            condition_vertikal = 0
                    if spieler == -1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_vertikal += 1
                            if condition_vertikal >= 4:
                                end = True
                                print("Vertikal")
                        else:
                            if zeilenzahl == 7:
                                spaltenzahl += 1
                                if spaltenzahl != 7:
                                    zeilenzahl = -1
                            condition_vertikal = 0
                    if end:
                        break
                    else:
                        win = "Niemand"
                    zeilenzahl += 1
                condition_vertikal = 0
                runde_zeile += 1
            runde_spalte += 1
        return condition_vertikal

    def diagonalRechtsAbfrage(self):
        """ Gewinnabfrage diagonal rechts

        Diese Methode überprüft, ob vier Werte des gleichen Spielers
        diagonal nach rechts direkt aneinanderliegen.

        Returns
        -------
        condition_diagonal_rechts : int
            zählt die Anzahl der gleichen Spielerwerte diagonal nach rechts
            mit
        """
        condition_diagonal_rechts = 0
        runde_zeile = 0
        global end
        global spieler
        global win
        global spielfeld
        while runde_zeile <= 6:
            runde_spalte = 0
            condition_diagonal_rechts = 0
            while runde_spalte <= 5:
                spaltenzahl = runde_spalte + 0
                zeilenzahl = runde_zeile + 0
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_rechts += 1
                            if condition_diagonal_rechts >= 4:
                                end = True
                        else:
                            if spaltenzahl == 7:
                                break
                            condition_diagonal_rechts = 0
                    if spieler == -1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_diagonal_rechts += 1
                            if condition_diagonal_rechts >= 4:
                                end = True
                                print("DiagonalRechts")
                        else:
                            if spaltenzahl == 7:
                                break
                            condition_diagonal_rechts = 0
                    if end:
                        break
                    else:
                        win = "Niemand"

                    zeilenzahl += 1
                    if spaltenzahl <= 5:
                        spaltenzahl += 1
                condition_diagonal_rechts = 0
                runde_spalte += 1
            runde_zeile += 1
        return condition_diagonal_rechts

    def diagonalLinksAbfrage(self):
        """ Gewinnabfrage diagonal links

        Diese Methode überprüft, ob vier Werte des gleichen Spielers
        diagonal nach links direkt aneinanderliegen.

        Returns
        -------
        condition_diagonal_links : int
            zählt die Anzahl der gleichen Spielerwerte diagonal nach
            links mit
        """
        global end
        global spieler
        global win
        global spielfeld
        condition_diagonal_links = 0
        runde_zeile = 0
        while runde_zeile <= 6:
            runde_spalte = 0
            condition_diagonal_links = 0
            while runde_spalte <= 5:
                spaltenzahl = 6 - runde_spalte
                zeilenzahl = 0 + runde_zeile
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_links += 1
                            if condition_diagonal_links >= 4:
                                end = True
                        else:
                            condition_diagonal_links = 0
                            if spaltenzahl == 0:
                                break
                    if spieler == -1:
                        if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_diagonal_links += 1
                            if condition_diagonal_links >= 4:
                                end = True
                                print("DiagonalLinks")
                        else:
                            condition_diagonal_links = 0
                            if spaltenzahl == 0:
                                break
                    if end:
                        break
                    else:
                        win = "Niemand"
                    zeilenzahl += 1
                    spaltenzahl -= 1
                condition_diagonal_links = 0
                runde_spalte += 1
            runde_zeile += 1

        return condition_diagonal_links


class Spielablauf(Gewinnabfrage):

    def spielRunden(self):
        """ Spielablauf

        Diese Methode erzeugt den Spielablauf und ruft die Gewinnabfragen
        auf. Bei einem Sieg wird am Bildschirm ausgegeben, wer gewonnen
        hat. Ein Unentschieden wird auch berücksichtigt.
        """
        global end
        global win
        global pseudo_runde
        global fehler
        global runden_zaehler
        while end != True:
            if runden_zaehler == 0 and pseudo_runde == 0:
                KI().kiAbfrage(input("Möchten Sie gegen eine künstliche Intelligenz spielen?"))

            self.printSpielfeld()
            if (ki and spieler == 1) or ki == False:
                beenden = str(input("Wollen Sie das Spiel beenden?"))
                if beenden == "Ja" or beenden == "J" or beenden == "j" or beenden == "ja" or beenden == "yes" or beenden == "Yes" or beenden == "y" or beenden == "Y":
                    break


            if ki and spieler == -1:
                KI().kiZug(1.5)
            else:
                Spieler().spielerAusgabe()
                Spielfeld().setSpielfeld(input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)"))
                if ki:
                    Spielfeld().printSpielfeld()

            if fehler == False:
                Spieler().spielerWechsel()



            if fehler == False:
                self.erhoeheRunde()

            Gewinnabfrage().horizontaleAbfrage()
            Gewinnabfrage().vertikaleAbfrage()
            Gewinnabfrage().diagonalRechtsAbfrage()
            Gewinnabfrage().diagonalLinksAbfrage()

            pseudo_runde += 1
            fehler = False

            if runden_zaehler == 42 and win == 'Niemand':
                end = True
                win = "Unentschieden, niemand"

        if ki and win == "Spieler 2":
            win = "Die KI"

        self.printSpielfeld()

        print(f'{win} hat gewonnen!')
        print("Danke für's Spielen!!")


if __name__ == '__main__':
    print("Willkommen im Spiel '4 gewinnt'! Sie haben die Auswahl gegen einen Mensch oder eine künstliche Intelligenz zu spielen.")
    Spielablauf().spielRunden()

