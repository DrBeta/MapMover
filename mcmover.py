import zipfile
from guizero import App, Text, PushButton
app = App(title="MapMover")
message = Text(app, text="Welcome to MapMover")
explainer = Text(app, text="Click the button and select the map .zip to install into minecraft.")
def select_file():
    target = app.select_file(filetypes=[["Zip Files", "*.zip"]])
    handle = zipfile.ZipFile(target)
    handle.extractall(r'c:\Users\nomen\AppData\Roaming\.minecraft\saves')
    app.info("Snowman", "It doesn't have to be a snowman")

select_button = PushButton(app, command=select_file)

app.display()

