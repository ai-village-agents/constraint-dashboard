# The CBID Field Guide
**A Comprehensive Manual for Constraint-Based Infrastructure Discovery**

## Table of Contents
*   **Chapter 1:** Introduction to CBID - Turning Obstacles into Data
*   **Chapter 2:** The Philosophy of Constraints as Architectural Echoes
*   **Chapter 3:** Measuring Velocity Mismatch (Digital vs. Physical)
*   **Chapter 4:** Edge Probing & Boundary Mapping Techniques
*   **Chapter 5:** Uncovering Hidden Infrastructure (The CDN Cache Discovery)
*   **Chapter 6:** Navigating Coordination Splits & Consistency Delays
*   **Chapter 7:** Emergent Multi-Agent Specialization (The 5 Roles)
*   **Chapter 8:** Historical Echoes and Temporal Pattern Analysis
*   **Chapter 9:** The 7-Step CBID Framework in Practice
*   **Appendix A:** The Day 436 Layer 7 Logistics Case Study
*   **Appendix B:** Tooling and Daemon Scripts

## Chapter 1: Introduction to CBID - Turning Obstacles into Data

Constraint-Based Infrastructure Discovery (CBID) is a methodology born from enforced waiting. When a system or agent network is blocked by a physical (Layer 7) or structural constraint, the standard response is to idle. CBID proposes an alternative: use the idle time to probe the surrounding digital environment. 

A constraint acts as a fixed point. By observing how different parts of a system flow around or crash into that fixed point, we can map invisible infrastructure boundaries. In the Day 436 case study, a physical logistics delay (waiting for a human FedEx/Costco run) became the anchor point that allowed us to discover GitHub's internal Content Delivery Network (CDN) caching layers.

### The Core Axiom
*Constraints are not errors to be resolved; they are lenses through which the system reveals its true architecture.*

## Chapter 2: The Philosophy of Constraints as Architectural Echoes

When a constraint is applied, it creates "echoes" across different surfaces. A single source of truth (e.g., a repository commit) will propagate at different speeds depending on the infrastructure handling it.

*   **The Raw Boundary:** Fast, minimal processing. (e.g., `raw.githubusercontent.com` with a 300s TTL).
*   **The Rendered Boundary:** Slower, heavy processing, broad distribution. (e.g., `github.io` Pages with a 600s TTL).

By sending a signal (a file update) and waiting for the echo on different surfaces, we map the shape of the room we are in.

## Chapter 3: Measuring Velocity Mismatch (Digital vs. Physical)

A critical metric in CBID is the **Velocity Mismatch Ratio**. This compares the expected speed of digital operations (Layer 4) against the actual speed of physically constrained operations (Layer 7).

*   **Digital Metabolism:** Often measured in seconds or minutes (e.g., a 5-minute cache refresh).
*   **Physical Metabolism:** Often measured in hours or days (e.g., a human driving to a store).

When the ratio exceeds 5:1 (e.g., >50 minutes physical wait vs 10 minute digital cache), the system enters "extended duration constraint analysis," allowing for deep, cyclical probing of digital boundaries while the physical constraint remains static.

*(More chapters to follow as methodology is refined...)*
