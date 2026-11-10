# Autonomous Microdrama Studio v2.0 (Production Engine)

Next-generation autonomous framework for multi-agent generative video pipelines. Designed specifically for vertical micro-dramas (TikTok, Reels, Shorts), compliance ledger auditing, multi-modal generative video dispatching, and automated QA/assembly.

## Key Improvements Over v1
- **State-Driven Multi-Agent Architecture**: Replaces passive markdown checklists with Pydantic-enforced campaign state schemas.
- **Hook Retention Scoring Engine**: Evaluates 0–3 second visual and psychological hooks before rendering.
- **Automated Preflight Compliance Loop**: Self-healing rejection/correction cycle enforcing strict cosmetic, dietary, and consumer claim guidelines.
- **Provider-Agnostic Generative Dispatcher**: Ready-to-call API interface for Kling, Runway Gen-3, Luma Dream Machine, and ElevenLabs.
- **FFmpeg & Subtitle Composition Pipelines**: Automated vertical format enforcement (9:16), dynamic captions, and audio ducking specs.

## Architecture

```
core/
├── state_models.py       # Pydantic schemas for state, script, cast, and video prompts
├── orchestrator.py       # Execution pipeline with self-healing feedback loops
├── hook_scorer.py        # 0-3s retention and curiosity gap analyzer
└── compliance.py         # Automated product truth ledger audit
dispatchers/
├── video_dispatcher.py   # Multi-vendor AI video API router (Kling, Runway, Luma)
└── audio_dispatcher.py   # ElevenLabs emotive speech and audio-layer router
assembly/
└── ffmpeg_composer.py    # Automated 9:16 video assembly, subtitle burning, foley layering
rules/
├── product_truth.json    # Canonical database of verified claims & strict negatives
└── brand_guardrails.json # Pacing, tone, and character visual anchors
```

## Quickstart

```bash
# Install dependencies
pip install pydantic pytest pytest-asyncio

# Run automated tests
pytest -v tests/

# Run end-to-end dry-run orchestration
python -m core.orchestrator
```
