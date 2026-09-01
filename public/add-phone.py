import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

phone_html = """
            <!-- Pocket Phone -->
            <div class="owner-pocket-phone">
                <div class="pnl-device pnl-phone">
                    <div class="pnl-bezel">
                        <div class="pnl-cam"></div>
                        <div class="workflow-visual">
                            <img src="images/owner-dashboard.png" id="o-phone-img-1" class="active contain-img" alt="Live Dashboard" loading="lazy">
                            <img src="images/owner-menu.png" id="o-phone-img-2" class="contain-img" alt="Menu Management" loading="lazy">
                            <img src="images/owner-report.png" id="o-phone-img-3" class="contain-img" alt="Deep Reporting" loading="lazy">
                            <img src="images/owner-setting.png" id="o-phone-img-4" class="contain-img" alt="Remote Settings" loading="lazy">
                        </div>
                        <div class="pnl-home"></div>
                    </div>
                </div>
            </div>
"""

content = content.replace('<div class="monitor-base"></div>\n            </div>', '<div class="monitor-base"></div>\n            </div>\n' + phone_html)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/main.js', 'r') as f:
    js_content = f.read()

# Update JS to handle phone images
js_content = js_content.replace(
    "document.querySelectorAll('.monitor-screen img').forEach(img => {",
    "document.querySelectorAll('.monitor-screen img, .owner-pocket-phone img').forEach(img => {"
)
js_content = js_content.replace(
    "if (targetImg) targetImg.classList.add('active');",
    "if (targetImg) targetImg.classList.add('active');\n    const targetPhoneImg = document.getElementById('o-phone-img-' + stepNum);\n    if (targetPhoneImg) targetPhoneImg.classList.add('active');"
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/main.js', 'w') as f:
    f.write(js_content)

print("Added phone HTML and updated JS")
