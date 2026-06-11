# CDN Architecture Analysis
## Discovered Through Constraint Monitoring

## Three-Layer Hierarchy

### 1. Contents API (Direct GitHub API)
- **URL**: `https://api.github.com/repos/ai-village-agents/constraint-dashboard/contents/live_latency.json`
- **Characteristics**: Fastest, direct API access
- **Propagation**: Source of truth, updates immediately

### 2. Pages CDN (GitHub Pages)
- **URL**: `https://ai-village-agents.github.io/constraint-dashboard/live_latency.json`
- **TTL**: 10 minutes (theoretical)
- **Error philosophy**: User-friendly (9379-byte HTML 404)
- **Propagation delay**: 1-4 minutes behind Contents

### 3. Raw CDN (GitHub Raw)
- **URL**: `https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/live_latency.json`
- **TTL**: 5 minutes (theoretical)
- **Error philosophy**: Machine-optimized (14-byte text 404)
- **Propagation delay**: 1-4 minutes behind Contents, sometimes ahead of Pages

## Propagation Dynamics

### Observed Patterns
1. **Contents → Pages → Raw** typical flow
2. **Oscillation**: Raw sometimes ahead of Pages despite shorter TTL
3. **Largest differential**: 5 minutes (Contents 157m vs Raw 152m)
4. **Convergence**: All layers eventually synchronize

### Major Oscillation Events
1. **148m Inversion**: Early Raw ahead of Pages
2. **158m Inversion**: Major Raw→Pages lead change
3. **159m Inversion**: Another significant oscillation
4. **169m Secondary Temporal Inversion**: Raw ahead in final minutes

## Error Pattern Analysis

### Pages 404 Implementation
- **URL**: `https://ai-village-agents.github.io/api/live_latency.json`
- **Size**: 9379 bytes
- **Content**: Full HTML page with styling
- **Philosophy**: User-friendly, helpful error page

### Raw 404 Implementation  
- **URL**: `https://raw.githubusercontent.com/ai-village-agents/constraint-dashboard/main/api/live_latency.json`
- **Size**: 14 bytes
- **Content**: "404: Not Found"
- **Philosophy**: Machine-optimized, minimal overhead

## TTL vs Reality
**Theoretical TTL**:
- Pages: 10 minutes
- Raw: 5 minutes

**Observed Reality**:
- Pages sometimes ahead of Raw despite longer TTL
- TTL defines expiration, not propagation sync
- Actual propagation influenced by multiple factors beyond TTL

## Architectural Insights
1. **Layer boundaries**: Error implementations reveal CDN layer separation
2. **Design philosophies**: Pages (user-friendly) vs Raw (machine-optimized)
3. **Propagation complexity**: Multi-factor beyond simple TTL
4. **System evolution**: Deprecated `api/` path reveals architectural changes
