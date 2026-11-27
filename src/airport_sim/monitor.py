"""Monitoring (Monitor) and summary metrics.

Owner: Lane A

The Monitor records queue lengths (len(res.queue)) and the number of busy
servers (len(res.users)) into the RunResult every DT minutes.
summarize(run) produces a dict with fixed keys from a single replication;
analysis.py (Lane B) uses these keys.
"""

from __future__ import annotations

import simpy

from .model import RunResult

# KEYS of the summarize() output (INTERFACE - do not change; you may add keys)
METRIC_KEYS = (
    "avg_delay_checkin",        # d_c: mean wait in the check-in queue (min)
    "avg_delay_security",       # d_s: mean wait in the security queue (min)
    "avg_time_in_system",       # w : mean time in system (min)
    "avg_num_queue_checkin",    # q_c: time-average number of people in the check-in queue
    "avg_num_queue_security",   # q_s: time-average number of people in the security queue
    "avg_num_in_system",        # L  : time-average number of people in the system
    "util_checkin",             # u_c: mean busy desks / N_DESKS
    "util_security",            # u_s: mean busy scanners / N_SCANNERS
    "max_queue_checkin",        # maximum length of the check-in queue
    "max_queue_security",       # maximum length of the security queue
)


class Monitor:
    """SimPy process that takes one sample every DT.

    Usage (inside model.AirportSystem.run):
        Monitor(env, desks, scanners, config.DT, result, stop_event=empty_event)
    """

    def __init__(self, env: simpy.Environment, desks: simpy.Resource,
                 scanners: simpy.Resource, dt: float, result: RunResult,
                 stop_event: simpy.Event | None = None):
        """TODO: store the fields and start env.process(self.run())."""
        raise NotImplementedError("Monitor.__init__ - Lane A")

    def run(self):
        """Sampling loop (generator).

        TODO:
            while stop_event has not been triggered:
                result.t.append(env.now)
                result.Qc.append(len(desks.queue))
                result.Qs.append(len(scanners.queue))
                result.Bc.append(len(desks.users))
                result.Bs.append(len(scanners.users))
                yield env.timeout(dt)
        """
        raise NotImplementedError("Monitor.run - Lane A")
        yield


def summarize(run: RunResult) -> dict:
    """Returns a dict keyed by METRIC_KEYS for a single replication.

    TODO:
        * Delays: statistics.mean(run.checkin_delays) etc.
        * Time averages: approximated with the Dt samples
              q_c ~ mean(run.Qc),  L ~ mean(Qc + Bc + Qs + Bs)
          (more accurate: time-weighted integral / sim_end_time; state the
           choice in the notebook)
        * Utilization: mean(run.Bc) / N_DESKS, mean(run.Bs) / N_SCANNERS
        * Maxima: max(run.Qc), max(run.Qs)
        * "num_served" and "sim_end_time" may also be added.
    """
    raise NotImplementedError("summarize - Lane A")
