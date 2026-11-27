"""Animation (BONUS, 10%).

Owner: Lane C

Plan:
    Replays the RunResult.event_log [(time, pid, event_name), ...] afterwards.
    The model is not re-run.

    Visual layout (matplotlib):
        [Check-in queue: row of dots] -> [N_DESKS boxes] ->
        [Security queue: row of dots] -> [N_SCANNERS boxes] -> exit
        Clock in the top corner: "t = 123.0 min", plus the number of
        passengers in the system.

    Steps:
        1. Frame times: frames = np.arange(0, run.sim_end_time, step)
        2. State at each frame time: scan event_log in time order to find
           where each pid is (checkin queue, desk, security queue, scanner,
           departed). Event names: model.EVENT_NAMES.
        3. update(frame) function with matplotlib.animation.FuncAnimation:
           update the dot positions and box colors (busy/idle).
        4. anim.save(out_path, writer=PillowWriter(fps=...)) -> GIF
           (Display in the notebook: IPython.display.Image(out_path))

    Optional: a live version with pygame (animate_pygame) that uses the same
    state computation function (state_at).
"""

from __future__ import annotations

from .model import RunResult


def state_at(run: RunResult, t: float) -> dict:
    """State at time t.

    Returns: {"queue_checkin": [pid...], "desks": [pid...],
              "queue_security": [pid...], "scanners": [pid...],
              "departed": int}
    TODO: compute by replaying event_log up to t
    (for efficiency, update incrementally between frames).
    """
    raise NotImplementedError("state_at - Lane C")


def animate(run: RunResult, out_path: str = "results/animation.gif",
            step: float = 1.0, fps: int = 15, max_time: float | None = None):
    """Replays event_log with FuncAnimation and saves it as a GIF.

    step: simulated time between frames (min)
    max_time: upper time limit to shorten the GIF (None -> sim_end_time)
    Returns: out_path
    """
    raise NotImplementedError("animate - Lane C")


def animate_pygame(run: RunResult, speed: float = 10.0):
    """Optional: live playback with pygame (pygame is commented out in requirements)."""
    raise NotImplementedError("animate_pygame - Lane C (optional)")
