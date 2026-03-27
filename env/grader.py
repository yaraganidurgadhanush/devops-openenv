def grade(env):
    if env.state_data["service_status"] == "healthy":
        return 1.0
    elif env.steps > 3:
        return 0.5
    return 0.0
