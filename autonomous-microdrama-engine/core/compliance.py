from typing import List, Tuple
import json

class ComplianceAuditor:
    def __init__(self, truth_ledger: dict):
        self.verified_claims = [c.lower() for c in truth_ledger.get("verified_claims", [])]
        self.forbidden_claims = [f.lower() for f in truth_ledger.get("forbidden_claims", [])]
        self.required_disclaimers = truth_ledger.get("required_disclaimers", [])

    def audit_text(self, text: str) -> Tuple[bool, List[str]]:
        violations = []
        lower_text = text.lower()
        for forbidden in self.forbidden_claims:
            if forbidden in lower_text:
                violations.append(f"VIOLATION: Forbidden claim '{forbidden}' detected.")
        is_compliant = len(violations) == 0
        return is_compliant, violations
