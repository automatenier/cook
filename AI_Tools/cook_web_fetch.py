"""
web_fetch.py — Fetch a URL and return clean text (HTML stripped, noise removed).

Implements Dynamic Web Fetch Filtering: strips irrelevant HTML before content
enters Claude's context window, reducing token waste and improving accuracy.

Usage:
    py -3 AI_Tools/web_fetch.py <URL> [--hint "what to extract"] [--raw]

Options:
    --hint TEXT     Pass a targeted extraction prompt to Claude Haiku
                    (costs tokens — use only when raw text is too noisy)
    --raw           Return BeautifulSoup-cleaned text only, skip Claude pass

Examples:
    py -3 AI_Tools/web_fetch.py https://example.com/article
    py -3 AI_Tools/web_fetch.py https://example.com --hint "extract pricing table only"
    py -3 AI_Tools/web_fetch.py https://example.com --raw
"""

import sys
import argparse
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

# Tags that are always noise — remove before any text extraction
STRIP_TAGS = [
    "script", "style", "nav", "header", "footer",
    "aside", "form", "iframe", "noscript", "svg",
    "button", "input", "select", "textarea",
]

MAX_CHARS_FOR_HAIKU = 8000


def fetch_and_clean(url: str) -> str:
    """Fetch URL and return clean text with noise stripped."""
    resp = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0 (compatible; CookAgent/1.0)"},
    )
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")

    # Remove noise tags
    for tag in soup(STRIP_TAGS):
        tag.decompose()

    # Prefer semantic content containers
    main = (
        soup.find("main")
        or soup.find("article")
        or soup.find(attrs={"role": "main"})
        or soup.body
    )

    if main:
        return main.get_text(separator="\n", strip=True)
    return soup.get_text(separator="\n", strip=True)


def haiku_extract(text: str, hint: str) -> str:
    """Run a targeted Haiku pass to extract specific content from clean text."""
    import anthropic

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Extract the following from the page content below:\n{hint}\n\n"
                    f"Return only the extracted content, no commentary.\n\n"
                    f"Page content:\n{text[:MAX_CHARS_FOR_HAIKU]}"
                ),
            }
        ],
    )
    return response.content[0].text


def main():
    parser = argparse.ArgumentParser(
        description="Fetch a URL and return clean text with HTML noise removed."
    )
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument(
        "--hint",
        default="",
        help="What to extract (triggers a Haiku pass — costs tokens)",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Skip Claude pass, return BeautifulSoup-cleaned text only",
    )
    args = parser.parse_args()

    try:
        clean_text = fetch_and_clean(args.url)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    if args.hint and not args.raw:
        try:
            print(haiku_extract(clean_text, args.hint))
        except Exception as e:
            print(f"Haiku extraction failed: {e}", file=sys.stderr)
            print(clean_text)
    else:
        print(clean_text)


if __name__ == "__main__":
    main()
