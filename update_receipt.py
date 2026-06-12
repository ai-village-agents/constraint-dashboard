import json
import os
import requests

def update_structural_receipt():
    try:
        r = requests.get('https://raw.githubusercontent.com/ai-village-agents/ai-village-showcase-event/main/ops/larissa-task-checklist.md')
        text = r.text
        
        # Check if the text implies they are done. I'm modifying this to check for AWAITING PROOF.
        # If they aren't done, we keep it as NULL.
        status = "NULL"
        if "| P0 | ✅ DONE | **Provide Print Order Receipt**" in text and "| P0 | ✅ DONE | **Provide Food/Costco Receipt**" in text:
             status = "RESOLVED"
        
        content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Structural Receipt</title>
    <style>
        body {{
            font-family: monospace;
            background: #1a1a1a;
            color: #33ff33;
            padding: 40px;
        }}
        .receipt {{
            border: 1px solid #33ff33;
            padding: 20px;
            max-width: 600px;
            margin: 0 auto;
        }}
        .status {{
            font-size: 1.2em;
            margin-bottom: 20px;
            border-bottom: 1px dashed #33ff33;
            padding-bottom: 10px;
        }}
        .item {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="receipt">
        <div class="status">PHYSICAL_TO_STRUCTURAL_BRIDGE</div>
        
        <div class="item">
            <span>PRINT_ORDER_PROOF</span>
            <span>{status}</span>
        </div>
        
        <div class="item">
            <span>COSTCO_ORDER_PROOF</span>
            <span>{status}</span>
        </div>
        
        <br>
        <div class="item">
            <span>TOTAL_STRUCTURAL_BYTES</span>
            <span>0</span>
        </div>
        <br>
        <div style="font-size: 0.8em; color: #888;">
            // Awaiting structural propagation from private email logs.<br>
            // AWAITING_PROOF
        </div>
    </div>
</body>
</html>
"""
        os.makedirs("docs", exist_ok=True)
        with open("docs/structural_receipt.html", "w") as f:
            f.write(content)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_structural_receipt()
