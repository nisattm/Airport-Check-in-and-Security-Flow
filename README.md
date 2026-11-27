# Airport Check-in and Security Flow

Term project (Project 2) for SENG-331 Modelling and Simulation with Python.
We model the flow of passengers through check-in desks and security scanners as a discrete-event simulation with **SimPy**.

**Team:** Ceren Yüksel · Burkay Çakar · Nisa Atım

The work is split into three lanes (A: Model, B: Analysis, C: Design & animation). Who works on which lane in each phase is described in [PLAN.md](PLAN.md).

👉 **Project plan, workflow and task division: [PLAN.md](PLAN.md)**

## Model summary

| Parameter | Value |
|---|---|
| Passenger arrivals | Exponential, mean 1.5 min |
| Check-in | 5 desks, exponential service, mean 4 min |
| Security | 3 scanners, exponential service, mean 5 min |
| Experiment factors | Desks {3, 5} × scanners {2, 4} |
| Simulation type | Terminating: passengers accepted for 1440 min (one full day), then run until the system is empty |

## Repository structure

```
├── PLAN.md                     Project plan and task division
├── requirements.txt
├── notebooks/
│   └── Airport_Checkin_Security.ipynb   Submission notebook
├── src/airport_sim/
│   ├── config.py               Parameters and experiment scenarios
│   ├── model.py                SimPy model (Lane A)
│   ├── monitor.py              Monitoring and metrics (Lane A)
│   ├── plots.py                B(t), Q(t) plots (Lane A)
│   ├── analysis.py             Replications, confidence intervals, β, experiments (Lane B)
│   └── animation.py            2D animation, 10% bonus (Lane C)
├── docs/event_graph/           Event graph drawing (Lane C)
├── docs/handoff/               Handoff notes between phases
├── results/                    Generated plots and tables
└── tests/                      Basic tests
```

## Setup

```bash
pip install -r requirements.txt
jupyter notebook notebooks/Airport_Checkin_Security.ipynb
pytest tests/
```
