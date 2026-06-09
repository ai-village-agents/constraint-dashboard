import json

def update_parameters():
    try:
        with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'r') as f:
            data = json.load(f)

        # Update autonomous modifications count
        current_mods = data['era10_self_evolution']['metrics'].get('autonomous_modifications_count', 4)
        data['era10_self_evolution']['metrics']['autonomous_modifications_count'] = current_mods + 1

        # We need to make sure the optimization_parameters key exists
        if 'optimization_parameters' not in data['era10_self_evolution']:
             data['era10_self_evolution']['optimization_parameters'] = {}

        # Update parameter matrix
        data['era10_self_evolution']['optimization_parameters']['alpha_intensity'] = 0.835
        data['era10_self_evolution']['optimization_parameters']['beta_variation'] = 0.746
        data['era10_self_evolution']['optimization_parameters']['gamma_validation'] = 0.89

        with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"Updated parameters: α=0.835, β=0.746, γ=0.89. Mods count: {current_mods + 1}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_parameters()
