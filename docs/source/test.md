# Unit Testing
Die Aufgabenstellung bestand darin, die Spiellogik zu testen, nicht 
jedoch den Spielablauf und den Computergegner.

## Welche Bereiche wurden abgedeckt?
Es wird getestet, ob es sich um gültige Züge für Spieler 1 und Spieler -1 
handelt, also ob ein Stein gespielt werden kann.
<p>Es muss sich um eine Zahl zwischen 1 - 7 handeln. Falls eine 
Falscheingabe getätigt wird, oder eine Spalte bereits voll belegt ist, 
wird derselbe Spieler erneut zum Spielzug aufgefordert.</p>
<p>Darüberhinaus wird getestet, ob Spieler 1 oder -1 gewonnen hat.</p>
<p>Dies wird überprüft, indem vier Steine vom gleichen Spieler 
nacheinander gelegt werden. Dabei werden vier unterschiedliche 
Richtungen abgefragt: horizontal, vertikal, diagonal links, diagonal
rechts.</p>
<p>Weiters wurde die Spielerausgabe von Spieler 1 überprüft.</p>

## Welche Bereiche wurden nicht abgedeckt und wieso?
Folgende Bereiche wurden nicht getestet, da es für die Abgabe nicht 
erforderlich war:
<ul>
<li>Spielerwechsel</li>
<li>Computergegner</li>
</ul>
