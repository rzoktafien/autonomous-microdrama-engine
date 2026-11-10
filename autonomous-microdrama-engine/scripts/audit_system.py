import os
import json
import sys

def audit():
    print("[*] Running System Integrity & Guardrail Audit...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    truth_path = os.path.join(base_dir, "rules", "product_truth.json")
    
    if not os.path.exists(truth_path):
        print(f"[!] Error: Missing {truth_path}")
        sys.exit(1)
        
    with open(truth_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "verified_claims" in data, "Missing verified_claims in Product Truth"
        assert "forbidden_claims" in data, "Missing forbidden_claims in Product Truth"
        print(f" [✓] Product Truth Ledger validated ({len(data['verified_claims'])} verified claims, {len(data['forbidden_claims'])} forbidden claims).")

    print("[✓] System integrity audit passed.")

if __name__ == "__main__":
    audit()
