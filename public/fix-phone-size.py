import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace the 340px width rule
old_width = """.pnl-phone .pnl-bezel {
    width: 340px !important; /* increased from 280px */
}"""

new_width = """.pnl-phone .pnl-bezel {
    width: 270px !important; /* Decreased to prevent it from being massively tall */
}"""

css = css.replace(old_width, new_width)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Updated phone width to 270px")
