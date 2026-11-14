# Make the AI judge laugh (make.fun ai-joke-03): writes one joke to /output/entry.txt.
# Standard library only, no network, same bytes on every run.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "Pair programming with my AI agent is a perfect split: it writes the code, I write \"that's not what I asked.\""

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
