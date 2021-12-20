zeile = [0, 0, 0, 0, 0, 0, 0]

spielfeld = [zeile,
             zeile,
             zeile,
             zeile,
             zeile,
             zeile]

zeile_ausgabe = 0
while zeile_ausgabe < 6:
    print(spielfeld[zeile_ausgabe])
    zeile_ausgabe += 1

print("Willkommen im Spiel '4 gewinnt'! Sie haben die Auswahl gegen einen Mensch oder eine künstliche Intelligenz zu spielen.")
# if input("Möchten Sie gegen eine künstliche Intelligenz spielen?") == "Ja":
#     print("richtig")
#     pass


print(input("Bitte wählen Sie eine Spalte für den nächsten Spielzug aus (1-7)"))
