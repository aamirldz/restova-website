import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace padding: 60px to 40px for maximum compactness without looking crushed
css = css.replace("padding: 60px 0 !important;", "padding: 40px 0 !important;")
css = css.replace("padding: 24px !important; /* Less internal padding */", "padding: 20px !important;")

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Made it even tighter")
