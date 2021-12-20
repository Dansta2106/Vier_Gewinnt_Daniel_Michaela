zeile1 = [0, 0, 0, 0, 0, 0, 0]
zeile2 = [0, 0, 0, 0, 0, 0, 0]
zeile3 = [0, 0, 0, 0, 0, 0, 0]
zeile4 = [0, 0, 0, 0, 0, 0, 0]
zeile5 = [0, 0, 0, 0, 0, 0, 0]
zeile6 = [0, 0, 0, 0, 0, 0, 0]

spielfeld = [zeile1,
             zeile2,
             zeile3,
             zeile4,
             zeile5,
             zeile6]


print("Willkommen im Spiel '4 gewinnt'! Sie haben die Auswahl gegen einen Mensch oder eine künstliche Intelligenz zu spielen.")
# if input("Möchten Sie gegen eine künstliche Intelligenz spielen?") == "Ja":
#     print("richtig")
#     pass

spieler = 1

end = False
while end != True:
    fehler = False
    zeile_ausgabe = 0
    while zeile_ausgabe < 6:
        print(spielfeld[zeile_ausgabe])
        zeile_ausgabe += 1

    beenden = input("Wollen Sie das Spiel beenden?")
    if beenden == "Ja" or beenden == "J" or beenden == "j" or beenden == "ja" or beenden == "yes" or beenden == "Yes" or beenden == "y" or beenden == "Y":
        break

    eingabe = int(input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)"))
    if 1 <= eingabe <= 7:
        for reihe in spielfeld[::-1]:
            if reihe[eingabe - 1] == 0:
                reihe[eingabe - 1] = spieler
                break
    else:
        print("Fehler, falsche Eingabe")
        fehler = True
    if fehler == False:
        if spieler == 1:
            spieler -= 2
        else:
            spieler += 2

    for reihe in spielfeld[::-1]:
        # Horizontales abfragen des Gewinns
        condition_spieler_1 = 0
        condition_spieler_2 = 0
        vorige_spalte_spieler1 = False
        vorige_spalte_spieler2 = False
        for spalte in reihe:
            if spalte != 1:
                vorige_spalte_spieler1 = False
            if spalte == 1 and vorige_spalte_spieler1 != True:
                vorige_spalte_spieler1 = True
                condition_spieler_1 = 1
            elif spalte == 1 and vorige_spalte_spieler1 == True:
                condition_spieler_1 += 1
            if spalte != -1:
                vorige_spalte_spieler2 = False
            if spalte == -1 and vorige_spalte_spieler2 != True:
                vorige_spalte_spieler2 = True
                condition_spieler_2 = 1
            elif spalte == -1 and vorige_spalte_spieler2 == True:
                condition_spieler_2 += 1

        # Vertikales Abfragen des Gewinns
        condition_spieler_1_vertikal = 0
        condition_spieler_2_vertikal = 0
        vorige_zeile_spieler1 = False
        vorige_zeile_spieler2 = False
        for spalte in reihe:
            if spalte != 1:
                vorige_zeile_spieler1


        if condition_spieler_1 >= 4:
            end = True
            print("Spieler 1 hat gewonnen")
        if condition_spieler_2 >= 4:
            end = True
            print("Spieler 2 hat gewonnen")


print("Danke für's Spielen!!")
