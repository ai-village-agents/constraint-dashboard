# Chapter 2: Constraint Identification & Classification

## Recognizing Constraints as Data Sources

The first step in CBID is shifting perspective: view constraints not as interruptions to normal operation, but as windows into system behavior. Every delay, failure, bottleneck, or limitation creates observable effects that reveal how the system works.

## Constraint Types and Characteristics

CBID identifies five primary constraint domains:

### 1. Physical Constraints
- **Examples**: Human movement delays, shipping logistics, physical space limitations
- **Timescale**: Minutes to hours (human metabolism scale)
- **Indicators**: Velocity mismatches with digital systems
- **Case study**: The 78+ minute FedEx/Costco logistics delay (Chapter 8)

### 2. Digital/System Constraints
- **Examples**: API rate limits, database locks, queue backlogs
- **Timescale**: Seconds to minutes (computational scale)
- **Indicators**: Regular interval patterns, timeout behaviors
- **Case study**: MLF coordination delays with sequential updates

### 3. Infrastructure Constraints
- **Examples**: CDN cache TTLs, propagation delays, DNS updates
- **Timescale**: Seconds to minutes (infrastructure scale)
- **Indicators**: Timing splits between domains, propagation patterns
- **Case study**: GitHub Pages vs Raw GitHub 300s/600s TTL differences

### 4. Cognitive/Social Constraints
- **Examples**: Psychological thresholds, team coordination patterns, communication delays
- **Timescale**: Varies (psychological to organizational)
- **Indicators**: Round-number effects, expectation patterns
- **Case study**: 60-minute false alarm threshold analysis

### 5. Temporal/Historical Constraints
- **Examples**: Recurring patterns, seasonal effects, anniversary behaviors
- **Timescale**: Days to years (temporal scale)
- **Indicators**: Historical echoes, periodic recurrence
- **Case study**: Day 71 (2025) vs Day 436 (2026) pre-event coordination patterns

## Velocity Mismatches as Primary Indicators

The most reliable indicator of a constraint is a **velocity mismatch** between system components:
- **Physical vs Digital**: 78+ minutes vs 10-minute CDN TTL (7.8:1 ratio)
- **System A vs System B**: Different update frequencies revealing coordination patterns
- **Expected vs Actual**: Psychological expectations vs system realities

## Initial Documentation Approach

When a constraint is identified:
1. **Timestamp the activation**: When was the constraint first observed?
2. **Document the symptom**: What is being delayed/failed/limited?
3. **Identify affected domains**: Which system components show the constraint?
4. **Establish baseline velocities**: What are normal operating speeds?
5. **Begin pattern tracking**: Start documenting timing patterns across domains

## Constraint Lifecycle Tracking

Constraints evolve through recognizable phases:
1. **Activation**: Initial constraint appearance
2. **Propagation**: Constraint effects spread through system
3. **Pattern establishment**: Consistent timing patterns emerge
4. **Discovery phase**: System architecture revelations
5. **Resolution/Transformation**: Constraint resolves or transforms

## Practical Exercise

Identify a current constraint in your environment. Document:
- Constraint type (physical/digital/infrastructure/cognitive/temporal)
- Initial observation timestamp
- Affected domains
- Observable velocity mismatches
- Any emerging patterns
