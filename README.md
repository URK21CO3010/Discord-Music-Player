Install all dependencies using:
`pip install -r requirements.txt`

This project requires FFmpeg to function correctly. Below are the instructions for installing FFmpeg on various operating systems.

## Installation Instructions

### 1. **Install FFmpeg**

FFmpeg is a free software that needs to be installed separately. Follow the instructions below for your operating system:

#### **Windows**

1. Download the FFmpeg executable from the [FFmpeg official website](https://ffmpeg.org/download.html).
2. Extract the contents to a folder, for example, `C:\ffmpeg`.
3. Add the path to FFmpeg to your system’s `PATH` environment variable:
   - Right-click on `This PC` or `My Computer` and select `Properties`.
   - Click on `Advanced system settings`.
   - Click on `Environment Variables`.
   - In the `System variables` section, find the `Path` variable and click `Edit`.
   - Add the path to the FFmpeg `bin` folder (e.g., `C:\ffmpeg\bin`).
   - Click `OK` to close all dialog boxes.
4. Open a new command prompt and type `ffmpeg -version` to verify that FFmpeg is installed correctly.

#### **macOS**

1. Open the Terminal application.
2. Install Homebrew if you haven't already:
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Install FFmpeg using Homebrew:
   `brew install ffmpeg`
4. Type ffmpeg -version in the Terminal to check if FFmpeg is installed.
