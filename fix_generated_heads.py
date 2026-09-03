import glob
import re

html_files = glob.glob("public/**/*.html", recursive=True)
for filepath in html_files:
    if filepath in ["public/index.html", "public/ar/index.html", "public/404.html"] or "mock-" in filepath:
        continue

    with open(filepath, "r") as f:
        html = f.read()

    # Determine if it's arabic
    is_ar = "/ar/" in filepath
    # Extract route (e.g. public/pos/index.html -> pos, public/ar/pos/index.html -> pos)
    parts = filepath.split("/")
    route = parts[-2]
    
    canonical_suffix = f"/ar/{route}/" if is_ar else f"/{route}/"

    # Replace the canonical tag block entirely, including the hardcoded hreflang tags
    # The existing template block looks roughly like:
    # <link rel="canonical" href="...">
    # <link rel="alternate" ...>
    # <link rel="alternate" ...>
    # <link rel="alternate" ...>
    
    # Let's just use regex to strip out everything between <title> and <!-- Open Graph --> 
    # and replace it with the fresh placeholders.
    
    replacement = f"""</title>
    <link rel="canonical" href="{{{{CANONICAL_DOMAIN}}}}{canonical_suffix}">
    
    {{{{HREFLANG_TAGS}}}}
    
    <!-- Open Graph -->
    <meta property="og:url" content="{{{{CANONICAL_DOMAIN}}}}{canonical_suffix}">
"""
    
    html = re.sub(r'</title>.*?<!-- Open Graph -->', replacement, html, flags=re.DOTALL)
    
    # Fix the og:url duplication just in case
    # The template has og:url twice now? No, we replaced the first chunk up to <!-- Open Graph -->.
    # But wait, og:url comes AFTER <!-- Open Graph -->.
    # Let's fix og:url explicitly.
    html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{{{{CANONICAL_DOMAIN}}}}{canonical_suffix}">', html)

    with open(filepath, "w") as f:
        f.write(html)
        
print("Fixed headers in generated files.")
