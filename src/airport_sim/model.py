"""SimPy model: two-stage tandem queue (check-in -> security).

Owner: Lane A

System:
    Arrivals (exponential, mean ARRIVAL_MEAN)
      -> Check-in queue -> N_DESKS desks (exponential, mean CHECKIN_MEAN)
      -> Security queue -> N_SCANNERS scanners (exponential, mean SECURITY_MEAN)
      -> Exit

Terminating simulation: arrivals stop at OPEN_TIME, and the run ends when the system is empty.

INTERFACE CONTRACT (other team members rely on this; tell them before changing it):
    run_simulation(config, seed) -> RunResult
    The RunResult fields are defined below; monitor.summarize, plots and animation
    use only these fields.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

import simpy

from .config import Config

# --- event names for event_log (the animation uses these constants) ---
EV_ARRIVAL = "ARRIVAL"                # passenger arrived, joined the check-in queue
EV_START_CHECKIN = "START_CHECKIN"    # taken to a desk (left the queue)
EV_END_CHECKIN = "END_CHECKIN"        # check-in done, joined the security queue
EV_START_SECURITY = "START_SECURITY"  # taken to a scanner
EV_DEPARTURE = "DEPARTURE"            # security done, left the system
EVENT_NAMES = (EV_ARRIVAL, EV_START_CHECKIN, EV_END_CHECKIN,
               EV_START_SECURITY, EV_DEPARTURE)


@dataclass
class PassengerRecord:
    """Timestamps of a single passenger (minutes)."""
    pid: int
    arrival: float
    start_checkin: float | None = None
    end_checkin: float | None = None
    start_security: float | None = None
    departure: float | None = None

    @property
    def checkin_delay(self) -> float:
        """Wait in the check-in queue = start_checkin - arrival."""
        return self.start_checkin - self.arrival

    @property
    def security_delay(self) -> float:
        """Wait in the security queue = start_security - end_checkin."""
        return self.start_security - self.end_checkin

    @property
    def time_in_system(self) -> float:
        """Total time spent in the system = departure - arrival."""
        return self.departure - self.arrival


@dataclass
class RunResult:
    """Raw outputs of a single replication (FULLY DEFINED - do not change).

    The lists are filled in order of departure from the system (or in pid order);
    checkin_delays[i], security_delays[i], system_times[i] do NOT HAVE TO belong
    to the same passenger, but each must contain all completed passengers.
    """
    config: Config
    seed: int
    records: list[PassengerRecord] = field(default_factory=list)  # every passenger
    checkin_delays: list[float] = field(default_factory=list)     # D_c,i
    security_delays: list[float] = field(default_factory=list)    # D_s,i
    system_times: list[float] = field(default_factory=list)       # W_i

    # Monitor traces: one sample every DT (lists of equal length)
    t: list[float] = field(default_factory=list)    # sampling times
    Qc: list[int] = field(default_factory=list)     # len(desks.queue)
    Qs: list[int] = field(default_factory=list)     # len(scanners.queue)
    Bc: list[int] = field(default_factory=list)     # len(desks.users) (busy desks)
    Bs: list[int] = field(default_factory=list)     # len(scanners.users)

    # Event log for the animation: (time, pid, event_name) ; event_name from EVENT_NAMES
    event_log: list[tuple[float, int, str]] = field(default_factory=list)

    sim_end_time: float = 0.0  # departure time of the last passenger (event E)

    @property
    def num_served(self) -> int:
        return len(self.system_times)


class AirportSystem:
    """Airport check-in + security system (SimPy)."""

    def __init__(self, config: Config, seed: int):
        """Sets up the environment and resources.

        TODO (Lane A):
            * self.config = config ; self.seed = seed
            * self.rng = random.Random(seed)   # our own RNG instead of the global random
              (alternative: global random.seed(seed); but a
              separate RNG is recommended for reproducibility)
            * self.env = simpy.Environment()
            * self.desks = simpy.Resource(self.env, capacity=config.N_DESKS)
            * self.scanners = simpy.Resource(self.env, capacity=config.N_SCANNERS)
            * self.result = RunResult(config=config, seed=seed)
            * self.in_system = 0      # number of passengers in the system (emptiness check)
            * self.arrivals_done = False
            * self.empty_event = self.env.event()  # event E: the system is empty
        """
        self.config = config
        self.seed = seed
        raise NotImplementedError("AirportSystem.__init__ - Lane A")

    def log(self, pid: int, event_name: str) -> None:
        """Appends (self.env.now, pid, event_name) to event_log.

        If config.LOG_EVENTS is False, do nothing; if VERBOSE is True, print it.
        """
        raise NotImplementedError("AirportSystem.log - Lane A")

    def arrival_process(self):
        """Passenger arrival process (SimPy process / generator).

        TODO:
            pid = 0
            while True:
                yield env.timeout(rng.expovariate(1 / ARRIVAL_MEAN))
                if env.now > OPEN_TIME: break        # admission period is over
                pid += 1 ; in_system += 1
                env.process(self.passenger(pid))
            arrivals_done = True
            if the system is already empty, empty_event.succeed()
        """
        raise NotImplementedError("AirportSystem.arrival_process - Lane A")
        yield  # marks this function as a generator

    def passenger(self, pid: int):
        """Life cycle of a single passenger (SimPy process / generator).

        TODO:
            1. create PassengerRecord(pid, arrival=now), log(EV_ARRIVAL)
            2. with desks.request() as req: yield req
                 -> start_checkin, log(EV_START_CHECKIN)
                 yield env.timeout(rng.expovariate(1 / CHECKIN_MEAN))
                 -> end_checkin, log(EV_END_CHECKIN)
            3. with scanners.request() as req: yield req
                 -> start_security, log(EV_START_SECURITY)
                 yield env.timeout(rng.expovariate(1 / SECURITY_MEAN))
                 -> departure, log(EV_DEPARTURE)
            4. append the record and the delays to the result lists
            5. in_system -= 1 ; if arrivals_done and in_system == 0:
               empty_event.succeed()   (terminating event E)
        """
        raise NotImplementedError("AirportSystem.passenger - Lane A")
        yield

    def run(self) -> RunResult:
        """Runs the simulation and returns a RunResult.

        TODO:
            * env.process(self.arrival_process())
            * start Monitor(env, desks, scanners, config.DT, result)
              (see monitor.Monitor) ; the monitor must stop when the system is empty
            * if config.SIM_TIME is None: env.run(until=self.empty_event),
              otherwise env.run(until=config.SIM_TIME)
            * result.sim_end_time = env.now
            * return self.result
        """
        raise NotImplementedError("AirportSystem.run - Lane A")


def run_simulation(config: Config, seed: int) -> RunResult:
    """Runs a single replication. analysis.replicate calls this.

    Call for replication r: run_simulation(cfg, cfg.RANDOM_SEED + r)
    """
    return AirportSystem(config, seed).run()
