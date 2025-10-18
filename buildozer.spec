[app]
title = Food Analyzer
package.name = foodanalyzer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy,pillow,plyer,numpy,android

[buildozer]
log_level = 2

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 30
android.minapi = 21
android.sdk = 20
android.ndk = 23b

orientation = portrait

android.accept_sdk_license = True
