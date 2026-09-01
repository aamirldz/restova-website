import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace Starter UL
starter_ul = """<ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>1</strong> Kitchen Display</li>
                    <li><strong>1</strong> Captain App</li>
                    <li>Standard Reports</li>
                    <li>Email Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li>1 POS Terminal.*?</ul>', 
    starter_ul, 
    content, 
    flags=re.DOTALL
)

# Replace Growth UL
growth_ul = """<ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>2</strong> Kitchen Displays</li>
                    <li><strong>3</strong> Captain Apps</li>
                    <li>Advanced Reports</li>
                    <li>Email &amp; Phone Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li><strong>3 POS Terminals.*?</ul>', 
    growth_ul, 
    content, 
    flags=re.DOTALL
)

# Replace Enterprise UL
enterprise_ul = """<ul class="price-features">
                    <li><strong>3</strong> POS Terminals</li>
                    <li><strong>5</strong> Kitchen Displays</li>
                    <li><strong>8</strong> Captain Apps</li>
                    <li>Executive Reports</li>
                    <li>Priority 24/7 Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li><strong>Unlimited Terminals.*?</ul>', 
    enterprise_ul, 
    content, 
    flags=re.DOTALL
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Updated pricing cards")
