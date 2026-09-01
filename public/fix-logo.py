import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<span class="app-name">Restova Owner</span>', 
    '<span class="app-name">Restova POS</span>'
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Updated text to Restova POS")
