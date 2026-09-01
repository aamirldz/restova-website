import re

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'r') as f:
    content = f.read()

# Remove the phone from its current spot (after monitor-base </div> </div>)
# Actually, let's just find and move it.
pattern = r'            <!-- Pocket Phone -->.*?</div>\s*</div>\s*</div>'
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    phone_html = match.group(0)
    # Remove it
    content = content.replace(phone_html, '')
    
    # Insert it right before the closing div of white-monitor
    insert_pattern = r'(<div class="monitor-base"></div>\n            )(</div>)'
    content = re.sub(insert_pattern, r'\1' + phone_html + r'\n            \2', content)

with open('/Users/aamirakwarali/Desktop/restova-website/public/index.html', 'w') as f:
    f.write(content)

print("Moved pocket phone inside white-monitor DOM element")
