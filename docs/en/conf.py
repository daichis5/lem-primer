import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _shared_conf import *  # noqa: F403

language = "en"
html_title = "LEM Primer"
