TASKS = {
    "easy": {
        "description": "CPU spike due to high traffic",
        "solution": "scale_up",
        "initial_state": {
            "logs": """
[WARN] CPU usage exceeded 95%
[ERROR] Request latency increasing
[INFO] Autoscaler not triggered
""",
            "metrics": {"cpu": 95, "memory": 60, "latency": 300},
            "alerts": ["High CPU usage"],
            "service_status": "degraded"
        }
    },

    "medium": {
        "description": "Memory leak issue",
        "solution": "restart_service",
        "initial_state": {
            "logs": """
[WARN] Memory usage growing steadily
[ERROR] OutOfMemory risk detected
[INFO] Garbage collection ineffective
""",
            "metrics": {"cpu": 60, "memory": 95, "latency": 500},
            "alerts": ["Memory critical"],
            "service_status": "degraded"
        }
    },

    "hard": {
        "description": "Deployment failure",
        "solution": "rollback",
        "initial_state": {
            "logs": """
[INFO] Deploy version v2.1
[ERROR] NullPointerException in auth-service
[CRITICAL] Service crash loop detected
""",
            "metrics": {"cpu": 70, "memory": 70, "latency": 1200},
            "alerts": ["Service timeout"],
            "service_status": "down"
        }
    }
}
