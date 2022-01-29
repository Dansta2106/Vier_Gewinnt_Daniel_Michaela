import random, time

zeile1 = [0, 0, 0, 0, 0, 0, 0]
zeile2 = [0, 0, 0, 0, 0, 0, 0]
zeile3 = [0, 0, 0, 0, 0, 0, 0]
zeile4 = [0, 0, 0, 0, 0, 0, 0]
zeile5 = [0, 0, 0, 0, 0, 0, 0]
zeile6 = [0, 0, 0, 0, 0, 0, 0]

spielfeld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6]

spieler = 1
runden_zaehler = 0
end = False
win = "Niemand"
fehler = False
ki = False
pseudo_runde = 0


class Spieler():

    def spielerWechsel(self):
        global spieler
        if spieler == 1:
            spieler -= 2
        else:
            spieler += 2

    def spielerAusgabe(self):
        if spieler == 1:
            if ki:
                print("Sie sind dran")
            else:
                print("Spieler 1 ist dran")
        if spieler == -1:
            print("Spieler 2 ist dran")
        return spieler


class Spielfeld(Spieler):

    def getSpielfeld(self):
        return spielfeld


    def setSpielfeld(self):
        global fehler
        eingabe_start = input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)")
        try:
            eingabe = int(eingabe_start)
            if 1 <= eingabe <= 7 and Spielfeld().getSpielfeld()[0][eingabe - 1] == 0:
                for reihe in Spielfeld().getSpielfeld()[::-1]:
                    if reihe[eingabe - 1] == 0:
                        reihe[eingabe - 1] = spieler
                        break
            else:
                print("Fehler, falsche Eingabe")
                fehler = True
        except ValueError:
            print("Fehler, falsche Eingabe")
            fehler = True
            self.spielerWechsel()

    def printSpielfeld(self):
        zeile_ausgabe = 0
        if (ki and spieler == 1 and fehler == False) or ki == False:
            while zeile_ausgabe < 6:
                print(spielfeld[zeile_ausgabe])
                zeile_ausgabe += 1


class KI(Spielfeld):

    def kiAbfrage(self):
        global ki
        ki_abfrage = input("Möchten Sie gegen eine künstliche Intelligenz spielen?")
        if ki_abfrage == "Ja" or ki_abfrage == "J" or ki_abfrage == "j" or ki_abfrage == "ja" or ki_abfrage == "yes" or ki_abfrage == "Yes" or ki_abfrage == "y" or ki_abfrage == "Y":
            ki = True

    def kiZug(self):
        if ki == True and spieler == -1:
            time.sleep(1.5)
            random_number = random.randint(1, 7)
            if 1 <= random_number <= 7 and spielfeld[0][random_number - 1] == 0:
                for reihe in spielfeld[::-1]:
                    if reihe[random_number - 1] == 0:
                        reihe[random_number - 1] = spieler
                        break
                print(f'Die KI hat in der Spalte {random_number} gespielt')


class Gewinnabfrage(KI):

    def getWin(self):
        return win

    def erhoeheRunde(self):
        global runden_zaehler
        runden_zaehler += 1
        return runden_zaehler

    def getRunde(self):
        return runden_zaehler

    def horizontaleAbfrage(self):
        global spieler
        global end
        global win
        condition_horizontal = 0
        zeilenzahl = 0
        while zeilenzahl <= 5:
            condition_horizontal = 0
            spaltenzahl = 0
            while spaltenzahl <= 6:
                if spieler == 1:
                    if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                        win = "Spieler 2"
                        condition_horizontal += 1
                        if condition_horizontal >= 4:
                            end = True
                            break
                    else:
                        condition_horizontal = 0
                if spieler == -1:
                    if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
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
        global end
        global spieler
        global win
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
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
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
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
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
        condition_diagonal_rechts = 0
        runde_zeile = 0
        global end
        global spieler
        global win
        while runde_zeile <= 6:
            runde_spalte = 0
            condition_diagonal_rechts = 0
            while runde_spalte <= 5:
                spaltenzahl = runde_spalte + 0
                zeilenzahl = runde_zeile + 0
                while zeilenzahl <= 5:
                    if spieler == 1:
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_rechts += 1
                            if condition_diagonal_rechts >= 4:
                                end = True
                        else:
                            if spaltenzahl == 7:
                                break
                            condition_diagonal_rechts = 0
                    if spieler == -1:
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
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
        global end
        global spieler
        global win
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
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                            win = "Spieler 2"
                            condition_diagonal_links += 1
                            if condition_diagonal_links >= 4:
                                end = True
                        else:
                            condition_diagonal_links = 0
                            if spaltenzahl == 0:
                                break
                    if spieler == -1:
                        if Spielfeld().getSpielfeld()[len(Spielfeld().getSpielfeld()) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
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
        global end
        global win
        global pseudo_runde
        global fehler
        while end != True:
            if runden_zaehler == 0 and pseudo_runde == 0:
                self.kiAbfrage()

            self.printSpielfeld()
            if (ki and spieler == 1) or ki == False:
                beenden = str(input("Wollen Sie das Spiel beenden?"))
                if beenden == "Ja" or beenden == "J" or beenden == "j" or beenden == "ja" or beenden == "yes" or beenden == "Yes" or beenden == "y" or beenden == "Y":
                    break


            if ki and spieler == -1:
                KI().kiZug()
            else:
                Spieler().spielerAusgabe()
                Spielfeld().setSpielfeld()
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

            if Gewinnabfrage().getRunde() == 42 and win == 'Niemand':
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

