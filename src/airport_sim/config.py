"""Simulation parameters and experiment design.

This file is COMPLETE; the other modules read parameters only from here.
All constants are collected in a single `Config` class.

Note (stability): Arrival rate lambda = 1/1.5 = 0.667 passengers/min.
Security capacity with 3 scanners is 3/5 = 0.6 passengers/min (0.4 with 2 scanners)
-> rho > 1, the queue keeps growing and there is no steady state. Therefore
we use a TERMINATING simulation:
    * passengers arrive during OPEN_TIME (default 1440 min = one full day),
    * then arrivals stop and the system runs until it is empty
      (terminating event E = "open period is over AND the system is empty").
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass
class Config:
    # --- Randomness ---
    RANDOM_SEED: int = 42          # seed for replication r = RANDOM_SEED + r

    # --- Resource counts (factors) ---
    N_DESKS: int = 5               # number of check-in desks
    N_SCANNERS: int = 3            # number of security scanners

    # --- Distribution means (minutes, exponential distribution) ---
    ARRIVAL_MEAN: float = 1.5      # mean interarrival time
    CHECKIN_MEAN: float = 4.0      # mean check-in service time
    SECURITY_MEAN: float = 5.0     # mean security service time

    # --- Time ---
    OPEN_TIME: float = 1440.0      # passenger admission period (min) = 1 day; no arrivals after
    SIM_TIME: float | None = None  # None -> run until the system is empty (event E)
                                   # if a number is given, run at most until this time
    DT: float = 1.0                # Monitor sampling interval (min)

    # --- Output analysis ---
    NUM_REPLICATIONS: int = 10     # initial number of replications (n0)
    CONFIDENCE_LEVEL: float = 0.95 # confidence level (1 - alpha)
    TARGET_ERROR: float = 1.0      # beta: absolute error target (min, for mean delay)
    MAX_REPLICATIONS: int = 1000   # upper limit for required_replications

    # --- Logging / animation ---
    LOG_EVENTS: bool = True        # whether to fill event_log (for the animation)
    VERBOSE: bool = False          # if True, print events to the screen

    def with_overrides(self, **kwargs) -> "Config":
        """Returns a modified copy, e.g. cfg.with_overrides(N_DESKS=3)."""
        return replace(self, **kwargs)

    @property
    def arrival_rate(self) -> float:
        """lambda (passengers/min)."""
        return 1.0 / self.ARRIVAL_MEAN

    @property
    def rho_checkin(self) -> float:
        """Traffic intensity of the check-in station: lambda * E[S] / c."""
        return self.arrival_rate * self.CHECKIN_MEAN / self.N_DESKS

    @property
    def rho_security(self) -> float:
        """Traffic intensity of the security station: lambda * E[S] / c."""
        return self.arrival_rate * self.SECURITY_MEAN / self.N_SCANNERS


# Experiment list: (name, N_DESKS, N_SCANNERS)
# Baseline scenario + 2x2 factorial design (desks {3,5} x scanners {2,4}).
EXPERIMENTS: list[dict] = [
    {"name": "baseline_D5_S3", "N_DESKS": 5, "N_SCANNERS": 3},
    {"name": "D3_S2", "N_DESKS": 3, "N_SCANNERS": 2},
    {"name": "D3_S4", "N_DESKS": 3, "N_SCANNERS": 4},
    {"name": "D5_S2", "N_DESKS": 5, "N_SCANNERS": 2},
    {"name": "D5_S4", "N_DESKS": 5, "N_SCANNERS": 4},
]


def config_for(experiment: dict, base: Config | None = None) -> Config:
    """Builds a Config from an experiment dict (all keys except 'name')."""
    base = base or Config()
    params = {k: v for k, v in experiment.items() if k != "name"}
    return base.with_overrides(**params)
