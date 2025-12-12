# No Pic. No Proof. — Media Authenticity Review (Gemini-Assisted)

**No Pic. No Proof.** is a practical, defensible workflow for reviewing images and videos for **inconsistencies** that may suggest manipulation or synthetic generation.

This project is **not** an “AI detector.”  
It is a **multi-signal review pipeline** that combines:
- **Artifact preservation** (hashing)
- **Metadata extraction** (EXIF/container)
- **Basic technical checks** (format/codecs/export clues)
- **Visual/temporal indicators** (edges, lighting, texture, frames)
- **Gemini-assisted descriptive review** (observations only, no conclusions)

The output is designed for **clear documentation** that can support attorney review and professional reporting.

---

## Goals

✅ Provide a repeatable workflow for media review  
✅ Document findings in neutral, court-safe language  
✅ Use AI to **describe** anomalies, not “declare” authenticity  
✅ Keep the process transparent and auditable  
✅ Avoid over-claims (“this proves it is AI”)  

---

## Non-Goals (Important)

This repo does **not**:
- Determine authenticity with certainty
- Replace a full forensic lab workflow
- Provide legal conclusions or advice
- Encourage unauthorized access, hacking, or scraping

> **Rule:** If you don’t have the original file/source context, your confidence should remain conservative.

---

## How Gemini Is Used (Correctly)

Gemini is used as an **assistant analyst** to:
- Summarize observable inconsistencies
- Compare “expected camera output” vs “observed characteristics”
- Suggest alternative benign explanations (compression, re-exporting)
- Draft neutral findings language and limitations

Gemini must **not**:
- Conclude “AI-generated” or “authentic”
- State certainty
- Make identity claims about people in media

**Output language should look like this:**
- “These characteristics are inconsistent with typical native camera output.”
- “The absence of original metadata limits conclusions.”
- “No single indicator is determinative.”

---

## Repository Layout (Planned)

