#!/usr/bin/env bash
# Perplexity API Research Script für Nischenanalyse
# Usage: ./scripts/perplexity_research.sh "Suchanfrage"
#
# Liest PERPLEXITY_API_KEY aus .env im Projektroot.
# Gibt die Antwort als reinen Text auf stdout aus.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# .env laden
if [[ -f "$PROJECT_ROOT/.env" ]]; then
  export "$(grep -v '^#' "$PROJECT_ROOT/.env" | grep 'PERPLEXITY_API_KEY' | xargs)"
fi

if [[ -z "${PERPLEXITY_API_KEY:-}" ]]; then
  echo "FEHLER: PERPLEXITY_API_KEY nicht gesetzt. Bitte in .env eintragen." >&2
  exit 1
fi

QUERY="$1"

RESPONSE=$(curl -sS https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(cat <<ENDJSON
{
  "model": "sonar",
  "messages": [
    {
      "role": "system",
      "content": "Du bist ein Amazon KDP Marktforscher. Antworte auf Deutsch. Gib konkrete Daten, Buchtitel, Autorennamen und Zahlen an wo möglich. Formatiere als Markdown."
    },
    {
      "role": "user",
      "content": $(printf '%s' "$QUERY" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')
    }
  ],
  "search_recency_filter": "month"
}
ENDJSON
)")

# Antwort extrahieren
echo "$RESPONSE" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if 'choices' in data:
    print(data['choices'][0]['message']['content'])
    # Quellen ausgeben falls vorhanden
    if 'citations' in data:
        print('\n---\n## Quellen')
        for i, url in enumerate(data['citations'], 1):
            print(f'{i}. {url}')
elif 'error' in data:
    print(f\"FEHLER: {data['error'].get('message', data['error'])}\", file=sys.stderr)
    sys.exit(1)
else:
    print(json.dumps(data, indent=2))
"
