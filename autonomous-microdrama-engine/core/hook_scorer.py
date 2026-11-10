from typing import Tuple, List

class HookRetentionScorer:
    """
    Scores the first 0-3 seconds for vertical video microdramas.
    Checks for high emotional contrast, open curiosity gaps, and fast pattern interrupts.
    """
    RETENTION_TRIGGERS = [
        "jangan pernah", "rahasia", "kenapa", "tertangkap basah", "sumpah",
        "ternyata", "hancur", "menyesal", "terbongkar", "shock", "bukti"
    ]
    
    WEAK_STARTERS = [
        "halo guys", "selamat pagi", "di video kali ini", "kembali lagi", "perkenalkan"
    ]

    def evaluate_hook(self, hook_sentence: str) -> Tuple[float, List[str]]:
        score = 50.0
        feedback = []
        lower_hook = hook_sentence.lower().strip()

        for weak in self.WEAK_STARTERS:
            if lower_hook.startswith(weak):
                score -= 30.0
                feedback.append(f"Pattern Interrupt Failed: Hook begins with passive greeting '{weak}'.")

        matched_triggers = [t for t in self.RETENTION_TRIGGERS if t in lower_hook]
        if matched_triggers:
            bonus = min(len(matched_triggers) * 15.0, 40.0)
            score += bonus
            feedback.append(f"High Curiosity Triggers detected: {', '.join(matched_triggers)}")
        else:
            feedback.append("Low Curiosity Gap: No strong emotional hook or conflict anchor found in first 3 seconds.")

        if len(lower_hook.split()) < 3:
            score -= 20.0
            feedback.append("Hook too brief to establish dramatic stakes.")
        elif len(lower_hook.split()) > 15:
            score -= 15.0
            feedback.append("Hook too verbose for 0-3 second threshold.")

        final_score = max(0.0, min(100.0, score))
        return final_score, feedback
