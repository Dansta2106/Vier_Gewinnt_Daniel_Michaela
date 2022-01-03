import random, time

zeile1 = [0, 0, 0, 0, 0, 0, 0]
zeile2 = [0, 0, 0, 0, 0, 0, 0]
zeile3 = [0, 0, 0, 0, 0, 0, 0]
zeile4 = [0, 0, 0, 0, 0, 0, 0]
zeile5 = [0, 0, 0, 0, 0, 0, 0]
zeile6 = [0, 0, 0, 0, 0, 0, 0]

spielfeld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6]


print("Willkommen im Spiel '4 gewinnt'! Sie haben die Auswahl gegen einen Mensch oder eine künstliche Intelligenz zu spielen.")
ki_abfrage = input("Möchten Sie gegen eine künstliche Intelligenz spielen?")
ki = False
if ki_abfrage == "Ja" or ki_abfrage == "J" or ki_abfrage == "j" or ki_abfrage == "ja" or ki_abfrage == "yes" or ki_abfrage == "Yes" or ki_abfrage == "y" or ki_abfrage == "Y":
    ki = True

eingabe = 0
spieler = 1
runden_zaehler = 0
fehler = False
end = False
while end != True:
    zeile_ausgabe = 0
    if (ki and fehler == False) or ki == False:
        while zeile_ausgabe < 6:
            print(spielfeld[zeile_ausgabe])
            zeile_ausgabe += 1
    fehler = False
    win = "Niemand"
    if (ki and spieler == 1) or ki == False:
        beenden = str(input("Wollen Sie das Spiel beenden?"))
        if beenden == "Ja" or beenden == "J" or beenden == "j" or beenden == "ja" or beenden == "yes" or beenden == "Yes" or beenden == "y" or beenden == "Y":
            break
        if spieler == 1:
            if ki:
                print("Sie sind dran")
            else:
                print("Spieler 1 ist dran")
        if spieler == -1:
            print("Spieler 2 ist dran")
    if ki == True and spieler == -1:
        time.sleep(1.5)
        random_number = random.randint(1, 7)
        if 1 <= random_number <= 7 and spielfeld[0][random_number-1] == 0:
            for reihe in spielfeld[::-1]:
                if reihe[random_number - 1] == 0:
                    reihe[random_number - 1] = spieler
                    break
            print(f'Die KI hat in der Spalte {random_number} gespielt')
        else:
            fehler = True
        if fehler == False:
            if spieler == 1:
                spieler -= 2
            else:
                spieler += 2
    else:
        eingabe_start = input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)")
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

        if fehler == False or spielfeld[0][eingabe-1] == 0:
            if spieler == 1:
                spieler -= 2
            else:
                spieler += 2


    # Horizontales abfragen des Gewinns
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
                        break
                else:
                    condition_horizontal = 0
            spaltenzahl += 1
        zeilenzahl += 1

        # Vertikales Abfragen des Gewinns
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
                    if spielfeld[len(spielfeld)-1-zeilenzahl][spaltenzahl] == spieler - 2:
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
                            print("Es ist Condition Vertikal Spieler 1")
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


    # diagonal nach rechts abfragen des Gewinns
    condition_diagonal_rechts = 0
    spaltenzahl = 0
    zeilenzahl = 0
    runde_zeile = 0
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
                            print("Es ist condition diagonal rechts")
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

        # Gewinn diagonal nach links abfragen
    condition_diagonal_links = 0
    runde_zeile = 0
    while runde_zeile <= 6:
        runde_spalte = 0
        condition_diagonal_links = 0
        while runde_spalte <= 5:
            spaltenzahl = 6 - runde_spalte
            zeilenzahl = 0 + runde_zeile
            while zeilenzahl <= 5:
                if spaltenzahl < 0:
                    spaltenzahl = 0
                if spieler == 1:
                    if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler - 2:
                        win = "Spieler 2"
                        condition_diagonal_links += 1
                        if condition_diagonal_links >= 4:
                            print(f'{zeilenzahl}, {spaltenzahl}')
                            end = True
                    else:
                        if spaltenzahl == 0:
                            break
                        condition_diagonal_links = 0
                if spieler == -1:
                    if spielfeld[len(spielfeld) - 1 - zeilenzahl][spaltenzahl] == spieler + 2:
                        win = "Spieler 1"
                        condition_diagonal_links += 1
                        if condition_diagonal_links >= 4:
                            end = True
                            print("Es ist condition diagonal links")
                    else:
                        if spaltenzahl == 0:
                            break
                        condition_diagonal_links = 0
                if end:
                    break
                else:
                    win = "Niemand"
                zeilenzahl += 1
                spaltenzahl -= 1
            condition_diagonal_links = 0
            runde_spalte += 1
        runde_zeile += 1

    if fehler == False:
        runden_zaehler += 1

    if runden_zaehler == 42 and win == 'Niemand':
        end = True
        win = "Unentschieden, niemand"

if ki and win == "Spieler 2":
    win = "Die KI"


zeile_ausgabe = 0
while zeile_ausgabe < 6:
    print(spielfeld[zeile_ausgabe])
    zeile_ausgabe += 1


print(f'{win} hat gewonnen!')
print("Danke für's Spielen!!")
