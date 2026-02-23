#!/usr/bin/env python3
"""Cover-Generator für Buch 4: Wenn der Sommer bleibt"""

import os, sys, json, time, urllib.request, urllib.error

# --- Config ---
DOTENV = os.path.join(os.path.dirname(__file__), ".env")
OUTPUT_DIR = "zillertal/buch04"
MODEL = "https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions"
WIDTH, HEIGHT = 900, 1440  # 1:1.6 KDP-Ratio

COVERS = [
    {
        "name": "cover_v1.jpg",
        "desc": "Klassisches Romance-Cover",
        "prompt": (
            "Professional romance book cover, photorealistic style, vertical format 1:1.6. "
            "A man and woman in their early forties standing close together on a sunlit alpine meadow. "
            "The man has brown hair with subtle gray at the temples, warm brown eyes, wearing a casual "
            "button-down shirt with sleeves rolled up. The woman has dark blonde hair in a loose ponytail, "
            "green eyes, light summer freckles, wearing a simple white blouse. They are looking at each other "
            "with tender smiles, shoulders almost touching. Background: majestic Austrian Alps in soft focus, "
            "green summer meadows with wildflowers, golden evening light creating a warm glow. Leave upper third "
            "empty and light for title text. Color palette: warm greens, golden yellows, soft blues, earth tones. "
            "Professional publishing quality, cinematic lighting, romantic mood, no text on image."
        )
    },
    {
        "name": "cover_v2.jpg",
        "desc": "Setting-fokussiert",
        "prompt": (
            "Professional book cover, atmospheric landscape, vertical format 1:1.6. "
            "A serene alpine lake at sunset in the Austrian Tyrol. Crystal clear turquoise water reflecting "
            "majestic mountain peaks. Wildflower meadow in the foreground with daisies and alpine flowers. "
            "Two sets of hiking boots and a woven picnic blanket visible at the edge of the water, suggesting "
            "two people just out of frame. Golden hour lighting casting warm amber and pink hues across the "
            "mountains and sky. A small traditional Tyrolean village visible in the distant valley below. "
            "Leave generous space at top for title text, lighter sky area. Color palette: turquoise water, "
            "golden light, soft pinks, deep greens. Slightly painterly style, romantic, nostalgic. "
            "Professional publishing quality, no text on image."
        )
    },
    {
        "name": "cover_v3.jpg",
        "desc": "Symbolisch/Modern",
        "prompt": (
            "Professional book cover, minimalist romantic style, vertical format 1:1.6. "
            "Close-up of two hands intertwined against a blurred background of alpine summer scenery. "
            "One hand is masculine, slightly weathered, wearing a simple watch. The other is feminine "
            "with subtle freckles and natural nails. Between their fingers, a single edelweiss flower. "
            "Soft golden sunlight filtering through, creating a warm dreamy bokeh effect. The background "
            "suggests green meadows and distant blue mountains, completely out of focus. Intimate, tender, "
            "romantic mood. Leave ample space at top for large title text. Color palette: warm gold, "
            "soft skin tones, hints of green and white. Modern romance, elegant, emotional. "
            "Professional publishing quality, high-end editorial photography style, no text on image."
        )
    }
]

# --- Load token ---
token = None
if os.path.exists(DOTENV):
    for line in open(DOTENV):
        line = line.strip()
        if line.startswith("REPLICATE_API_TOKEN=") or line.startswith("REPLICATE_API_KEY="):
            token = line.split("=", 1)[1].strip()
token = token or os.environ.get("REPLICATE_API_TOKEN") or os.environ.get("REPLICATE_API_KEY")
if not token:
    sys.exit("Kein REPLICATE_API_TOKEN/KEY gefunden. Bitte in .env eintragen.")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Prefer": "wait",
}

def api(method, url, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"API-Fehler {e.code}: {e.read().decode()}")
        return None

def generate_cover(prompt, output_path):
    print(f"\nGeneriere: {output_path}")
    print(f"Prompt: {prompt[:100]}...")

    payload = {
        "input": {
            "prompt": prompt,
            "width": WIDTH,
            "height": HEIGHT,
            "output_format": "jpg",
            "output_quality": 95
        }
    }

    pred = api("POST", MODEL, payload)
    if not pred:
        return False

    pred_id = pred["id"]
    pred_url = f"https://api.replicate.com/v1/predictions/{pred_id}"
    print(f"Prediction ID: {pred_id}")

    # Polling
    for attempt in range(1, 61):
        status = pred.get("status")
        if status == "succeeded":
            break
        if status == "failed":
            print(f"Fehlgeschlagen: {pred.get('error')}")
            return False
        print(f"  [{attempt}/60] Status: {status}")
        time.sleep(5)
        pred = api("GET", pred_url)
        if not pred:
            return False

    output = pred.get("output")
    if not output:
        print("Kein Output erhalten.")
        return False

    img_url = output[0] if isinstance(output, list) else output
    print(f"Bild-URL: {img_url}")

    # Download
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    urllib.request.urlretrieve(img_url, output_path)
    size_kb = os.path.getsize(output_path) // 1024
    print(f"Gespeichert: {output_path} ({size_kb} KB)")
    return True

# --- Main ---
print("=" * 50)
print("COVER-GENERATOR: Wenn der Sommer bleibt")
print("=" * 50)

for i, cover in enumerate(COVERS):
    output_path = os.path.join(OUTPUT_DIR, cover["name"])

    # Skip if already exists
    if os.path.exists(output_path):
        print(f"\n--- {cover['desc']} ---")
        print(f"⏭️  {cover['name']} existiert bereits, überspringe")
        continue

    # Wait between requests to avoid rate limiting
    if i > 0:
        print("\n⏳ Warte 15s wegen Rate-Limiting...")
        time.sleep(15)

    print(f"\n--- {cover['desc']} ---")
    success = generate_cover(cover["prompt"], output_path)
    if success:
        print(f"✅ {cover['name']} erfolgreich generiert")
    else:
        print(f"❌ {cover['name']} fehlgeschlagen")

print("\n" + "=" * 50)
print("Fertig! Cover liegen in:", OUTPUT_DIR)
print("Nächster Schritt: Typografie hinzufügen (Canva/Photoshop)")
