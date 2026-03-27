def grade(env):
    score = 0.0

    # correctness
    if env.state_data["service_status"] == "healthy":
        score += 0.5

    # efficiency
    if env.steps <= 2:
        score += 0.3
    elif env.steps <= 4:
        score += 0.2

    # penalty
    if env.steps > 5:
        score -= 0.2

    return max(0.0, min(score, 1.0))
