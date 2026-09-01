with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace emails
content = content.replace('support@restova.com', 'aamirldz07@gmail.com')

# Replace phone/whatsapp
old_wa = '<a href="https://wa.me/919395256576" target="_blank">WhatsApp</a>'
new_wa = '<a href="https://wa.me/919939525676" target="_blank">+91 9939525676</a>'
content = content.replace(old_wa, new_wa)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Updated contact information")
