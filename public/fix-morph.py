import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Remove the buggy pseudo-element CSS
css = re.sub(r'/\* Base state for pseudo-elements.*?/\* The Morphed State \*/', '/* The Morphed State */', css, flags=re.DOTALL)
css = re.sub(r'/\* Reveal the Stand and Base \*/.*?(?=/\* Also reset)', '', css, flags=re.DOTALL)

# Add the new reliable flex-based CSS
new_css = """
#captainDevice {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

/* Hidden by default */
.cpt-stand, .cpt-base {
    opacity: 0;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

/* The Morphed State */
.morph-to-desktop {
    width: 100% !important;
}
.morph-to-desktop .pnl-bezel {
    width: 100% !important;
    max-width: 800px;
    border-radius: 12px !important;
    padding: 8px 8px 24px 8px !important;
}
.morph-to-desktop .workflow-visual {
    aspect-ratio: 16 / 10 !important;
    border-radius: 4px !important;
}
.morph-to-desktop .pnl-notch,
.morph-to-desktop .pnl-home-bar {
    opacity: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Reveal the real Stand and Base elements */
.morph-to-desktop .cpt-stand {
    opacity: 1;
    height: 30px !important;
}
.morph-to-desktop .cpt-base {
    opacity: 1;
    height: 8px !important;
}
"""

css = css.replace('/* The Morphed State */', new_css)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Updated CSS")
