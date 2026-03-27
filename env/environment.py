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

        correct_action = action["action_type"] == self.current_task["solution"]

        if correct_action:
            reward += 0.5
            self.state_data["service_status"] = "healthy"
            done = True
        else:
            reward -= 0.3
            done = False

        # Partial reward (progress simulation)
        if self.state_data["metrics"]["latency"] > 1000:
            reward += 0.2

        return Observation(**self.state_data), Reward(value=reward), done, {}
