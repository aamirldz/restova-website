import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace the previous bluish-white gradient with a richer blue
old_grad = "background: linear-gradient(135deg, #f0f5ff 0%, #e0eaff 50%, #c2d6ff 100%) !important;"
new_grad = "background: linear-gradient(135deg, #e0eaff 0%, #bfdbfe 40%, #93c5fd 100%) !important;"

css = css.replace(old_grad, new_grad)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Applied richer blue gradient")
