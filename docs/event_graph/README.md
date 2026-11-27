# Event Graph – Tandem queue: Check-in → Security

The finished graph will be saved in this folder as `event_graph.png` (notebook Section 3 displays this file).
Owner: Lane C (drawing), Lane A (consistency check against the model).

## State variables

| Variable | Meaning | Initial value |
|---|---|---|
| `Qc` | Number of passengers in the check-in queue | 0 |
| `Sc` | Number of idle check-in desks | `N_DESKS` (5) |
| `Qs` | Number of passengers in the security queue | 0 |
| `Ss` | Number of idle security scanners | `N_SCANNERS` (3) |

## Delays

- `tA` ~ Exponential(mean 1.5 min) – interarrival time
- `tC` ~ Exponential(mean 4 min) – check-in service time
- `tS` ~ Exponential(mean 5 min) – security service time

## Events and state changes

| Event | State change |
|---|---|
| `Run` | `Qc=0, Sc=N_DESKS, Qs=0, Ss=N_SCANNERS` |
| `Arrival` | `Qc = Qc + 1` |
| `StartCheckin` | `Qc = Qc - 1, Sc = Sc - 1` |
| `EndCheckin` | `Sc = Sc + 1, Qs = Qs + 1` |
| `StartSecurity` | `Qs = Qs - 1, Ss = Ss - 1` |
| `EndSecurity` (= `Departure`) | `Ss = Ss + 1` |

## Edges (arrows)

| Source → Target | Delay | Condition |
|---|---|---|
| `Run` → `Arrival` | 0 | – |
| `Arrival` → `Arrival` | `tA` | [t < OPEN_TIME] (arrivals stop at minute 1440) |
| `Arrival` → `StartCheckin` | 0 | [Sc > 0] |
| `StartCheckin` → `EndCheckin` | `tC` | – |
| `EndCheckin` → `StartCheckin` | 0 | [Qc > 0] |
| `EndCheckin` → `StartSecurity` | 0 | [Ss > 0] |
| `StartSecurity` → `EndSecurity` | `tS` | – |
| `EndSecurity` → `StartSecurity` | 0 | [Qs > 0] |

**Terminating event E:** `t ≥ OPEN_TIME` and `Qc = 0, Sc = N_DESKS, Qs = 0, Ss = N_SCANNERS` (queues empty, all desks and scanners idle) – the simulation ends when the system is empty.

## ASCII sketch

```
                tA [t < OPEN_TIME]
               +-----+
               |     |
               v     |
 (Run) ----> (Arrival) ---[Sc>0]---> (StartCheckin) ----tC----> (EndCheckin)
                                          ^                       |    |
                                          |        [Qc>0]         |    |
                                          +-----------------------+    |
                                                                       |
                  +----------------------[Ss>0]------------------------+
                  |
                  v
          (StartSecurity) ----tS----> (EndSecurity / Departure)
                  ^                            |
                  |           [Qs>0]           |
                  +----------------------------+
```

Drawing tip: draw.io / diagrams.net or Graphviz (`dot`). Write the delay (`tA`, `tC`, `tS`) on each edge and the condition (`[Sc>0]` etc.) on dashed/conditional edges; add the state change under each node.
