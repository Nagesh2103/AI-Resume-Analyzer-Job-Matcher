def get_match_level(score):
    if score >= 80:
        return "Excellent Match"
    elif score >= 60:
        return "Good Match"
    elif score >= 40:
        return "Moderate Match"
    else:
        return "Low Match"

def prepare_matching_result(result):
    score = result.get("match_score", 0)
    result["match_level"] = get_match_level(score)
    return result