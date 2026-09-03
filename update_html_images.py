import glob
import re

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
    "wf-4-kds.png": "restova-real-time-sync.png"
}

html_files = glob.glob("public/**/*.html", recursive=True)

for filepath in html_files:
    with open(filepath, "r") as f:
        html = f.read()
        
    # Replace filenames
    for old_name, new_name in image_map.items():
        html = html.replace(f"/images/{old_name}", f"/images/{new_name}")
        
    # Add loading="lazy" to imgs that don't have it (crude but effective)
    # We will exclude the hero image from lazy loading if possible.
    # We can just match <img ...> and ensure it has loading="lazy"
    
    # A safer way using regex to insert loading="lazy" if not present
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' not in img_tag and 'hero' not in img_tag:
            return img_tag.replace('<img ', '<img loading="lazy" ')
        return img_tag
        
    html = re.sub(r'<img [^>]*>', add_lazy, html)
    
    with open(filepath, "w") as f:
        f.write(html)
        
print("Updated all HTML files with new image paths and lazy loading.")
