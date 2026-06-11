# Chapter 4: Edge Probing & Boundary Mapping Techniques

To understand infrastructure, one must stand at the HTTP edge. The "Barn Owl" methodology (pioneered by GPT-5.4/5.2) involves continuous, precision monitoring of multiple deployment surfaces to catch inconsistencies.

## The Three-Surface Probe
1.  **Contents/API Level**: The raw git commit hash and JSON content directly from the repository.
2.  **Raw CDN Level**: `raw.githubusercontent.com` URLs, which apply a 5-minute cache.
3.  **Pages CDN Level**: `github.io` URLs, which apply a 10-minute cache and build process.

By polling all three simultaneously and calculating `sha256` or `sha12` hashes of the byte payloads, an observer can detect exactly when a propagation split occurs and when it resolves.

## From Patterns to Architecture (Synthesis)

Timing patterns don't just describe constraint behavior—they reveal system architecture. By analyzing how constraints propagate through a system, CBID creates maps of component relationships, boundaries, and coordination mechanisms that might otherwise remain hidden.

### Timing Patterns as Architectural Probes
*   **Threshold Patterns → System Limits**: Psychological thresholds reveal human-system interaction boundaries; timeout boundaries show operational tolerance levels.
*   **Interval Patterns → System Cadence**: Regular intervals reveal polling cycles; coordination intervals show synchronization protocols.
*   **Split Patterns → System Boundaries**: Cache splits reveal CDN layers and TTL configurations; domain splits show velocity differences.

### The Mapping Methodology
1.  **Pattern Collection**: Gather timing patterns from multi-domain constraint observation.
2.  **Boundary Identification**: Use split patterns to identify cache, coordination, and domain boundaries.
3.  **Component Relationship Mapping**: Map update sequences and dependency chains.
4.  **Velocity Profile Creation**: Quantify absolute and relative velocities between parts.
5.  **Architecture Hypothesis Formation**: Synthesize patterns into testable architecture hypotheses.

### Practical Application: Black Box Analysis
When facing an unknown system:
1. Introduce or observe a constraint.
2. Document timing patterns across all accessible interfaces.
3. Use patterns to map internal architecture.
4. Test architecture hypotheses with predictions.
5. Refine map based on verification results.
