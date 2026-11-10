import pytest
import os
import json
from core.state_models import MicrodramaEpisode, ScenePrompt, CharacterProfile
from core.compliance import ComplianceAuditor
from core.hook_scorer import HookRetentionScorer

@pytest.fixture
def product_truth():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    truth_file = os.path.join(base_dir, "rules", "product_truth.json")
    with open(truth_file, "r", encoding="utf-8") as f:
        return json.load(f)

def test_compliance_auditor_flags_forbidden_claims(product_truth):
    auditor = ComplianceAuditor(product_truth)
    bad_script = "Serum ini memutihkan kulit seketika secara permanen dalam sekali pakai!"
    is_compliant, violations = auditor.audit_text(bad_script)
    assert not is_compliant
    assert len(violations) > 0

def test_compliance_auditor_passes_clean_script(product_truth):
    auditor = ComplianceAuditor(product_truth)
    good_script = "Kulitku tetap terhidrasi sepanjang hari berkat Ceramide Complex."
    is_compliant, violations = auditor.audit_text(good_script)
    assert is_compliant
    assert len(violations) == 0

def test_hook_scorer_penalizes_weak_starters():
    scorer = HookRetentionScorer()
    score, feedback = scorer.evaluate_hook("Halo guys kembali lagi bersamaku hari ini")
    assert score < 50.0

def test_hook_scorer_rewards_high_tension_openers():
    scorer = HookRetentionScorer()
    score, feedback = scorer.evaluate_hook("Sumpah, ternyata selama ini rahasia besarnya terbongkar!")
    assert score >= 70.0
