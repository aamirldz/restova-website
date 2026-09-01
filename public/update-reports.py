import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Shared reports block
reports_block = """<li>⬇ GST Excel Exports</li>
                    <li>⬇ Exec Summary Reports</li>
                    <li>⬇ Daily/Weekly/Monthly Reports</li>"""

# Update Starter
starter_new = f"""<ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>1</strong> Kitchen Display</li>
                    <li><strong>1</strong> Captain App</li>
                    {reports_block}
                    <li>Email Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li><strong>1</strong> POS Terminal.*?Email Support</li>\s*</ul>', 
    starter_new, 
    content, 
    flags=re.DOTALL
)

# Update Growth
growth_new = f"""<ul class="price-features">
                    <li><strong>1</strong> POS Terminal</li>
                    <li><strong>2</strong> Kitchen Displays</li>
                    <li><strong>3</strong> Captain Apps</li>
                    {reports_block}
                    <li>Email &amp; Phone Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li><strong>1</strong> POS Terminal.*?Email &amp; Phone Support</li>\s*</ul>', 
    growth_new, 
    content, 
    flags=re.DOTALL
)

# Update Enterprise
enterprise_new = f"""<ul class="price-features">
                    <li><strong>3</strong> POS Terminals</li>
                    <li><strong>5</strong> Kitchen Displays</li>
                    <li><strong>8</strong> Captain Apps</li>
                    {reports_block}
                    <li>Priority Support</li>
                </ul>"""
content = re.sub(
    r'<ul class="price-features">\s*<li><strong>3</strong> POS Terminals.*?Priority 24/7 Support</li>\s*</ul>', 
    enterprise_new, 
    content, 
    flags=re.DOTALL
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Updated pricing reports and support")
