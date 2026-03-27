from env.environment import DevOpsEnv

def run_baseline():
    env = DevOpsEnv()
    scores = {}

    for task in ["easy", "medium", "hard"]:
        obs = env.reset(task)

        # step 1: investigate
        env.step({"action_type": "investigate", "target": "service"})

        # step 2: decision
        if "CPU" in obs.logs:
            action = {"action_type": "scale_up", "target": "service"}
        elif "Memory" in obs.logs:
            action = {"action_type": "restart_service", "target": "service"}
        else:
            action = {"action_type": "rollback", "target": "service"}

        env.step(action)

        scores[task] = 1.0 if env.state_data["service_status"] == "healthy" else 0.0

    return scores
