import yaml

def enforce_rules(sections, similarity_scores):
    with open("config.yaml") as f:
        rules = yaml.safe_load(f)
    status = {}
    for rule in rules['rules']:
        sec = rule['section']
        if rule.get('required') and sec not in sections:
            status[sec] = "Missing"
        elif rule.get('min_similarity') and similarity_scores.get(sec, {}).get('similarity', 0) < rule['min_similarity']:
            status[sec] = "Low similarity"
        else:
            status[sec] = "Pass"
    return status
