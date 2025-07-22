import gdown
import os
import zipfile


gdrive_link = "https://drive.google.com/file/d/1Fox-l7wnw_0CwPaQlphPm2J7tieSdELt/view?usp=drive_link"

filename = "MP.zip"
ex_folder = "MP"

gdown.download(gdrive_link, filename, quiet=False)

if not os.path.exists(ex_folder):
    os.mkdir(ex_folder)

with zipfile.ZipFile(filename, mode ="r") as zref:
    zref.extractall(ex_folder)

os.remove(filename)


