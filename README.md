# Mi Agenda Android

Mi Agenda Android es una aplicación desarrollada en Python utilizando Kivy. Su objetivo es permitir al usuario registrar notas personales o diarias, guardar información por estado emocional, grabar audio, transcribir voz a texto, exportar notas en distintos formatos y compartir el contenido mediante correo electrónico o WhatsApp.

El proyecto está pensado como una aplicación de escritorio y también como una base para compilar una versión Android mediante Buildozer.

---

## Descripción general

La aplicación permite crear una agenda personal donde el usuario puede escribir cómo estuvo su día, guardar notas, revisar un historial, grabar audios, transcribir grabaciones y exportar la información generada.

Entre sus principales funciones se incluyen:

- Creación de notas personales.
- Selección del estado emocional del día.
- Guardado de notas en formato JSON.
- Exportación de notas en TXT, DOCX y PDF.
- Grabación de audio desde el micrófono.
- Transcripción automática de audio a texto.
- Transcripción en vivo.
- Reproducción de audios guardados.
- Eliminación de notas y audios.
- Edición y renombrado de notas.
- Envío del contenido por correo electrónico.
- Envío del contenido por WhatsApp.
- Configuración de idioma de transcripción.
- Corrección básica de acentos, puntuación y mayúsculas.
- Preparación para compilar como aplicación Android.

---

## Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías y librerías:

- Python 3
- Kivy
- SpeechRecognition
- SoundDevice
- SciPy
- NumPy
- SoundFile
- python-docx
- ReportLab
- Buildozer

---

## Estructura recomendada del proyecto

La carpeta del proyecto debería quedar organizada de la siguiente forma:

```text
mi-agenda-android/
├── main.py
├── buildozer.spec
├── README.md
├── requirements.txt
└── .gitignore