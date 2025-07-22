import gdown
import os
import zipfile
import requests
import subprocess


req1_url = "https://aka.ms/vs/17/release/vc_redist.x86.exe"
req2_url = "https://aka.ms/vs/17/release/vc_redist.x64.exe"

req1_name = "vcredist.x86.exe"
req2_name = "vcredist.x64.exe"

print("Downloading and installing requirements...")
response1 = requests.get(req1_url, stream=True)
response2 = requests.get(req2_url, stream=True)

with open(req1_name, "wb") as f1:
    for chunk in response1.iter_content(chunk_size=65536):
        if chunk:
            f1.write(chunk)

subprocess.run([req1_name], shell=True)


with open(req2_name, "wb") as f2:
    for chunk in response2.iter_content(chunk_size=65536):
        if chunk:
            f2.write(chunk)

subprocess.run([req2_name], shell=True)


gdrive_link = "https://drive.google.com/file/d/1Fox-l7wnw_0CwPaQlphPm2J7tieSdELt/view?usp=drive_link"

filename = "MP.zip"
ex_folder = "MP"

print("Downloading the game...")

gdown.download(gdrive_link, filename, quiet=False)

if not os.path.exists(ex_folder):
    os.mkdir(ex_folder)

with zipfile.ZipFile(filename, mode ="r") as zref:
    zref.extractall(ex_folder)

os.remove(filename)
print("Done.")

