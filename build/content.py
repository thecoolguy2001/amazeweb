# -*- coding: utf-8 -*-
"""All site copy. Transcribed from the published Framer original, then
updated: the site no longer ships Framer templates, so platform references
name Shopify and custom builds instead."""

SITE = {"name": "Amazé Web", "copyright": "Copyright © 2026 Amazé"}

NAV = [("Templates", "/templates/"), ("Services", "/services/"), ("Support", "/support/")]

SOCIALS = [
    ("TikTok",    "https://tiktok.com/@amazeweb.shop"),
    ("Instagram", "https://www.instagram.com/amazeweb.shop"),
    ("X",         "https://x.com/amazewebservice"),
    ("Facebook",  "https://www.facebook.com/share/1Byrb4N2jq/?mibextid=wwXIfr"),
    ("LinkedIn",  "https://www.linkedin.com/company/amaze-web"),
]

FOOTER = {
    "stmt": "Turn your ideas into experiences, effortlessly.",
    "cols": [
        ("Quick Links", [("Home", "/"), ("About Us", "/#case-study"),
                         ("Our Vision", "/#ourvision"), ("FAQ", "/#faqss")]),
        ("Main Pages", [("Templates", "/templates/"), ("Services", "/services/"),
                        ("Support", "/support/")]),
        ("Other", [("Back To Top", "#top"), ("Form Submit", "/support/#support-message")]),
    ],
}

FAQ = [
    ("Get Started", [
        ("How does AmazeWeb work?",
         "Choose a template, purchase it through our checkout, and receive everything you need to customize and launch your website."),
        ("What platforms do you support?",
         "AmazeWeb focuses on Shopify templates and custom-built sites, with additional services for website setup, email design, and brand assets."),
        ("Can you set up the website for me?",
         "Yes. If you want help, you can add a setup service and we’ll install the template, connect basic pages, and prepare the site for launch."),
    ]),
    ("Design", [
        ("Can I customize the design?",
         "Yes. You can update colors, fonts, images, sections, buttons, and copy so the template matches your brand."),
        ("Are the templates mobile-friendly?",
         "Yes. AmazeWeb templates are designed to look clean on desktop, tablet, and mobile."),
        ("Can I request a custom design?",
         "Yes. If you need something more specific than a template, you can book a custom website or brand design service."),
    ]),
    ("Setup", [
        ("Can AmazeWeb set up the website for me?",
         "Yes. You can add setup support if you want us to install the template and prepare the website for launch."),
        ("What do I need before setup starts?",
         "You’ll need your logo, brand colors, images, website copy, product info, and access to your Shopify account or hosting."),
        ("Can you connect my domain?",
         "Yes. Domain connection can be included with setup support, depending on your platform and hosting provider."),
    ]),
    ("Support", [
        ("What happens after I purchase?",
         "After purchase, you’ll receive access to the template files, setup instructions, and any included resources."),
        ("Can I get help after purchase?",
         "Yes. Basic support is available for questions about downloading, accessing, or using your template."),
        ("Do you provide long-term website management?",
         "AmazeWeb focuses on templates, setup, and launch support. Ongoing maintenance may be offered separately depending on availability."),
    ]),
]

IMG = "/assets/img/"
LOGO = IMG + "9Rb6ELE5jVlzfGlbglZUejG8k.png"

# --- homepage sticky cards -------------------------------------------------
HOME_CARDS = [
    {"title": "Designing Premium Website Templates",
     "body": "Crafted for speed, style, and performance. Our templates are built to look stunning right out of the box, with flexible layouts that adapt to your brand’s personality. Launch faster without sacrificing design quality or user experience.",
     "cta": ("Browse Templates", "/templates/"),
     "img": IMG + "HBt1P1lrolW51BNI8Z2o6uf2rs.png", "ratio": "428/269",
     "dim": True},
    {"title": "Delivering End-to-End Creative Solutions",
     "body": "From concept to launch, I handle every detail. Whether it’s building a high-performing website, designing intuitive interfaces, or crafting cohesive brand systems every project is guided by strategy, creativity, and precision.",
     "cta": ("View Services", "/services/"),
     "img": IMG + "HwBYfWSfyi6G2G045HaZGZXPc0Q.png", "ratio": "428/240",
     "dim": False},
    {"title": "Personalized Support That Actually Supports You",
     "body": "Every project comes with direct, one-on-one guidance. Whether you need help setting up your site, customizing a design, or troubleshooting, you’ll have expert support that’s fast, clear, and genuinely helpful.",
     "cta": ("Get Support", "/support/"),
     "img": IMG + "RTjbsnkPpAAeiE7d5IHsWvFzjco.png", "ratio": "428/269",
     "dim": False},
]

# Drawn scenes, one per service ("art" names a scene in build.py). The home
# cards keep their photos.
SERVICES_CARDS = [
    {"title": "Template Setup & Launch Support",
     "body": "Need help turning a template into a finished website? AmazeWeb can set up your Shopify template, replace placeholder content, adjust colors, connect pages, organize sections, and prepare your site for launch.",
     "cta": ("Learn More", "/services/setup/"),
     "art": "setup",
     "dim": True},
    {"title": "Custom Web Development",
     "body": "Need something built from scratch? AmazeWeb can design and develop a custom website based on your brand, content, features, and goals, giving you a site that feels made specifically for you.",
     "cta": ("Learn More", "/services/custom/"),
     "art": "custom",
     "dim": False},
    {"title": "Business Tools",
     "body": "Upgrade your site and business with extra tools and features. Add email design, signup forms, booking links, automations, AI tools, analytics, extra pages, product sections, and other integrations built around how your business works.",
     "cta": ("Learn More", "/services/tools/"),
     "art": "tools",
     "dim": False},
]

VISION = {"label": "Our Vision",
          "lead": "Design solutions that elevate brands and create seamless user experiences.",
          "tail": "I help bring ideas to life with strategy and creativity"}

def _svc(name, body, shots, tags, icon, variant="", art=None):
    """shots lists image files; art instead names a drawn tile set in build.py."""
    return {"name": name, "body": body, "shots": [IMG + s for s in shots],
            "tags": tags, "icon": icon, "variant": variant, "art": art}

HOME_SVC = [
    _svc("Creative Direction",
         "Shape the entire creative vision for your brand. Ensuring your identity feels intentional, distinctive, and unforgettable. Every touchpoint is crafted to tell your story with clarity, emotion, and impact.",
         ["LGDtCdeGWOBQctfcyQdUAqRQ.png", "Wob2IiVf0Qf8a4f3C8BGkgsGA.png", "mNl8apblPCRUgHesQx8Rjntd9vc.png"],
         ["Logo design", "Brand guideline", "Brand strategy", "+more"], "scan",
         art="branding"),
    _svc("Web Development",
         "Transforming designs into fully responsive and interactive websites. Whether it’s a landing page or a full-scale web experience, I build fast, modern sites optimized for seamless performance.",
         ["jqIuFi9hfEHbRxZa7p0SZHPsrkQ.png", "MVpdciinfDWQQ6UE6NdJFCe59oE.png", "VS8qzOk6qRLeJDr4BNatI7UAm8Q.png"],
         ["Landing page", "Multipages", "Web migration", "+more"], "code", "blue lift",
         art="webdev"),
    _svc("UI/UX Design",
         "Designing user-centered experiences that are both functional and visually engaging. From concept to final prototype, we focus on intuitive interfaces that drive engagement and enhance usability.",
         ["kFcT28JBAneTQjyVSMGiDyiwRlw.png", "Fm5dfyOw1px3Dsxu5sZmvHsOrKw.png", "6GwrKzXzNodjRpfhql82bLNul1E.jpg"],
         ["Web & app design", "Design system", "Prototyping", "+more"], "monitor", "drop",
         art="uiux"),
]

SERVICES_SVC = [
    _svc("Branding Design",
         "A strong brand is more than just a logo—it’s the foundation of how your audience perceives you. I create cohesive and impactful brand identities that ensure consistency and recognition across all touchpoints",
         ["82V0lDZt5IN8w9i1157kfT8pSU.jpg", "8ZlsEfjDITR5nOu3Yn61F22cbg.jpg", "Y1hHthCTPz6YNLIhonp2E5s5WU.jpg"],
         ["Logo design", "Brand guideline", "Brand strategy", "+more"], "scan",
         art="branding"),
    _svc("Web Development",
         "Transforming designs into fully responsive, interactive websites. Whether it’s a landing page or a full-scale web experience, I build fast, modern sites optimized for seamless performance",
         ["At4lVgdsU3vOE8OU9MxhtrSyU.png", "DxUbioKrcg6pEvPVPn8MKs3ShqY.png", "b89txAvenwqESiiy4RmX2Rq3cqw.png"],
         ["Landing page", "Multipages", "Web migration", "+more"], "code", "blue lift",
         art="webdev"),
    _svc("UI/UX Design",
         "Designing user-centered experiences that are both functional and visually engaging. From concept to final prototype, I focus on intuitive interfaces that drive engagement and enhance usability",
         ["kFcT28JBAneTQjyVSMGiDyiwRlw.png", "Fm5dfyOw1px3Dsxu5sZmvHsOrKw.png", "6GwrKzXzNodjRpfhql82bLNul1E.jpg"],
         ["Web & app design", "Design system", "Prototyping", "+more"], "monitor", "drop",
         art="uiux"),
]

# --- templates / themes ----------------------------------------------------
THEMES = [
    dict(slug="showcase", name="Showcase", kicker="Portfolio Site",
         sub="A portfolio template that puts selected work, proof, and a clear contact path in one polished narrative.",
         overview="Showcase is for work-led brands that need a calm, credible place to make the work count.",
         who="Independent creatives, studios, and consultants curating a focused body of work.",
         does="Project-led storytelling, selected-work pacing, and a direct inquiry path.",
         includes="Home, project pages, case-study modules, about, and a contact flow."),
    dict(slug="styler", name="Styler", kicker="Fashion & Style Site",
         sub="A fashion-forward concept for collections, editorial storytelling, and a distinct visual point of view.",
         overview="Styler is tailored for brands that want their visual identity and latest edit to lead the conversation.",
         who="Stylists, fashion labels, boutiques, and image-led personal brands.",
         does="Collection framing, visual hierarchy, and lookbook-ready pacing.",
         includes="Home, a filterable collection, a product page with colour and size, a shop-the-look lookbook with hotspots, and a working cart."),
    dict(slug="artist-site", name="Arts", kicker="Artist Site",
         sub="An artist-focused presence designed to make a body of work feel intentional, current, and easy to explore.",
         overview="Arts keeps the focus on the work while giving each release, exhibition, or commission a clear place to land.",
         who="Visual artists, makers, illustrators, and creative practices.",
         does="Work curation, exhibition context, and a direct collector or inquiry route.",
         includes="Home, gallery with series filter and salon or grid hang, exhibitions and CV, editions shop, about, and an enquiry form."),
    dict(slug="startup-site", name="Startup", kicker="Startup Site",
         sub="A launch-ready concept built to explain a new offer, establish trust, and move visitors toward action.",
         overview="Startup helps a young product communicate why it matters before visitors have time to scroll away.",
         who="Early-stage products, founders, and teams preparing a clear first impression.",
         does="Value-proposition clarity, proof placement, and conversion-focused next steps.",
         includes="Home, product, pricing with a monthly and yearly toggle, a filterable changelog, and contact."),
    dict(slug="real-estate-site", name="Realtor", kicker="Real Estate Site",
         sub="A considered real-estate concept for presenting listings, local knowledge, and a trusted advisor relationship.",
         overview="Realtor organizes local expertise and property discovery around the decisions clients need to make.",
         who="Independent agents, broker teams, and property specialists.",
         does="Listing discovery, credibility building, and inquiry capture.",
         includes="Home, listings with filter and sort, a single-property brief with a monthly cost estimator, neighborhood guides, and an inquiry form."),
    dict(slug="production-site", name="Production", kicker="Production Studio Site",
         sub="A studio-led concept for showcasing reels, capabilities, and the people behind memorable work.",
         overview="Production gives motion-led work a confident home without turning the studio story into an afterthought.",
         who="Production companies, creative studios, filmmakers, and directors.",
         does="Reel-first impact, service clarity, and project inquiry momentum.",
         includes="Home reel with scrubbable frames, filterable work index, a project page with credits, services and rates, studio, and a brief form."),
    dict(slug="restaurant-site", name="Restaurant", kicker="Restaurant Site",
         sub="A warm restaurant concept for turning appetite into reservations, orders, and repeat visits.",
         overview="Restaurant makes the essentials easy to find while keeping the dining experience front and center.",
         who="Restaurants, cafés, bars, chefs, and hospitality concepts.",
         does="Menu discovery, atmosphere building, and reservation or order actions.",
         includes="Home, a menu that switches by day part, reservations with slot picking, events and private dining, and a visit page with hours."),
    dict(slug="blue-collar-site", name="Handy", kicker="Home Services Site",
         sub="A practical home-services concept that makes capability, coverage, and booking feel immediately clear.",
         overview="Handy is built to turn local searches into confident calls and quote requests.",
         who="Tradespeople, contractors, repair businesses, and local home-service teams.",
         does="Trust signals, service clarity, and fast estimate requests.",
         includes="Home, services, service area, reviews, contact, and an estimate form."),
    dict(slug="clothing-site", name="Mod", kicker="Clothing Site",
         sub="A clothing concept that frames a collection with strong visual rhythm and an uncomplicated path to shop.",
         overview="Mod lets the clothes set the tone, then makes it simple to move from inspiration to purchase.",
         who="Independent apparel labels, capsule collections, and design-led retailers.",
         does="Collection discovery, product focus, and clear shopping actions.",
         includes="Home, a shop whose cards recolour in place, a product page with per-colour stock, a full size guide, and a working cart."),
    dict(slug="cosmetics-site", name="Beauty", kicker="Cosmetics Site",
         sub="A cosmetics concept built to make product benefits, routines, and brand character feel beautifully connected.",
         overview="Beauty guides visitors from discovery to a confident routine without losing the brand’s point of view.",
         who="Skincare, cosmetics, wellness, and beauty brands.",
         does="Routine guidance, product education, and purchase confidence.",
         includes="Home, shop filtered by routine step, a product page with full percentages, a routine builder covering eight cases, and a working cart."),
    dict(slug="pupper", name="Pupper", kicker="Pet Business Site",
         sub="A friendly pet-business concept that balances personality with the practical details owners need.",
         overview="Pupper makes it easy for pet owners to understand the service and take the next step.",
         who="Pet care, grooming, training, boarding, and pet-focused local brands.",
         does="Service trust, booking clarity, and warm owner reassurance.",
         includes="Home, services with a live price estimator, a booking request form, the day hour by hour, team, and unedited reviews."),
    dict(slug="icon", name="Icon", kicker="Boutique Site",
         sub="A boutique concept for editing a distinctive point of view into an inviting, easy-to-shop experience.",
         overview="Icon brings a careful retail edit to the web with room for the brand story behind every collection.",
         who="Boutiques, specialty retailers, and independent lifestyle stores.",
         does="Curated discovery, product confidence, and repeatable brand recognition.",
         includes="Home, shop with separate online and in-shop stock, a product page, visit and opening hours, and a cart that splits paying now from collecting."),
    dict(slug="drop", name="Drop", kicker="Product Launch Site",
         sub="A launch-page concept for concentrating anticipation, key product details, and a decisive next action.",
         overview="Drop keeps the launch story focused so a visitor understands the moment and knows exactly what to do next.",
         who="New products, limited releases, campaigns, and founder launches.",
         does="Message focus, launch timing, and action-oriented conversion.",
         includes="Home, product page, release details, proof, email signup, cart, and checkout flow."),
    dict(slug="kiddie", name="Fun Time", kicker="Kids Site",
         sub="A bright, family-friendly concept that helps parents understand the offer while keeping the experience approachable.",
         overview="Fun Time makes key parent decisions easy while leaving space for the brand’s playful energy.",
         who="Kids’ brands, family activities, learning programs, and playful local services.",
         does="Parent reassurance, offer clarity, and simple enrollment or inquiry paths.",
         includes="Home, programs and holiday camps, a weekly timetable, safety and fees, and contact — all filtered by one age control."),
]

# ---------------------------------------------------------------- commerce
# One set of purchase terms, inherited by all 14 theme pages. The money
# fields are deliberately None: a page falls back to "Coming Soon" until a
# real number is set here, so nothing false is ever published. Setting
# `price` publishes it everywhere at once.
COMMERCE = {
    "note":        "One-time template access",
    "price":       None,          # e.g. "$79"
    "setup_from":  None,          # e.g. "$249" -- shown as "Setup from $249"
    "support":     "Includes 30 days of setup support after purchase.",
    "license":     "One license covers one live site.",
    # Stripe Payment Link per template, e.g. "https://buy.stripe.com/xxx".
    # With one set, the theme page shows a Buy button instead of only "Ask".
    "buy_url":     None,
    "excluded_h":  "Not included",
    "excluded":    "Content writing, custom sections, brand design, and ongoing "
                   "changes after launch. Setup and add-ons are available separately.",
}

# Templates that are actually built, with a live demo and real screenshots.
# A theme not listed here keeps the striped placeholder and shows no demo
# button, so the page never promises a preview that does not exist.
# Images live at /assets/img/tpl/<slug>-{card,hero,desk,tab,phone}.png
BUILT = {
    "drop":             "/demo/drop/",
    "showcase":         "/demo/showcase/",
    "blue-collar-site": "/demo/handy/",
    "artist-site":      "/demo/arts/",
    "startup-site":     "/demo/startup/",
    "real-estate-site": "/demo/realtor/",
    "production-site":  "/demo/production/",
    "restaurant-site":  "/demo/restaurant/",
    "pupper":           "/demo/pupper/",
    "kiddie":           "/demo/funtime/",
    "styler":           "/demo/styler/",
    "clothing-site":    "/demo/mod/",
    "cosmetics-site":   "/demo/beauty/",
    "icon":             "/demo/icon/",
}
for _t in THEMES:
    if _t["slug"] in BUILT:
        _t["demo"]  = BUILT[_t["slug"]]
        _t["shots"] = f'/assets/img/tpl/{_t["slug"]}'

# Setup tiers, shown on /services/setup/. The block is skipped entirely while
# this is empty, so the page never advertises a tier that has no price.
# Shape: dict(name=..., price=..., summary=..., includes=[...])
SETUP_TIERS = []

# Which templates ship as Shopify themes. The rest are not storefronts, so they
# carry no platform tag at all rather than a second label that says "not Shopify".
SHOPIFY_THEMES = {"styler", "clothing-site", "cosmetics-site", "icon", "drop"}
for _t in THEMES:
    if _t["slug"] in SHOPIFY_THEMES:
        _t["platform"] = "Shopify"
    else:
        # Not a storefront, so not something a buyer could install and use on
        # their own. These are shown on /services/custom/ as work we have
        # built, and are not for sale.
        _t["example"] = True

# Said plainly on every example page and over the gallery: these are our own
# builds with invented brands, not commissioned client work.
EXAMPLES_HEAD = "Sites we have built"
EXAMPLES_NOTE = ("Each of these is a complete, working site you can click through. They are our "
                 "own builds, made to show the standard and the range — the businesses in them "
                 "are invented, not clients.")
EXAMPLE_LEAD = ("This is one of our own builds, not a client project. The brand, the words and "
                "the pictures in it are invented; the site itself is real and you can use every "
                "page of it. Yours would be built the same way, around your business.")

THEME_SLUG_TO_CARD = {t["slug"]: t for t in THEMES}

MAKE_IT_YOURS = ("Customize colors, fonts, imagery, copy, sections, and buttons to fit your brand. "
    "Template access includes the responsive layout and any instructions or resources supplied with "
    "the final product. Basic support covers access and template-use questions; optional setup and "
    "launch support is available separately.")

# --- services sub-pages ----------------------------------------------------
# Transcribed from the published pages. Note two things the live site does:
#   * /services/custom reuses the /services/tools intro panel copy verbatim.
#   * every section heading below has an empty body on the live site.
# Statements are (grey_clause, black_clause); grey may be "".
_P2 = {"title": "Not sure what you need? Tell us about your business.",
       "body": "Describe what is happening and we will recommend the smallest thing that "
               "fixes it, even when that means spending less with us.",
       "cta": ("Learn More", "/support/#support-message"),
       "dim": False}

_TOOLS_INTRO = {
    "title": "Simple digital tools that help customers find, contact and review your business.",
    "body": "Each of these works on its own, costs a fraction of a website, and starts paying "
            "for itself the week it goes live. Most customers start here and build up from it.",
    "cta": ("Learn More", "/support/#support-message"),
    "dim": True}

SERVICE_PAGES = {
 "setup": {
   "title": "Setup & Add-Ons | Amazé Web",
   "desc": "Template setup and launch support from AmazeWeb: installation, your own content, "
           "domain connection, and a site that works on a phone.",
   "hero": ("Setup & Add-Ons.", "You choose the design, we handle the build."),
   "panel": {"title": "You choose the design. We handle the setup.",
             "body": "Buying a template is the easy part. Getting it installed, filled with your "
                     "own words and images, connected to your domain and working properly on a "
                     "phone is where most people stall. That is the part we do.",
             "cta": ("Buy Template Setup", "/support/#support-message"),
             "dim": True},
   "sections": [
     ("Setup", "Everything between buying a template and", "having a website that works."),
     ("Add-Ons", "", "Bolt on whatever the template didn’t come with."),
     ("How it runs", "", "Four steps, and the first one takes a minute."),
     ("Other ways we help", "", ""),
   ],
   "panel2": _P2,
 },
 "custom": {
   "title": "Custom Websites | Amazé Web",
   "desc": "A custom website from AmazeWeb, designed and built from scratch around your brand, "
           "content, features, and goals.",
   "hero": ("Custom Website.", "Built from scratch around your business."),
   "panel": _TOOLS_INTRO,
   "sections": [
     ("What you get", "Three levels,", "depending on how much already exists."),
     ("What we build", "", "Different businesses, same standard."),
     ("Process", "", "You see it in the browser halfway through, not at the end."),
     ("Before we start", "", "What we will need from you."),
     ("Other ways we help", "", ""),
   ],
   "panel2": _P2,
 },
 "tools": {
   "title": "Business Tools | Amazé Web",
   "desc": "Small digital tools from AmazeWeb that help customers find, contact and review "
           "your business.",
   "hero": ("Business Tools.", "Small things that bring customers in."),
   "panel": _TOOLS_INTRO,
   "sections": [
     ("Get found and reviewed", "Most local customers decide.", "before they ever reach your website."),
     ("Everyday Tools", "", "One link, one scan, one page that does its job."),
     ("Email & automation", "Most small businesses do not lose customers to competitors.",
      "They lose them to nobody answering."),
     # live page reads "Other way we help" (missing s) — kept verbatim
     ("Other way we help", "", ""),
   ],
   "panel2": _P2,
 },
}
