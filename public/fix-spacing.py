with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'r') as f:
    css = f.read()

# Fix the overly generic CSS selectors from my timeline fix
css = css.replace('.workflow-steps {\\n    position: relative;\\n    display: flex;\\n    flex-direction: column;\\n    gap: 60px !important;\\n}', 
                  '.workflow-track .workflow-steps {\\n    position: relative;\\n    display: flex;\\n    flex-direction: column;\\n    gap: 60px !important;\\n}')

css = css.replace('.workflow-step {\\n    display: flex !important;',
                  '.workflow-track .workflow-step {\\n    display: flex !important;')

css = css.replace('.workflow-step.active {\\n    opacity: 1 !important;',
                  '.workflow-track .workflow-step.active {\\n    opacity: 1 !important;')

with open('/Users/aamirakwarali/Desktop/restova-website/public/style.css', 'w') as f:
    f.write(css)
print("Fixed CSS selectors")
