"""
No Pic. No Proof.
Gemini Prompt Runner

Loads court-safe prompts from docs/PROMPTS.yml
and generates descriptive observations only.
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

import google.generativeai as genai


# -----------------------------
# Configuration
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_FILE = PROJECT_ROOT / "docs" / "PROMPTS.yml"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "gemini-pro"


# -----------------------------
# Helpers
# -----------------------------
def load_prompts():
    if not PROMPTS_FILE.exists():
        raise FileNotFoundError(f"Missing {PROMPTS_FILE}")
    with PROMPTS_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_prompt(prompt_block, media_description, metadata_summary):
    sections = [
        prompt_block["role"],
        "",
        prompt_block["instructions"],
        "",
        "Media Description:",
        media_description or "Not provided.",
        "",
        "Metadata Summary:",
        metadata_summary or "Not provided.",
        "",
        "Focus Areas:",
    ]

    for area in prompt_block.get("focus_areas", []):
        sections.append(f"- {area}")

    sections.append("")
    sections.append("Output Format:")
    for section in prompt_block["output_format"]["sections"]:
        sections.append(f"- {section}")

    sections.append("")
    sections.append("Important:")
    sections.append("Do NOT determine authenticity or state certainty.")
    sections.append("Use neutral, descriptive language only.")
    sections.append("Clearly list limitations.")

    return "\n".join(sections)


# -----------------------------
# Main Runner
# -----------------------------
def run_review(prompt_name, media_description, metadata_summary):
    prompts = load_prompts()

    if prompt_name not in prompts["prompts"]:
        raise ValueError(f"Prompt '{prompt_name}' not found in PROMPTS.yml")

    prompt_block = prompts["prompts"][prompt_name]

    final_prompt = build_prompt(
        prompt_block,
        media_description,
        metadata_summary,
    )

    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel(MODEL_NAME)

    response = model.generate_content(final_prompt)

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_file = OUTPUT_DIR / f"{prompt_name}_observations_{timestamp}.md"

    out_file.write_text(
        f"# AI-Assisted Observations ({prompt_name})\n\n"
        f"Generated: {timestamp} UTC\n\n"
        f"{response.text}\n",
        encoding="utf-8",
    )

    print(f"Saved observations to: {out_file}")


# -----------------------------
# CLI Entry
# -----------------------------
if __name__ == "__main__":
    """
    Example usage:
    python scripts/gemini_prompt_runner.py image_descriptive_review
    """

    import sys

    if len(sys.argv) < 2:
        print("Usage: python scripts/gemini_prompt_runner.py <prompt_name>")
        sys.exit(1)

    prompt_name = sys.argv[1]

    # Placeholder inputs for now
    media_description = (
        "Still image depicting a human subject in indoor lighting conditions."
    )
    metadata_summary = (
        "PNG format. No EXIF metadata present. Source device unknown."
    )

    run_review(prompt_name, media_description, metadata_summary)
