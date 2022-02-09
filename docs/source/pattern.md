# Iterator
Iterator ist ein Verhaltensmuster, das Zugriff auf verschiedene Arten von Sammlungen ermöglicht (list, dict, …). Derartige Sammlungen sind einer der am häufigsten verwendeten Datentypen in der Programmierung. 

## Problem
Am häufigsten kommen Listen zum Einsatz. Einige Sammlungen basieren jedoch auf Stapeln, Bäumen, Diagrammen und anderen komplexen Datenstrukturen.
Eine Sammlung bietet immer die Möglichkeit, auf ihre Elemente zuzugreifen, damit diese Elemente weiter weiterverwendet werden können. Man sollte die Möglichkeit haben, jedes Element der Sammlung zu durchlaufen, ohne immer wieder auf dieselben Elemente zugreifen zu müssen.
Für eine Liste geht das noch recht einfach, aber wie durchläuft man sequentiell Elemente einer komplexen Datenstruktur, z. B. eines Baums? 

## Lösung
Die Hauptidee besteht darin, das Durchlaufen einer Sammlung in ein separates Objekt namens Iterator zu extrahieren.
Es wird nicht nur der Algorithmus implementiert, sondern auch ein Iterator-Objekt, welches alle Durchlaufdetails speichert, wie z. B. die aktuelle Position und wie viele Elemente noch bis zum Ende übrig sind. Dadurch können mehrere Iteratoren gleichzeitig und unabhängig voneinander dieselbe Collection durchlaufen.
Iteratoren stellen eine primäre Methode zum Abrufen von Elementen der Sammlung bereit. Der Client kann diese Methode so lange ausführen, bis nichts zurückgegeben wird, was bedeutet, dass der Iterator alle Elemente durchlaufen hat.
Alle Iterator-Objekte müssen dieselbe Schnittstelle implementieren. Dadurch wird der Code mit jedem Durchlaufalgorithmus kompatibel, solange ein geeigneter Iterator vorhanden ist. Wenn eine spezielle Methode zum Durchlaufen einer Sammlung benötigt wird, kann eine neue Iterator-Klasse erstellt werden, ohne die Sammlung ändern zu müssen.

## Anwendbarkeit
Das Iterator-Muster kann verwendet werden, wenn durch die Sammlung der Objekte eine komplexe Datenstruktur gegeben ist, man die Komplexität vor Clients jedoch verbergen möchte (zB.: aus Bequemlichkeits- oder Sicherheitsgründen).

## Pro und Kontra
<p> •	Der Code und die Sammlungen können bereinigt werden, indem umfangreiche Durchlaufalgorithmen in separate Klassen extrahiert werden.</p>
<p> •	Neue Arten von Sammlungen und Iteratoren können implementiert und an vorhandenen Code übergeben werden, ohne etwas zu beschädigen.</p>
<p> •	 Dieselbe Sammlung kann parallel durchlaufen werden, da jedes Iterator-Objekt seinen eigenen Iterationszustand enthält.</p>
<p> •	 Dadurch kann eine Iteration verzögert und bei Bedarf fortgesetzt werden.</p>

<p> •	Das Anwenden des Musters kann den Code bei einfachen Sammlungen überfordern.</p>
<p> •	Die Verwendung eines Iterators ist möglicherweise weniger effizient als das direkte Durchlaufen von Elementen.</p>
