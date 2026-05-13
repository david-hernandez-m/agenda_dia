[app]
title = Mi Agenda Android
package.name = miagenda
package.domain = org.pepito
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,wav
version = 1.0
requirements = python3,kivy,speechrecognition,sounddevice,scipy,numpy,soundfile,python-docx,reportlab
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24

[buildozer]
log_level = 2
warn_on_root = 1