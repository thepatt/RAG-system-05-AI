import os
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

_env = os.environ.get

"""
# Chroma config
"""
CHROMA_HOST = _env("CHROMA_HOST", "CHROMA_HOST")
CHROMA_PORT = _env("CHROMA_PORT", "CHROMA_PORT")
