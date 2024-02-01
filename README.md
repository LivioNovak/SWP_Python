Homework and other task regarding  the Python-part of SWP

---

## Aufgabe 01: Lotto
*Aufgabenstellung:* 
> Programmiere Lottoziehung als Methode
> * [ ] random.getrand() 
> * [X] Algorithmus zum Zufallszahlenziehen muss so programmiert sein, dass keine Zufallszahl zweimal gezogen werden kann
>      (d.h. wenn Sie alle 45 Zahlen ziehen mussten, würden Sie den ̈Zufallszahlengenerator nur 45 mal benutzen dürfen)
> * [X] Ziehe die sechs Zahlen und gib Sie am Bildschirm aus


*Erweiterung:*
> Programmiere Lottoziehung Statistik als Methode
> * [X] Mach 1000 Ziehungen
> * [X] Erstelle Dictionary fur Statistik, wie oft welche Zahl gezogen wurde
> * [X] Ruf die Statistikmethode nach jede Ziehung auf und inkrementiere den Zähler


*Anmerkungen:*

* Zufallszahl wurde mit random.randint() gelöst: 
  * Methode, die ganzzahlen mit immer der selben Wahrscheinlichkeit generiert.
  * Parameter: (kleinste Zahl, größte Zahl - ausgeschlossen)


*Erweiterung 1.1:*
* Globale Variablen wurden entfernt. Stattdessen werden die benötigte Listen, Dictionaries, etc. als parameter mitgegeben bzw. returned
* jegliche Fixzahl i Code (außer 0 & 1) wurde durch einen Parameter abgelöst für mehr dynamik
* Parameter: ( [Untergrenze(inklusiv)] , [Obergrenze(exklusiv)] )
 


--- 

<br/>

## Aufgabe 02: Poker
*Aufgabenstellung:*
> Pokerspielsimulator als Aufgabe über mehrere Wochen:
> * [X] überlege wie man die Pokerkarten modellieren könnte (vier Farben, 13 Symbole)
> * [X] gib zufällig fünf Karten
> * [X] recherchiere welche Kombinationen beim Pokerspiel exisiteren
> * [X] schreibe Funktionen fur die Kombinationen Paar, Drillinge, Poker, Flash, Strasse usw.
> * [X] spiele 100000 mal und zähle die Anzahl der verschiedenen Kombinationen
> * [X] berechne den prozentuellen Anteil einer Kombination zu der Gesamtspieleanzahl
> * [X] recherchiere die richtige Anteile im Netz und vergleiche die Ergebnisse

*Anmerkungen:*

* Jede gezogene Karte wird als Objekt gespeichert, die 1 Zahl für den Wert & 1 für die Farbe speichert
* Konstanten werden in einer eigenen Datei angelegt (constants.py)

*Erweiterung 1.1:*

* Funktionen für Kombinationen wurden in ein eigenes File *combinations.py* ausgelagert
* unittests wurden in *tests/unittests.py" eingefügt. Überprüft werden folgende fünf Funktionen:
  * get_value()
  * royal_flush()
  * straight_flush()
  * four_of_a_kind()
  * full_house() 
 


--- 

<br/>

## Aufgabe 03: Firmenstruktur
*Aufgabensstellung:*
> * [X] Bitte UML-Klassendiagramm zeichnen
>
> programmiere in Python: 
> * [X] eine Firma
> * [X] Es gibt Personen, Mitarbeiter, Abteilungsleiter
> * [X] Es gibt mehrere Abteilungen, jede(r) Mitarbeiter ist in einer Abteilung
> * [X] Es gibt beide Geschlechter
> * [X] es gibt nur einen Abteilungsleiter pro Abteilung
> * [ ] Mitarbeiter gehören immer zu einer Abteilung
> * [X] ein Abteilungsleiter ist auch ein Mitarbeiter
> 
>Umsetzung:
> * [X] modelliere die Objekte über Vererbung
> * [ ] erzeuge zum Schluss ein Firmenobjekt
>
> programmiere folgende Methoden:
> * [X] man muss alle Objekte instanzieren können
> * [X] wieviele Mitarbeiter, Abteilungsleiter gibts in der Firma
> * [X] wieviel Abteilungen gibt es
> * [ ] welche Abteilung hat die größte Mitarbeiterstärke
> * [X] wie ist der Prozentanteil Frauen Männer
>
> Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.

*Anmerkungen:*

* Umsetzung so gut wie fertig, aber nicht getestet 


---

<br/>

## Aufgabe 04: Schere-Stein-Papier (advanced)
*Referenzmaterial:*

https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock

http://www.samkass.com/theories/RPSSL.html

*Aufgabenstellung:*
> * [X] Als Terminal-Spiel umsetzen
> * [X] Spielmodi COMP vs PLAYER
> * [X] zähle wer wie oft gewonnen
> * [X] zähle alle gewählte Symbole
> * [X] überlege wie die Daten dauerhaft gespeichert werden könnten
> * [X] biete ein Menü an Spielen, Statistik

*Anmerkungen:*

* Es gibt zwei Spielmodi, Player vs Player & Player vs COM
* Das Statistikmenü bietet recht viel Platz für Verbesserungen
