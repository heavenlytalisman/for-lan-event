import gdown
import os
import zipfile

gdrive_link = ""

filename = "game.zip"
ex_folder = "game"

gdown.download(gdrive_link, filename, quiet=False)

if not os.path.exists(ex_folder):
    os.mkdir(ex_folder)

with zipfile.ZipFile(filename, mode ="r") as zref:
    zref.extractall(ex_folder)


