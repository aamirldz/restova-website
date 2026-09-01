import re

# Fix HTML
with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()
content = content.replace('src="/logo.png" alt="Restova App" class="app-logo"', 'src="logo.png" alt="Restova App" class="app-logo"')
with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)


# Fix CSS
with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

bad_css = """.phone-logo-screen {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    background: #ffffff !important;
    gap: 12px !important;
    z-index: 20;
}"""

good_css = """.phone-logo-screen {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    background: #ffffff !important;
    gap: 12px !important;
    z-index: 20;
}"""

css = css.replace(bad_css, good_css)

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)

print("Fixed CSS and HTML for phone logo screen")
