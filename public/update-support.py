import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace Starter support
content = content.replace('<li>Email Support</li>', '<li>WhatsApp &amp; Phone Call Support</li>')

# Replace Growth support
content = content.replace('<li>Email &amp; Phone Support</li>', '<li>WhatsApp &amp; Phone Call Support</li>')

# Replace Enterprise support
content = content.replace('<li>Priority Support</li>', '<li>WhatsApp &amp; Phone Call Support</li>')

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Updated support lines in pricing")
