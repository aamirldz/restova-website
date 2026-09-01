import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

old_html = """<div class="workflow-visual phone-logo-screen">
                            <img src="logo.png" alt="Restova App" class="app-logo">
                            <span class="app-name">Restova POS</span>
                        </div>"""

new_html = """<div class="workflow-visual phone-logo-screen">
                            <div class="splash-inner">
                                <img src="logo.png" alt="Restova App" class="app-logo">
                                <span class="app-name">Restova POS</span>
                            </div>
                        </div>"""

content = content.replace(old_html, new_html)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

css += """
/* Bulletproof Centering */
.phone-logo-screen {
    position: relative !important;
    background: #ffffff !important;
}

.splash-inner {
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 12px !important;
    width: 100% !important;
}

.splash-inner img.app-logo {
    position: relative !important;
    top: auto !important;
    left: auto !important;
    width: 60px !important;
    height: 60px !important;
    opacity: 1 !important;
    display: block !important;
    object-fit: contain !important;
    transform: none !important;
}

.splash-inner .app-name {
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    color: #1a1a2e !important;
    white-space: nowrap !important;
}
"""

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)

print("Applied bulletproof centering")
