
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    #FIX: Refactored logic into logic_utils.py using Claude Code Agent mode
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    #FIX: Refactored logic into logic_utils.py using Claude Code Agent mode
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    #FIX: Refactored logic into logic_utils.py using Claude Code Agent mode
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go LOWER!"
        else:
            return "Too Low", "📉 Go HIGHER!"
    except TypeError:
        #FIX: convert guess to int instead of string for int comparison rather than string comparison to fix the too high/low logic
        #I Identified the bug, asked AI to explain the cause, and then fixed it myself. 
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    #FIX: Refactored logic into logic_utils.py using Claude Code Agent mode
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    #FIX: subtract 5 points for each incorrect guess regardless of whether it's too high or too low. 
    #I Identified the bug, asked AI to explain the cause, and then fixed it myself. 
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
