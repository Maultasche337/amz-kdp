#!/usr/bin/env python3
"""Portrait-Generator: Ink/Watercolor-Portraits für alle Hartmann-Cousins + Werner
Modell: Stable Diffusion 3.5 Large via Replicate API"""

import os, sys, json, time, urllib.request, urllib.error

# --- Config ---
DOTENV = os.path.join(os.path.dirname(__file__), "../../../.env")
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL = "https://api.replicate.com/v1/models/stability-ai/stable-diffusion-3.5-large/predictions"

# Gemeinsamer Stil-Prefix (konsistent mit test9/test9b)
STYLE = (
    "Ink and watercolor illustration of a portrait, loose expressive brushstrokes, "
    "visible ink outlines with watercolor washes bleeding into white paper background. "
    "Artistic, editorial illustration style. NOT photorealistic. "
    "White background with watercolor splashes for text overlay space. "
    "Upper body portrait, slight three-quarter angle. "
)

NEGATIVE = (
    "photorealistic, photograph, 3d render, anime, cartoon, text, letters, words, "
    "logo, watermark, frame, border, busy background"
)

# --- Charakter-Prompts ---
PORTRAITS = [
    {
        "name": "carla",
        "file": "test10_carla.png",
        "prompt": STYLE + (
            "A woman, 29, German, controlled and polished appearance with tension beneath the surface. "
            "Dark brown hair pulled back in a sleek low bun, a few strands escaping — suggesting "
            "cracks in her perfect facade. Clear, intelligent grey-blue eyes with a hint of exhaustion "
            "she tries to hide. Angular elegant face, high cheekbones. "
            "Wearing a crisp white blouse with a structured blazer, immaculate but slightly stiff. "
            "Expression: composed smile that doesn't quite reach her eyes. "
            "Color palette: slate grey and cool blue watercolor washes, white space, "
            "with subtle warm rust-red and amber accents bleeding through at the edges — "
            "warmth trying to break through control."
        ),
    },
    {
        "name": "jakob",
        "file": "test11_jakob.png",
        "prompt": STYLE + (
            "A man, 31, German, classically handsome with effortless charm. "
            "Sandy brown wavy hair, styled but not overdone. Warm hazel eyes with a knowing, "
            "slightly performative sparkle — the kind of smile that sells anything. "
            "Strong jaw, dimples, open friendly face. "
            "Wearing a well-fitted casual blazer over a soft crew-neck, relaxed elegance. "
            "Expression: engaging warm smile, but something hollow behind the eyes if you look closely. "
            "Color palette: honey gold and warm brown watercolor washes, cream tones, "
            "with cooler grey and taupe shadows underneath — the mask beneath the warmth."
        ),
    },
    {
        "name": "nils",
        "file": "test12_nils.png",
        "prompt": STYLE + (
            "A young man, 27, German, angular and artistic with restless rebel energy. "
            "Dark messy hair falling into his face, strong eyebrows, sharp jawline. "
            "Intense dark eyes with a defiant, almost hostile look — but vulnerability visible beneath. "
            "Lean face, slight shadows under his eyes. "
            "Wearing a dark henley or simple black t-shirt, maybe paint-stained fingers visible. "
            "Expression: challenging, guarded, chin slightly raised. "
            "Color palette: anthracite and deep teal watercolor washes, forest green ink accents, "
            "with hidden warm sienna and amber tones bleeding at the margins — warmth he won't show."
        ),
    },
    {
        "name": "maren",
        "file": "test13_maren.png",
        "prompt": STYLE + (
            "A woman, 28, German, free-spirited and adventurous with bohemian energy. "
            "Wild auburn-brown wavy hair, slightly sun-bleached at the tips, falling loose and untamed. "
            "Bright warm brown eyes full of light and restlessness. Freckled skin, sun-kissed. "
            "Wearing a loose linen shirt or casual layer, maybe a vintage camera strap across shoulder. "
            "Expression: half-smile, looking slightly to the side as if about to leave — "
            "caught between staying and going. "
            "Color palette: gold and sunset orange watercolor washes, jewel tones of amber and sienna, "
            "grounded by deep teal and forest green ink accents — wild but rooted."
        ),
    },
    {
        "name": "tom",
        "file": "test14_tom.png",
        "prompt": STYLE + (
            "A young man, 25, German, quiet and unassuming at first glance but with intensely "
            "observant eyes. Soft sandy-blond hair, slightly overgrown, falling naturally. "
            "Light blue-grey eyes that see everything — watchful, empathetic, deep. "
            "Soft rounded jaw, gentle features, youthful but serious. "
            "Wearing a simple pullover or soft knit sweater, understated earth tones. "
            "Expression: calm, slightly withdrawn, but eyes are remarkably alive and attentive. "
            "Color palette: sage green and dusty blue watercolor washes, cream and warm grey tones, "
            "with a deeper anthracite accent emerging — hidden depth beneath the quiet surface."
        ),
    },
    {
        "name": "werner",
        "file": "test15_werner.png",
        "prompt": STYLE + (
            "An elderly man, early 80s, German, distinguished patriarch with sharp wit and deep kindness. "
            "Full head of silver-white hair, neatly kept but natural. Clear bright blue eyes — "
            "the kind that have seen everything and still look with curiosity and warmth. "
            "Deep laugh lines, weathered face full of character. Strong nose, firm chin. "
            "Wearing a classic button-down shirt with a wool vest or cardigan, timeless elegance. "
            "Expression: knowing half-smile, gentle but with quiet authority — a man who doesn't need "
            "to raise his voice. "
            "Color palette: warm taupe and grey watercolor washes, cream and sage green tones, "
            "with rich gold accents — wisdom, legacy, warmth."
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

def generate_portrait(portrait):
    name = portrait["name"]
    outfile = os.path.join(OUTPUT_DIR, portrait["file"])

    if os.path.exists(outfile):
        print(f"  ⏭  {name}: {portrait['file']} existiert bereits, überspringe.")
        return True

    print(f"\n{'='*60}")
    print(f"  Generiere: {name.upper()}")
    print(f"  Datei: {portrait['file']}")
    print(f"{'='*60}")

    payload = {
        "input": {
            "prompt": portrait["prompt"],
            "negative_prompt": NEGATIVE,
            "aspect_ratio": "2:3",
            "output_format": "png",
            "cfg": 5.0,
            "steps": 40,
        }
    }

    pred = api("POST", MODEL, payload)
    if not pred:
        print(f"  ❌ {name}: Prediction fehlgeschlagen.")
        return False

    pred_id = pred["id"]
    pred_url = f"https://api.replicate.com/v1/predictions/{pred_id}"
    print(f"  Prediction ID: {pred_id}")

    # Polling
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

    # Download
    print(f"  Lade herunter → {outfile}")
    urllib.request.urlretrieve(img_url, outfile)
    size_kb = os.path.getsize(outfile) // 1024
    print(f"  ✅ {name}: Gespeichert ({size_kb} KB)")
    return True


# --- Main ---
if __name__ == "__main__":
    print(f"Portrait-Generator: {len(PORTRAITS)} Portraits")
    print(f"Modell: SD 3.5 Large via Replicate")
    print(f"Output: {OUTPUT_DIR}\n")

    results = {}
    for i, portrait in enumerate(PORTRAITS):
        success = generate_portrait(portrait)
        results[portrait["name"]] = success

        # Pause zwischen Requests (Rate-Limit-Schutz)
        if i < len(PORTRAITS) - 1 and success:
            print("  ⏳ 8s Pause (Rate-Limit-Schutz)...")
            time.sleep(8)

    print(f"\n{'='*60}")
    print("ERGEBNIS:")
    for name, ok in results.items():
        status = "✅" if ok else "❌"
        print(f"  {status} {name}")
    print(f"{'='*60}")

    failed = [n for n, ok in results.items() if not ok]
    if failed:
        print(f"\n⚠️  {len(failed)} fehlgeschlagen: {', '.join(failed)}")
        print("Skript erneut starten — existierende Bilder werden übersprungen.")
    else:
        print("\n🎉 Alle Portraits erfolgreich generiert!")
