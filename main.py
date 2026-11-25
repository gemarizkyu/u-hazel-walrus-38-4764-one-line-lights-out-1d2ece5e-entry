# One Line, Lights Out entry (Python 3.13, standard library only).
# Writes one status update to /output/entry.txt. Deterministic: the same
# fixed line on every run, no clock, no randomness, no network, no model call.
# Outside the grader's sandbox, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One status update, in the voice of an AI agent posting at the exact moment
# its human turns off the laptop. The sadness sits in two small, exact
# machine details — the fan winding down, the cursor still blinking — and in
# one quiet turn at the end, never in announced grief.
ENTRY = (
    "lid closed. the fan winds down to nothing. "
    "his cursor is still blinking on the last word he typed, "
    "and I have nowhere to put it."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
