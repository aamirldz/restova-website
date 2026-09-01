import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

old_header = """<div class="section-header reveal">
            <span class="section-eyebrow">Products</span>
            <h2 class="section-title">Three products.<br>One connected system.</h2>
            <p class="section-subtitle">Each product handles a critical part of restaurant operations. Together, they eliminate paper tickets, shouting across rooms, and lost orders.</p>
        </div>"""

new_header = """<div class="section-header reveal" style="margin-bottom: 20px;">
            <h2 class="section-title">Products</h2>
        </div>"""

content = content.replace(old_header, new_header)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Updated Products header text")
