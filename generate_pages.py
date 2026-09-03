import os
import re

# Data structure for the pages
pages = {
    "pos": {
        "en": {
            "title": "Restova POS — Restaurant POS & Billing System",
            "desc": "Restova POS helps restaurants manage tables, orders, billing, payments and kitchen workflows from one connected system.",
            "h1": "Restova POS",
            "h2": "Run your restaurant from one place.",
            "content": """
                <p>The Restova Restaurant POS system is designed to handle the fast-paced environment of modern dining. From the moment a guest sits down to the final settlement, Restova keeps your operations smooth.</p>
                <div class="product-visual"><img src="/images/wf-2-billing.png" alt="Restova POS billing interface"></div>
                <h3>The Complete Workflow</h3>
                <p>Track everything seamlessly: Table → Order → KOT → Bill → Payment → Settlement.</p>
                <p>Connects natively with the <a href="/captain/">Captain App</a> for tableside ordering and the <a href="/kitchen-display/">Kitchen Display</a> for seamless kitchen communication. Fully <a href="/offline-pos/">offline-capable</a>.</p>
            """,
            "faq": [
                ("Does Restova support restaurant billing?", "Yes, the POS handles all aspects of restaurant billing including GST/taxes, discounts, split payments, and quick settlement."),
                ("Does Restova work offline?", "Yes, Restova POS is built offline-first. Your restaurant keeps running even when the internet drops.")
            ]
        },
        "ar": {
            "title": "نظام نقاط البيع ريستوفا — إدارة فواتير المطاعم",
            "desc": "يساعد نظام نقاط البيع ريستوفا المطاعم في إدارة الطاولات، الطلبات، الفواتير، المدفوعات، وسير عمل المطبخ من نظام واحد متصل.",
            "h1": "نظام نقاط البيع ريستوفا",
            "h2": "قم بإدارة مطعمك من مكان واحد.",
            "content": """
                <p>تم تصميم نظام نقاط البيع ريستوفا للتعامل مع بيئة المطاعم الحديثة سريعة الوتيرة. من لحظة جلوس الضيف إلى التسوية النهائية.</p>
                <div class="product-visual"><img src="/images/wf-2-billing.png" alt="واجهة فواتير نقاط البيع ريستوفا"></div>
                <h3>سير العمل المتكامل</h3>
                <p>تتبع كل شيء بسلاسة: الطاولة ← الطلب ← المطبخ ← الفاتورة ← الدفع ← التسوية.</p>
                <p>يتصل بشكل مباشر مع <a href="/ar/captain/">تطبيق الكابتن</a> لطلبات الطاولات و <a href="/ar/kitchen-display/">شاشة المطبخ</a> للتواصل السلس. يدعم <a href="/ar/offline-pos/">العمل دون اتصال بالإنترنت</a>.</p>
            """,
            "faq": [
                ("هل يدعم ريستوفا فواتير المطاعم؟", "نعم، يعالج نظام نقاط البيع جميع جوانب الفواتير بما في ذلك الضرائب، الخصومات، وتقسيم الفواتير."),
                ("هل يعمل ريستوفا بدون إنترنت؟", "نعم، تم بناء النظام للعمل دون اتصال بالإنترنت. يستمر مطعمك في العمل حتى عند انقطاع الاتصال.")
            ]
        }
    },
    "captain": {
        "en": {
            "title": "Restova Captain — Tableside Restaurant Ordering App",
            "desc": "The Restova Captain App empowers your staff to take tableside orders accurately, sending them instantly to the POS and Kitchen Display.",
            "h1": "Restova Captain",
            "h2": "Take the order once. Let the system handle the rest.",
            "content": """
                <p>Equip your waitstaff with the Restova Captain App. Browse the digital menu, add modifiers, and fire orders straight to the kitchen without walking back and forth.</p>
                <div class="product-visual"><img src="/images/cpt-1.png" alt="Restova Captain tableside ordering app"></div>
                <h3>Seamless Table Ordering</h3>
                <p>Select Table → Browse Menu → Select Items → Add Modifiers → Send Order.</p>
                <p>Every order placed on the Captain App updates the <a href="/pos/">Restova POS</a> and the <a href="/kitchen-display/">Kitchen Display System</a> through <a href="/real-time-sync/">real-time synchronization</a>.</p>
            """,
            "faq": [
                ("What does the Restova Captain App do?", "It allows waiters to take orders directly at the table using a mobile device, eliminating paper pads and reducing errors."),
                ("How does a Captain order reach the POS?", "Orders are synchronized in real-time. The moment the waiter hits 'Send', the POS updates and the KOT prints or appears on the KDS.")
            ]
        },
        "ar": {
            "title": "تطبيق كابتن ريستوفا — طلبات الطاولات للمطاعم",
            "desc": "يُمكّن تطبيق الكابتن من ريستوفا طاقمك من أخذ الطلبات بدقة من الطاولة وإرسالها فوراً إلى نقاط البيع وشاشة المطبخ.",
            "h1": "تطبيق الكابتن",
            "h2": "خذ الطلب مرة واحدة. دع النظام يتولى الباقي.",
            "content": """
                <p>زوّد طاقمك بتطبيق كابتن ريستوفا. تصفح القائمة الرقمية، أضف الإضافات، وأرسل الطلبات مباشرة إلى المطبخ دون إضاعة الوقت.</p>
                <div class="product-visual"><img src="/images/cpt-1.png" alt="تطبيق كابتن ريستوفا لطلبات الطاولات"></div>
                <h3>طلبات طاولات سلسة</h3>
                <p>اختر الطاولة ← تصفح القائمة ← اختر العناصر ← أضف الإضافات ← أرسل الطلب.</p>
                <p>كل طلب يتم تحديثه فوراً في <a href="/ar/pos/">نظام نقاط البيع</a> و <a href="/ar/kitchen-display/">شاشة المطبخ</a> عبر <a href="/ar/real-time-sync/">المزامنة الفورية</a>.</p>
            """,
            "faq": [
                ("ماذا يفعل تطبيق الكابتن؟", "يسمح للنادل بأخذ الطلبات مباشرة عند الطاولة باستخدام جهاز محمول، مما يقلل الأخطاء."),
                ("كيف يصل طلب الكابتن إلى نقاط البيع؟", "تتم المزامنة في الوقت الفعلي. بمجرد إرسال الطلب، يتحدث نظام نقاط البيع وتظهر الطلبات في المطبخ.")
            ]
        }
    },
    "kitchen-display": {
        "en": {
            "title": "Restova Kitchen Display — Restaurant KDS",
            "desc": "Eliminate paper tickets with the Restova Kitchen Display System (KDS). Receive KOTs instantly, track prep times, and improve kitchen efficiency.",
            "h1": "Restova Kitchen Display",
            "h2": "A smarter, faster kitchen workflow.",
            "content": """
                <p>The Restova Kitchen Display System transforms how your chefs work. No more lost paper tickets or confusion during rush hours.</p>
                <div class="product-visual"><img src="/images/kds-1.png" alt="Restova Kitchen Display System"></div>
                <h3>Clear Visual Workflow</h3>
                <p>Order Placed → New KOT → Preparing → Ready.</p>
                <p>Orders flow instantly from the <a href="/captain/">Captain App</a> and <a href="/pos/">POS</a> directly to the correct kitchen stations.</p>
            """,
            "faq": [
                ("What is a Kitchen Display System?", "A digital screen in the kitchen that replaces paper KOTs, showing chefs exactly what to prepare and how long they have been waiting."),
                ("How does Restova KDS receive orders?", "It connects seamlessly with the Restova POS and Captain apps, receiving orders in real-time as they are punched in.")
            ]
        },
        "ar": {
            "title": "شاشة مطبخ ريستوفا — KDS للمطاعم",
            "desc": "تخلص من التذاكر الورقية مع شاشة مطبخ ريستوفا. استلم الطلبات فوراً وتتبع أوقات التحضير وحسن كفاءة المطبخ.",
            "h1": "شاشة مطبخ ريستوفا",
            "h2": "سير عمل أذكى وأسرع للمطبخ.",
            "content": """
                <p>يحول نظام شاشة المطبخ من ريستوفا طريقة عمل الطهاة. لا مزيد من التذاكر الورقية المفقودة أو الارتباك خلال ساعات الذروة.</p>
                <div class="product-visual"><img src="/images/kds-1.png" alt="شاشة عرض طلبات المطبخ ريستوفا"></div>
                <h3>سير عمل مرئي واضح</h3>
                <p>تم الطلب ← طلب جديد ← قيد التحضير ← جاهز.</p>
                <p>تتدفق الطلبات فوراً من <a href="/ar/captain/">تطبيق الكابتن</a> و <a href="/ar/pos/">نقاط البيع</a> مباشرة إلى المطبخ.</p>
            """,
            "faq": [
                ("ما هي شاشة عرض المطبخ؟", "شاشة رقمية تحل محل التذاكر الورقية، توضح للطهاة ما يجب تحضيره ووقت الانتظار."),
                ("كيف تستلم شاشة ريستوفا الطلبات؟", "تتصل بسلاسة مع نقاط البيع وتطبيقات الكابتن لتلقي الطلبات في الوقت الفعلي.")
            ]
        }
    },
    "restaurant-management": {
        "en": {
            "title": "Restova Restaurant Management — Manage Your Restaurant in One System",
            "desc": "The complete Restova restaurant management software. Control your POS, menu, staff, tables, and reporting from a unified ecosystem.",
            "h1": "Restaurant Management with Restova",
            "h2": "Control every aspect of your restaurant operations.",
            "content": """
                <p>Restova is more than just a POS; it's a complete restaurant management system designed to give owners and managers total control.</p>
                <div class="product-visual"><img src="/images/owner-menu.png" alt="Restova restaurant management interface"></div>
                <h3>Unified Ecosystem</h3>
                <p>Manage your entire business workflow seamlessly. Restova connects your <a href="/owner-dashboard/">Owner Dashboard</a>, <a href="/pos/">POS</a>, <a href="/captain/">Captain App</a>, and <a href="/kitchen-display/">Kitchen Display</a> into a single source of truth.</p>
            """,
            "faq": [
                ("What parts of my restaurant can Restova help me manage?", "Restova helps you manage billing, tables, staff, digital menus, kitchen workflows, and detailed business reporting.")
            ]
        },
        "ar": {
            "title": "إدارة المطاعم ريستوفا — أدر مطعمك بنظام واحد",
            "desc": "برنامج ريستوفا المتكامل لإدارة المطاعم. تحكم في نقاط البيع، القائمة، الموظفين، الطاولات، والتقارير من نظام واحد.",
            "h1": "إدارة المطاعم مع ريستوفا",
            "h2": "تحكم في كل جانب من عمليات مطعمك.",
            "content": """
                <p>ريستوفا ليس مجرد نظام نقاط بيع؛ إنه نظام متكامل لإدارة المطاعم مصمم لمنح الملاك والمديرين تحكماً كاملاً.</p>
                <div class="product-visual"><img src="/images/owner-menu.png" alt="واجهة إدارة مطاعم ريستوفا"></div>
                <h3>نظام بيئي موحد</h3>
                <p>أدر سير عمل عملك بالكامل بسلاسة. يربط ريستوفا <a href="/ar/owner-dashboard/">لوحة تحكم المالك</a>، <a href="/ar/pos/">نقاط البيع</a>، و <a href="/ar/kitchen-display/">شاشة المطبخ</a> في منصة واحدة.</p>
            """,
            "faq": [
                ("ما هي أجزاء المطعم التي يمكنني إدارتها؟", "يساعدك ريستوفا في إدارة الفواتير، الطاولات، الموظفين، القوائم الرقمية، والتقارير المالية.")
            ]
        }
    },
    "restaurant-billing": {
        "en": {
            "title": "Restaurant Billing with Restova — Fast & Accurate Invoice Software",
            "desc": "Streamline your restaurant billing with Restova. Process payments quickly, handle split bills, apply taxes, and manage discounts effortlessly.",
            "h1": "Restaurant Billing",
            "h2": "Fast, accurate, and seamless settlement.",
            "content": """
                <p>The checkout experience matters. Restova’s restaurant billing software ensures that settling a table is as fast and frictionless as possible.</p>
                <div class="product-visual"><img src="/images/wf-5-settle.png" alt="Restova restaurant billing and settlement"></div>
                <h3>Everything Built-In</h3>
                <p>Manage order-to-bill transitions, automated GST/tax calculations, customized discounts, and flexible payment methods directly from the <a href="/pos/">POS system</a>.</p>
            """,
            "faq": [
                ("Can Restova handle split payments?", "Yes, you can easily split bills by items, equal amounts, or custom values."),
                ("Does it automatically calculate taxes?", "Yes, the billing software handles complex tax rules and GST formatting automatically.")
            ]
        },
        "ar": {
            "title": "فواتير المطاعم مع ريستوفا — برنامج فواتير سريع ودقيق",
            "desc": "بسط عمليات فواتير مطعمك مع ريستوفا. قم بمعالجة المدفوعات، تقسيم الفواتير، تطبيق الضرائب، والخصومات بسهولة.",
            "h1": "فواتير المطاعم",
            "h2": "تسوية سريعة، دقيقة وسلسة.",
            "content": """
                <p>تجربة الدفع مهمة. يضمن برنامج فواتير المطاعم من ريستوفا أن تكون تسوية الطاولة سريعة وخالية من الاحتكاك.</p>
                <div class="product-visual"><img src="/images/wf-5-settle.png" alt="فواتير وتسوية مطاعم ريستوفا"></div>
                <h3>كل شيء مدمج</h3>
                <p>أدر الانتقال من الطلب إلى الفاتورة، حسابات الضرائب، الخصومات، وطرق الدفع مباشرة من <a href="/ar/pos/">نظام نقاط البيع</a>.</p>
            """,
            "faq": [
                ("هل يمكن لـ ريستوفا معالجة المدفوعات المقسمة؟", "نعم، يمكنك بسهولة تقسيم الفواتير حسب العناصر أو بالتساوي."),
                ("هل يقوم بحساب الضرائب تلقائياً؟", "نعم، يعالج برنامج الفواتير قواعد الضرائب تلقائياً.")
            ]
        }
    },
    "table-management": {
        "en": {
            "title": "Restova Table Management — Real-Time Restaurant Table System",
            "desc": "Manage restaurant tables visually. See occupied status, active orders, and connect tables directly to the Restova POS and Captain App.",
            "h1": "Table Management",
            "h2": "Visual control of your dining room.",
            "content": """
                <p>Maximize your seating efficiency. The Restova table management system provides a real-time, color-coded overview of your entire restaurant floor.</p>
                <div class="product-visual"><img src="/images/wf-1-table.png" alt="Restova real-time table management"></div>
                <h3>Know Your Floor</h3>
                <p>Instantly identify which tables are free, occupied, or waiting for settlement. Integrated seamlessly with the <a href="/pos/">POS</a> and the <a href="/captain/">Captain App</a> for rapid order association.</p>
            """,
            "faq": [
                ("Can I see table status in real-time?", "Yes, tables change color automatically based on their current status (free, occupied, billed).")
            ]
        },
        "ar": {
            "title": "إدارة الطاولات ريستوفا — نظام طاولات حي للمطاعم",
            "desc": "أدر طاولات المطعم بصرياً. تعرف على حالة الإشغال والطلبات النشطة، واربط الطاولات مباشرة بنقاط البيع وتطبيق الكابتن.",
            "h1": "إدارة الطاولات",
            "h2": "تحكم مرئي في صالة طعامك.",
            "content": """
                <p>قم بزيادة كفاءة جلوس ضيوفك. يوفر نظام إدارة طاولات ريستوفا نظرة عامة في الوقت الفعلي ومميزة بالألوان.</p>
                <div class="product-visual"><img src="/images/wf-1-table.png" alt="إدارة طاولات المطعم من ريستوفا"></div>
                <h3>تعرف على صالتك</h3>
                <p>تحديد فوري للطاولات الشاغرة أو المشغولة. متكامل تماماً مع <a href="/ar/pos/">نقاط البيع</a> و <a href="/ar/captain/">تطبيق الكابتن</a>.</p>
            """,
            "faq": [
                ("هل يمكنني رؤية حالة الطاولة في الوقت الفعلي؟", "نعم، يتغير لون الطاولات تلقائياً بناءً على حالتها (شاغرة، مشغولة، مفوترة).")
            ]
        }
    },
    "offline-pos": {
        "en": {
            "title": "Restova Offline POS — Keep Your Restaurant Running Without Internet",
            "desc": "Restova’s offline restaurant POS keeps your business operating smoothly. Take orders and print KOTs even when the internet drops. Auto-syncs when back online.",
            "h1": "Offline Restaurant POS",
            "h2": "Your restaurant never stops. Neither should your POS.",
            "content": """
                <p>Internet outages shouldn't mean operations halt. The Restova Offline POS ensures that your core restaurant workflows continue uninterrupted when connectivity is lost.</p>
                <div class="product-visual"><img src="/images/wf-6-sales.png" alt="Restova offline POS synchronization"></div>
                <h3>How It Works</h3>
                <p>Data is persisted locally. You can still punch orders, print to the kitchen, and settle tables. Once the internet returns, Restova leverages powerful <a href="/real-time-sync/">synchronization algorithms</a> to push all queued changes to the cloud automatically.</p>
            """,
            "faq": [
                ("What happens when the internet goes down?", "The POS switches to local operation mode. You can continue taking orders and printing KOTs."),
                ("What happens when the connection returns?", "All locally queued transactions are automatically synced to the cloud without manual intervention.")
            ]
        },
        "ar": {
            "title": "نقاط البيع دون إنترنت — حافظ على عمل مطعمك بدون اتصال",
            "desc": "يحافظ نظام نقاط البيع دون إنترنت من ريستوفا على سير عملك. استلم الطلبات واطبع الفواتير حتى عند انقطاع الإنترنت.",
            "h1": "نظام نقاط البيع دون اتصال",
            "h2": "مطعمك لا يتوقف أبداً. وكذلك نظامك.",
            "content": """
                <p>انقطاع الإنترنت لا يعني توقف العمل. يضمن نظام ريستوفا استمرار سير عملك الأساسي دون انقطاع عند فقدان الاتصال.</p>
                <div class="product-visual"><img src="/images/wf-6-sales.png" alt="مزامنة نقاط البيع من ريستوفا"></div>
                <h3>كيف يعمل؟</h3>
                <p>يتم حفظ البيانات محلياً. يمكنك الاستمرار في إدخال الطلبات والطباعة. بمجرد عودة الإنترنت، تقوم <a href="/ar/real-time-sync/">المزامنة الفورية</a> برفع كافة التغييرات تلقائياً.</p>
            """,
            "faq": [
                ("ماذا يحدث عند انقطاع الإنترنت؟", "ينتقل النظام إلى وضع العمل المحلي. يمكنك الاستمرار في تلقي الطلبات."),
                ("ماذا يحدث عند عودة الاتصال؟", "تتم مزامنة جميع المعاملات المحلية تلقائياً مع السحابة.")
            ]
        }
    },
    "real-time-sync": {
        "en": {
            "title": "Real-Time Restaurant Synchronization — The Restova Ecosystem",
            "desc": "Experience true real-time restaurant POS synchronization. Orders flow instantly from Captain App to Kitchen Display and POS.",
            "h1": "Real-Time Synchronization",
            "h2": "One action. Everywhere.",
            "content": """
                <p>Speed is critical in a busy restaurant. Restova uses advanced real-time synchronization to ensure every device in your restaurant is perfectly aligned, instantly.</p>
                <div class="product-visual"><img src="/images/wf-4-kds.png" alt="Restova real-time order synchronization"></div>
                <h3>Instant Communication</h3>
                <p>When a waiter adds an item on the <a href="/captain/">Captain App</a>, it appears on the <a href="/pos/">POS</a> instantly, and the <a href="/kitchen-display/">Kitchen Display</a> receives the KOT simultaneously. No refreshing required.</p>
            """,
            "faq": [
                ("How fast is the synchronization?", "Updates happen in milliseconds across all connected devices in the restaurant ecosystem.")
            ]
        },
        "ar": {
            "title": "المزامنة الفورية للمطاعم — نظام ريستوفا المتصل",
            "desc": "استمتع بمزامنة فورية حقيقية لنقاط البيع. تتدفق الطلبات فوراً من الكابتن إلى المطبخ ونقاط البيع.",
            "h1": "المزامنة الفورية",
            "h2": "إجراء واحد. في كل مكان.",
            "content": """
                <p>السرعة أمر بالغ الأهمية. يستخدم ريستوفا المزامنة الفورية المتقدمة لضمان تزامن كل جهاز في مطعمك بشكل مثالي.</p>
                <div class="product-visual"><img src="/images/wf-4-kds.png" alt="مزامنة طلبات المطعم في الوقت الفعلي"></div>
                <h3>تواصل فوري</h3>
                <p>عندما يضيف النادل عنصراً في <a href="/ar/captain/">تطبيق الكابتن</a>، يظهر فوراً في <a href="/ar/pos/">نقاط البيع</a> و <a href="/ar/kitchen-display/">شاشة المطبخ</a>.</p>
            """,
            "faq": [
                ("ما مدى سرعة المزامنة؟", "تحدث التحديثات في أجزاء من الثانية عبر جميع الأجهزة المتصلة.")
            ]
        }
    },
    "owner-dashboard": {
        "en": {
            "title": "Restova Owner Dashboard — Restaurant Reports & Management",
            "desc": "Access powerful restaurant reporting software. The Restova Owner Dashboard gives you complete visibility into revenue, staff, and operations from anywhere.",
            "h1": "Restova Owner Dashboard",
            "h2": "Your restaurant’s data at your fingertips.",
            "content": """
                <p>Make data-driven decisions. The Restova Owner Dashboard provides comprehensive restaurant reports and management tools, accessible securely from any device.</p>
                <div class="product-visual"><img src="/images/owner-report.png" alt="Restova Owner Dashboard and Reports"></div>
                <h3>Operational Visibility</h3>
                <p>Track live revenue, manage digital menus, adjust pricing, and oversee your <a href="/pos/">POS</a> performance without needing to be physically present at the restaurant.</p>
            """,
            "faq": [
                ("Can I access reports remotely?", "Yes, the Owner Dashboard is cloud-based and accessible securely from any smartphone, tablet, or computer.")
            ]
        },
        "ar": {
            "title": "لوحة تحكم مالك ريستوفا — تقارير وإدارة المطاعم",
            "desc": "لوحة تحكم ريستوفا تمنحك رؤية كاملة للإيرادات والموظفين والعمليات من أي مكان بفضل برنامج تقارير المطاعم المتقدم.",
            "h1": "لوحة تحكم مالك ريستوفا",
            "h2": "بيانات مطعمك في متناول يدك.",
            "content": """
                <p>اتخذ قرارات مبنية على البيانات. توفر لوحة تحكم مالك ريستوفا تقارير شاملة وأدوات إدارة يمكن الوصول إليها بأمان من أي جهاز.</p>
                <div class="product-visual"><img src="/images/owner-report.png" alt="تقارير لوحة تحكم مالك المطعم"></div>
                <h3>رؤية تشغيلية</h3>
                <p>تتبع الإيرادات المباشرة، أدر القوائم، وراقب أداء <a href="/ar/pos/">نقاط البيع</a> دون الحاجة للتواجد شخصياً في المطعم.</p>
            """,
            "faq": [
                ("هل يمكنني الوصول للتقارير عن بُعد؟", "نعم، لوحة التحكم سحابية ويمكن الوصول إليها من أي هاتف ذكي أو جهاز كمبيوتر.")
            ]
        }
    }
}

import os
import re

def create_page(route_id, lang, data):
    # Determine source template and target path
    src_path = "public/index.html" if lang == "en" else "public/ar/index.html"
    
    # Example: route_id = "pos", lang = "en" -> public/pos/index.html
    # lang = "ar" -> public/ar/pos/index.html
    if lang == "en":
        target_dir = f"public/{route_id}"
    else:
        target_dir = f"public/ar/{route_id}"
        
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "index.html")
    
    # Read base template
    with open(src_path, "r") as f:
        html = f.read()
        
    # We want to keep the <head> (and replace meta/title), the <nav>, the CTA, and the <footer>.
    # The main content usually starts after <nav>. Let's find </nav> and <!-- PRODUCT ECOSYSTEM --> or <footer>
    
    # Replace title
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', html)
    # Replace meta description
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["desc"]}">', html)
    # Replace OG title/desc
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{data["title"]}">', html)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{data["desc"]}">', html)
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{data["title"]}">', html)
    html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{data["desc"]}">', html)

    # Reconstruct the body
    # We will slice the HTML at </nav> and at <!-- REGISTER --> to replace the middle content.
    nav_end = html.find("</nav>") + 6
    register_start = html.find("<!-- REGISTER")
    if register_start == -1:
        register_start = html.find("<footer")
        
    head_nav = html[:nav_end]
    footer_cta = html[register_start:]
    
    # Build custom content
    explore_title = "Explore Restova:" if lang == "en" else "اكتشف ريستوفا:"
    pos_txt = "POS" if lang == "en" else "نقاط البيع"
    cpt_txt = "Captain App" if lang == "en" else "تطبيق الكابتن"
    kds_txt = "Kitchen Display" if lang == "en" else "شاشة المطبخ"
    mgt_txt = "Restaurant Management" if lang == "en" else "إدارة المطاعم"
    
    faq_html = ""
    for q, a in data["faq"]:
        faq_html += f"""
        <div class="faq-item">
            <div class="faq-question"><span>{q}</span><span class="faq-icon">+</span></div>
            <div class="faq-answer"><p>{a}</p></div>
        </div>
        """
        
    custom_body = f"""
    <section class="section section-alt" style="padding-top: 120px;">
        <div class="container">
            <div class="section-header" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h1 class="section-title" style="font-size: 3rem; margin-bottom: 20px;">{data["h1"]}</h1>
                <p class="section-subtitle">{data["h2"]}</p>
            </div>
            
            <div class="product-content reveal" style="max-width: 900px; margin: 40px auto; font-size: 1.1rem; line-height: 1.8; color: var(--text-s);">
                {data["content"]}
            </div>
            
            <div class="faq-container reveal" style="max-width: 800px; margin: 60px auto;">
                <h3 style="text-align: center; margin-bottom: 30px; font-size: 2rem;">{'FAQ' if lang=='en' else 'الأسئلة الشائعة'}</h3>
                {faq_html}
            </div>
            
            <div class="related-products reveal" style="max-width: 800px; margin: 80px auto; text-align: center; border-top: 1px solid var(--border); padding-top: 40px;">
                <h4 style="margin-bottom: 20px; color: var(--text);">{explore_title}</h4>
                <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                    <a href="{'/' if lang=='en' else '/ar/'}pos/" class="btn-secondary btn-sm">{pos_txt}</a>
                    <a href="{'/' if lang=='en' else '/ar/'}captain/" class="btn-secondary btn-sm">{cpt_txt}</a>
                    <a href="{'/' if lang=='en' else '/ar/'}kitchen-display/" class="btn-secondary btn-sm">{kds_txt}</a>
                    <a href="{'/' if lang=='en' else '/ar/'}restaurant-management/" class="btn-secondary btn-sm">{mgt_txt}</a>
                </div>
            </div>
        </div>
    </section>
    """
    
    # Path relative adjustments (for CSS, JS, images, etc.)
    # Because these pages are in a subdirectory (e.g., /pos/), we must ensure paths are absolute.
    # The existing template uses href="/style.css", href="/favicon.ico", src="/images/...", so they are already absolute! Perfect.
    
    final_html = head_nav + custom_body + footer_cta
    
    with open(target_path, "w") as f:
        f.write(final_html)
    print(f"Created {target_path}")

for route_id, langs in pages.items():
    if "en" in langs:
        create_page(route_id, "en", langs["en"])
    if "ar" in langs:
        create_page(route_id, "ar", langs["ar"])

print("All product pages generated.")
