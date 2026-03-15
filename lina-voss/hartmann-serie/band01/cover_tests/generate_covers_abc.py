#!/usr/bin/env python3
"""Cover-Generator: 3 Varianten (A/B/C) für Band 1 — Tageslicht
Modell: Ideogram v2 Turbo via Replicate API (gut für Text-Rendering)

Text auf dem Cover (EXAKT):
  LINA ELISE VOSS
  TAGESLICHT
  Ein Grumpy-meets-Sunshine Liebesroman
  Die Hartmann-Agentur 1
"""

import os, sys, json, time, urllib.request, urllib.error

DOTENV = os.path.join(os.path.dirname(__file__), "../../../../.env")
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = "https://api.replicate.com/v1/models/ideogram-ai/ideogram-v2-turbo/predictions"

# Der exakte Text der auf jedem Cover stehen MUSS
COVER_TEXT = (
    'Text on cover reads exactly: '
    'Top: "LINA ELISE VOSS" in elegant script font. '
    'Center large: "TAGESLICHT" in bold serif capital letters. '
    'Below title: "Ein Grumpy-meets-Sunshine Liebesroman" in smaller serif font. '
    'Bottom: "Die Hartmann-Agentur 1" in small caps. '
)

COVERS = [
    {
        "name": "cover_A_typo",
        "file": "cover_A_typography.png",
        "prompt": (
            "Professional book cover design, 2:3 portrait format for Kindle eBook. "
            "Style inspired by Emily Key / Manhattan Millionärs series. "
            "TYPOGRAPHY-DOMINANT DESIGN, NO PEOPLE, NO FIGURES, NO FACES. "
            "Background: soft marble or watercolor texture in steel blue, light navy and silver-grey tones. "
            "Decorative torn paper effect revealing a deeper blue-grey layer underneath. "
            "Gold metallic foil accents and gold dust/glitter particles scattered at corners. "
            "Warm amber and gold tones for the title typography. "
            "Clean, luxurious, modern romance aesthetic. "
            "Plenty of white/light space. Elegant and premium feel. "
            + COVER_TEXT
        ),
    },
    {
        "name": "cover_B_portrait",
        "file": "cover_B_portrait.png",
        "prompt": (
            "Professional book cover design, 2:3 portrait format for Kindle eBook. "
            "INK AND WATERCOLOR ILLUSTRATION of a man, 32, dark tousled hair, intense dark eyes, "
            "angular jaw with stubble, white dress shirt with open collar. "
            "Artistic editorial illustration style with loose expressive brushstrokes, "
            "visible ink outlines, watercolor washes bleeding outward. NOT photorealistic. "
            "He looks emotionally guarded, frozen, controlled — not angry but EMPTY. "
            "Color palette: bold steel blue, navy and silver-grey watercolor washes, "
            "with striking warm amber and burnt sienna accents bleeding through — "
            "like warmth escaping through cracks in ice. "
            "Upper portion has space for author name, lower portion for title. "
            "White paper texture visible at edges. "
            + COVER_TEXT +
            "Title 'TAGESLICHT' in warm amber/gold serif against the blue-grey washes. "
            "Author name in elegant script at top."
        ),
    },
    {
        "name": "cover_C_silhouette",
        "file": "cover_C2_silhouette.png",
        "prompt": (
            "Professional book cover design, 2:3 portrait format for Kindle eBook. "
            "DOUBLE EXPOSURE / SILHOUETTE DESIGN. "
            "Dark silhouette of a man's head and shoulders in profile or three-quarter view, "
            "filled with a warm golden sunset cityscape — Hamburg Speicherstadt warehouse district "
            "with red brick warehouses, canal reflections, harbor cranes in distance, warm amber evening light. "
            "NO modern skyscrapers, NO generic city skyline. Distinctly HAMBURG architecture: "
            "Speicherstadt brick facades, Elbphilharmonie silhouette, church spires, harbor. "
            "Inside the silhouette: a smaller female figure walking toward the light. "
            "Background: deep navy to dark steel blue gradient, moody and atmospheric. "
            "The silhouette edges dissolve into watercolor-like washes of navy and amber. "
            "Cinematic, emotional, contemporary romance aesthetic. "
            'Text on cover reads exactly: '
            'Top: "LINA ELISE VOSS" in elegant white script font. '
            'Center large: "Tageslicht" in warm amber/gold bold serif letters, large and prominent. '
            'Below title: "Ein Grumpy-meets-Sunshine Liebesroman" in smaller white serif font. '
            'Bottom: "DIE HARTMANN-AGENTUR BAND 1" in white small caps. '
        ),
    },
]

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

def generate_cover(cover):
    name = cover["name"]
    outfile = os.path.join(OUTPUT_DIR, cover["file"])

    print(f"\n{'='*60}")
    print(f"  Generiere: {name}")
    print(f"  Datei: {cover['file']}")
    print(f"{'='*60}")

    payload = {
        "input": {
            "prompt": cover["prompt"],
            "resolution": "640x1536",
        }
    }

    # Retry bei Rate-Limit (429)
    pred = None
    for retry in range(5):
        pred = api("POST", MODEL, payload)
        if pred:
            break
        print(f"  ⏳ Rate-Limit, warte 15s (Retry {retry+1}/5)...")
        time.sleep(15)

    if not pred:
        print(f"  ❌ {name}: Prediction fehlgeschlagen.")
        return False

    pred_id = pred["id"]
    pred_url = f"https://api.replicate.com/v1/predictions/{pred_id}"
    print(f"  Prediction ID: {pred_id}")

    for attempt in range(1, 121):
        status = pred.get("status")
        if status == "succeeded":
            break
        if status in ("failed", "canceled"):
            print(f"  ❌ {name}: Status={status}, Error={pred.get('error')}")
            return False
        print(f"  [{attempt}/120] Status: {status} — warte 5s...")
        time.sleep(5)
        pred = api("GET", pred_url)
        if not pred:
            return False

    output = pred.get("output")
    if not output:
        print(f"  ❌ {name}: Kein Output erhalten.")
        return False

    img_url = output[0] if isinstance(output, list) else output
    print(f"  Bild-URL: {img_url}")
    urllib.request.urlretrieve(img_url, outfile)
    size_kb = os.path.getsize(outfile) // 1024
    print(f"  ✅ {name}: Gespeichert ({size_kb} KB)")
    return True


if __name__ == "__main__":
    print("Cover-Generator: 3 Varianten für Tageslicht")
    print(f"Modell: Ideogram v2 Turbo via Replicate")
    print(f"Output: {OUTPUT_DIR}\n")

    results = {}
    for i, cover in enumerate(COVERS):
        success = generate_cover(cover)
        results[cover["name"]] = success
        if i < len(COVERS) - 1 and success:
            print("  ⏳ 15s Pause (Rate-Limit-Schutz)...")
            time.sleep(15)

    print(f"\n{'='*60}")
    print("ERGEBNIS:")
    for name, ok in results.items():
        status = "✅" if ok else "❌"
        print(f"  {status} {name}")
    print(f"{'='*60}")
