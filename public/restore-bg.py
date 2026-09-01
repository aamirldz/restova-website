import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Remove the #hero override that set the slate background
css = re.sub(r'#hero\s*\{\s*background:\s*#f8fafc\s*!important;[^}]*\}', '', css)

# Remove the #hero::before override that added the subtle glow
css = re.sub(r'#hero::before\s*\{[^}]*\}', '', css)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Restored original background")
