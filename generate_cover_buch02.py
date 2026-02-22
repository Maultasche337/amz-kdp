#!/usr/bin/env python3
"""Cover-Generator für Buch 2: Solange der Schnee liegt"""

import os, sys, json, time, urllib.request, urllib.error

# --- Config ---
DOTENV = os.path.join(os.path.dirname(__file__), ".env")
OUTPUT = "zillertal/buch02/cover.jpg"
MODEL = "https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions"
WIDTH, HEIGHT = 900, 1440  # 1:1.6 KDP-Ratio

# Variante 2: Setting-fokussiert (keine Gesichter)
PROMPT = (
    "Painterly illustration book cover, vertical format, professional publishing quality, "
    "soft impressionistic style with warm edges. "
    "A cozy alpine guesthouse at dusk, nestled in a snow-covered Tyrolean valley. "
    "Heavy snowflakes fall gently from a deep blue evening sky. The guesthouse has warm "
    "amber light glowing from its windows, smoke rising from a stone chimney. Traditional "
    "Austrian architecture with wooden balconies and green shutters covered in snow. "
    "In the foreground, a path leads to the guesthouse door, with fresh footprints in the "
    "pristine white snow — two sets of footprints, walking toward each other but not yet meeting. "
    "A wooden sled with a red wool blanket sits beside the snowy path. Tall fir trees heavy "
    "with snow frame the scene on both sides. "
    "The mountains in the background are partially hidden by gently falling snow, creating "
    "depth and romantic mystery. The overall mood is warm despite the cold, inviting, romantic — "
    "like coming home after a long journey. "
    "Color palette: Deep twilight blue sky, warm golden-orange from windows, pure white snow, "
    "dark green fir trees, touches of red from the blanket. "
    "Impressionistic, dreamy quality with visible brushstrokes. "
    "Leave generous empty space at top for dark title text and bottom for author name in cream."
)

# --- Load token from .env ---
token = None
if os.path.exists(DOTENV):
    for line in open(DOTENV):
        line = line.strip()
        # Support both KEY and TOKEN naming
        if line.startswith("REPLICATE_API_KEY=") or line.startswith("REPLICATE_API_TOKEN="):
            token = line.split("=", 1)[1].strip()
            break
token = token or os.environ.get("REPLICATE_API_TOKEN") or os.environ.get("REPLICATE_API_KEY")
if not token:
    sys.exit("Kein REPLICATE_API_KEY/TOKEN gefunden.")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "wait",
}

def api(method, url, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"API-Fehler {e.code}: {e.read().decode()}")

# --- Prediction erstellen ---
print("Sende Anfrage an Replicate (FLUX 1.1 Pro)...")
print(f"Prompt: {PROMPT[:100]}...")
payload = {"input": {"prompt": PROMPT, "width": WIDTH, "height": HEIGHT,
                     "output_format": "jpg", "output_quality": 95}}
pred = api("POST", MODEL, payload)
pred_id = pred["id"]
pred_url = f"https://api.replicate.com/v1/predictions/{pred_id}"
print(f"Prediction ID: {pred_id}")

# --- Polling ---
for attempt in range(1, 61):
    status = pred.get("status")
    if status == "succeeded":
        break
    if status == "failed":
        sys.exit(f"Generierung fehlgeschlagen: {pred.get('error')}")
    print(f"  [{attempt}/60] Status: {status} — warte 5s...")
    time.sleep(5)
    pred = api("GET", pred_url)

output = pred.get("output")
if not output:
    sys.exit("Kein Output erhalten.")
img_url = output[0] if isinstance(output, list) else output
print(f"Bild-URL: {img_url}")

# --- Download ---
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
print(f"Lade herunter → {OUTPUT}")
urllib.request.urlretrieve(img_url, OUTPUT)
size_kb = os.path.getsize(OUTPUT) // 1024
print(f"Gespeichert: {OUTPUT} ({size_kb} KB)")
print("\nFertig! Nächster Schritt: Titel-Text in Canva hinzufügen")
print("  Titel: 'Solange der Schnee liegt' (Playfair Display, Creme/Weiß)")
print("  Untertitel: 'Zillertal-Herzen 2' (Kapitälchen)")
print("  Autorin: 'Maja Sternberg' (unten)")
