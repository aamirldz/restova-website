import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Replace all old aspect ratios with EXACT image aspect ratios so nothing ever gets cropped
css += """
/* ═══════════════════════════════════════════════
   FIX: EXACT ASPECT RATIOS TO PREVENT IMAGE CROPPING
   ═══════════════════════════════════════════════ */
.pnl-desktop .workflow-visual {
    aspect-ratio: 2934 / 1838 !important;
}
.pnl-phone .workflow-visual {
    aspect-ratio: 1220 / 2712 !important;
}
.pnl-tablet .workflow-visual {
    aspect-ratio: 2940 / 1840 !important;
}
"""

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Applied exact aspect ratios")
