import json
from .state_models import CampaignState, MicrodramaEpisode, ScenePrompt, CharacterProfile
from .compliance import ComplianceAuditor
from .hook_scorer import HookRetentionScorer

class AutonomousMicrodramaOrchestrator:
    def __init__(self, product_truth_path: str):
        with open(product_truth_path, "r", encoding="utf-8") as f:
            self.truth_ledger = json.load(f)
        self.auditor = ComplianceAuditor(self.truth_ledger)
        self.hook_scorer = HookRetentionScorer()

    def run_preflight_cycle(self, episode: MicrodramaEpisode) -> bool:
        print(f"[*] Starting Preflight Validation for Episode: {episode.title}")
        hook_score, hook_feedback = self.hook_scorer.evaluate_hook(episode.hook_sentence_0_3s)
        episode.hook_score = hook_score
        print(f" -> Hook Score: {hook_score}/100. Feedback: {hook_feedback}")

        all_dialogue = " ".join([s.dialogue for s in episode.scenes if s.dialogue])
        is_compliant, violations = self.auditor.audit_text(all_dialogue)
        
        if not is_compliant:
            print(f" [!] REJECTED by Compliance Auditor:")
            for v in violations:
                print(f"     - {v}")
            episode.compliance_score = 0.0
            return False

        if hook_score < 60.0:
            print(" [!] REJECTED by Hook Engine: Retention score below 60.")
            return False

        episode.compliance_score = 100.0
        print(" [✓] Preflight Passed: Ready for Generative Dispatch.")
        return True

if __name__ == "__main__":
    import os
    truth_file = os.path.join(os.path.dirname(__file__), "../rules/product_truth.json")
    orchestrator = AutonomousMicrodramaOrchestrator(truth_file)
    sample_episode = MicrodramaEpisode(
        episode_id="EP_01",
        title="Rahasia di Balik Cermin",
        hook_sentence_0_3s="Ternyata selama ini dia sembunyikan bukti itu di tasku!",
        conflict_premise="Persaingan kantor dan tuduhan pencurian formula kosmetik.",
        product_integration_scene=3,
        characters=[
            CharacterProfile(
                character_id="CHAR_01",
                name="Siska",
                archetype="Protagonis Berdaya",
                visual_anchor_prompt="Indonesian woman 26yo, elegant corporate blazer, high ponytail, photorealistic, 8k",
                voice_preset_id="elevenlabs_id_01",
                costume_tokens=["navy blue blazer", "minimalist silver pendant"]
            )
        ],
        scenes=[
            ScenePrompt(
                scene_index=1,
                dialogue="Ternyata selama ini dia sembunyikan bukti itu di tasku!",
                character_speaking="Siska",
                emotion="Terkejut dan marah",
                camera_angle="Dutch angle close-up",
                motion_action="Membuka tas dengan tangan gemetar",
                lighting_aesthetic="Dramatic rim light, low-key neon glow",
                video_prompt="A dramatic cinematic vertical 9:16 shot of an elegant Indonesian woman opening her bag with trembling hands...",
                negative_prompt="blurry, distorted face, low quality, oversaturated"
            )
        ]
    )
    success = orchestrator.run_preflight_cycle(sample_episode)
    print(f"Orchestration Result: {'SUCCESS' if success else 'REVISION_REQUIRED'}")
