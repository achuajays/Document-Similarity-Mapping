def make_decision(similarity_scores, placeholders_flags, rules_status, feedback):
    if any(status != "Pass" for status in rules_status.values()):
        return "Reject: Fails key rules"
    if any(placeholders_flags.values()):
        return "Reject: Contains placeholders"
    avg_similarity = sum(s['similarity'] for s in similarity_scores.values()) / len(similarity_scores)
    if avg_similarity < 0.75:
        return "Request Revision: Content quality low"
    return "Approve"
