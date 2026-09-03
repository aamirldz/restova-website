import os
import glob
import json

old_domain = "https://restova.com"
new_domain = "https://restova.aamirakwarali.com.np"

# Update seo.config.json
with open("seo.config.json", "r") as f:
    config = json.load(f)
if config.get("canonical_domain") == old_domain:
    config["canonical_domain"] = new_domain
with open("seo.config.json", "w") as f:
    json.dump(config, f, indent=4)
print("Updated seo.config.json")

# Update all HTML files in public/
html_files = glob.glob("public/**/*.html", recursive=True)
count = 0
for filepath in html_files:
    with open(filepath, "r") as f:
        content = f.read()
    if old_domain in content:
        content = content.replace(old_domain, new_domain)
        with open(filepath, "w") as f:
            f.write(content)
        count += 1
print(f"Updated {count} HTML files.")

