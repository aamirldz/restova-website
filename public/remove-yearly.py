import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Remove yearly billing line using regex
content = re.sub(r'<strong>Billed ₹[0-9,]+ yearly</strong><br>', '', content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Removed yearly billing text")
