name: Build Kivy APK

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          python3-pip \
          openjdk-11-jdk \
          git \
          zip \
          unzip \
          build-essential
          
    - name: Install Buildozer
      run: |
        pip3 install buildozer
        pip3 install cython==0.29.33
        
    - name: Accept Android licenses
      run: |
        mkdir -p ~/.android
        touch ~/.android/repositories.cfg
        yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses || true
        
    - name: Build APK
      run: |
        buildozer -v android debug
      timeout-minutes: 40
