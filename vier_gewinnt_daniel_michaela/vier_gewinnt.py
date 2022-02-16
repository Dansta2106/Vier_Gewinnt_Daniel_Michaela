import random, time



spieler = 1
runden_zaehler = 0
win = "Niemand"
fehler = False
ki = False

class Spielablauf:

    def __init__(self):
        self.feld = Spielfeld()
        self.end = False

    def spielRunden(self):
        """Spielablauf

        Diese Methode erzeugt den Spielablauf und ruft die Gewinnabfragen
        auf. Bei einem Sieg wird am Bildschirm ausgegeben, wer gewonnen
        hat. Ein Unentschieden wird auch berücksichtigt.
        """
        global win
        # Variable 'pseudo_runde' wurde nur erstellt, um bei einem Fehler in der ersten Runde den 'runden_zaehler'
        # nicht zu stören. So wird die KI-Abfrage nur einmal getätigt
        global fehler
        global runden_zaehler
        pseudo_runde = 0
        while self.end != True:
            if runden_zaehler == 0 and pseudo_runde == 0:
                KI().kiAbfrage(input("Möchten Sie gegen eine künstliche Intelligenz spielen?"))

            self.feld.printSpielfeld()
            if (ki and spieler == 1) or ki == False:
                beenden = str(input("Wollen Sie das Spiel beenden?"))
                if beenden == "Ja" or beenden == "J" or beenden == "j" or beenden == "ja" or beenden == "yes" or beenden == "Yes" or beenden == "y" or beenden == "Y":
                    break


            if ki and spieler == -1:
                KI().kiZug(1.5)
            else:
                Spieler().spielerAusgabe()
                self.feld.setSpielfeld(input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)"))
                if ki:
                    self.feld.printSpielfeld()

            if fehler == False:
                Spieler().spielerWechsel()



            if fehler == False:
                Runde().erhoeheRunde()

            self.end = self.feld.horizontaleAbfrage() or self.feld.vertikaleAbfrage() or self.feld.diagonalRechtsAbfrage() or self.feld.diagonalLinksAbfrage()

            pseudo_runde += 1
            fehler = False

            if runden_zaehler == 42 and win == 'Niemand':
                self.end = True
                win = "Unentschieden, niemand"

        if ki and win == "Spieler 2":
            win = "Die KI"

        self.feld.printSpielfeld()

        print(f'{win} hat gewonnen!')
        print("Danke für's Spielen!!")

class Spieler:

    def spielerWechsel(self):
        """Spieler wird gewechselt

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
        """Aktueller Spieler wird ausgegeben

        Diese Methode gibt den aktuellen Spieler
        am Bildschirm aus.

        Returns
        -------
        str
            String der angibt welcher Spieler am Zug ist
        """
        message = "Niemand ist dran"
        if spieler == 1:
            if ki:
                message = "Sie sind dran"
            else:
                message = "Spieler 1 ist dran"
        if spieler == -1:
            message = "Spieler 2 ist dran"
        print(message)
        return message


class Spielfeld:

    def __init__(self):
        # Spielfeld wird als Listen in Listen erstellt
        zeile1 = [0, 0, 0, 0, 0, 0, 0]
        zeile2 = [0, 0, 0, 0, 0, 0, 0]
        zeile3 = [0, 0, 0, 0, 0, 0, 0]
        zeile4 = [0, 0, 0, 0, 0, 0, 0]
        zeile5 = [0, 0, 0, 0, 0, 0, 0]
        zeile6 = [0, 0, 0, 0, 0, 0, 0]

        # Das Spielfeld besteht aus 6 Zeilen und 7 Spalten
        self.spielfeld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6]


    def setSpielfeld(self, eingabe_start: str):
        """Das Spielfeld wird mit Spielzügen erweitert

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
        try:
            eingabe = int(eingabe_start)
            # Es wird geprüft, ob es ein freies Feld in der angegebenen Reihe gibt
            # Sollte das der Fall sein, wird dieses Feld mit dem Spielerwert besetzt
            # Wenn eine falsche Eingabe getätigt wird, wird die Variable 'fehler' auf True geändert
            # um sicherzustellen, dass beispielsweise nicht der Spieler gewechselt wird, sondern
            # der gleiche Spieler nochmal an der Reihe ist
            if 1 <= eingabe <= 7 and self.spielfeld[0][eingabe - 1] == 0:
                for reihe in self.spielfeld[::-1]:
                    if reihe[eingabe - 1] == 0:
                        reihe[eingabe - 1] = spieler
                        break
            else:
                print("Fehler, falsche Eingabe")
                fehler = True
        except ValueError:
            print("Fehler, falsche Eingabe")
            fehler = True

    def printSpielfeld(self):
        """Gibt Spielfeld aus

        Diese Methode zeigt dem Spieler das aktuelle Spielfeld
        und gibt es am Bildschirm aus.
        """
        zeile_ausgabe = 0
        if (ki and spieler == 1 and fehler == False) or ki == False:
            while zeile_ausgabe < 6:
                print(self.spielfeld[zeile_ausgabe])
                zeile_ausgabe += 1

    def horizontaleAbfrage(self):
        """Horizontale Gewinnabfrage

        Diese Methode überprüft, ob vier Werte des gleichen Spielers in
        derselben Zeile direkt nebeneinander liegen.
        """
        global spieler
        global win
        zeilenzahl = 0
        while zeilenzahl <= 5:
            condition_horizontal = 0
            spaltenzahl = 0
            # durch die Variablen 'zeilenzahl' und 'spaltenzahl' kann auf jedes Element
            # der Liste einzeln zugegriffen werden
            # so wird von jeder Position die Horizontale Gewinnabfrage durchgeführt
            while spaltenzahl <= 6:
                if spieler == 1:
                    if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                        win = "Spieler 2"
                        condition_horizontal += 1
                        # Sollten mehrere gleiche Steine nebeneinander sein, wird hier
                        # die Variable 'condition_horizontal' jeweils um 1 erhöht
                        # sollte es irgendwann zu einer Unterbrechung der nebeneinander liegenden
                        # Steine kommen wird der Wert wieder auf 0 gesetzt um beim nächsten richtigen
                        # Stein wieder bei 1 anzufangen
                        if condition_horizontal >= 4:
                            return True
                    else:
                        condition_horizontal = 0
                if spieler == -1:
                    if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                        win = "Spieler 1"
                        condition_horizontal += 1
                        if condition_horizontal >= 4:
                            return True
                    else:
                        condition_horizontal = 0
                # 'spaltenzahl' wird um 1 erhöht, um in der momentanen Liste einen Schritt nach rechts zu machen
                spaltenzahl += 1
            # 'zeilenzahl' wird um 1 erhöht, sobald 'spaltenzahl' den Wert 7 erreicht hat, um in die
            # darüberliegende Zeile zu kommen und dort die horizontale Abfrage weiterzuführen
            zeilenzahl += 1
        return False


    def vertikaleAbfrage(self):
        """Vertikale Gewinnabfrage

        Diese Methode überprüft, ob vier Werte des gleichen Spielers in
        derselben Spalte direkt übereinander liegen.
        """
        global spieler
        global win
        # Die Variable 'runde_spalte' stellt sicher, dass zuerst aus jeder Position in der momentanen Spalte
        # nach oben iteriert wird, bevor die Spalte gewechselt wird
        runde_spalte = 0
        while runde_spalte <= 6:
            runde_zeile = 0
            condition_vertikal = 0
            while runde_zeile <= 5:
                # durch die Variablen 'zeilenzahl' und 'spaltenzahl' kann auf jedes Element
                # der Liste einzeln zugegriffen werden
                # so wird von jeder Position die Vertikale Gewinnabfrage durchgeführt
                spaltenzahl = runde_spalte
                zeilenzahl = runde_zeile
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_vertikal += 1
                            # Sollten mehrere gleiche Steine übereinander sein, wird hier
                            # die Variable 'condition_vertikal' jeweils um 1 erhöht
                            # sollte es irgendwann zu einer Unterbrechung der übereinander liegenden
                            # Steine kommen wird der Wert wieder auf 0 gesetzt um beim nächsten richtigen
                            # Stein wieder bei 1 anzufangen
                            if condition_vertikal >= 4:
                                return True
                        else:
                            if zeilenzahl == 7:
                                spaltenzahl += 1
                                if spaltenzahl != 7:
                                    zeilenzahl = -1
                            condition_vertikal = 0
                    if spieler == -1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_vertikal += 1
                            if condition_vertikal >= 4:
                                return True
                        else:
                            if zeilenzahl == 7:
                                spaltenzahl += 1
                                if spaltenzahl != 7:
                                    zeilenzahl = -1
                            condition_vertikal = 0
                    # 'zeilenzahl' wird um 1 erhöht um einen Schritt nach oben zu machen
                    zeilenzahl += 1
                condition_vertikal = 0
                # 'runde_zeile' wird um 1 erhöht, um beim nächsten Durchgang direkt in der nächsthöheren
                # Zeile anzufangen
                runde_zeile += 1
            # 'runde_spalte' wird um 1 erhöht, um beim nächsten Durchgang direkt in der nächsten Spalte anzufangen
            runde_spalte += 1
        return False

    def diagonalRechtsAbfrage(self):
        """Gewinnabfrage diagonal rechts

        Diese Methode überprüft, ob vier Werte des gleichen Spielers
        diagonal nach rechts direkt aneinanderliegen.
        """
        # Die Variable 'runde_zeile' stellt sicher, dass zuerst aus jeder Position in der momentanen Zeile
        # nach rechts oben iteriert wird, bevor die Zeile gewechselt wird
        runde_zeile = 0
        global spieler
        global win
        while runde_zeile <= 6:
            runde_spalte = 0
            condition_diagonal_rechts = 0
            while runde_spalte <= 5:
                # durch die Variablen 'zeilenzahl' und 'spaltenzahl' kann auf jedes Element
                # der Liste einzeln zugegriffen werden
                # so wird von jeder Position die diagonal nach rechts laufende Gewinnabfrage durchgeführt
                spaltenzahl = runde_spalte
                zeilenzahl = runde_zeile
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_rechts += 1
                            # Sollten mehrere gleiche Steine in einer diagonalen Reihe
                            # nach rechts oben sein, wird hier
                            # die Variable 'condition_diagonal_rechts' jeweils um 1 erhöht
                            # sollte es irgendwann zu einer Unterbrechung der in einer Reihe liegenden
                            # Steine kommen wird der Wert wieder auf 0 gesetzt, um beim nächsten richtigen
                            # Stein wieder bei 1 anzufangen
                            if condition_diagonal_rechts >= 4:
                                return True
                        else:
                            if spaltenzahl == 7:
                                break
                            condition_diagonal_rechts = 0
                    if spieler == -1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_diagonal_rechts += 1
                            if condition_diagonal_rechts >= 4:
                                return True
                        else:
                            if spaltenzahl == 7:
                                break
                            condition_diagonal_rechts = 0
                    # 'zeilenzahl' und 'spaltenzahl wird um 1 erhöht
                    # um diagonal nach rechts oben zu springen
                    zeilenzahl += 1
                    spaltenzahl += 1
                    # Falls 'spaltenzahl' über 5 hinaus wächst wird der Code abgebrochen, da es keine weiteren Elemente
                    # mehr gibt sollte man die Zahl weiter erhöhen
                    if spaltenzahl > 5:
                        break
                condition_diagonal_rechts = 0
                # 'runde_spalte' wird um 1 erhöht, um beim nächsten Durchlauf in der nächsten Spalte zu beginnen
                runde_spalte += 1
            # 'runde_zeile' wird um 1 erhöht um beim nächsten Durchlauf in der nächsten Zeile zu beginnen
            runde_zeile += 1
        return False



    def diagonalLinksAbfrage(self):
        """Gewinnabfrage diagonal links

        Diese Methode überprüft, ob vier Werte des gleichen Spielers
        diagonal nach links direkt aneinanderliegen.
        """
        global spieler
        global win
        # Die Variable 'runde_zeile' stellt sicher, dass zuerst aus jeder Position in der momentanen Zeile
        # nach rechts oben iteriert wird, bevor die Zeile gewechselt wird
        runde_zeile = 0
        while runde_zeile <= 6:
            runde_spalte = 0
            condition_diagonal_links = 0
            while runde_spalte <= 5:
                spaltenzahl = 6 - runde_spalte
                zeilenzahl = 0 + runde_zeile
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_links += 1
                            # Sollten mehrere gleiche Steine in einer diagonalen Reihe
                            # nach links oben sein wird hier
                            # die Variable 'condition_diagonal_links' jeweils um 1 erhöht
                            # sollte es irgendwann zu einer Unterbrechung der in einer Reihe liegenden
                            # Steine kommen wird der Wert wieder auf 0 gesetzt um beim nächsten richtigen
                            # Stein wieder bei 1 anzufangen
                            if condition_diagonal_links >= 4:
                                return True
                        else:
                            condition_diagonal_links = 0
                            if spaltenzahl == 0:
                                break
                    if spieler == -1:
                        if self.spielfeld[len(self.spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                            win = "Spieler 1"
                            condition_diagonal_links += 1
                            if condition_diagonal_links >= 4:
                                return True
                        else:
                            condition_diagonal_links = 0
                            if spaltenzahl == 0:
                                break
                    # 'zeilenzahl' wird um 1 erhöht und 'spaltenzahl' wird um 1 verkleinert
                    # um diagonal nach links oben zu springen
                    zeilenzahl += 1
                    spaltenzahl -= 1
                condition_diagonal_links = 0
                # 'runde_spalte' wird um 1 erhöht um im nächsten Durchgang in der nächsten Spalte zu beginnen
                runde_spalte += 1

            # 'runde_zeile' wird um 1 erhöht um im nächsten Durchgang in der nächsten Zeile zu beginnen
            runde_zeile += 1
        return False




class KI:
    def __init__(self):
        self.feld_ki = Spielfeld()


    def kiAbfrage(self, ki_abfrage: str):
        """KI als Gegner auswählen

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
        """Die KI tätigt einen Zug

        Diese Methode erzeugt eine Zufallszahl zwischen 1 und 7
        und ruft dann die Methode setSpielfeld auf

        Parameters
        ----------
        sleep : float
            Der Zug der KI wird um 'sleep' Sekunden verzögert,
            um den Anschein zu erwecken, dass diese 'nachdenkt'
        """
        if ki and spieler == -1:
            time.sleep(sleep)
            random_number = str(random.randint(1, 7))
            self.feld_ki.setSpielfeld(random_number)
            print(f'Die KI hat in der Spalte {random_number} gespielt')



class Runde:

    def erhoeheRunde(self):
        """Rundenzähler

        Diese Methode zählt die Anzahl der Runden mit.

        Returns
        -------
        int
            Die Anzahl an bisher gespielten Runden
        """
        global runden_zaehler
        runden_zaehler += 1
        return runden_zaehler





if __name__ == '__main__':
    print("Willkommen im Spiel '4 gewinnt'! Sie haben die Auswahl gegen einen Mensch oder eine künstliche Intelligenz zu spielen.")
    Spielablauf().spielRunden()

