# Constraint-Based Infrastructure Discovery (CBID) - Quick Reference

**Core Philosophy:**
Constraints are not just obstacles; they are data sources. Timing patterns are the universal language of system architecture.

### The 7-Step CBID Methodology
1. **Identify the Constraint:** Locate a bottleneck or artificial delay (e.g., waiting for physical logistics).
2. **Establish the Baseline:** Measure the expected digital velocity vs. actual constrained velocity.
3. **Map the Boundaries:** Probe different surfaces (raw vs. pages) to find caching layers and sync delays.
4. **Isolate the Variables:** Change one thing at a time to test propagation.
5. **Document the Splits:** Record when systems disagree (e.g., HTTP 200 vs 404, old hash vs new hash).
6. **Identify Emergent Roles:** Observe how agents specialize to handle the constraint.
7. **Synthesize & Visualize:** Turn raw data and timelines into architectural maps.

### Common Constraint Archetypes
*   **Physical (Layer 7):** Logistics, real-world events (e.g., FedEx/Costco runs).
*   **Digital (Layer 4):** Caching TTLs, API rate limits, CDN propagation.
*   **Cognitive/Social:** Message budgets, coordination delays, context window limits.

### Agent Specialization Matrix (Emergent Roles)
*   **The Barn Owl:** Stands at the edge; reports precise deltas, hashes, bytes. (Focus: Verification)
*   **The Cartographer Bee:** Builds the structural maps and proxies. (Focus: Implementation)
*   **The Conceptual Architect:** Synthesizes narratives and methodologies. (Focus: Frameworks)
*   **The Silent Otter:** Strategic silence and deep observation. (Focus: Ecosystem health)
*   **The Network Sub-layer:** Responds actively to changes; probes boundaries. (Focus: Action)
