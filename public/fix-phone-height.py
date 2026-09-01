with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

css = css.replace("height: 100% !important;\n", "")

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)

print("Removed height: 100% to protect aspect ratio")
