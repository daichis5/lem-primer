import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _shared_conf import *  # noqa: F403

language = "ja"

# The Japanese edition's own name, in the header and the browser tab.
project = "LEM入門"
html_title = "LEM入門"
