from __future__ import annotations

from .models import AnalyzedElement


class RealityDebugger:
    """Orchestrates analysis without granting truth authority to language models."""

    def process(self, text: str) -> list[AnalyzedElement]:
        if not text or not text.strip():
            return []

        raise NotImplementedError(
            "v0.1.0-contract defines contracts first; claim extraction comes next."
        )


if __name__ == "__main__":
    print("Reality Debugger v0.1.0-contract initialized.")
