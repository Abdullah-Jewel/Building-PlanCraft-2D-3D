#!/usr/bin/env python3
"""Builds the PlanCraft 3D website into ./dist (ready for GitHub Pages).
Edit site.config.json, then run:  python3 build.py [path/to/planner/index.html]
"""
import json, os, shutil, sys, html
from articles import A

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, 'site.config.json'), encoding='utf-8'))
OUT = os.path.join(HERE, 'dist')
APP_SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'planner', 'index.html')
BASE = ('https://' + C['custom_domain']) if C['custom_domain'] else C['base_url'].rstrip('/')
B = C['brand']; E = html.escape

def contact_line():
    if C['contact_email']:
        return '<a href="mailto:%s">%s</a>' % (E(C['contact_email']), E(C['contact_email']))
    return '<a href="%s">the project page on GitHub (open an issue)</a>' % E(C['github_issues'])


def profile_card():
    img = '<img src="%sassets/photo.jpg" alt="%s" width="190" height="237" loading="lazy">' % ('', E(C['author_full'])) if C.get('photo') else ''
    return ('<div class="profile">%s<div><h2>%s</h2><p class="role">%s</p>'
            '<p>%s is a free home planning tool made by <b>%s</b>, studying Electrical and Electronic Engineering (EEE) at CUET, Bangladesh. '
            'It started as a personal project to plan a family house and grew into a full 2D and 3D planner with a cost estimator that uses local material prices.</p></div></div>'
            % (img, E(C['author_full']), E(C['author_role']), E(B), E(C['author_full'])))

CSS = """
:root{--bg:#f8fafc;--card:#fff;--tx:#0f172a;--mu:#475569;--bd:#e2e8f0;--ac:#0284c7;--ac2:#0369a1;--on:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--tx:#e5eaf3;--mu:#9aa8bf;--bd:#223049;--ac:#38bdf8;--ac2:#7dd3fc;--on:#04202e}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--tx);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
a{color:var(--ac2)}a:hover{text-decoration:none}
.wrap{max-width:1040px;margin:0 auto;padding:0 18px}
header.site{background:var(--card);border-bottom:1px solid var(--bd);position:sticky;top:0;z-index:5}
header.site .wrap{display:flex;align-items:center;gap:14px;min-height:60px;flex-wrap:wrap;padding-top:6px;padding-bottom:6px}
.logo{display:flex;align-items:center;gap:8px;font-weight:700;color:var(--tx);text-decoration:none;font-size:18px}
.logo svg{width:28px;height:28px}
nav.main{margin-left:auto;display:flex;gap:4px;flex-wrap:wrap}
nav.main a{padding:10px 12px;border-radius:8px;color:var(--tx);text-decoration:none;font-size:15px;min-height:44px;display:inline-flex;align-items:center}
nav.main a:hover,nav.main a[aria-current]{background:var(--bd)}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:10px;background:var(--ac);color:var(--on);font-weight:700;text-decoration:none;border:0}
.btn.alt{background:transparent;color:var(--tx);border:1px solid var(--bd)}
.hero{padding:56px 0 40px;text-align:center}
.hero h1{font-size:clamp(30px,5vw,50px);line-height:1.15;margin:0 0 14px}
.hero p{max-width:640px;margin:0 auto 24px;color:var(--mu);font-size:19px}
.hero .cta{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:24px 0}
.card{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:18px}
.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0;color:var(--mu);font-size:15.5px}
a.card{display:block;text-decoration:none;color:inherit}a.card:hover{border-color:var(--ac)}
section.s{padding:24px 0}section.s>h2{font-size:28px;margin:0 0 4px}
.lead{color:var(--mu);margin:0 0 8px}
article.post{max-width:760px;margin:0 auto;padding:30px 0 50px}
article.post h1{font-size:clamp(28px,4.5vw,40px);line-height:1.2;margin:0 0 8px}
article.post h2{margin:30px 0 8px;font-size:24px}
.meta{color:var(--mu);font-size:14px;margin-bottom:20px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px;display:block;overflow-x:auto}
th,td{border:1px solid var(--bd);padding:8px 10px;text-align:left}th{background:var(--card)}
.note{background:var(--card);border:1px solid var(--bd);border-left:4px solid var(--ac);padding:12px 14px;border-radius:8px;color:var(--mu);font-size:15px}
.crumbs{font-size:14px;color:var(--mu);padding-top:18px}
footer.site{border-top:1px solid var(--bd);background:var(--card);margin-top:40px;padding:26px 0;color:var(--mu);font-size:15px}
footer.site .cols{display:flex;gap:28px;flex-wrap:wrap}
footer.site a{color:var(--mu)}
.profile{display:flex;gap:26px;align-items:center;background:var(--card);border:1px solid var(--bd);border-radius:18px;padding:22px;margin:8px 0 26px}
.profile img{width:190px;height:237px;object-fit:cover;object-position:center top;border-radius:14px;flex:none}
article.post .profile h2{margin:0 0 2px;font-size:26px}.profile .role{color:var(--ac2);font-weight:600;margin:0 0 10px;font-size:15.5px}.profile p{margin:0 0 10px}
@media (max-width:640px){.profile{flex-direction:column;text-align:left;align-items:flex-start}.profile img{width:100%;height:auto;aspect-ratio:4/5}}
.tool-cta{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:20px;margin:34px 0;display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap}
@media (max-width:640px){body{font-size:16.5px}.hero{padding:36px 0 24px}}
"""

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3 4 9.5v13L16 29l12-6.5v-13z" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-linejoin="round"/><path d="M4 9.5 16 16l12-6.5M16 16v13" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-linejoin="round"/></svg>'

def head(title, desc, path, depth, extra=''):
    up = '../' * depth
    canon = BASE + '/' + path
    ga = ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","%s");</script>' % (C['ga_id'], C['ga_id'])) if C['ga_id'] else ''
    ads = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-%s" crossorigin="anonymous"></script>' % C['adsense_publisher_id']) if C['adsense_enabled'] and C['adsense_publisher_id'] else ''
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s">'
            '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website"><meta property="og:url" content="%s">'
            '<meta name="theme-color" content="#0284c7"><link rel="icon" href="%sfavicon.svg" type="image/svg+xml"><link rel="stylesheet" href="%sstyle.css">%s%s%s</head><body>'
            % (E(title), E(desc), E(canon), E(title), E(desc), E(canon), up, up, ga, ads, extra))

def top(depth, cur=''):
    up = '../' * depth
    items = [('Planner', 'app/'), ('Guides', 'guides/'), ('About', 'about.html'), ('Contact', 'contact.html')]
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (up, h, ' aria-current="page"' if cur == h else '', t) for t, h in items)
    return ('<header class="site"><div class="wrap"><a class="logo" href="%s">%s%s</a><nav class="main" aria-label="Main">%s</nav></div></header>' % (up or './', LOGO, E(B), nav))

def foot(depth):
    up = '../' * depth
    return ('<footer class="site"><div class="wrap"><div class="cols"><div><b>%s</b><br>Free 2D and 3D floor planner with Bangladesh cost estimates.</div>'
            '<div><a href="%sapp/">Planner</a><br><a href="%sguides/">Guides</a><br><a href="%sabout.html">About</a></div>'
            '<div><a href="%sprivacy.html">Privacy policy</a><br><a href="%sterms.html">Terms</a><br><a href="%scontact.html">Contact</a></div></div>'
            '<p>&copy; 2026 %s. Estimates and guides are for planning only and are not engineering advice.</p></div></footer></body></html>'
            % (E(B), up, up, up, up, up, up, E(C.get('author_full') or C['author'])))

def page(path, title, desc, body, depth=0, cur=''):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(head(title, desc, path, depth) + top(depth, cur) + '<main id="main">' + body + '</main>' + foot(depth))

# ---------- reset
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
open(os.path.join(OUT, 'style.css'), 'w').write(CSS)
open(os.path.join(OUT, 'favicon.svg'), 'w').write(LOGO.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" '))
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
if C['custom_domain']: open(os.path.join(OUT, 'CNAME'), 'w').write(C['custom_domain'] + '\n')

if C.get('photo') and os.path.exists(os.path.join(HERE,C['photo'])):
    os.makedirs(os.path.join(OUT,'assets'),exist_ok=True)
    shutil.copy(os.path.join(HERE,C['photo']),os.path.join(OUT,'assets','photo.jpg'))

# ---------- planner app
if os.path.exists(APP_SRC):
    os.makedirs(os.path.join(OUT, 'app'), exist_ok=True)
    shutil.copy(APP_SRC, os.path.join(OUT, 'app', 'index.html'))
else:
    print('WARNING: planner file not found at', APP_SRC)

# ---------- home
feat = [('2D and 3D planning', 'Draw walls at any angle, place doors, windows and furniture, then walk through in first-person 3D.'),
        ('Bangladesh cost estimate', 'Foundation, frame, masonry, finishes and services priced with editable local rates in BDT, USD, INR or EUR.'),
        ('Rebar schedule', 'Steel split into 10, 12, 16 and 20 mm bars with 12 m bar counts and cost.'),
        ('Column grid and setbacks', 'Generate columns at corners and long spans, and check walls against setback lines.'),
        ('Sun and north', 'Rotate north and move the sun by month and hour to test shadows and orientation.'),
        ('Plumbing layer', 'Place fixtures, stacks, septic tank and water tank, and join them with pipes.'),
        ('Up to ten floors and roofs', 'Floor selector, copy-floor-up, flat roof with stair cover room, hip and gable roofs.'),
        ('DXF, PDF and PNG export', 'Take your plan into AutoCAD or print it.')]
faq = [('Is PlanCraft 3D free?', 'Yes. You can use the planner in your browser without an account.'),
       ('Where are my drawings stored?', 'On your own device. Use Save / Load to keep a copy as a file.'),
       ('How accurate is the cost estimate?', 'It is a planning estimate from your drawing and typical Bangladesh rules of thumb. Prices change, so edit the unit rates to your dealer quotes.'),
       ('Does it replace an engineer?', 'No. Structural design, soil testing and approvals need a licensed engineer or architect.')]
home = ('<div class="wrap"><section class="hero"><h1>Plan your dream home in 2D and 3D</h1>'
        '<p>A free floor planner with a Bangladesh cost estimator, column grid, plumbing layer, sun study and CAD export. Works on phones and computers.</p>'
        '<div class="cta"><a class="btn" href="app/">Open the planner</a><a class="btn alt" href="guides/">Read the guides</a></div></section>'
        '<section class="s"><h2>What you can do</h2><div class="grid">%s</div></section>'
        '<section class="s"><h2>Latest guides</h2><p class="lead">Practical notes for people building in Bangladesh.</p><div class="grid">%s</div><p><a href="guides/">All guides</a></p></section>'
        '<section class="s"><h2>Questions</h2>%s</section></div>'
        % (''.join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (E(a), E(b)) for a, b in feat),
           ''.join('<a class="card" href="guides/%s.html"><h3>%s</h3><p>%s</p></a>' % (a['slug'], E(a['title']), E(a['desc'])) for a in A[:6]),
           ''.join('<div class="card" style="margin-bottom:12px"><h3>%s</h3><p>%s</p></div>' % (E(q), E(a)) for q, a in faq)))
ld = json_ld = '<script type="application/ld+json">%s</script>' % json.dumps({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": B, "applicationCategory": "DesignApplication", "operatingSystem": "Web, Android", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": BASE + '/'})
page('index.html', B + ' | Free 2D and 3D floor planner with Bangladesh cost estimate', 'Plan a house in 2D and 3D, generate a column grid, test sun and shadows, lay out plumbing and estimate cost in taka. Free in your browser.', home + ld, 0)

# ---------- guides
for a in A:
    related = [x for x in A if x['slug'] != a['slug']][:3]
    body = ('<div class="wrap"><article class="post"><div class="crumbs"><a href="../">Home</a> / <a href="./">Guides</a></div><h1>%s</h1><div class="meta">By %s &middot; Updated %s</div>%s'
            '<div class="tool-cta"><div><b>Try it on your own plan</b><br><span class="lead">Free, in your browser, no sign-up.</span></div><a class="btn" href="../app/">Open the planner</a></div>'
            '<h2>More guides</h2><div class="grid">%s</div></article></div>'
            % (E(a['title']), E(C.get('author_full') or C['author']), C['updated'], a['body'], ''.join('<a class="card" href="%s.html"><h3>%s</h3></a>' % (r['slug'], E(r['title'])) for r in related)))
    ldj = '<script type="application/ld+json">%s</script>' % json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['desc'], "author": {"@type": "Person", "name": C.get("author_full") or C["author"]}, "dateModified": C['updated']})
    page('guides/%s.html' % a['slug'], a['title'] + ' | ' + B, a['desc'], body + ldj, 1, 'guides/')
gi = ('<div class="wrap"><section class="s" style="padding-top:34px"><h1 style="margin:0 0 6px">Guides for home builders</h1><p class="lead">Plain-language guides on cost, layout, structure and services, written for building in Bangladesh.</p><div class="grid">%s</div></section></div>'
      % ''.join('<a class="card" href="%s.html"><h3>%s</h3><p>%s</p></a>' % (a['slug'], E(a['title']), E(a['desc'])) for a in A))
page('guides/index.html', 'Home building guides for Bangladesh | ' + B, 'Guides on construction cost, room sizes, materials, rebar, setbacks, columns, sun orientation, plumbing and stairs.', gi, 1, 'guides/')

# ---------- about / contact / privacy / terms
about = ('<div class="wrap"><article class="post"><h1>About %s</h1>'
         '%s'
         '<h2>Why it exists</h2><p>Many people in Bangladesh plan a house with only a hand sketch and a contractor\'s verbal estimate. We want everyone to see their plan in 3D, check the layout, and understand the cost before spending money.</p>'
         '<h2>How the estimates work</h2><p>The planner measures your drawing (walls, floors, openings, columns, pipes) and applies typical Bangladesh rules of thumb for concrete, steel, brick, finishes and services. All unit prices are editable, so you can use your own dealer quotes. The numbers are planning estimates, not quotations.</p>'
         '<h2>What it is not</h2><p>It is not structural design software. A licensed structural engineer must design the frame and foundation, and local authorities approve building plans.</p>'
         '<h2>Contact</h2><p>Feedback and bug reports are welcome. Reach us through %s.</p>'
         '<p><a class="btn" href="app/">Open the planner</a></p></article></div>' % (E(B), profile_card(), contact_line()))
page('about.html', 'About ' + B, 'About the free PlanCraft 3D floor planner and who makes it.', about, 0, 'about.html')

contact = ('<div class="wrap"><article class="post"><h1>Contact</h1>' + profile_card() +
           '<h2>Get in touch</h2><p>Questions, feedback, bug reports and partnership requests are welcome. Please contact us through %s.</p>'
           '<p>When you report a problem, tell us your device, browser and what you were doing. We read every message and usually reply within a few days.</p>'
           '<h2>Good to know</h2><ul><li>The planner and guides are free to use, and your drawings stay on your own device.</li><li>Material prices in the cost estimate are approximate and editable, so send corrections if a price in your district looks far off.</li><li>Suggestions for new features, guides and local material rates are especially welcome.</li></ul>'
           '<p class="note">We cannot give structural design advice or approve building plans. Please consult a licensed engineer or architect for that.</p>'
           '<p><a class="btn" href="app/">Open the planner</a></p></article></div>' % contact_line())
page('contact.html', 'Contact | ' + B, 'How to contact the PlanCraft 3D team with feedback or bug reports.', contact, 0, 'contact.html')

priv = ('<div class="wrap"><article class="post"><h1>Privacy policy</h1><div class="meta">Last updated %(u)s</div>'
 '<p>This policy explains what information %(b)s ("we", "the site") handles when you use this website and the planner. We keep it short and plain.</p>'
 '<h2>Your drawings</h2><p>Your floor plans, prices and settings are stored in your own browser (local storage) and are not uploaded to our servers. If you clear your browser data, they are removed. Use Save / Load to keep a file copy.</p>'
 '<h2>Information collected automatically</h2><p>We use Google Analytics to count visits and understand which pages and features are used. Google Analytics uses cookies and similar technologies and may collect your IP address, device and browser information, and pages viewed. We do not combine this with your name or contact details.</p>'
 '<h2>Advertising</h2><p>This site may show ads served by Google AdSense and other Google advertising services. Google and its partners use cookies to serve ads based on your visits to this and other sites. You can manage personalised ads at <a href="https://adssettings.google.com">Google Ads Settings</a>, and learn how Google uses data from sites that use its services at <a href="https://policies.google.com/technologies/partner-sites">policies.google.com/technologies/partner-sites</a>. In the European Economic Area, the United Kingdom and Switzerland, we ask for your consent before using cookies for personalised ads.</p>'
 '<h2>Cookies</h2><p>Cookies come from the analytics and advertising services above. You can block or delete cookies in your browser settings. Some features of third-party services may stop working if you do.</p>'
 '<h2>Third-party services</h2><p>The planner loads open-source libraries (React, Three.js, jsPDF) and styles from public content delivery networks, which receive your IP address when your browser requests them.</p>'
 '<h2>Children</h2><p>The site is not directed to children under 13 and we do not knowingly collect their personal information.</p>'
 '<h2>Your choices</h2><p>You can use the planner without creating an account. You can opt out of Google Analytics with the <a href="https://tools.google.com/dlpage/gaoptout">browser add-on</a>.</p>'
 '<h2>Changes</h2><p>We may update this policy. The date at the top shows the latest version.</p>'
 '<h2>Contact</h2><p>For privacy questions, contact us through %(c)s.</p></article></div>') % dict(u=C['updated'], b=E(B), c=contact_line())
page('privacy.html', 'Privacy policy | ' + B, 'How PlanCraft 3D handles your drawings, analytics and advertising cookies.', priv, 0)

terms = ('<div class="wrap"><article class="post"><h1>Terms of use</h1><div class="meta">Last updated %s</div>'
 '<p>By using %s you agree to these terms.</p>'
 '<h2>Planning tool only</h2><p>The planner, cost estimates and guides are for general planning. They are not engineering design, legal advice or a contractor quotation. Always have your plan, structure, soil conditions and approvals checked by licensed professionals and your local authority.</p>'
 '<h2>No warranty</h2><p>The service is provided as is. Quantities, prices and drawings may contain errors, and market prices change. We are not liable for loss arising from decisions made using this site.</p>'
 '<h2>Your content</h2><p>You own the plans you create. We do not claim rights to them.</p>'
 '<h2>Acceptable use</h2><p>Do not misuse the site, try to break it, or use it to break the law.</p>'
 '<h2>Changes</h2><p>We may change or stop features at any time.</p></article></div>') % (C['updated'], E(B))
page('terms.html', 'Terms of use | ' + B, 'Terms of use for the PlanCraft 3D website and planner.', terms, 0)

nf = '<div class="wrap"><article class="post"><h1>Page not found</h1><p>That page does not exist. Try the <a href="/">home page</a> or the <a href="/guides/">guides</a>.</p></article></div>'
# 404 uses absolute-from-base links so it works at any depth
p404 = head('Page not found | ' + B, 'Page not found.', '404.html', 0).replace('href="style.css"', 'href="%s/style.css"' % BASE).replace('href="favicon.svg"', 'href="%s/favicon.svg"' % BASE)
nf = nf.replace('href="/"', 'href="%s/"' % BASE).replace('href="/guides/"', 'href="%s/guides/"' % BASE)
open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8').write(p404 + top(0).replace('href="./"', 'href="%s/"' % BASE) + nf + foot(0))

# ---------- ads.txt, robots, sitemap
if C['adsense_publisher_id']:
    line = 'google.com, %s, DIRECT, f08c47fec0942fa0\n' % C['adsense_publisher_id']
    open(os.path.join(OUT, 'ads.txt'), 'w').write(line)
    open(os.path.join(OUT, 'app-ads.txt'), 'w').write(line)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % BASE)
urls = ['', 'app/', 'guides/', 'about.html', 'contact.html', 'privacy.html', 'terms.html'] + ['guides/%s.html' % a['slug'] for a in A]
open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % ''.join('<url><loc>%s/%s</loc><lastmod>%s</lastmod></url>' % (BASE, u, C['updated']) for u in urls))
print('Built', len(os.listdir(OUT)), 'items in', OUT, 'base', BASE)
