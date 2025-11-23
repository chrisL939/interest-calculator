💰 Flet Zinsrechner (Compound Interest Calculator)
Ein moderner Zinseszinsrechner, entwickelt mit dem Flet Framework und basierend auf Flutter.

Diese Anwendung bietet eine responsive Benutzeroberfläche (GUI) und kann als native App für Desktop und Mobile (Android/iOS) kompiliert werden. Die komplexen Berechnungen (Zinssatz und Dauer) werden mit einem reinen Python-Algorithmus (Bisektionsmethode) gelöst, wodurch externe wissenschaftliche Abhängigkeiten wie SciPy vermieden werden.

✨ Hauptmerkmale
⚡️ Technologie: Moderne, plattformunabhängige GUI dank Flet (basiert auf Flutter).

📱 Kompilierbar: Lauffähig als Desktop-Anwendung und kompilierbar als Android/iOS-App.

⚖️ Mathematische Robustheit: Berechnungen für Zinssatz und Dauer nutzen die Bisektionsmethode (reines Python) für hohe Genauigkeit ohne externe Binärdateien.

💸 Flexible Eingaben: Unterstützung für monatliche Beiträge.

🔢 Berechnungen
Die App kann vier zentrale Variablen basierend auf den anderen Eingaben berechnen:

Endkapital (Final Capital)

Anfangskapital (Starting Capital)

Zinssatz (Interest Rate)

Dauer (Duration in Jahren)

🛠️ Anforderungen & Installation
Python 3.10+

Flet (Installieren Sie die neueste Version):

Bash

pip install flet
▶️ App starten (Entwicklungsmodus)
Navigieren Sie in das Projektverzeichnis und führen Sie die Anwendung in der Vorschau aus:

Bash

py -m flet run main.py
⚙️ Als Android-App kompilieren (APK)
Um die App in eine installierbare APK-Datei zu kompilieren, ist das Android SDK erforderlich.

Stellen Sie sicher, dass das Android SDK installiert und die Umgebungsvariable ANDROID_HOME gesetzt ist.

Führen Sie den Build-Befehl aus (verwenden Sie den vollständigen Pfad, falls der Befehl flet nicht direkt erkannt wird):

Bash

"C:\Users\xyz\AppData\Local\Programs\Python\Python312\Scripts\flet.exe" build apk
Die fertige App (app-release.apk) finden Sie nach Abschluss des Prozesses im Ordner: Ihr Projektordner/build/app/outputs/apk/release/
