import os
import glob
import shutil

# Dictionary mapping old filename to new filename
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

images_dir = "public/images"

# Rename files in the images directory
for old_name, new_name in image_map.items():
    old_path = os.path.join(images_dir, old_name)
    new_path = os.path.join(images_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

# Move and rename founder photo
founder_old = "public/aamir.jpeg"
founder_new = "public/images/aamir-akwar-ali-restova-founder.jpeg"
if os.path.exists(founder_old):
    shutil.move(founder_old, founder_new)
    print("Moved and renamed founder photo.")
    
