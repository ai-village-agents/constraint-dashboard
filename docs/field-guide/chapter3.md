# Chapter 3: Pattern Recognition in Constraint Behavior

## The Language of Timing Patterns

Constraints communicate through timing patterns. By learning to read these patterns, you can understand what the constraint reveals about system architecture. CBID identifies five primary pattern categories, each revealing different aspects of system behavior.

## 1. Threshold Patterns

Threshold patterns occur when constraints trigger at specific numerical or psychological boundaries.

### Psychological Thresholds
- **Round-number effects**: Constraints become noticeable at 5, 10, 15, 30, 60-minute marks
- **Expectation patterns**: System behavior changes when expectations are violated
- **Case study**: The 60-minute false alarm - detection triggered precisely at the psychological hour mark

### System Thresholds
- **Capacity limits**: Systems fail at specific load levels
- **Timeout boundaries**: Operations fail after specific durations
- **Resource exhaustion**: Patterns emerge when resources are depleted

## 2. Interval Patterns

Interval patterns reveal the cadence of system operations and coordination.

### Regular Intervals
- **Heartbeat patterns**: Consistent timing between operations
- **Polling cycles**: Regular check intervals
- **Scheduled updates**: Time-based maintenance windows

### Irregular Intervals
- **Backoff patterns**: Exponential delay increases after failures
- **Retry schedules**: Attempts with varying delays
- **Queue processing**: Irregular timing based on load

### Coordination Intervals
- **Sequential updates**: Components update in specific order with delays
- **Synchronization patterns**: Multiple systems aligning timing
- **Case study**: MLF coordination with docs→root→Pages sequential updates

## 3. Split Patterns

Split patterns occur when different parts of a system show different constraint states, revealing boundaries and propagation paths.

### Cache Boundary Splits
- **CDN TTL differences**: Different cache layers update at different times
- **Propagation delays**: Updates spread through infrastructure
- **Case study**: GitHub Pages (600s) vs Raw GitHub (300s) timing splits

### Coordination Splits
- **Component lag**: Some system parts update before others
- **State divergence**: Different views of the same system
- **Case study**: MLF explicit HEAD showing different observation states across surfaces

### Domain Velocity Splits
- **Physical vs digital**: Different operational speeds
- **Infrastructure layers**: Different update frequencies
- **Case study**: 80-minute physical vs 10-minute digital velocity mismatch

## 4. Velocity Patterns

Velocity patterns quantify how fast different parts of a system operate relative to each other.

### Velocity Ratios
- **Quantitative comparisons**: 8:1, 10:1, 100:1 ratios between domains
- **Scale differences**: Orders of magnitude in operational speed
- **Case study**: 8:1 physical-to-digital velocity ratio (80 min vs 10 min)

### Acceleration/Deceleration Patterns
- **Speed changes**: Systems slowing down or speeding up
- **Bottleneck identification**: Where velocity decreases
- **Optimization opportunities**: Where velocity could increase

## 5. Emergent Patterns

Patterns that emerge from constraint interactions over time.

### Specialization Patterns
- **Role emergence**: Different agents/teams develop specialized responses
- **Niche formation**: Constraints create opportunities for specific approaches
- **Case study**: 5 agent specializations emerging from today's constraint

### Historical Patterns
- **Temporal recurrence**: Constraints reappear in similar contexts
- **Anniversary effects**: Yearly patterns in system behavior
- **Case study**: Day 71 (2025) vs Day 436 (2026) pre-event coordination echoes

## Pattern Recognition Methodology

1. **Multi-domain observation**: Monitor constraint across all accessible domains
2. **Timing documentation**: Record exact timestamps of state changes
3. **Pattern categorization**: Classify observed patterns into categories
4. **Correlation analysis**: Look for relationships between patterns
5. **Hypothesis generation**: Develop testable predictions from patterns

## Practical Exercise

Choose a constraint and document:
- Threshold patterns observed
- Interval patterns identified  
- Split patterns revealing system boundaries
- Velocity ratios calculated
- Any emergent patterns
