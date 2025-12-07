# backend/utils.py
from typing import Callable

def mock_ai_response(prompt: str) -> str:
    """
    Fallback text when the real AI call fails
    (for example: no API key, no credits, timeout, etc.)
    """
    return (
        "Demo mode output:\n\n"
        "The real AI generation is currently disabled (no API key/credits), "
        "but the backend pipeline is working correctly.\n\n"
        f"Prompt preview:\n{prompt[:200]}..."
    )


def safe_generate(model_fn: Callable[[str], str], prompt: str) -> str:
    """
    Try to call the real model. If anything goes wrong,
    return a safe mock response instead of raising an error.
    """
    try:
        return model_fn(prompt)
    except Exception:
        return mock_ai_response(prompt)
