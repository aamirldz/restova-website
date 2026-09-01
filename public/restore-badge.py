import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Remove the .hero-badge override
css = re.sub(r'\.hero-badge\s*\{[^}]*\}', '', css)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Restored original hero badge")
