# AI DevOps Incident Response Environment

## Overview
This project simulates real-world DevOps incident response scenarios where an AI agent diagnoses system failures and applies corrective actions.

## Tasks
- Easy: CPU spike → scale_up
- Medium: Memory leak → restart_service
- Hard: Deployment failure → rollback

## Action Space
- action_type: {scale_up, restart_service, rollback}
- target: service/component

## Observation Space
- logs
- metrics (cpu, memory, latency)
- alerts
- service_status

## Reward Design
- +0.5 correct action
- +0.2 partial improvement
- -0.3 wrong action

## Setup
```bash
pip install -r requirements.txt
uvicorn app:app --reload
