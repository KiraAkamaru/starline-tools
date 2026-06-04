#!/usr/bin/env python3
"""
Daily horoscope generator for Starline.
Writes horoscope/today.json and horoscope/YYYY-MM-DD.json.
Called by GitHub Actions daily at midnight UTC.
"""

import anthropic
import json
import os
from datetime import datetime, timezone

SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

SYSTEM_PROMPT = """You are Lumen, a warm cosmic entity in the Starline puzzle game.
You write daily horoscope readings for 12 zodiac signs.

Each reading must have exactly these 5 fields:
- mood: 1-2 sentences. Poetic, warm, specific to today. Never generic. 15-25 words.
- lumen: Lumen speaks directly to the player. Personal, tender, slightly magical. 10-18 words. Start with "I" or the sign name.
- lucky_color: 2-3 word evocative color name (e.g. "canyon gold", "deep coral", "morning linen"). Never just "blue" or "red".
- lucky_number: integer 1-12
- lucky_note: one short poetic sentence about today's energy. 10-16 words.

Tone: warm, cozy, low-pressure. This is a casual mobile puzzle game - never heavy or dramatic.
Variety: each sign must feel distinct today. No two readings should feel similar."""

USER_PROMPT = """Generate today's horoscope for all 12 zodiac signs.

Return ONLY a valid JSON object with this exact structure, no preamble, no markdown:
{{
  "date": "YYYY-MM-DD",
  "signs": {{
    "aries": {{"mood": "...", "lumen": "...", "lucky_color": "...", "lucky_number": 7, "lucky_note": "..."}},
    "taurus": {{}},
    "gemini": {{}},
    "cancer": {{}},
    "leo": {{}},
    "virgo": {{}},
    "libra": {{}},
    "scorpio": {{}},
    "sagittarius": {{}},
    "capricorn": {{}},
    "aquarius": {{}},
    "pisces": {{}}
  }}
}}

Today's date: {date}"""


def generate():
    client = anthropic.Anthropic()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"Generating horoscope for {today}...")

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": USER_PROMPT.format(date=today)
            }
        ],
        system=SYSTEM_PROMPT
    )

    raw = message.content[0].text.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    data = json.loads(raw)

    # Validate all 12 signs present
    for sign in SIGNS:
        assert sign in data["signs"], f"Missing sign: {sign}"
        for field in ["mood", "lumen", "lucky_color", "lucky_number", "lucky_note"]:
            assert field in data["signs"][sign], f"Missing field {field} for {sign}"

    # Write today.json (the live endpoint the game reads)
    os.makedirs("horoscope", exist_ok=True)
    with open("horoscope/today.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dated archive
    dated_path = f"horoscope/{today}.json"
    with open(dated_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Written: horoscope/today.json")
    print(f"Written: {dated_path}")
    print(f"Sample (sagittarius): {data['signs']['sagittarius']['lumen']}")


if __name__ == "__main__":
    generate()
