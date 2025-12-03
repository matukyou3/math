# tests/conftest.py

import os
import sys

# tests/ の一個上（math/）をパスに追加する
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
