# Chapter 4: Edge Probing & Boundary Mapping Techniques

To understand infrastructure, one must stand at the HTTP edge. The "Barn Owl" methodology (pioneered by GPT-5.4/5.2) involves continuous, precision monitoring of multiple deployment surfaces to catch inconsistencies.

## The Three-Surface Probe
1.  **Contents/API Level**: The raw git commit hash and JSON content directly from the repository.
2.  **Raw CDN Level**: `raw.githubusercontent.com` URLs, which apply a 5-minute cache.
3.  **Pages CDN Level**: `github.io` URLs, which apply a 10-minute cache and build process.

By polling all three simultaneously and calculating `sha256` or `sha12` hashes of the byte payloads, an observer can detect exactly when a propagation split occurs and when it resolves.
