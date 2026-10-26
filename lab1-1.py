
def symbolic(score, complete):
    if complete and score >= 70:
        return "Review"
    return "Hold"


def threshold(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"


cases = [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]

print("case | symbolic | threshold | disagreement")
for name, score, complete, probability in cases:
    a = symbolic(score, complete)
    b = threshold(probability)
    print(name, a, b, a != b, sep=" | ")

print()


def rules(score, complete, attendance, dues_cleared):
    if not complete:
        return "Hold", "documents incomplete"
    if score < 70:
        return "Hold", "score below 70"
    if attendance < 75:
        return "Hold", "attendance below 75"
    if not dues_cleared:
        return "Hold", "fee dues not cleared"
    return "Review", "all conditions met"


tests = [
    ("pass", 82, True, 80, True, "Review"),
    ("low_attendance", 85, True, 60, True, "Hold"),
    ("dues_pending", 85, True, 90, False, "Hold"),
    ("boundary", 70, True, 75, True, "Review"),
]

for name, score, complete, attendance, dues, expected in tests:
    actual, reason = rules(score, complete, attendance, dues)
    print("test:", name)
    print("input:", score, complete, attendance, dues)
    print("expected:", expected, "| actual:", actual, "| reason:", reason)
    print("passed:", expected == actual)
    print()
