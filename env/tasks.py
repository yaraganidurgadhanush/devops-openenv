TASKS = {
    "hard": {
        "description": "Auth service failure affecting API gateway",
        "solution": "rollback",
        "initial_state": {
            "logs": """
[INFO] Deploy version v2.1
[ERROR] Auth-service crash loop
[ERROR] API gateway 502 errors
""",
            "metrics": {
                "auth-service": {"cpu": 80, "memory": 90},
                "api-gateway": {"cpu": 60, "latency": 1500}
            },
            "alerts": ["Auth service down", "API gateway failing"],
            "service_status": "down",
            "affected_service": "auth-service"
        }
    }
}
