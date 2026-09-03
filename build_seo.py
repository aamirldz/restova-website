import json
import os
import glob

def build():
    print("SEO Build: Starting...")
    with open("seo.config.json", "r") as f:
        config = json.load(f)
        
    domain = config["canonical_domain"].rstrip("/")
    
    # 1. Update HTML files
    html_files = glob.glob("public/**/*.html", recursive=True)
    for filepath in html_files:
        with open(filepath, "r") as f:
            content = f.read()
            
        # Replace template tags if they exist
        new_content = content.replace("{{CANONICAL_DOMAIN}}", domain)
        
        if content != new_content:
            with open(filepath, "w") as f:
                f.write(new_content)
            print(f"Updated domain in {filepath}")
            
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
    
    for route in config.get("public_routes", []):
        path = route["path"].lstrip("/")
        url = f"{domain}/{path}"
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{url}</loc>\n'
        sitemap_content += f'    <changefreq>{route["changefreq"]}</changefreq>\n'
        sitemap_content += f'    <priority>{route["priority"]}</priority>\n'
        sitemap_content += '  </url>\n'
        
    sitemap_content += '</urlset>\n'
    
    with open(sitemap_path, "w") as f:
        f.write(sitemap_content)
    print("Generated public/sitemap.xml")
    
    print("SEO Build: Complete.")

if __name__ == "__main__":
    build()
