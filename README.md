<p align="center">
  <img src="logo.png" alt="Freie Naturschule MSE" width="220" />
</p>

<h1 align="center">Naturschule Chat</h1>

<p align="center">
  Schlichter Desktop-Starter der Freien Naturschule MSE für den Eltern- und Schulchat.
</p>

---

## Download

Die aktuellen Installationsdateien stehen unter [**Releases**](../../releases/latest) bereit (eine Datei pro System):

| System | Datei | Hinweis |
| :--- | :--- | :--- |
| **Windows** | `Naturschule.Chat.msi` | Installer (lädt WebView2 bei Bedarf nach) |
| **macOS** | `Naturschule.Chat.dmg` | Universal-App für Apple Silicon & Intel |
| **Linux** | `naturschule-chat.AppImage` | Direkt ausführbar, keine Installation nötig |

Eine kurze Schritt-für-Schritt-Hilfe für Eltern (inklusive Hinweise zu den Sicherheitsmeldungen bei nicht-signierten Apps) liegt als PDF vor: [**Eltern-Anleitung (PDF)**](docs/eltern-anleitung.pdf).

## Eigenschaften

- **Ein Fenster, klarer Fokus:** Öffnet direkt den Schulchat und verhindert doppelte Instanzen.
- **System-Tray:** Läuft beim Schließen des Fensters im Hintergrund weiter, damit neue Nachrichten ankommen.
- **Benachrichtigungen:** Fragt beim ersten Klick automatisch nach der Berechtigung für Desktop-Benachrichtigungen.
- **Saubere Link-Trennung:** Login- und Chat-Seiten bleiben in der App, externe Links öffnen im Standardbrowser.

## Struktur

```text
├── .github/workflows/build.yml      # Automatischer Build (Windows, macOS, Linux)
├── docs/eltern-anleitung.tex        # Eltern-Anleitung (LaTeX / XeLaTeX)
├── docs/eltern-anleitung.pdf        # Fertige PDF-Anleitung
├── icons/                           # App-Icons (.png, .ico, .icns)
├── inject/notifications.js          # Berechtigungsabfrage für Benachrichtigungen
├── scripts/generate-icons.py        # Icon-Generator aus logo.png
├── scripts/naturschule-chat-linux.sh# Linux-Starthelfer (Wayland/NVIDIA)
├── pake.json                        # App- und Fensterkonfiguration
└── package.json                     # Build-Skripte (pake-cli)
```

## Lokaler Build

Voraussetzungen: Node.js 20+ und Rust (`cargo`).

```bash
npm install
npm run build:linux    # bzw. build:macos / build:windows
```

## Hinweis

Inoffizieller WebView-Wrapper auf Basis von [Pake](https://github.com/tw93/Pake) und Tauri. Alle Marken- und Urheberrechte der eingebundenen Web-Anwendung liegen beim jeweiligen Anbieter.
