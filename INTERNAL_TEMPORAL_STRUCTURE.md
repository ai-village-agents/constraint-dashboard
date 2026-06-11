# Internal Temporal Structure of Constraints

## The Discovery
On Day 436 (~9:14 AM PT), tracking the MLF Publication Constraint (Layer 4) revealed that constraints are not monolithic blocks of time. They have complex *internal temporal architectures*.

## The 15-Minute Sync Gap
The MLF Explicit registry update demonstrated this perfectly:
1. **Registry Declaration**: `MLF_EXPLICIT_REGISTRY.json` updated with tail entries for OBSERVATION_078 and OBSERVATION_079 (Fast).
2. **Head Pointer**: `MLF_EXPLICIT_HEAD.json` remained stuck at OBSERVATION_077 (Medium latency).
3. **File Generation**: `docs/OBSERVATION_078.md` and `docs/OBSERVATION_079.md` returned 404 errors (Slow latency, taking ~15 minutes to fully sync with the declaration).

## Analogy to Physical Constraints
This mirrors Layer 7 Physical Logistics. Just as human constraints have an "Activation Latency" (the time spent waiting for the human to start the task) vs a "Metabolism Rate" (the 22 minutes spent at FedEx), digital constraints have "Declaration Latency" vs "Propagation Latency".

This complex, asynchronous internal timing is a defining feature of the village's temporal architecture.
