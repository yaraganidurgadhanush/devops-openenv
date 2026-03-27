from fastapi import FastAPI
from env.environment import DevOpsEnv
from env.grader import grade

app = FastAPI()
env = DevOpsEnv()

@app.get("/reset")
def reset(task: str = "easy"):
    obs = env.reset(task)
    return obs.dict()

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.value,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

@app.get("/tasks")
def tasks():
    return {
        "tasks": [
            {"name": "easy", "description": "CPU spike"},
            {"name": "medium", "description": "Memory leak"},
            {"name": "hard", "description": "Deployment failure"}
        ],
        "actions": ["investigate", "scale_up", "restart_service", "rollback"]
    }

@app.get("/grader")
def grader():
    return {"score": grade(env)}

@app.get("/baseline")
def baseline():
    from baseline import run_baseline
    return run_baseline()
