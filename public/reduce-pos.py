import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace steps
old_steps = """<div class="w-step active" data-img="wf-1" onclick="switchWorkflow(this)">
                            <h4>1. Table Management</h4>
                            <p>Select an available table and monitor floor status with live timers and bill amounts.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-2" onclick="switchWorkflow(this)">
                            <h4>2. Order & Billing</h4>
                            <p>Punch items instantly. Taxes and totals auto-calculate flawlessly.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-3" onclick="switchWorkflow(this)">
                            <h4>3. KOT</h4>
                            <p>Send tickets directly to the kitchen with one tap.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-4" onclick="switchWorkflow(this)">
                            <h4>4. KDS Sync</h4>
                            <p>Watch orders appear instantly on the kitchen display system.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-5" onclick="switchWorkflow(this)">
                            <h4>5. Settle Bill</h4>
                            <p>Split bills, apply discounts, and accept any payment method.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-6" onclick="switchWorkflow(this)">
                            <h4>6. Sales History</h4>
                            <p>Track all completed orders and daily revenue seamlessly.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>"""

new_steps = """<div class="w-step active" data-img="wf-1" onclick="switchWorkflow(this)">
                            <h4>1. Tables & Orders</h4>
                            <p>Select tables and punch items instantly. Taxes auto-calculate.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-2" onclick="switchWorkflow(this)">
                            <h4>2. Instant KOTs</h4>
                            <p>Send tickets directly to the kitchen display with one tap.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-3" onclick="switchWorkflow(this)">
                            <h4>3. Fast Billing</h4>
                            <p>Split bills, apply discounts, and accept any payment method.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>
                        <div class="w-step" data-img="wf-4" onclick="switchWorkflow(this)">
                            <h4>4. Sales Tracking</h4>
                            <p>Track daily revenue and completed orders seamlessly.</p>
                            <div class="w-step-progress"><div class="w-step-progress-bar"></div></div>
                        </div>"""

content = content.replace(old_steps, new_steps)

# Replace Images
old_images = """<img src="images/wf-1-table.png" id="wf-1" class="active contain-img" alt="POS 1">
                                <img src="images/wf-2-billing.png" id="wf-2" class="contain-img" alt="POS 2">
                                <img src="images/wf-3-kot.png" id="wf-3" class="contain-img" alt="POS 3">
                                <img src="images/wf-4-kds.png" id="wf-4" class="contain-img" alt="POS 4">
                                <img src="images/wf-5-settle.png" id="wf-5" class="contain-img" alt="POS 5">
                                <img src="images/wf-6-sales.png" id="wf-6" class="contain-img" alt="POS 6">"""

new_images = """<img src="images/wf-2-billing.png" id="wf-1" class="active contain-img" alt="POS 1">
                                <img src="images/wf-3-kot.png" id="wf-2" class="contain-img" alt="POS 2">
                                <img src="images/wf-5-settle.png" id="wf-3" class="contain-img" alt="POS 3">
                                <img src="images/wf-6-sales.png" id="wf-4" class="contain-img" alt="POS 4">"""

content = content.replace(old_images, new_images)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Reduced POS steps to 4")
