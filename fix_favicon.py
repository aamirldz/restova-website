import glob
import re

html_files = glob.glob("public/**/*.html", recursive=True)
count = 0

old_fav = '<link rel="icon" href="/favicon.ico">'
new_fav = '<link rel="icon" type="image/x-icon" href="/favicon.ico">\n    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">'

for filepath in html_files:
    with open(filepath, "r") as f:
        content = f.read()
        
    if old_fav in content:
        content = content.replace(old_fav, new_fav)
        with open(filepath, "w") as f:
            f.write(content)
        count += 1
    elif "favicon" not in content and "</head>" in content:
        # Fallback if it's missing entirely
        head_tag = '<!-- Favicon -->\n    ' + new_fav + '\n    <link rel="apple-touch-icon" href="/logo.png">\n</head>'
        content = content.replace("</head>", head_tag)
        with open(filepath, "w") as f:
            f.write(content)
        count += 1

print(f"Updated favicons in {count} HTML files.")
