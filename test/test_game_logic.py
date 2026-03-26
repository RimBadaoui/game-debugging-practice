import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess


def test_too_low_string_comparison_bug():
    """
    When check_guess falls into the except TypeError branch it uses string
    comparison instead of numeric comparison.

    str(9) > "10"  →  "9" > "10"  →  True  (lexicographic)
    So the function wrongly returns "Too High" instead of "Too Low".

    Affects any guess whose string representation sorts higher than the
    secret's string representation even though the number is smaller:
    e.g. 9 vs 10, 2 vs 10, 19 vs 20, etc.
    """
    # 9 < 10 numerically → should be "Too Low"
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too Low", (
        f"Expected 'Too Low' (9 < 10) but got '{outcome}'. "
        "String comparison '9' > '10' is True, causing wrong direction."
    )
