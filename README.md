💰 Flet Zinsrechner (Compound Interest Calculator)
Ein moderner Zinseszinsrechner, entwickelt mit dem Flet Framework, basierend auf Flutter.

Diese Anwendung bietet eine responsive Benutzeroberfläche (GUI) und kann als native App für Desktop und Mobile (Android/iOS) kompiliert werden. Die komplexen Berechnungen (Zinssatz und Dauer) werden mit einem reinen Python-Algorithmus (Bisektionsmethode) gelöst, wodurch externe wissenschaftliche Abhängigkeiten vermieden werden.

✨ Hauptmerkmale
Die wichtigsten Vorteile und technischen Details auf einen Blick:

⚡️ Technologie: Moderne, plattformunabhängige GUI dank Flet.

📱 Kompatibel: Lauffähig als Desktop-Anwendung und kompilierbar als Android/iOS-App.

⚖️ Mathematische Robustheit: Berechnungen für Zinssatz und Dauer nutzen die Bisektionsmethode für hohe Präzision.

💸 Flexible Eingaben: Unterstützung für monatliche Beiträge.

🔢 Berechnungen
Die App löst die Zinseszinsformel nach vier zentralen Variablen auf:

Endkapital

Anfangskapital

Zinssatz

Dauer (in Jahren)

🛠️ Anforderungen
Um die Anwendung auszuführen, benötigen Sie:

Python 3.10+

Flet (Installieren Sie die neueste Version):

Bash

pip install flet
▶️ App starten (Entwicklungsmodus)
Navigieren Sie in das Projektverzeichnis und starten Sie die Anwendung in der Vorschau:

Bash

py -m flet run main.py
⚙️ Als Android-App kompilieren (APK)
Für die Kompilierung benötigen Sie das Android SDK und den aktivierten Entwicklermodus in Windows.

Stellen Sie sicher, dass das Android SDK installiert und die Umgebungsvariable ANDROID_HOME gesetzt ist.

Führen Sie den Build-Befehl aus (verwenden Sie den vollständigen Pfad):
