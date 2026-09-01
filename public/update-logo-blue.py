import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace the previous dark blue gradient with the exact logo blue
old_grad = "background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%) !important; /* Deep Navy to Rich Dark Blue */"
new_grad = "background: linear-gradient(135deg, #202040 0%, #000080 100%) !important; /* Logo Exact Dark Blue */"

if old_grad in css:
    css = css.replace(old_grad, new_grad)
else:
    # Append if not found
    css += "\n#hero { background: linear-gradient(135deg, #202040 0%, #000080 100%) !important; }\n"

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Applied exact logo dark blue")
