#!/usr/bin/env python3
"""Test 16: Leon Hartmann — überarbeitetes Portrait mit stärkerem Eis-Kontrast.
Modell: Stable Diffusion 3.5 Large via Replicate API"""

import os, sys, json, time, urllib.request, urllib.error

DOTENV = os.path.join(os.path.dirname(__file__), "../../../.env")
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = "https://api.replicate.com/v1/models/stability-ai/stable-diffusion-3.5-large/predictions"

STYLE = (
    "Ink and watercolor illustration of a portrait, loose expressive brushstrokes, "
    "visible ink outlines with watercolor washes bleeding into white paper background. "
    "Artistic, editorial illustration style. NOT photorealistic. "
    "White background with watercolor splashes for text overlay space. "
    "Upper body portrait, slight three-quarter angle. "
)

NEGATIVE = (
    "photorealistic, photograph, 3d render, anime, cartoon, text, letters, words, "
    "logo, watermark, frame, border, busy background, smiling, happy"
)

PORTRAIT = {
    "name": "leon_v2",
    "file": "test16_leon_v2.png",
    "prompt": STYLE + (
        "A man, 32, German, hauntingly intense and emotionally frozen. "
        "Dark tousled hair falling across his forehead, looks like he slept at the office. "
        "Deep dark eyes — guarded, watchful, registering everything while giving nothing away. "
        "Strong angular jaw with light stubble, sharp cheekbones, exhaustion visible beneath the control. "
        "White dress shirt with open collar, sleeves rolled up, slightly wrinkled — effortlessly attractive "
        "but completely unaware of it. "
        "Expression: closed off, intense, a wall of ice — but something raw and vulnerable barely visible "
        "behind the eyes if you look long enough. NOT grumpy, NOT angry — FROZEN. Empty. Controlled. "
        "Color palette: BOLD deep steel blue, navy and silver-grey watercolor washes dominating the piece, "
        "strong ink outlines in near-black, with striking warm amber and burnt sienna accents bleeding "
        "through the cold — like heat trying to escape through cracks in ice. "
        "High contrast between the cold blues and warm amber. Dramatic, moody, emotionally charged."
    ),
}

# --- Load token ---
token = None
if os.path.exists(DOTENV):
    for line in open(DOTENV):
        line = line.strip()
        if line.startswith("REPLICATE_API_KEY="):
            token = line.split("=", 1)[1].strip()
        elif line.startswith("REPLICATE_API_TOKEN="):
            token = line.split("=", 1)[1].strip()
token = token or os.environ.get("REPLICATE_API_KEY") or os.environ.get("REPLICATE_API_TOKEN")
if not token:
    sys.exit("Kein Replicate API Token gefunden.")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "wait",
}

def api(method, url, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"API-Fehler {e.code}: {e.read().decode()}")
        return None

def generate():
    outfile = os.path.join(OUTPUT_DIR, PORTRAIT["file"])
    print(f"Generiere: LEON v2 (test16)")
    print(f"Datei: {outfile}\n")

    payload = {
        "input": {
            "prompt": PORTRAIT["prompt"],
            "negative_prompt": NEGATIVE,
            "aspect_ratio": "2:3",
            "output_format": "png",
            "cfg": 5.5,
            "steps": 45,
        }
    }

    pred = api("POST", MODEL, payload)
    if not pred:
        sys.exit("Prediction fehlgeschlagen.")

    pred_id = pred["id"]
    pred_url = f"https://api.replicate.com/v1/predictions/{pred_id}"
    print(f"Prediction ID: {pred_id}")

    for attempt in range(1, 121):
        status = pred.get("status")
        if status == "succeeded":
            break
        if status in ("failed", "canceled"):
            sys.exit(f"Status={status}, Error={pred.get('error')}")
        print(f"[{attempt}/120] Status: {status} — warte 5s...")
        time.sleep(5)
        pred = api("GET", pred_url)
        if not pred:
            sys.exit("Polling fehlgeschlagen.")

    output = pred.get("output")
    if not output:
        sys.exit("Kein Output erhalten.")

    img_url = output[0] if isinstance(output, list) else output
    print(f"Bild-URL: {img_url}")
    urllib.request.urlretrieve(img_url, outfile)
    size_kb = os.path.getsize(outfile) // 1024
    print(f"✅ Gespeichert: {outfile} ({size_kb} KB)")

if __name__ == "__main__":
    generate()
