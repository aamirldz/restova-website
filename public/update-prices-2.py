import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Replace Starter Pricing
content = content.replace(
    '<div class="price-amount">₹999</div>',
    '<div class="price-amount">₹850</div>'
)
content = content.replace(
    '<strong>Billed ₹11,988 yearly</strong>',
    '<strong>Billed ₹10,200 yearly</strong>'
)

# Replace Growth Pricing
content = content.replace(
    '<div class="price-amount">₹1,333</div>',
    '<div class="price-amount">₹1,250</div>'
)
content = content.replace(
    '<strong>Billed ₹15,996 yearly</strong>',
    '<strong>Billed ₹15,000 yearly</strong>'
)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)
print("Updated pricing numbers to 850 and 1250")
