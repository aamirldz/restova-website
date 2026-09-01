import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<img src="logo.png" alt="Restova App" class="app-logo">',
    '<img src="/logo.png" alt="Restova App" class="app-logo" style="opacity: 1 !important; visibility: visible !important; display: block !important; width: 60px !important; height: 60px !important; position: static !important; transform: none !important;">'
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Forced logo styles inline in HTML")
