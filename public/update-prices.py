import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace Starter Pricing
starter_old = r'<div class="price-amount">₹8,000</div>\s*<div class="price-period">per year</div>\s*<div class="price-desc">For small restaurants getting started</div>'
starter_new = """<div class="price-amount">₹999</div>
                <div class="price-period">per month</div>
                <div class="price-desc"><strong>Billed ₹11,988 yearly</strong><br>For small restaurants getting started</div>"""
content = re.sub(starter_old, starter_new, content)

# Replace Growth Pricing
growth_old = r'<div class="price-amount">₹18,000</div>\s*<div class="price-period">per year</div>\s*<div class="price-desc">For growing restaurants with teams</div>'
growth_new = """<div class="price-amount">₹1,333</div>
                <div class="price-period">per month</div>
                <div class="price-desc"><strong>Billed ₹15,996 yearly</strong><br>For growing restaurants with teams</div>"""
content = re.sub(growth_old, growth_new, content)

# Replace Enterprise Pricing
enterprise_old = r'<div class="price-amount">₹36,000</div>\s*<div class="price-period">per year</div>\s*<div class="price-desc">For multi-outlet chains</div>'
enterprise_new = """<div class="price-amount">₹3,999</div>
                <div class="price-period">per month</div>
                <div class="price-desc"><strong>Billed ₹47,988 yearly</strong><br>For multi-outlet chains</div>"""
content = re.sub(enterprise_old, enterprise_new, content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Updated pricing numbers")
