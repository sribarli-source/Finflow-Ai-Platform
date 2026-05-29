# FinFlow AI Platform

Fraud detection platform built to mirror real fintech production systems. Scores transactions in real time, detects anomalies using ML, streams events through AWS SQS, and exposes full observability through Prometheus and Grafana.

Built to sharpen hands-on skills across the stack I work with daily — AWS, Kubernetes, Terraform, Prometheus, and ML/AI.

---

## What it does

- Real-time transaction fraud scoring via REST API
- ML model with anomaly detection and risk scoring
- Event pipeline via AWS SQS and Lambda
- Prometheus metrics — request rate, latency, fraud score distribution
- OpenTelemetry instrumentation for distributed tracing
- Kubernetes deployment with horizontal auto-scaling
- Full AWS infrastructure provisioned with Terraform
- CI/CD pipeline via GitHub Actions

---

## Stack

| Layer | Tech |
|---|---|
| API | FastAPI, Python |
| ML / AI | Scikit-learn, MLflow, anomaly detection |
| Observability | Prometheus, Grafana, OpenTelemetry |
| Infrastructure | Terraform, AWS (EKS, SQS, Lambda, S3, VPC, IAM) |
| Orchestration | Kubernetes, Helm, Docker |
| CI/CD | GitHub Actions |
| Config | Ansible |

---

## Structure

```
app/          FastAPI fraud scoring API + Prometheus metrics
ml/           Model training, feature engineering, MLflow tracking
terraform/    AWS infrastructure — EKS, SQS, Lambda, VPC, IAM
k8s/          Kubernetes manifests — deployment, HPA, service
ansible/      Configuration management playbooks
```

---

## Run locally

```bash
git clone https://github.com/sribarli-source/Finflow-Ai-Platform.git
cd Finflow-Ai-Platform
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Score a transaction:
```bash
curl -X POST http://localhost:8000/score \
  -H "Content-Type: application/json" \
  -d '{"amount": 9500, "merchant": "unknown", "location": "foreign"}'
```

Check metrics:
```bash
curl http://localhost:8000/metrics
```

---

## Deploy to Kubernetes

```bash
kubectl apply -f k8s/
kubectl get pods -n finflow
kubectl get hpa -n finflow
```

---

## Provision AWS infrastructure

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

---

## Build status

| Component | Status |
|---|---|
| Fraud scoring API | Done |
| Prometheus metrics | Done |
| ML model + anomaly detection | In progress |
| Terraform AWS (EKS, SQS, Lambda) | In progress |
| Kubernetes + HPA | In progress |
| GitHub Actions CI/CD | In progress |
| Grafana dashboards | Planned |
| OpenTelemetry tracing | Planned |

---

Built by [Srinivas Barli](https://linkedin.com/in/sribarli) — Senior SRE / Platform Engineer  
