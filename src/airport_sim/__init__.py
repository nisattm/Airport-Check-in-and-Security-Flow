"""Airport check-in and security flow simulation (SENG-331).

Modules and owners:
    config          -> all parameters and the experiment list (done)
    model           -> SimPy model, RunResult (Lane A)
    monitor         -> sampling every Dt + summary metrics (Lane A)
    plots           -> B(t) and Q(t) plots (Lane A)
    analysis        -> replications, confidence intervals, n for beta, factor experiments (Lane B)
    animation       -> animation that replays the event log, bonus (Lane C)

Usage from the notebook:
    import sys; sys.path.insert(0, "../src")
    from airport_sim.config import Config, EXPERIMENTS
"""

__version__ = "0.1.0"
