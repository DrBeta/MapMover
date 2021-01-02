import zipfile
from guizero import App, Text, PushButton
import os 
import pyperclip
app = App(title="MapMover")
message = Text(app, text="Welcome to MapMover")
explainer = Text(app, text="Click the button and select the map .zip to install into minecraft.")
def select_file():
    target = app.select_file(filetypes=[["Zip Files", "*.zip"]])
    handle = zipfile.ZipFile(target)
    appdata = os.getenv('APPDATA')
    print(appdata + r"\.minecraft\saves")
    handle.extractall(appdata + r"\.minecraft\saves")
    app.info("Done", "Your map was successfully moved!")

select_button = PushButton(app, command=select_file, text="Select Zip")
def donate():
    pyperclip.copy("37iMBHQZ9e4tLF1MNibwytixR7pfVPbApe")
    app.info("Donate", "Bitcoin address copied to clipboard!")
PushButton(app, command=donate, text="Love it? Send me Bitcoin!")

app.display()

