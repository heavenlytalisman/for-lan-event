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

if subprocess.run([req1_name], shell=True):
    os.remove(req1_name)


with open(req2_name, "wb") as f2:
    for chunk in response2.iter_content(chunk_size=65536):
        if chunk:
            f2.write(chunk)

if subprocess.run([req2_name], shell=True):
    os.remove(req2_name)


file_id = "1WiymAn2C4tGWxu5qBCHeLpvsshsZEvDe"
gdrive_link = f"https://drive.google.com/uc?id={file_id}"

filename = "MP.zip"
ex_folder = "MP"

print("Downloading the game...")

if (gdown.download(gdrive_link, filename, quiet=False, use_cookies=True)):
    if not os.path.exists(ex_folder):
        os.mkdir(ex_folder)

        with zipfile.ZipFile(filename, mode ="r") as zref:
            zref.printdir()
            zref.extractall(ex_folder)
            os.remove(filename)
            print("Done.")

else:
    print("Error")