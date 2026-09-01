import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace .pnl-stand definition
old_stand = """.pnl-stand {
    width: 80px;
    height: 30px;
    background: linear-gradient(180deg, #d4d4d8, #a1a1aa);
    margin: 0 auto;
    clip-path: polygon(15% 0%, 85% 0%, 100% 100%, 0% 100%);
}"""

# Use standard border-based trapezoid to completely bypass Safari's clip-path rendering bug
new_stand = """.pnl-stand {
    width: 80px;
    height: 0;
    border-bottom: 30px solid #b0b0b5;
    border-left: 12px solid transparent;
    border-right: 12px solid transparent;
    margin: 0 auto;
    background: transparent;
    transform: translateZ(0);
}"""

css = css.replace(old_stand, new_stand)

# Since height is now 0 (the height comes from border-bottom), we must update the morph reveal heights
old_reveal = """/* Reveal the real Stand and Base elements */
.morph-to-desktop .cpt-stand {
    position: relative !important;
    visibility: visible;
    opacity: 1;
    height: 30px !important;
}"""

new_reveal = """/* Reveal the real Stand and Base elements */
.morph-to-desktop .cpt-stand {
    position: relative !important;
    visibility: visible;
    opacity: 1;
    height: 0 !important;
    border-bottom-width: 30px !important;
}"""
css = css.replace(old_reveal, new_reveal)

# And the hidden state for cpt-stand
old_hidden = """/* Hidden by default */
.cpt-stand, .cpt-base {
    position: absolute;
    visibility: hidden;
    opacity: 0;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}"""

new_hidden = """/* Hidden by default */
.cpt-stand, .cpt-base {
    position: absolute;
    visibility: hidden;
    opacity: 0;
    height: 0 !important;
    border-bottom-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}"""
css = css.replace(old_hidden, new_hidden)


with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Removed clip-path and replaced with border trapezoid")
