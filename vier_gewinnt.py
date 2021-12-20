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
