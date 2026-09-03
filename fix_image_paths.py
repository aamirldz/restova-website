import glob
import os

image_map = {
    "wf-1-table.png": "restova-pos-table-management.png",
    "wf-2-billing.png": "restova-pos-billing.png",
    "wf-5-settle.png": "restova-pos-settlement.png",
    "cpt-1.png": "restova-captain-app-ordering.png",
    "kds-1.png": "restova-kitchen-display-system.png",
    "owner-dashboard.png": "restova-owner-dashboard.png",
    "owner-report.png": "restova-restaurant-management-dashboard.png",
    "owner-menu.png": "restova-restaurant-menu-management.png",
    "wf-6-sales.png": "restova-offline-pos-sync.png",
    "wf-4-kds.png": "restova-real-time-sync.png",
    "aamir.jpeg": "aamir-akwar-ali-restova-founder.jpeg"
}

files_to_check = glob.glob("public/**/*.html", recursive=True) + glob.glob("public/**/*.js", recursive=True)

count = 0
for filepath in files_to_check:
    with open(filepath, "r") as f:
        content = f.read()
        
    original = content
    for old_name, new_name in image_map.items():
        content = content.replace(old_name, new_name)
        
    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        count += 1
        print(f"Fixed {filepath}")

print(f"Updated {count} files.")
