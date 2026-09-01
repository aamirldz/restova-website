import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

correct_pricing = """<div class="pricing-cards reveal">
            <div class="price-card">
                <div class="price-plan">Starter</div>
                <div class="price-amount">₹850</div>
                <div class="price-period">per month</div>
                <div class="price-desc">For small restaurants getting started</div>
                <ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>1</strong> Kitchen Display</li>
                    <li><strong>1</strong> Captain App</li>
                    <li>⬇ GST Excel Exports</li>
                    <li>⬇ Exec Summary Reports</li>
                    <li>⬇ Daily/Weekly/Monthly Reports</li>
                    <li>Email Support</li>
                </ul>
                <a href="#register" class="btn-secondary btn-block">Get Started</a>
            </div>
            <div class="price-card featured">
                <div class="price-badge">Most Popular</div>
                <div class="price-plan">Growth</div>
                <div class="price-amount">₹1,250</div>
                <div class="price-period">per month</div>
                <div class="price-desc">For growing restaurants with teams</div>
                <ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>2</strong> Kitchen Displays</li>
                    <li><strong>3</strong> Captain Apps</li>
                    <li>⬇ GST Excel Exports</li>
                    <li>⬇ Exec Summary Reports</li>
                    <li>⬇ Daily/Weekly/Monthly Reports</li>
                    <li>Email &amp; Phone Support</li>
                </ul>
                <a href="#register" class="btn-primary btn-block">Get Started</a>
            </div>
            <div class="price-card">
                <div class="price-plan">Enterprise</div>
                <div class="price-amount">₹3,999</div>
                <div class="price-period">per month</div>
                <div class="price-desc">For multi-outlet chains</div>
                <ul class="price-features">
                    <li><strong>3</strong> POS Terminals</li>
                    <li><strong>5</strong> Kitchen Displays</li>
                    <li><strong>8</strong> Captain Apps</li>
                    <li>⬇ GST Excel Exports</li>
                    <li>⬇ Exec Summary Reports</li>
                    <li>⬇ Daily/Weekly/Monthly Reports</li>
                    <li>Priority Support</li>
                </ul>
                <a href="#register" class="btn-secondary btn-block">Contact Sales</a>
            </div>
        </div>"""

content = re.sub(
    r'<div class="pricing-cards reveal">.*?</div>\s*</div>\s*</div>\s*</section>', 
    correct_pricing + '\n    </div>\n</section>', 
    content, 
    flags=re.DOTALL
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Restored and fixed pricing cards")
