import tkinter as tk
from tkinter import scrolledtext, ttk

class VoiceAssistantGUI:
    def __init__(self, root, start_listening_callback):
        self.root = root
        self.start_listening_callback = start_listening_callback

        self.root.title("Голосовой ассистент")
        self.root.geometry("400x500")
        self.root.configure(bg="#F0F0F0")

        # Стиль для ttk
        style = ttk.Style()
        style.configure("TLabel", background="#F0F0F0", font=("Helvetica", 12))
        style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        style.map("TButton", background=[('active', '#45a049')])

        # Поле для ввода имени ассистента
        self.name_label = ttk.Label(root, text="Введите имя ассистента:")
        self.name_label.pack(pady=10)

        self.name_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.name_entry.pack(pady=10, padx=20, fill='x')

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Helvetica", 12))
        self.text_area.pack(pady=10, padx=20, fill='both', expand=True)

        self.start_button = ttk.Button(root, text="Начать слушать", command=self.start_listening)
        self.start_button.pack(pady=10)

    def start_listening(self):
        assistant_name = self.name_entry.get().strip()
        if not assistant_name:
            self.text_area.insert(tk.END, "Пожалуйста, введите имя ассистента.\n")
            return
        self.start_listening_callback(assistant_name)

    def insert_text(self, text):
        self.text_area.insert(tk.END, text + "\n")