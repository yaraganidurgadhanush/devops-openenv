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

        # 🧠 Investigation phase
        if action["action_type"] == "investigate":
            reward += 0.2
            self.state_data["logs"] += "\n[INFO] Root cause identified"
            return Observation(**self.state_data), Reward(value=reward), False, {}

        target = action.get("target")

        # ✅ Handle tasks with or without affected_service
        affected_service = self.state_data.get("affected_service", None)

        if action["action_type"] == correct_solution:
            if affected_service:
                if target == affected_service:
                    reward += 0.7
                    self.state_data["service_status"] = "healthy"
                    done = True
                else:
                    reward -= 0.5
            else:
                reward += 0.6
                self.state_data["service_status"] = "healthy"
                done = True
        else:
            reward -= 0.5

        # 🔥 Dynamic degradation (IMPORTANT)
        if not done:
            if "latency" in self.state_data["metrics"]:
                self.state_data["metrics"]["latency"] += 100
            if "cpu" in self.state_data["metrics"]:
                self.state_data["metrics"]["cpu"] += 2

        # ⚡ Efficiency bonus
        if done and self.steps <= 2:
            reward += 0.2

        # 🚨 Prevent infinite loops
        if self.steps >= 6:
            done = True
            reward -= 0.5

        return Observation(**self.state_data), Reward(value=reward), done, {}
