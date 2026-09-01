import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace the hidden state
old_hidden = """/* Hidden by default */
.cpt-stand, .cpt-base {
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
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}"""

css = css.replace(old_hidden, new_hidden)

# Replace the revealed state
old_reveal = """/* Reveal the real Stand and Base elements */
.morph-to-desktop .cpt-stand {
    opacity: 1;
    height: 30px !important;
}
.morph-to-desktop .cpt-base {
    opacity: 1;
    height: 8px !important;
}"""

new_reveal = """/* Reveal the real Stand and Base elements */
.morph-to-desktop .cpt-stand {
    position: relative !important;
    visibility: visible;
    opacity: 1;
    height: 30px !important;
}
.morph-to-desktop .cpt-base {
    position: relative !important;
    visibility: visible;
    opacity: 1;
    height: 8px !important;
}"""

css = css.replace(old_reveal, new_reveal)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Updated CSS to prevent cutout rendering bugs")
