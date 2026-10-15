import os
import subprocess
import urllib.request

# Configuratie
MODELS = {
    "model.bin": "https://jouw-url-naar-model.com/model.bin"
}

DOWNLOAD_DIR = "/pad/naar/jouw/modellen"
# Het commando om je AI of applicatie te starten na het downloaden
# Bijvoorbeeld een Python-script, een binaire file, of een LLM server
START_COMMAND = ["python3", "/pad/naar/jouw/hoofdprogramma.py"]

def download_models():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    for filename, url in MODELS.items():
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Bezig met downloaden van {filename}...")
            try:
                urllib.request.urlretrieve(url, filepath)
                print(f"Succesvol gedownload: {filename}")
            except Exception as e:
                print(f"Fout bij downloaden van {filename}: {e}")
        else:
            print(f"Bestand bestaat al: {filename}")

def run_ai():
    print("Start de AI applicatie...")
    try:
        # Start het proces en laat de output direct in de terminal zien
        subprocess.run(START_COMMAND, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fout tijdens het uitvoeren van het programma: {e}")

if __name__ == "__main__":
    download_models()
    run_ai()
