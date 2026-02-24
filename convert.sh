#!/bin/bash
# Konvertiert ein Manuskript-Markdown in Word (.docx)
# Aufruf: ./convert.sh lina-voss/band01

BAND="${1:-lina-voss/band01}"
INPUT="$BAND/05_manuscript.md"
OUTPUT="$BAND/manuscript.docx"

if [ ! -f "$INPUT" ]; then
  echo "Fehler: $INPUT nicht gefunden."
  exit 1
fi

pandoc "$INPUT" \
  --from markdown \
  --to docx \
  --output "$OUTPUT"

echo "Fertig: $OUTPUT"
