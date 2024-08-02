# ITF Match Recorder
This repository contains two Python scripts for recording ITF tennis match livestreams. The scripts scrape a website to find video URLs and then record the selected livestream using `ffmpeg`.

## Files

- `siteparser.py`: Parses a website to find video items and allows the user to select a match to download the HTML page.
- `videodownloader.py`: Records the livestream from a given URL using `ffmpeg`.

## Requirements

- `requests`
- `beautifulsoup4`
- `InquirerPy`
- `ffmpeg`

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Ensure you have ffmpeg installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html). Otherwise, you can install it using Homebrew on macOS:

```bash
brew install ffmpeg
```

### Setting up a virtual environment

To create a virtual environment called `venv` and install the required packages, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory: `/Users/alexwest/Documents/ITF-Match-Recorder/`.
3. Run the following command to create a virtual environment:
  ```bash
  python -m venv venv
  ```
4. Activate the virtual environment:
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
5. Once the virtual environment is activated, install the required packages from the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

Now you have successfully set up a virtual environment called `venv` and installed the required packages.