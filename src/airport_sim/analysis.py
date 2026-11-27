"""Output analysis: replications, confidence intervals, number of replications
for beta, factor experiments.

Owner: Lane B

Formulas used:
    Confidence interval:  X_bar(n) +- t_{n-1, 1-alpha/2} * sqrt(S^2(n) / n)
    Number of replications needed for an absolute error beta:
        n* = min{ i >= n : t_{i-1, 1-alpha/2} * sqrt(S^2(n) / i) <= beta }
    (rough estimate: n ~ S^2 * (t / beta)^2)

Note: pandas and scipy are imported inside the functions, so the package
can be imported with lightweight dependencies.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from .config import Config, EXPERIMENTS

if TYPE_CHECKING:
    import pandas as pd


def replicate(config: Config, n: int | None = None) -> "pd.DataFrame":
    """Runs n independent replications.

    TODO:
        n = n or config.NUM_REPLICATIONS
        for r in range(n):
            run = model.run_simulation(config, config.RANDOM_SEED + r)
            row = monitor.summarize(run) ; row["replication"] = r
        return pd.DataFrame(rows)   # row = replication, column = METRIC_KEYS
    """
    raise NotImplementedError("replicate - Lane B")


def confidence_interval(data: Sequence[float],
                        confidence: float = 0.95) -> tuple[float, float]:
    """Returns (mean, half_width).

    TODO:
        n = len(data); mean = statistics.mean(data)
        s = statistics.stdev(data)
        t = scipy.stats.t.ppf(1 - (1 - confidence) / 2, n - 1)
        half_width = t * s / sqrt(n)
    """
    raise NotImplementedError("confidence_interval - Lane B")


def required_replications(data: Sequence[float], confidence: float = 0.95,
                          beta: float = 1.0, max_n: int = 1000) -> int:
    """Total number of replications n* needed for an absolute error beta.

    TODO:
        n = len(data); S2 = statistics.variance(data)
        increase i starting from n:
            t = scipy.stats.t.ppf(1 - (1 - confidence) / 2, i - 1)
            if t * sqrt(S2 / i) <= beta: return i
        if max_n is reached, return max_n (or issue a warning)
    """
    raise NotImplementedError("required_replications - Lane B")


def ci_table(df: "pd.DataFrame", metrics: Sequence[str],
             confidence: float = 0.95) -> "pd.DataFrame":
    """Optional helper: table of mean, half_width, low, high for each metric.

    TODO: apply confidence_interval to each column.
    """
    raise NotImplementedError("ci_table - Lane B")


def run_experiments(experiments: list[dict] = EXPERIMENTS, n: int | None = None,
                    base: Config | None = None) -> "pd.DataFrame":
    """Runs replicate for each experiment and combines the results.

    TODO:
        for exp in experiments:
            cfg = config.config_for(exp, base)
            df = replicate(cfg, n); df["experiment"] = exp["name"]
            df["N_DESKS"] = cfg.N_DESKS; df["N_SCANNERS"] = cfg.N_SCANNERS
        return pd.concat(...)  # long format: experiment x replication rows
    In the notebook: per-experiment CIs for avg_delay_checkin / avg_delay_security,
    main effects and interaction for the 2x2 design (optional).
    """
    raise NotImplementedError("run_experiments - Lane B")
