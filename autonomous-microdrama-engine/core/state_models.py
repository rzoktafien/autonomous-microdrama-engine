from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field

class CharacterProfile(BaseModel):
    character_id: str
    name: str
    archetype: str
    visual_anchor_prompt: str
    voice_preset_id: str
    costume_tokens: List[str]

class ScenePrompt(BaseModel):
    scene_index: int
    duration_seconds: float = Field(default=4.0, ge=2.0, le=10.0)
    dialogue: Optional[str] = None
    character_speaking: Optional[str] = None
    emotion: str
    camera_angle: str
    motion_action: str
    lighting_aesthetic: str
    video_prompt: str
    negative_prompt: str

class MicrodramaEpisode(BaseModel):
    episode_id: str
    title: str
    target_duration_seconds: int = 60
    hook_sentence_0_3s: str
    conflict_premise: str
    product_integration_scene: int
    characters: List[CharacterProfile]
    scenes: List[ScenePrompt]
    compliance_score: float = 0.0
    hook_score: float = 0.0

class CampaignState(BaseModel):
    campaign_id: str
    brand_name: str
    product_truth_id: str
    status: Literal["draft", "scripted", "qc_pending", "approved", "rendering", "assembled", "failed"] = "draft"
    episodes: List[MicrodramaEpisode] = []
    metadata: Dict[str, Any] = {}
