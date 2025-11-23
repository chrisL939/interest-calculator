Flet Zinsrechner (Interest Calculator)
Ein moderner Zinseszinsrechner, entwickelt mit dem Flet Framework.

Diese Anwendung bietet eine responsive Benutzeroberfläche (GUI) und ermöglicht die Kompilierung als native App für Desktop und Mobile (Android/iOS). Die komplexen Berechnungen (Zinssatz und Dauer) werden mit einem reinen Python-Algorithmus (Bisektionsmethode) gelöst, wodurch externe wissenschaftliche Abhängigkeiten wie SciPy vermieden werden.

✨ Features
Moderne GUI (Flet): Responsive Benutzeroberfläche, die auf Flutter basiert.

Plattformunabhängig: Lauffähig als Desktop-Anwendung und kompilierbar als Android/iOS-App.

Unterstützung monatlicher Beiträge.

Berechnet flexible Parameter:

Endkapital (Final Capital)

Anfangskapital (Starting Capital)

Zinssatz (Interest Rate)

Dauer (Duration in Jahren)

Robust: Interne numerische Lösung (Bisektionsmethode) ersetzt externe Abhängigkeiten (SciPy).

Eingabevalidierung und Fehlerbehandlung.

💻 Anforderungen
Python 3.10+

Flet (pip install flet)

▶️ App ausführen
Navigieren Sie in das Projektverzeichnis und starten Sie die Anwendung im Entwicklungsmodus:

Bash

py -m flet run main.py
📱 Als Android-App kompilieren (APK)
Um die App in eine installierbare APK-Datei zu kompilieren, benötigen Sie das Android SDK und müssen den Entwicklermodus in Windows aktivieren.

Führen Sie den Build-Befehl aus (ersetzen Sie den Pfad falls nötig):

Bash

"C:\Users\xyz\AppData\Local\Programs\Python\Python312\Scripts\flet.exe" build apk
Die fertige App (app-release.apk) finden Sie anschließend unter: Ihr Projektordner/build/app/outputs/apk/release/
