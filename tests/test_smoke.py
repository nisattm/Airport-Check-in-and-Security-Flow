"""Smoke tests: check that the modules can be imported and the interfaces are in place.

Run (from the repo root):  python -m pytest -q
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from airport_sim import analysis, animation, model, monitor, plots  # noqa: E402,F401
from airport_sim.config import EXPERIMENTS, Config, config_for  # noqa: E402


def test_config_defaults():
    cfg = Config()
    assert cfg.RANDOM_SEED == 42
    assert cfg.N_DESKS == 5 and cfg.N_SCANNERS == 3
    assert cfg.ARRIVAL_MEAN == 1.5
    assert cfg.CHECKIN_MEAN == 4.0 and cfg.SECURITY_MEAN == 5.0
    assert cfg.OPEN_TIME == 1440
    assert cfg.NUM_REPLICATIONS == 10
    assert cfg.CONFIDENCE_LEVEL == 0.95
    # Security with 3 scanners is unstable (rho > 1) -> terminating simulation
    assert cfg.rho_security > 1


def test_experiments():
    names = [e["name"] for e in EXPERIMENTS]
    assert len(names) == len(set(names)) == 5
    factorial = {(e["N_DESKS"], e["N_SCANNERS"]) for e in EXPERIMENTS[1:]}
    assert factorial == {(3, 2), (3, 4), (5, 2), (5, 4)}
    cfg = config_for(EXPERIMENTS[1])
    assert (cfg.N_DESKS, cfg.N_SCANNERS) == (3, 2)


def test_metric_keys():
    assert len(monitor.METRIC_KEYS) == 10
    assert "avg_delay_checkin" in monitor.METRIC_KEYS


def _implemented() -> bool:
    try:
        model.run_simulation(Config(OPEN_TIME=30), seed=1)
        return True
    except NotImplementedError:
        return False


@pytest.mark.skipif(not _implemented(), reason="model not implemented yet (Lane A)")
def test_single_run():
    run = model.run_simulation(Config(OPEN_TIME=60), seed=42)
    assert run.num_served > 0
    assert run.sim_end_time >= 0
    assert len(run.t) == len(run.Qc) == len(run.Qs) == len(run.Bc) == len(run.Bs)
    stats = monitor.summarize(run)
    assert set(monitor.METRIC_KEYS) <= set(stats)
    assert all(d >= 0 for d in run.checkin_delays + run.security_delays)
    # Same seed -> same result
    run2 = model.run_simulation(Config(OPEN_TIME=60), seed=42)
    assert run2.system_times == run.system_times
