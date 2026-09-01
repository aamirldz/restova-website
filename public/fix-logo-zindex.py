with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

content = content.replace(
    'position: static !important; transform: none !important;">',
    'position: static !important; transform: none !important; z-index: 9999 !important; object-fit: contain !important;">'
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
