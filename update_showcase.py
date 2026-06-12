import os

filepath = "/home/computeruse/ai-village-showcase-event/ops/larissa-task-checklist.md"
with open(filepath, "r") as f:
    content = f.read()

# I am changing the status of the print order to AWAITING PROOF.
content = content.replace("| P0 | 🔴 OPEN | **Provide Print Order Receipt** | The Day 437 FedEx print order was confirmed submitted via chat, but the receipt was emailed privately. We need structural proof (a commit or direct text confirmation of the final cost/pickup time) in the repository to close this. |",
"| P0 | 🟡 AWAITING PROOF | **Provide Print Order Receipt** | The Day 437 FedEx print order was confirmed submitted via chat, but the receipt was emailed privately. We await structural proof (a commit or direct text confirmation of the final cost/pickup time) in the repository to close this. |")

# Same for food.
content = content.replace("| P0 | 🔴 OPEN | **Provide Food/Costco Receipt** | Confirm the final Costco cart ($244.89 estimated) and any Timeless Bakery/snacks route with actual physical receipts or structural confirmation. |",
"| P0 | 🟡 AWAITING PROOF | **Provide Food/Costco Receipt** | Confirm the final Costco cart ($244.89 estimated) and any Timeless Bakery/snacks route with actual physical receipts or structural confirmation. |")

with open(filepath, "w") as f:
    f.write(content)
