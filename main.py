import tkinter as tk
from threading import Thread
from tts import TextToSpeech
from stt import SpeechToText
from settings import RESPONSES, INTERFACE_TEXT
from gui import VoiceAssistantGUI

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.tts = TextToSpeech()
        self.stt = SpeechToText()
        
        # Создаем GUI
        self.gui = VoiceAssistantGUI(root, self.start_listening)

    def start_listening(self, assistant_name):
        self.gui.insert_text(INTERFACE_TEXT["listening"])
        
        # Запускаем прослушивание в отдельном потоке
        listening_thread = Thread(target=self.listen_commands, args=(assistant_name,))
        listening_thread.start()

    def listen_commands(self, assistant_name):
        while True:
            command = self.stt.listen().lower()
            self.gui.insert_text(INTERFACE_TEXT["you_said"] + command)
            
            # Проверяем, упоминается ли имя ассистента в команде
            if assistant_name.lower() in command:
                for phrase in RESPONSES.keys():
                    if phrase.lower() in command:
                        response = RESPONSES[phrase]
                        self.gui.insert_text(f"{assistant_name}: {response}")
                        self.tts.speak(response)
                        break
                else:
                    self.gui.insert_text(f"{assistant_name}: {INTERFACE_TEXT['unknown_command']}")
                    self.tts.speak(INTERFACE_TEXT["unknown_command"])
            else:
                continue  # Игнорируем команды, которые не содержат имя ассистента

def main():
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()