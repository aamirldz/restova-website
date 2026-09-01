import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# I'll replace the existing app-logo inline styles entirely
pattern = r'<img src="/logo.png" alt="Restova App" class="app-logo"[^>]*>'
new_img = '<img src="/logo.png" alt="Restova App" class="app-logo active" style="opacity: 1 !important; visibility: visible !important; display: block !important; width: 90px !important; height: 90px !important; position: static !important; transform: none !important; z-index: 9999 !important; object-fit: contain !important; filter: none !important;">'

content = re.sub(pattern, new_img, content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Added active class, removed blur filter, increased size")
