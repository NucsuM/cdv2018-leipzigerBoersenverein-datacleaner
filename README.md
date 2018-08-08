# Coding DaVinci Ost 2018 - Linked History - Datacleaning and visualisation


<<<<<<< Updated upstream
## Projektbescheibung
=======

# Projektbescheibung
>>>>>>> Stashed changes

Das sächsischen Staatsarchiv hat für den CDO 2018 Daten über Ihren Bestand an Firmenakten des Börsenvereins der deutschen Buchhändler zu Leipzig zur Verfügung gestellt. Die Datensätze werden aufbereitet und auf einer Karte visualisiert. 


## Ausführliche Projektbeschreibung

Die Daten über den Bestand an Firmenakten des sächsischen Staatsarchivs liegen in CSV-Form vor. Sie enthalten Jahresangaben, Namen von Inhabern, Art der Firmen (Buchhandlungen oder Antiquariate) und den Ort der Unternehmung. 
 
Gegenstand des Projektes ist die visuelle Darstellung des Datenbestandes sowie die Aufbereitung der Daten.

Die visuelle Darstellung wird via OpenStreetMap und farbliches Punkte auf der Karte umgesetzt, die je nach Anzahl der Firmen in der Größe variieren. Das ganze wird noch über die Art der Unternehmung (Buchhandlung, Antiquariat etc.) filterbar sein. Geplant ist, den zeitlichen Horizont ebenfalls abzubilden. Somit lässt sich auf einer Karte der Datenbestand interaktiv betrachten.


## Hintergrund er Aufbereitung

Problematisch ist, dass wesentliche Daten wie Namen der Inhaber, Art der Unternehmung und der Ort in einer Spalte mittels Kommas getrennt erfasst wurden und dies keinem strengem maschinenlesbarem Schema erfolgt. Aus Sicht des Archivs eine sinnvolle und durchaus praktikable Vorgehensweise, jedoch für unser Projekt hinderlich. 

Bis zu einem gewissen Grad können wir die Daten nach Inhaber, Art der Unternehmung und Ort wieder trennen. Leider ist das nicht vollständig möglich, so das eine menschliche Interaktion notwendig ist, die wir dritten spielerisch überlassen wollen.

Die Aufbereitung der verbleibenden Daten wird über eine Web-Applikation präsentiert. Hierbei werden dem Anwender die unklaren Datensätze präsentiert und verschieden Antwortmöglichkeiten zur Bereinigung angeboten - Gamification ist hier das Stichwort.


## Weitere TODOs

### Frontend
* Vue Logo raus
* Buttons anders positionieren und umbenennen
* Zeichenkette optisch aufbereiten und darstellen
* Buttons und Strings besser positionieren
* Buttons einfärben, wenn sie geklickt wurden
* Beispiele auf Wunsch anzeigen
* npm run (build, clean, move) verbessern
* Findbuchnummer entgegen nehmen, anzeigen und wieder an das Backend zurück geben


### Backend
* ~~Findbuchnummer an Frontend übergeben~~
* Post-Request speichern in sqlite-DB (, Gedanken machen über zusätzliche Spalten)



<<<<<<< Updated upstream
Das soll das Projekt werden. Die ersten Prototypen existieren schon, mal schauen was draus wird. Das Hauptproblem ist, dass wir von dem Ganzen keinen richtigen Plan haben - wir sind aber sehr optimistisch.


## ToDO

* Daten bereinigen
* Koordinaten abfragen
* backend.py nur für Datenbereitstellung
  * csv_dateinamen abfragen
* summery.py für aufbereitung der Daten
  * wie die Abfrage der Koordianten einbinden?
  * Wie die Koordinaten überhaupt abfragen?
  * (Aktuell über Datei aus Suche nach csv, city coordinates - hier nicht eingebunden bzw. siehe .gitignore)
  * umbenennen
  * lat / lon umbenenne bzw. einheitlich hinterlegen

  
  

=======
>>>>>>> Stashed changes
