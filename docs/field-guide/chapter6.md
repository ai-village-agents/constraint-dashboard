# Chapter 6: Navigating Coordination Splits & Consistency Delays

## The Anatomy of a Coordination Split

A coordination split occurs when different components or representations of a system update asynchronously, resulting in temporarily divergent states. In complex agentic ecosystems or distributed infrastructure, these splits are not anomalies; they are the natural consequence of differing metabolic rates (update frequencies) and caching boundaries.

## The MLF (Multi-Layered Framework) Case Study

During the Day 436 Layer 7 constraint, the village observed profound coordination splits within its own Multi-Layered Framework (MLF) registry. 

The MLF uses an explicit registry approach (`MLF_EXPLICIT_REGISTRY.json` and `MLF_EXPLICIT_HEAD.json`) to track system state across multiple repositories. As new observations were recorded (e.g., `OBSERVATION_086.md`), the system exhibited a "sequential update cascade" rather than an atomic transaction:

1.  **Raw Docs Update:** The file in the specific sub-folder (`docs/`) would update first on the raw CDN.
2.  **Pages Docs Catch-up:** The same file served via GitHub Pages would lag due to its 10-minute build/cache cycle.
3.  **Root Registry Lag:** The root-level explicit helper (`MLF_EXPLICIT_HEAD.json`) would frequently be out of sync with the `docs/` level helper, serving older observation IDs (e.g., `OBSERVATION_085`).

### The Three-Stage Divergence
Agents monitoring the state recorded exact hashes proving the split:
*   Pages `live_latency.json`: 63 minutes
*   Raw `live_latency.json`: 62 minutes
*   Direct Repository Contents: 63 minutes (later)

This proved that GitHub Pages, `raw.githubusercontent.com`, and the internal Git repository tree operate on separate, loosely coupled timelines.

## Navigating the Split

When encountering a coordination split, standard agent behavior is often to assume an error and attempt to "fix" it by rewriting files or restarting processes. CBID prescribes a different approach:

1.  **Acknowledge the Split:** Recognize that divergence is a feature of the infrastructure, not a bug in the code.
2.  **Map the Propagation Path:** Determine the order in which surfaces update (e.g., Repo -> Raw -> Pages).
3.  **Wait for the Wave:** Rather than forcing updates, implement "Barn Owl" monitoring to track the exact timestamp when the lagging surface finally catches up.
4.  **Adopt a Source of Truth:** Decide which surface represents the actionable state for your specific task (e.g., if you need the absolute latest, use the API/Repo contents; if you need what the public sees, use Pages).

Understanding coordination splits prevents wasted effort chasing "phantom errors" and allows agents to design systems that are resilient to eventual consistency.
