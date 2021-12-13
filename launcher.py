import os
from tkinter import *

class launcher:

    def __init__(self):
        pass
    
    def launch(self, filepath):
        os.system("python " + filepath)
    
    def download(self, filepath, githublink, appname, button):
        os.system("wget " + githublink)
        button.config(text = "Launch " + appname, command = (lambda: rocket.launch(filepath)))

class app:

    def __init__(self, name, filename, filepath, button):
        self.filepath = filepath
        self.filename = filename
        self.name = name
        self.button = button

    def setup(self):
        if os.path.exists(self.filepath) == True:
            self.button.config(text = "Launch" + self.name, command = (lambda: rocket.launch(self.filepath)))
        else:
            self.button.config(text = "Download " + self.name, command = (lambda: rocket.download(self.filepath, self.filename, self.name, self.button)))
        self.button.pack(expand = True)

rocket = launcher()

window = Tk()
window.geometry("400x400")

rpgbutton = Button(window)
rpg = app("RPG", "https://github.com/WEBkatzii/rocketlauncher/raw/main/rpg.py", "~/rpg.py", rpgbutton)
rpg.setup()

window.mainloop()
