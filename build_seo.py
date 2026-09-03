import json
import os
import glob
import re

def build():
    print("SEO Build Phase 4: Starting...")
    with open("seo.config.json", "r") as f:
        config = json.load(f)
        
    domain = config["canonical_domain"].rstrip("/")
    route_groups = config.get("route_groups", [])
    
    # Store images found per URL for the image sitemap
    url_images = {}
    
    # 1. Update HTML files
    html_files = glob.glob("public/**/*.html", recursive=True)
    for filepath in html_files:
        if "mock-" in filepath or "404" in filepath:
            continue
            
        parts = filepath.split("/")
        # public/index.html
        # public/ar/index.html
        # public/pos/index.html
        # public/ar/pos/index.html
        # public/about/aamir-akwar-ali/index.html
        # public/ar/about/aamir-akwar-ali/index.html
        
        # We need a robust way to match route group
        route_url = filepath.replace("public", "").replace("index.html", "")
        if route_url == "":
            route_url = "/"
            
        matched_group = None
        matched_lang = None
        
        for group in route_groups:
            if group.get("en") == route_url:
                matched_group = group
                matched_lang = "en"
                break
            elif group.get("ar") == route_url:
                matched_group = group
                matched_lang = "ar"
                break
                
        if not matched_group:
            continue
            
        group = matched_group
        lang = matched_lang
        
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
        other_lang = "ar" if lang == "en" else "en"
        lang_switch_url = group.get(other_lang, "/")
        
        with open(filepath, "r") as f:
            content = f.read()
            
        content = content.replace("{{CANONICAL_DOMAIN}}", domain)
        content = content.replace("{{HREFLANG_TAGS}}", hreflang_block)
        content = content.replace("{{LANG_SWITCH_URL}}", lang_switch_url)
        
        # Find images for sitemap (only public/images/)
        imgs = re.findall(r'<img[^>]+src=["\'](/images/[^"\']+)["\'][^>]*>', content)
        # Exclude logo and og-image if desired, or keep them. Let's keep product/founder images.
        important_imgs = [domain + img for img in imgs if "og-image" not in img and "logo" not in img]
        
        full_url = domain + route_url
        if important_imgs:
            url_images[full_url] = important_imgs
        
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
        
    # 3. Generate sitemap.xml with image extension
    sitemap_path = "public/sitemap.xml"
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    
    for group in route_groups:
        priority = group.get("priority", "0.5")
        changefreq = group.get("changefreq", "weekly")
        
        for lang_key in ["en", "ar"]:
            if lang_key in group:
                url = domain + group[lang_key]
                sitemap_content += '  <url>\n'
                sitemap_content += f'    <loc>{url}</loc>\n'
                
                # Insert images if any
                if url in url_images:
                    # Deduplicate images for this URL
                    for img_loc in list(set(url_images[url])):
                        sitemap_content += f'    <image:image>\n      <image:loc>{img_loc}</image:loc>\n    </image:image>\n'
                        
                sitemap_content += f'    <changefreq>{changefreq}</changefreq>\n'
                sitemap_content += f'    <priority>{priority}</priority>\n'
                sitemap_content += '  </url>\n'
        
    sitemap_content += '</urlset>\n'
    
    with open(sitemap_path, "w") as f:
        f.write(sitemap_content)
    print("Generated public/sitemap.xml with image nodes.")
    
    print("SEO Build Phase 4: Complete.")

if __name__ == "__main__":
    build()
