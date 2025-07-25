import tkinter as tk

from frontend.components.label import Label
from frontend.components.entry import Entry
from frontend.components.button import Button
from frontend.components.textentry import TextEntry
from frontend.panels.settings_panel import Settings_Panel
from frontend.panels.history_panel import History_Panel
from frontend.panels.main_panel import Main_Panel

class Main_Screen:

    output_file_name = "output.mp3"

    def __init__(self, client, user, voice, character):
        self.client = client
        self.user = user
        self.character = character
        self.voice = voice
        self.label = Label()
        self.entry = Entry()
        self.button = Button()
        self.text_entry = TextEntry()
        self.settings_panel = Settings_Panel(client, voice, character)
        self.history_panel = History_Panel(user, voice)
        self.main_panel = Main_Panel(user, voice, self.output_file_name)

    def display_screen(self):
        root = tk.Tk()
        root.resizable(False, False)
        root.title("ThinkAloud")

        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, padx=10, pady=10)
        left_frame.pack(side="left", fill=tk.Y)

        separator_left = tk.Frame(main_frame, width=2, bg="gray")
        separator_left.pack(side="left", fill=tk.Y)

        center_frame = tk.Frame(main_frame, padx=20, pady=20)
        center_frame.pack(side="left", fill=tk.BOTH, expand=True)

        separator_right = tk.Frame(main_frame, width=2, bg="gray")
        separator_right.pack(side="left", fill=tk.Y)

        right_frame = tk.Frame(main_frame, padx=20, pady=20)
        right_frame.pack(side="left", fill=tk.BOTH, expand=True)

        self.settings_panel.display_panel(right_frame)
        self.history_panel.display_panel(left_frame)

        char_id = self.settings_panel.get_char_id
        self.main_panel.display_card(center_frame, char_id)

        root.mainloop()