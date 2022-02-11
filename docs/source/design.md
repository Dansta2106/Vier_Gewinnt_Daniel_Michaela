# Design des Codes
Die Aufgabe bestand darin, das Spiel "Vier gewinnt" zu programmieren.

<p>Das Spiel wurde mittels Klassen und deren dazugeröriger Methoden 
aufgebaut. Globale Variablen halfen uns dabei, den Code funktional zu 
gestalten. Am umfangreichsten stellten sich die vier unterschiedlichen 
Gewinnabfragen (horizontal, vertikal, diagonal rechts und diagonal 
links) heraus.</p>

## Klassen und Methoden
Anfänglich ist es uns schwer gefallen, das Projekt in Klassen 
einzuteilen. Dennoch konnten wir fünf für uns sinnvolle Klassen 
definieren.

<b>Einteilung in folgende Klassen:</b>
<ul>
<li>"Spieler"</li>
<li>"Spielfeld"</li>
<li>"KI"</li>
<li>"Gewinnabfrage"</li>
<li>"Spielablauf"</li>
</ul>

### Klasse Spieler
Die Klasse <b>"Spieler"</b> enthält die Methoden <i>"Spielerwechsel"</i> 
und <i>"Spielerausgabe"</i>.

### Klasse Spielfeld
Die Klasse <b>"Spielfeld"</b> beinhaltet die Methoden <i>"setSpielfeld"</i>, 
und <i>"printSpielfeld"</i>.

### Klasse KI
In der Klasse <b>"KI"</b> sind die Methoden <i>"ki_Abfrage"</i> und 
<i>"ki_Zug"</i> zu finden.

### Klasse Gewinnabfrage
Die Klasse <b>Gewinnabfrage</b> beinhaltet die Methoden <i>"erhoeheRunde"</i>, 
<i>"horizontaleAbfrage"</i>, <i>"vertikaleAbfrage"</i>, 
<i>"diagonalRechtsAbfrage"</i> und <i>"diagonalLinksAbfrage"</i>. 
Hier wird überprüft, ob ein Spiel gewonnen wurde, um es anschließend 
zu beenden.</p>

### Klasse Spielablauf
In der Klasse <b>Spielablauf</b> befindet sich die Methode 
<i>spielRunden</i>. Die Methode ruft nicht nur die Gewinnabfragen auf,
sondern fragt unter anderem auch ab, ob das Spiel unentschieden gespielt
wurde.

## Globale Variablen
Wir implementieren folgende globale Variablen, die in den Methoden 
verwendet werden. 
<ul>
<li>"spielfeld" (diese Variable wird als Liste in Liste implementiert 
und erzeugt das Spielfeld)</li>
<li>"spieler" (wechselt während des Spielverlaufs von 1 auf -1)</li>
<li>"runden_zaehler" (zählt die gespielten Runden mit)</li>
<li>"end" (entscheidet darüber, ob das Spiel durch Gewinn oder Abbruch 
beendet wird)</li>
<li>"win" (gibt aus welcher Spieler gewonnen hat)</li>
<li>"fehler" (diese Variable wird bei Falscheingabe auf True gesetzt)</li>
<li>"ki" (entscheidet darüber, ob gegen einen Computergegner gespielt wird)</li>
<li>"pseudo_runde" (wird gesetzt, damit nur einmal nach der KI gefragt wird)</li>
</ul>

## Conclusio
Wir vermuten, dass wir den Code eher kompliziert umgesetzt haben, da
wir anfänglich zu wenig Zeit in die Planung gesteckt haben. Wir hätten 
die Herangehensweise anderer im Vorfeld genauer studieren müssen,
um daraus zu lernen und diese in unseren Code einfließen zu lassen.