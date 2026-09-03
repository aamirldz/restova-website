import re

def update_head(filepath, is_arabic):
    with open(filepath, "r") as f:
        html = f.read()

    if is_arabic:
        title = "ريستوفا — نظام نقاط البيع وإدارة المطاعم"
        desc = "ريستوفا هو نظام تشغيل المطاعم المتكامل. نظام نقاط البيع، تطبيق كابتن المطعم، وشاشة المطبخ — جميعها متصلة في الوقت الفعلي. برنامج فواتير المطاعم يعمل بدون إنترنت."
        og_title = "ريستوفا — نظام تشغيل المطاعم"
    else:
        title = "Restova — Restaurant POS & Management System"
        desc = "Restova is a complete restaurant POS and management system. Captain ordering, Kitchen Display, and billing — all connected in real time. Works offline. Built for busy Indian restaurants."
        og_title = "Restova — Restaurant Operating System"
        
    head_content = f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{{{{CANONICAL_DOMAIN}}}}{'/ar/' if is_arabic else '/'}">
    
    {{{{HREFLANG_TAGS}}}}
    
    <!-- Open Graph -->
    <meta property="og:site_name" content="Restova">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{{{{CANONICAL_DOMAIN}}}}{'/ar/' if is_arabic else '/'}">
    <meta property="og:image" content="{{{{CANONICAL_DOMAIN}}}}/images/og-image.jpg">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{{{{CANONICAL_DOMAIN}}}}/images/og-image.jpg">
    
    <!-- Favicon -->
    <link rel="icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/logo.png">
    
    <!-- Fonts & Styles -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css?v=25">
"""

    pattern = re.compile(r'<head>.*?(?=\s*<script>)', re.DOTALL)
    new_html = pattern.sub(f"<head>\n{head_content}", html)
    with open(filepath, "w") as f:
        f.write(new_html)

update_head("public/index.html", False)
update_head("public/ar/index.html", True)
print("Updated head tags")
