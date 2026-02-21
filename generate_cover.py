#!/usr/bin/env python3
"""Cover-Generator via Replicate API (FLUX 1.1 Pro)"""

import os, sys, json, time, urllib.request, urllib.error

# --- Config ---
DOTENV = os.path.join(os.path.dirname(__file__), ".env")
OUTPUT  = "output/test_001/cover_v2.jpg"
MODEL   = "https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions"
# Seitenverhältnis 1:1.6 (KDP-Standard: z.B. 1600×2560)
WIDTH, HEIGHT = 900, 1440  # exakt 1:1.6 (KDP-Ratio), max für FLUX 1.1 Pro

PROMPT = (
    "Painterly watercolor book cover, vertical format, professional publishing quality. "
    "A winding forest path through an ancient larch forest in peak autumn glory — the trees "
    "are breathtaking in pure amber, gold and burnt sienna, needles catching pale morning "
    "light from the left. No human figures visible. In the far background below the treeline, "
    "a small Austrian mountain village barely visible through golden autumn haze: red-tiled "
    "roofs, a church steeple, farmhouse silhouettes. Immediate foreground: a pair of well-worn "
    "brown leather hiking boots resting on a mossy granite boulder, slightly muddy, laces "
    "loosened — the suggestion of someone who has paused to look. The mood is contemplative, "
    "quietly hopeful, an exhale. Color palette: golden amber dominates the upper two thirds, "
    "deep forest green in shadow areas, slate mountain grey in the far distance, warm "
    "cream-mist sky. Traditional watercolor technique with visible paper grain, delicate "
    "wet-on-wet backgrounds, crisp foreground detail. Top quarter empty and light-colored "
    "for dark charcoal title lettering. Bottom stripe in soft cream for author name."
)

# --- Load token from .env ---
token = None
if os.path.exists(DOTENV):
    for line in open(DOTENV):
        line = line.strip()
        if line.startswith("REPLICATE_API_TOKEN="):
            token = line.split("=", 1)[1].strip()
token = token or os.environ.get("REPLICATE_API_TOKEN")
if not token:
    sys.exit("Kein REPLICATE_API_TOKEN gefunden.")

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
print("Fertig. Tipp: Titel-Text in Canva einfügen (Playfair Display, Schiefergrau).")
