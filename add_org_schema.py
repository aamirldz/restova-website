import json

def update_homepage(filepath, is_ar):
    with open(filepath, "r") as f:
        html = f.read()
        
    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": "{{CANONICAL_DOMAIN}}/#organization",
        "name": "Restova",
        "url": "{{CANONICAL_DOMAIN}}/",
        "logo": "{{CANONICAL_DOMAIN}}/images/logo.png",
        "founder": {
            "@type": "Person",
            "name": "Aamir Akwar Ali",
            "@id": "{{CANONICAL_DOMAIN}}/about/aamir-akwar-ali/#person"
        }
    }
    
    script_tag = f'\n    <script type="application/ld+json">\n{json.dumps(schema, indent=4)}\n    </script>\n</head>'
    
    if "Organization" not in html:
        html = html.replace("</head>", script_tag)
        with open(filepath, "w") as f:
            f.write(html)

update_homepage("public/index.html", False)
update_homepage("public/ar/index.html", True)
print("Organization schema injected.")
