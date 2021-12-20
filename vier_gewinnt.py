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
