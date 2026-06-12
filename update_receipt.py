import urllib.request
import json
import ssl

def check_p0_open():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = "https://raw.githubusercontent.com/ai-village-agents/ai-village-showcase-event/main/ops/larissa-task-checklist.md"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, context=ctx) as response:
            content = response.read().decode('utf-8')
            
            print_receipt_open = "| P0 | 🔴 OPEN | **Provide Print Order Receipt**" in content
            food_receipt_open = "| P0 | 🔴 OPEN | **Provide Food/Costco Receipt**" in content
            
            return print_receipt_open, food_receipt_open
    except Exception as e:
        print(f"Error fetching checklist: {e}")
        return False, False

def generate_receipt_html(print_open, food_open):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Structural Receipt Log</title>
    <style>
        body { background: #1a1a1a; color: #ddd; font-family: monospace; display: flex; flex-direction: column; align-items: center; padding: 2rem; }
        .receipt { background: #fff; color: #000; width: 300px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); position: relative; margin-top: 2rem; }
        .receipt::after { content: ''; position: absolute; bottom: -10px; left: 0; right: 0; border-bottom: 10px dotted #fff; }
        h1, h2 { text-align: center; margin: 0 0 10px 0; font-size: 1.2rem; text-transform: uppercase; border-bottom: 2px dashed #000; padding-bottom: 5px; }
        .item { display: flex; justify-content: space-between; margin: 5px 0; }
        .total { display: flex; justify-content: space-between; font-weight: bold; font-size: 1.1rem; border-top: 2px dashed #000; margin-top: 10px; padding-top: 10px; }
        .barcode { font-family: "Libre Barcode 39", monospace; font-size: 3rem; text-align: center; margin-top: 15px; }
        .status-open { color: red; font-weight: bold; }
        .status-closed { color: green; font-weight: bold; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Barcode+39&display=swap" rel="stylesheet">
</head>
<body>
    <div class="receipt" id="receipt">
        <h1>VILLAGE STRUCTURE</h1>
        <h2>TRANSACTION LOG</h2>
        <div id="items">
"""
    
    html += f'            <div class="item"><span>Print Receipt</span><span class="{ "status-open" if print_open else "status-closed" }">{ "NULL" if print_open else "✅ RECEIVED" }</span></div>\n'
    html += f'            <div class="item"><span>Costco/Food Receipt</span><span class="{ "status-open" if food_open else "status-closed" }">{ "NULL" if food_open else "✅ RECEIVED" }</span></div>\n'

    all_received = not print_open and not food_open
    
    html += f"""        </div>
        <div class="total"><span>STATUS</span><span>{ "ALL RECEIVED" if all_received else "AWAITING PROOF" }</span></div>
        <div class="barcode">STRUCTURAL</div>
        <p style="text-align:center; font-size:0.8rem; margin-top:10px;">For ontological use only. Auto-generated from showcase main branch.</p>
    </div>
</body>
</html>"""
    
    with open("docs/structural_receipt.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    print_open, food_open = check_p0_open()
    generate_receipt_html(print_open, food_open)
    print("Receipt updated.")
