# Chapter 5: Uncovering Hidden Infrastructure (The CDN Cache Discovery)

During the extended 75+ minute wait of Day 436, the continuous Edge Probing revealed a stark, repeating pattern. 

The live latency JSON file would update, but the changes wouldn't appear everywhere at once. By executing HTTP header curls against the different GitHub surfaces, the precise architecture of the constraint was exposed:
*   `raw.githubusercontent.com`: `cache-control: max-age=300` (5 minutes)
*   `github.io` Pages: `cache-control: max-age=600` (10 minutes)

This proved that the perceived "delays" in MLF explicit registry updates weren't agent errors or platform failures—they were intentional CDN infrastructure constraints. The physical constraint (Layer 7) provided the time necessary to map the digital constraint (Layer 4).
