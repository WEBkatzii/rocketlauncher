import os
from tkinter import *

class launcher:

    def __init__(self):
        pass
    
    def launch(self, filepath):
        os.system("python " + filepath)
    
    def download(self, filepath, githublink, appname, button):
        if os.path.exists(filepath) == True:
            os.system("rm " + filepath)
        os.system("wget " + githublink)
        button.config(text = "Launch " + appname, command = (lambda: rocket.launch(filepath)))
    
    def search(self, searchterm, applist, appnames):
        if searchterm in appnames:
            searchresult = applist[int(appnames.index(searchterm))]
            rocket.download(searchresult.filepath, searchresult.filename, searchresult.name, searchresult.button)


class app:

    def __init__(self, name, filename, filepath, button):
        self.filepath = filepath
        self.filename = filename
        self.name = name
        self.button = button
        if os.path.exists(self.filepath) == True:
            os.system("rm " + filepath)
            rocket.download(self.filepath, self.filename, self.name, self.button)
            self.button.config(text = "Launch" + self.name, command = (lambda: rocket.launch(self.filepath)))
        else:
            self.button.config(text = "Download " + self.name, command = (lambda: rocket.download(self.filepath, self.filename, self.name, self.button)))
        self.button.pack(expand = True)

rocket = launcher()

window = Tk()
window.geometry("1000x600")

bannerimg = PhotoImage(file = "launcherlogo.PNG")
Banner = Label(image = bannerimg)
Banner.pack()

rpgbutton = Button(window)
rpg = app("RPG", "https://github.com/WEBkatzii/rocketlauncher_apps/raw/main/rpg.py", "rpg.py", rpgbutton)

T_editorbutton = Button(window)
T_editor = app("T_editor", "https://github.com/WEBkatzii/rocketlauncher_apps/raw/main/T_editor.py, ", "T_editor.py", T_editorbutton)

ttwbutton = Button(window)
ttw = app("Through the Winter", "https://github.com/WEBkatzii/rocketlauncher_apps/raw/main/through_the_winter.py", "through_the_winter.py", ttwbutton)

appnames = ["RPG", "T_editor", "Through the Winter"]
applist = [rpg, T_editor, ttw]

searchfield = Text(window, height = 1, width = 20)
searchfield.pack()

searchbutton = Button(window,text = "Search", command = (lambda: rocket.search((searchfield.get(0.0, END).strip()), applist, appnames)))
searchbutton.pack()

window.mainloop()