import vosk
import sys
import os
import json

class SpeechToText:
    def __init__(self):
        if not os.path.exists("model"):
            print("Пожалуйста, скачайте модель Vosk и распакуйте её в папку 'model'")
            sys.exit(1)

        self.model = vosk.Model("model")
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)

    def listen(self):
        import pyaudio
        
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                return result.get('text', '')