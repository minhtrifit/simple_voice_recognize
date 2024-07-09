# SIMPLE VOICE RECOGNIZE DOCUMENATAION

## Install packages
```console
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
pip install pyinstaller # use for installing destop app
```

## Run only voice record
```python
python record.py
```

## Run full project
```python
python main.py
```

## Install app for destop
```python
pyinstaller.exe --onefile --noconsole --icon=app.ico main.py
```