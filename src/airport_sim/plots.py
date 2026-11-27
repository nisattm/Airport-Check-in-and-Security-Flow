"""B(t) and Q(t) plots.

Owner: Lane A

B(t): number of busy servers over time (Bc = desks, Bs = scanners)
Q(t): number of people in queue over time (Qc = check-in, Qs = security)
Data source: RunResult.t, .Bc, .Bs, .Qc, .Qs (Monitor traces).
"""

from __future__ import annotations

from .model import RunResult


def plot_Bt(run: RunResult, out_path: str | None = None, ax=None):
    """B(t) plot; Bc and Bs as separate lines (plt.step recommended).

    TODO:
        * Capacity lines: y = N_DESKS and y = N_SCANNERS (dashed)
        * Vertical line at x = OPEN_TIME (when arrivals stop)
        * Axis labels: "Time (min)", "Number of busy servers"
        * Save if out_path is given (e.g. results/Bt_baseline.png)
        * Return the matplotlib Axes
    """
    raise NotImplementedError("plot_Bt - Lane A")


def plot_Qt(run: RunResult, out_path: str | None = None, ax=None):
    """Q(t) plot; Qc and Qs as separate lines.

    TODO:
        * Vertical line at x = OPEN_TIME
        * Mark the max(Qc), max(Qs) points (optional)
        * Axis labels: "Time (min)", "Number of passengers in queue"
        * Save if out_path is given ; return the Axes
    """
    raise NotImplementedError("plot_Qt - Lane A")
