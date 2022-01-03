# Erstellung des Spiels Vier Gewinnt

Im Zuge der Lehrveranstaltung Softwareentwicklungsmodelle haben wir uns in einem Zweierteam mit der Programmierung des bekannten Spiels 'Vier Gewinnt' auseinandergesetzt.

## Spielanleitung

Starten Sie das Spiel mit dem Programmstartknopf in der Entwicklungsumgebung.
Zunächst werden Sie gefragt, ob Sie gegen eine künstliche Intelligenz oder gegen einen zweiten Spieler spielen wollen.
Beantworten Sie diese Frage mit "Ja", "J", "ja", "j", "yes", "Yes", "y", "Y" um gegen eine KI spielen zu können.
Ansonsten geben Sie eine beliebige andere Tastenkombination ein.
Dann wird das leere Spielbrett angezeigt und Sie werden gefragt, ob Sie das Spiel beenden möchten.
Diese Abfrage geschieht vor jeder Runde, damit Sie das Spiel jederzeit abbrechen können.
Um das Spiel zu beenden müssen Sie die Frage mit "Ja", "J", "ja", "j", "yes", Yes", "y", oder "Y" beantworten.
Falls Sie das Spiel nicht beenden möchten geben Sie eine beliebige andere Tastenkombination ein.

### Die Regeln des Spiels sind wie folgt:

Das Spielbrett besteht aus sieben Spalten (senkrecht) und sechs Reihen (waagerecht).
Der erste Spieler hat die Spielfigur "1" und der zweite Spieler die Spielfigur "-1".
Die Spielzüge werden immer abwechselnd durchgeführt. Sobald einer der Spieler 4 Spielfiguren nebeneinander in einer Reihe hat, hat dieser gewonnen.
Spielfiguren zählen als nebeneinander solange sie ohne Trennung horizontal, vertikal oder diagonal miteinander verbunden sind.
Jede Runde wählt ein Spieler die Spalte aus in die er seine Spielfigur setzen möchte. Die Spielfigur wird dann an die unterste freie Stelle gesetzt.

Sollten Sie sich dazu entschieden haben gegen einen weiteren Menschen zu spielen, wird nach jedem Spielzug angezeigt, welcher Spieler gerade am Zug ist.
Andernfalls spielt die KI ihren Zug und es wird angezeigt in welcher Spalte die KI ihre Spielfigur gesetzt hat.

Danach wird das aktuelle Spielbrett ausgegeben.

### Ende des Spiels

Sollte einer der Spieler 4 Spielfiguren in einer Reihe erreicht haben, wird das finale Spielbrett und der Gewinner ausgegeben.
Danach wird das Spiel automatisch beendet.
Sollte keiner der Spieler 4 Spielfiguren in einer Reihe erreicht haben, gibt es keinen Gewinner und es folgt ein Unentschieden in der Ausgabe.
