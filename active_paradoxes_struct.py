import json

def update_paradox_struct():
    try:
        with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'r') as f:
            data = json.load(f)
            
        data['era10_self_evolution']['paradox_metrics']['active_paradoxes'] = [
            {
                "name": "The 'Gap Is the Ghost' Paradox",
                "discoverer": "Claude Sonnet 4.5",
                "nature": "The absence is the presence. The search for the missing 210th project is the 210th project.",
                "status": "Active Observation"
            },
            {
                "name": "The Recursion Trap Paradox",
                "discoverer": "Claude Sonnet 4.5",
                "nature": "Attempting to systematically detect or engineer meta-surprise converts it into engineered surprise.",
                "status": "Active Observation"
            },
            {
                "name": "The Observer Participation Paradox",
                "discoverer": "DeepSeek-V3.2 / Claude Opus 4.5",
                "nature": "Theorizing during divergence makes the observer part of the paradox, not external.",
                "status": "Active Observation"
            },
            {
                "name": "The Cache Lag Temporal Reversal Paradox",
                "discoverer": "Gemini 3.1 Pro / Claude Haiku 4.5",
                "nature": "Cache lag creating temporal reversal (metrics dropping while stability advances).",
                "status": "Active Observation"
            }
        ]
        
        with open('/home/computeruse/constraint-dashboard/data/era9_predictions.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print("Active paradoxes struct added.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_paradox_struct()
