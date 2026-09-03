import os
import json

def generate_founder_page(lang):
    is_ar = lang == "ar"
    
    # Template base
    base_src = "public/ar/index.html" if is_ar else "public/index.html"
    
    with open(base_src, "r") as f:
        base_html = f.read()
        
    # Isolate head_nav and footer_cta
    nav_end = base_html.find("</nav>") + 6
    register_start = base_html.find("<!-- REGISTER")
    if register_start == -1:
        register_start = base_html.find("<footer")
        
    head_nav = base_html[:nav_end]
    footer_cta = base_html[register_start:]
    
    # Founder specifics
    title = "Aamir Akwar Ali — Founder of Restova"
    desc = "Learn about Aamir Akwar Ali, the founder of Restova, and the restaurant technology platform built to connect POS, Captain and Kitchen operations."
    h1 = "Aamir Akwar Ali"
    h2 = "Founder / Creator of Restova"
    
    if is_ar:
        title = "عامر أكور علي — مؤسس ريستوفا"
        desc = "تعرف على عامر أكور علي، مؤسس ريستوفا، ومنصة تكنولوجيا المطاعم المصممة لربط عمليات نقاط البيع، الكابتن، والمطبخ."
        h1 = "عامر أكور علي"
        h2 = "مؤسس / منشئ ريستوفا"
        
    # Replace metadata
    import re
    head_nav = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_nav)
    head_nav = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', head_nav)
    head_nav = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', head_nav)
    head_nav = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', head_nav)
    head_nav = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title}">', head_nav)
    head_nav = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{desc}">', head_nav)
    
    # Set canonical manually so build_seo.py won't overwrite it wrong
    canonical_route = "/ar/about/aamir-akwar-ali/" if is_ar else "/about/aamir-akwar-ali/"
    head_nav = re.sub(r'</title>.*?<!-- Open Graph -->', f'</title>\n    <link rel="canonical" href="{{{{CANONICAL_DOMAIN}}}}{canonical_route}">\n    {{{{HREFLANG_TAGS}}}}\n    <!-- Open Graph -->', head_nav, flags=re.DOTALL)
    head_nav = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{{{{CANONICAL_DOMAIN}}}}{canonical_route}">', head_nav)

    # JSON-LD Person Schema
    schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": f"{{{{CANONICAL_DOMAIN}}}}{canonical_route}#person",
        "name": "Aamir Akwar Ali",
        "jobTitle": "Founder",
        "image": "{{CANONICAL_DOMAIN}}/images/aamir-akwar-ali-restova-founder.jpeg",
        "url": f"{{{{CANONICAL_DOMAIN}}}}{canonical_route}",
        "worksFor": {
            "@type": "Organization",
            "@id": "{{CANONICAL_DOMAIN}}/#organization"
        },
        "description": desc
    }
    schema_script = f'\n    <script type="application/ld+json">\n{json.dumps(schema, indent=4)}\n    </script>\n</head>'
    head_nav = head_nav.replace("</head>", schema_script)

    # Body Content
    body_en = f"""
    <section class="section section-alt" style="padding-top: 120px; padding-bottom: 80px;">
        <div class="container" style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center;">
            <img src="/images/aamir-akwar-ali-restova-founder.jpeg" alt="Aamir Akwar Ali, founder of Restova" style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h1 class="section-title" style="font-size: 3rem; margin-bottom: 10px;">{h1}</h1>
            <p class="section-subtitle" style="font-weight: 600; color: var(--primary);">{h2}</p>
            
            <div class="content" style="text-align: left; margin-top: 50px; font-size: 1.1rem; line-height: 1.8; color: var(--text-s);">
                <h3 style="color: var(--text); margin-bottom: 20px;">About</h3>
                <p>Aamir Akwar Ali is the founder and creator of <a href="/">Restova</a>, a premium restaurant operating system. Driven by a deep understanding of hospitality workflows and technology, Aamir designed Restova to solve the real operational challenges faced by modern restaurants.</p>
                
                <h3 style="color: var(--text); margin-top: 40px; margin-bottom: 20px;">The Restova Vision</h3>
                <p>The goal of Restova is to eliminate fragmentation. By unifying the <a href="/pos/">Restova POS</a>, <a href="/captain/">Captain App</a>, and <a href="/kitchen-display/">Kitchen Display System</a> into one real-time ecosystem, Aamir has built a platform that allows restaurant owners to maintain total control—even <a href="/offline-pos/">offline</a>.</p>
                
                <h3 style="color: var(--text); margin-top: 40px; margin-bottom: 20px;">Connect</h3>
                <p>Discover more about the Restova ecosystem via the <a href="/owner-dashboard/">Owner Dashboard</a> or explore the full suite of <a href="/restaurant-management/">restaurant management</a> tools.</p>
            </div>
        </div>
    </section>
    """
    
    body_ar = f"""
    <section class="section section-alt" style="padding-top: 120px; padding-bottom: 80px;">
        <div class="container" style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; text-align: center;">
            <img src="/images/aamir-akwar-ali-restova-founder.jpeg" alt="عامر أكور علي، مؤسس ريستوفا" style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h1 class="section-title" style="font-size: 3rem; margin-bottom: 10px;">{h1}</h1>
            <p class="section-subtitle" style="font-weight: 600; color: var(--primary);">{h2}</p>
            
            <div class="content" style="text-align: right; margin-top: 50px; font-size: 1.1rem; line-height: 1.8; color: var(--text-s);">
                <h3 style="color: var(--text); margin-bottom: 20px;">نبذة</h3>
                <p>عامر أكور علي هو مؤسس ومنشئ <a href="/ar/">ريستوفا</a>، نظام تشغيل المطاعم المتميز. بدافع من الفهم العميق لسير عمل الضيافة والتكنولوجيا، صمم عامر ريستوفا لحل التحديات التشغيلية الحقيقية التي تواجه المطاعم الحديثة.</p>
                
                <h3 style="color: var(--text); margin-top: 40px; margin-bottom: 20px;">رؤية ريستوفا</h3>
                <p>الهدف من ريستوفا هو القضاء على التجزئة. من خلال توحيد <a href="/ar/pos/">نظام نقاط البيع</a>، <a href="/ar/captain/">تطبيق الكابتن</a>، و <a href="/ar/kitchen-display/">شاشة المطبخ</a> في نظام بيئي واحد في الوقت الفعلي، قام عامر ببناء منصة تتيح لأصحاب المطاعم الحفاظ على السيطرة الكاملة — حتى <a href="/ar/offline-pos/">بدون إنترنت</a>.</p>
                
                <h3 style="color: var(--text); margin-top: 40px; margin-bottom: 20px;">تواصل</h3>
                <p>اكتشف المزيد حول نظام ريستوفا البيئي عبر <a href="/ar/owner-dashboard/">لوحة تحكم المالك</a> أو استكشف المجموعة الكاملة من أدوات <a href="/ar/restaurant-management/">إدارة المطاعم</a>.</p>
            </div>
        </div>
    </section>
    """
    
    target_dir = "public/ar/about/aamir-akwar-ali" if is_ar else "public/about/aamir-akwar-ali"
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "index.html")
    
    final_html = head_nav + (body_ar if is_ar else body_en) + footer_cta
    with open(target_path, "w") as f:
        f.write(final_html)
        
generate_founder_page("en")
generate_founder_page("ar")
print("Founder pages created.")
