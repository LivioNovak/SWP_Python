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

  
