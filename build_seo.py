import json
import os
import glob

def build():
    print("SEO Build Phase 3: Starting...")
    with open("seo.config.json", "r") as f:
        config = json.load(f)
        
    domain = config["canonical_domain"].rstrip("/")
    route_groups = config.get("route_groups", [])
    
    # 1. Update HTML files
    html_files = glob.glob("public/**/*.html", recursive=True)
    for filepath in html_files:
        if "mock-" in filepath or "404" in filepath:
            continue
            
        # Determine route id and lang
        # public/index.html -> home, en
        # public/ar/index.html -> home, ar
        # public/pos/index.html -> pos, en
        # public/ar/pos/index.html -> pos, ar
        
        parts = filepath.split("/")
        if len(parts) == 2 and parts[1] == "index.html":
            group_id = "home"
            lang = "en"
        elif len(parts) == 3 and parts[1] == "ar" and parts[2] == "index.html":
            group_id = "home"
            lang = "ar"
        elif len(parts) == 3 and parts[2] == "index.html":
            group_id = parts[1]
            lang = "en"
        elif len(parts) == 4 and parts[1] == "ar" and parts[3] == "index.html":
            group_id = parts[2]
            lang = "ar"
        else:
            continue
            
        # Find the route group
        group = next((g for g in route_groups if g["id"] == group_id), None)
        if not group:
            continue
            
        # Build hreflang tags
        hreflang_tags = []
        if "en" in group:
            url_en = domain + group["en"]
            hreflang_tags.append(f'<link rel="alternate" hreflang="en" href="{url_en}">')
        if "ar" in group:
            url_ar = domain + group["ar"]
            hreflang_tags.append(f'<link rel="alternate" hreflang="ar" href="{url_ar}">')
        if "x-default" in group:
            x_lang = group["x-default"]
            url_x = domain + group[x_lang]
            hreflang_tags.append(f'<link rel="alternate" hreflang="x-default" href="{url_x}">')
            
        hreflang_block = "\n    ".join(hreflang_tags)
        
        # Determine language switcher URL
        other_lang = "ar" if lang == "en" else "en"
        lang_switch_url = group.get(other_lang, "/")
        
        with open(filepath, "r") as f:
            content = f.read()
            
        # Replace placeholders
        content = content.replace("{{CANONICAL_DOMAIN}}", domain)
        content = content.replace("{{HREFLANG_TAGS}}", hreflang_block)
        content = content.replace("{{LANG_SWITCH_URL}}", lang_switch_url)
        
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated metadata in {filepath}")
            
    # 2. Generate robots.txt
    robots_path = "public/robots.txt"
    robots_content = "User-agent: *\n"
    for path in config.get("disallowed_paths", []):
        robots_content += f"Disallow: {path}\n"
    robots_content += f"\nSitemap: {domain}/sitemap.xml\n"
    with open(robots_path, "w") as f:
        f.write(robots_content)
    print("Generated public/robots.txt")
        
    # 3. Generate sitemap.xml
    sitemap_path = "public/sitemap.xml"
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for group in route_groups:
        priority = group.get("priority", "0.5")
        changefreq = group.get("changefreq", "weekly")
        
        for lang_key in ["en", "ar"]:
            if lang_key in group:
                url = domain + group[lang_key]
                sitemap_content += '  <url>\n'
                sitemap_content += f'    <loc>{url}</loc>\n'
                sitemap_content += f'    <changefreq>{changefreq}</changefreq>\n'
                sitemap_content += f'    <priority>{priority}</priority>\n'
                sitemap_content += '  </url>\n'
        
    sitemap_content += '</urlset>\n'
    
    with open(sitemap_path, "w") as f:
        f.write(sitemap_content)
    print("Generated public/sitemap.xml")
    
    print("SEO Build Phase 3: Complete.")

if __name__ == "__main__":
    build()
