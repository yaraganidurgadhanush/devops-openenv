TASKS = {
    "easy": {
        "description": "CPU spike due to high traffic",
        "solution": "scale_up",
        "initial_state": {
            "logs": "High CPU usage detected",
            "metrics": {"cpu": 95, "memory": 60, "latency": 300},
            "alerts": ["High CPU usage"],
            "service_status": "degraded"
        }
    },
    "medium": {
        "description": "Memory leak issue",
        "solution": "restart_service",
        "initial_state": {
            "logs": "Memory continuously increasing",
            "metrics": {"cpu": 60, "memory": 95, "latency": 500},
            "alerts": ["Memory critical"],
            "service_status": "degraded"
        }
    },
    "hard": {
        "description": "Deployment failure",
        "solution": "rollback",
        "initial_state": {
            "logs": "New deployment failed with errors",
            "metrics": {"cpu": 70, "memory": 70, "latency": 1200},
            "alerts": ["Service timeout"],
            "service_status": "down"
        }
    }
}
