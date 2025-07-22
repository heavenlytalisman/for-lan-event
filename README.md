
> **⚠️ It's made for my own personal use**  

This repository contains a Python script (`main.py`) and a Windows executable (`main.exe`) that automate downloading and installing the required Visual C++ Redistributables (x86 & x64) and retrieving the game ZIP from my Google Drive.

## Table of Contents

- [Overview](#overview)  
- [Requirements](#requirements)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Disclaimer](#disclaimer)  

## Overview

This project automates:  
1. Downloading and silently installing the Visual C++ Redistributable (x86 and x64).  
2. Downloading a ZIP file (`MP.zip`) from a private Google Drive link.  
3. Extracting its contents into an `MP/` folder.  
4. Providing a Windows executable (`main.exe`) for one-click installation.  
5. Including the installer Python script (`main.py`) for those who prefer running via Python.

## Requirements

- **Windows OS**: Windows 7 or later  
- **Optional (for Python script)**:  
  - Python 3.7 or later  
  - `requests` library  
  - `gdown` library  

Install Python dependencies with:  
```bash
pip install requests gdown
```
> You do *not* need Python installed if you use `main.exe`.

## Setup & Installation

### Option 1: Windows Executable

1. Download `main.exe` from this repository's Releases.  
2. Double-click `main.exe` and follow the prompts.  
   - Installs the Visual C++ Redistributables (x86 & x64).  
   - Downloads and extracts `JKMP.zip` into the `MP\` folder.  

### Option 2: Python Script

```bash
git clone https://github.com/your-username/mp-installer.git
cd mp-installer
pip install requests gdown
python main.py
```

## Usage

- After installation, launch the game via the shortcut or by running the executable inside the `MP\` directory.

## File Structure

```
/
├── main.py      # Python installer script (optional)
├── main.exe     # Windows installer executable
└── MP/          # Extracted game files (created at runtime)
```

## Disclaimer

- **It's made for my own personal use**;.  
- **No Warranty**: Use at your own risk; the author is not responsible for any damage or data loss.
