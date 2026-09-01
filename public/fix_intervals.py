import re
with open('/Users/aamirakwarali/Desktop/restova-website/public/main.js', 'r') as f:
    js = f.read()

# Replace global workflowInterval references with container-specific ones
js = js.replace('let workflowInterval;', '')
js = js.replace('clearInterval(workflowInterval);', 'const container = currentStep.closest(".workflow-container"); if(container.workflowInterval) clearInterval(container.workflowInterval);')

js = js.replace('workflowInterval = setInterval(() => {', 'container.workflowInterval = setInterval(() => {')

# Also fix the switchWorkflow 'stop' condition
js = js.replace('} else {\\n        clearInterval(workflowInterval);\\n    }', '} else {\\n        const container = stepEl.closest(".workflow-container");\\n        if(container && container.workflowInterval) clearInterval(container.workflowInterval);\\n    }')

with open('/Users/aamirakwarali/Desktop/restova-website/public/main.js', 'w') as f:
    f.write(js)
print("Intervals fixed")
