from env.models import Observation, Reward
from env.tasks import TASKS

class DevOpsEnv:
    def __init__(self):
        self.current_task = None
        self.state_data = None
        self.steps = 0

    def reset(self, task="easy"):
        self.current_task = TASKS[task]
        self.state_data = self.current_task["initial_state"].copy()
        self.steps = 0
        return Observation(**self.state_data)

    def state(self):
        return self.state_data

    def step(self, action):
    self.steps += 1
    reward = 0
    done = False

    correct_solution = self.current_task["solution"]

    # Step 1: Investigation phase
    if action["action_type"] == "investigate":
        reward += 0.2
        self.state_data["logs"] += " | Root cause identified"
        return Observation(**self.state_data), Reward(value=reward), False, {}

    # Step 2: Correct action
    if action["action_type"] == correct_solution:
        reward += 0.6
        self.state_data["service_status"] = "healthy"
        done = True
    else:
        reward -= 0.4

    # Efficiency bonus
    if self.steps <= 2:
        reward += 0.2

    return Observation(**self.state_data), Reward(value=reward), done, {}
