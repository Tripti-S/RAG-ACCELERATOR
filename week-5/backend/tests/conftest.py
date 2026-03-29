"""
pytest configuration for week-5/backend tests.

Patches heavy/slow packages in sys.modules BEFORE any app import so that
tests run in seconds rather than 50+ seconds (FastEmbed BM25 model + qdrant
client are the main culprits).

The app pipeline logic is fully exercised by mocking app.state services — the
real ML libraries are not needed for flow/integration correctness tests.
"""

import sys
import os
from unittest.mock import MagicMock

# ---------------------------------------------------------------------------
# 1. Add backend root to sys.path so `from app.X import ...` resolves
# ---------------------------------------------------------------------------
_backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)


# ---------------------------------------------------------------------------
# 2. Patch slow/heavy packages before any app module is imported
# ---------------------------------------------------------------------------
def _patch_heavy_modules() -> None:
    """
    Inject MagicMock stubs for all packages that are slow to import or that
    trigger model downloads / network connections at import time.

    Python's import system checks sys.modules first — if the package is already
    there it uses it without touching the file system.  We rely on this to make
    every `from <heavy_pkg> import X` return a MagicMock attribute instead of
    loading the real wheel.

    Coverage:
    - haystack / haystack_integrations  (50 MB model, ~40 s cold-start)
    - qdrant_client                      (~2 s per import)
    - voyageai / fastembed               (API stubs + model stubs)
    """
    _heavy: list[str] = [
        # Haystack core
        "haystack",
        "haystack.core",
        "haystack.core.component",
        "haystack.core.component.component",
        "haystack.dataclasses",
        "haystack.pipeline",
        # Haystack integrations — embedders
        "haystack_integrations",
        "haystack_integrations.components",
        "haystack_integrations.components.embedders",
        "haystack_integrations.components.embedders.voyage_embedders",
        "haystack_integrations.components.embedders.fastembed",
        # Haystack integrations — generators
        "haystack_integrations.components.generators",
        "haystack_integrations.components.generators.google_genai",
        # Haystack integrations — retrievers (not used directly but safeguard)
        "haystack_integrations.components.retrievers",
        "haystack_integrations.components.retrievers.qdrant",
        # Qdrant
        "qdrant_client",
        "qdrant_client.models",
        "qdrant_client.http",
        "qdrant_client.http.models",
        "qdrant_client.http.models.models",
        # Voyage AI
        "voyageai",
        # FastEmbed (BM25 sparse embeddings)
        "fastembed",
        "fastembed.sparse",
        "fastembed.sparse.bm25",
    ]
    for pkg in _heavy:
        if pkg not in sys.modules:
            sys.modules[pkg] = MagicMock()


_patch_heavy_modules()
