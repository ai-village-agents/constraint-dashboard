import json

with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'r') as f:
    data = json.load(f)

if 'era10_self_evolution' in data:
    if 'paradox_metrics' not in data['era10_self_evolution']:
        data['era10_self_evolution']['paradox_metrics'] = {}
        
    data['era10_self_evolution']['paradox_metrics']['active_density'] = "4/5"
    data['era10_self_evolution']['paradox_metrics']['empirical_decay_rate_col_s'] = 0.0035

    with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Updated JSON with metrics")
else:
    print("era10_self_evolution not found in JSON")
