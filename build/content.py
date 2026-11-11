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
         "Choose a template, buy it, and receive everything you need to customize and launch your website."),
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
# One set of purchase terms, inherited by every template page. One price for
# all five Shopify themes, set here and published everywhere at once. Setting
# a money field back to None returns that line to its honest empty state
# ("Coming Soon", no price on the card), so nothing false is ever published.
COMMERCE = {
    "note":        "One-time template access",
    "price":       "$299",
    "setup_from":  "$499",        # shown as "Setup from $499"
    "support":     "Includes 30 days of setup support after purchase.",
    "license":     "One license covers one live site.",
    # Stripe Payment Link per template, e.g. "https://buy.stripe.com/xxx".
    # With one set, the theme page shows a Buy button instead of only "Ask".
    "buy_url":     None,
    "excluded_h":  "Not included",
    "excluded":    "Content writing, custom sections, brand design, and ongoing "
                   "changes after launch. Setup and add-ons are available separately.",
}

# The price belongs in the FAQ too, and the FAQ must never disagree with the
# theme pages about it. Appended here rather than written into FAQ above,
# because it reads from COMMERCE -- and it disappears with the price.
if COMMERCE["price"]:
    _p, _s = COMMERCE["price"], COMMERCE.get("setup_from")
    FAQ[0][1].append((
        "What does it cost?",
        f"A Shopify template is {_p}, one-time, for a theme you install on your own store."
        + (f" Setup starts at {_s} if you would rather we installed it and put your content "
           f"in for you." if _s else "")
        + " Custom builds are quoted after a call, and the smaller business tools are priced "
          "individually on the page that lists them."))

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
# Every figure says "from": the work scales with how much content there is to
# place, and a number without "from" in front of it is a promise.
SETUP_TIERS = [
  dict(name="Launch", price="from $499",
       summary="The template you bought, installed and live with your own content.",
       includes=[
         "The theme installed on your own store, on your own account",
         "Your words, pictures and products in place of the demo content",
         "Colours and type set to your brand",
         "Every page connected, including the legal pages a shop needs",
         "Your domain pointed at it, with your email left exactly as it was",
         "Checked on a real phone before it goes live",
       ]),
  dict(name="Complete", price="from $899",
       summary="Launch, plus the pages and the catalogue the template did not come with.",
       includes=[
         "Everything in Launch",
         "Up to three extra pages: about, FAQ, a second collection",
         "Up to 50 products loaded in, with variants and images",
         "A signup form and the welcome email it sends",
         "A review link worth sending, and analytics that tell you something",
       ]),
  dict(name="Done for you", price="from $1,600",
       summary="Everything, including the brand basics and the tools that bring work in.",
       includes=[
         "Everything in Complete",
         "Your logo tidied up, or made from scratch if there is not one yet",
         "Booking or enquiry that reaches the inbox you actually read",
         "An automatic reply, so nobody is left wondering",
         "60 days of support after launch instead of 30",
       ]),
]

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

# The work gallery mixes client projects with our own builds. Add a client
# build by naming it here -- slug: "Client name" -- and the gallery copy, the
# card badge and that build's own page all follow from it. Anything not listed
# is one of ours and says so, because a build with an invented business must
# never read as work somebody commissioned.
CLIENT_BUILDS = {}       # e.g. "restaurant-site": "Saltfold"

# The grey panel under the template grid: a template is not the only way in,
# and a custom build can be a storefront too.
CUSTOM_PITCH = {"title": "Want a custom site?",
                "body": "We build from scratch as well, storefronts included. If none of the "
                        "templates is the right fit, we design and build the site around your "
                        "business instead.",
                "cta": ("See what we have built", "/services/custom/#our-work"),
                "dim": False}

# Stated once above the template grid. It reads from COMMERCE, so the page can
# never disagree with the theme pages about what a template costs.
TEMPLATES_NOTE = ("{price} each, one-time, for a theme you install on your own store. "
                  "Setup from {setup} if you would rather we did it for you.")

EXAMPLES_HEAD = "Sites we have built"
# A mix of client projects and our own builds. The line does not count either
# kind, because the mix changes; each build's own page says which it is.
EXAMPLES_NOTE = ("Client projects and our own builds. Each one is a complete, working site you "
                 "can click through, and each says which it is.")

EXAMPLE_LEAD = ("One of our own builds. The brand, the words and the pictures in it are invented; "
                "the site itself is real and every page of it works. Yours would be built the "
                "same way, around your business.")
CLIENT_LEAD = "Built for {client}. A real site, live and in use."

for _t in THEMES:
    if _t["slug"] in CLIENT_BUILDS:
        _t["client"] = CLIENT_BUILDS[_t["slug"]]

THEME_SLUG_TO_CARD = {t["slug"]: t for t in THEMES}

MAKE_IT_YOURS = ("Customize colors, fonts, imagery, copy, sections, and buttons to fit your brand. "
    "Template access includes the responsive layout and any instructions or resources supplied with "
    "the final product. Basic support covers access and template-use questions; optional setup and "
    "launch support is available separately.")

# --- services sub-pages ----------------------------------------------------
# Transcribed from the published pages. Note two things the live site does:
#   * every section heading below has an empty body on the live site.
# Statements are (grey_clause, black_clause); grey may be "".
_P2 = {"title": "Not sure what you need? Tell us about your business.",
       "body": "Describe what is happening and we will recommend the smallest thing that "
               "fixes it, even when that means spending less with us.",
       "cta": ("Learn More", "/support/#support-message"),
       "dim": False}

_CUSTOM_INTRO = {
    "title": "When a template is not the shape of your business.",
    "body": "A template decides the pages, the order and the shape before it knows anything "
            "about you, and most of the time that is fine. When it is not \u2014 when the way you "
            "sell does not fit a layout somebody else drew \u2014 we start from what you actually "
            "do and build the site around it.",
    "cta": ("Start a custom build", "/support/#support-message"),
    "dim": True}

_TOOLS_INTRO = {
    "title": "Simple digital tools that help customers find, contact and review your business.",
    "body": "Each of these works on its own, costs a fraction of a website, and starts paying "
            "for itself the week it goes live. Most customers start here and build up from it.",
    "cta": ("Learn More", "/support/#support-message"),
    "dim": True}


# The same terms sit on the setup and tools pages, because they are the same
# terms. Anything a third party charges for its own account is theirs, not
# ours, and a page that quotes a price has to say so.
_PRICE_COVER = ("What the prices cover", "One-time, and agreed before anything starts.", "", [
    ("One-time, not a subscription",
     "You pay once for the work. We do not bill monthly, and nothing we set up stops "
     "working if you stop talking to us."),
    ("Everything in your own accounts",
     "The store, the domain, the listing and the inbox are all in your name, so it stays "
     "yours whatever happens to us."),
    ("What is not in the price",
     "Shopify’s own plan, your domain registration, and whatever a third-party tool "
     "charges for its paid tier. Those are paid by you, directly to them, and we will tell "
     "you which ones a job needs before it starts."),
    ("Where a price is a range, or says “from”",
     "The low end is the straightforward version of the job; the high end is the one with "
     "more in it — more pages, more products, more of the writing and the photography made "
     "by us rather than handed to us. You are told which end you are at, and why, before "
     "anything starts, never afterwards."),
], "list")

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
     ("Setup", "Everything between buying a template and", "having a website that works.", [
        ("The theme installed",
         "Into your own store, on your own account, so it stays yours whatever happens to us."),
        ("Your content where the placeholder text was",
         "Your words, your pictures, your products and the prices you want shown — not the "
         "demo copy the template shipped with."),
        ("Colours and type set to your brand",
         "So it looks like you rather than like the demo everybody else also bought."),
        ("Every page connected",
         "Navigation, footer, contact, and the legal pages a shop is expected to have."),
        ("Your domain pointed at it",
         "Connected properly, with your email left exactly as it was."),
        ("Checked on a phone",
         "Which is how most of your customers will see it, whatever you designed it on."),
     ], "list"),
     ("Add-Ons", "", "Bolt on whatever the template didn’t come with.", [
        ("Extra Page",
         "A page beyond the ones your tier covers: a second about, an FAQ, another "
         "collection, a landing page for one campaign. Built in the theme you already have, "
         "so it matches everything around it.", "$75–$125 a page"),
        ("Site Migration",
         "Your old site’s words and pictures brought across, and redirects set from the old "
         "addresses to the new ones, so Google keeps sending people to the pages you already "
         "rank for.", "$150–$300"),
        ("Shopify Email Setup",
         "Your signup form, the welcome email it sends and a branded template to reuse, set "
         "up inside Shopify, so what lands in an inbox looks like the store it came from.",
         "$150–$300"),
     ], "cards"),
     ("How it runs", "", "Four steps, and the first one takes a minute.", [
        ("Tell us which template",
         "That, plus whatever you already have: logo, pictures, words, product list. A rough "
         "pile is fine."),
        ("We install and fill it",
         "The theme goes into your store and your content replaces the demo content."),
        ("You look at a live link",
         "On your own phone. You mark what you want changed, and we change it."),
        ("We launch it",
         "Domain connected, site live, and a note of what was done and where everything is."),
     ], "steps"),
     _PRICE_COVER,
     ("Other ways we help", "", "", [
        ("Shopify templates", "/templates/"),
        ("Custom website", "/services/custom/"),
        ("Business tools", "/services/tools/"),
        ("Ask a question", "/support/#support-message"),
     ], "links"),
   ],
   "panel2": _P2,
 },
 "custom": {
   "title": "Custom Websites | Amazé Web",
   "desc": "A custom website from AmazeWeb, designed and built from scratch around your brand, "
           "content, features, and goals.",
   "hero": ("Custom Website.", "Built from scratch around your business."),
   "panel": _CUSTOM_INTRO,
   "sections": [
     ("What you get", "Three levels,", "depending on how much already exists.", [
        ("Site only",
         "You have a name, a logo and a rough idea of what the pages should say. We design "
         "and build the site, put your words and pictures in, connect your domain and launch it.",
         "Quoted"),
        ("Site and brand",
         "There is no logo yet, or it was made in a hurry and you have never liked it. We "
         "settle the name treatment, the colours and the type first, then build on top of that.",
         "Quoted"),
        ("Site, brand and the tools around it",
         "The site, plus the things that actually bring work in: enquiry forms, booking, email, "
         "review links and analytics, set up and working on the day it goes live.",
         "Quoted"),
     ], "cards"),
     ("What we build", "", "Different businesses, same standard.", [
        ("Storefronts",
         "Shopify, built around your products instead of bending a theme until it nearly fits."),
        ("Service businesses",
         "Trades, clinics, studios. Prices visible, and a way to book that works on a phone "
         "held in one hand."),
        ("Food and venues",
         "A menu you can change yourself, opening hours that are right, and a table booked "
         "in two taps."),
        ("Portfolios and galleries",
         "The work first and large, with a contact path that does not get lost underneath it."),
        ("Launches",
         "One page, one date, one thing for the visitor to do."),
     ], "list"),
     ("Process", "", "You see it in the browser halfway through, not at the end.", [
        ("A call, then a brief",
         "What the business does, who buys from you, and what has to happen on the site for "
         "it to be worth building. Written down, so we are both working from the same page."),
        ("Structure and words",
         "Which pages exist, in what order, and what each one says. Agreed before anything "
         "is designed, because moving a sentence is cheap and moving a page is not."),
        ("Design in the browser",
         "A real link you can open on your own phone, not a flat picture of a website. You "
         "tell us what to change while it is still easy to change."),
        ("Build and test",
         "Real devices and real browsers. Every link followed, every form submitted, every "
         "page checked at phone, tablet and desktop width."),
        ("Launch",
         "Domain connected, the site live, and your email left exactly as it was."),
     ], "steps"),
     ("Before we start", "", "What we will need from you.", [
        ("Your logo",
         "As a file rather than a screenshot of one. If you do not have it, say so and we "
         "will make one."),
        ("Pictures you are allowed to use",
         "Your own photos are best. We will tell you what is missing and what we can source."),
        ("What you sell, and for how much",
         "Services or products, with the prices you want shown. If prices are not public, "
         "that is a decision, not a blocker."),
        ("Whatever words already exist",
         "An old site, a flyer, a rough list in your notes. Anything beats a blank page."),
        ("Access to your domain",
         "The login for wherever it is registered, or the go-ahead for us to buy one for you."),
        ("One person who decides",
         "Two people with different opinions is the single most common reason a build runs "
         "long."),
     ], "list"),
     ("What it costs", "Every custom build is quoted.",
      "No two are the same shape, so no two cost the same.", [
        ("You get one figure, in writing, before anything starts",
         "After the call and the brief we send a single price for the whole build. It does "
         "not move unless you ask for something that was not in the brief, and then you see "
         "the new figure before we touch it."),
        ("What moves the number",
         "How many pages there are, whether a brand exists yet, whether products, booking or "
         "payments have to work, and how much of the writing and the photography we are "
         "making rather than being handed."),
        ("What is not in it",
         "Shopify’s own plan, your domain, and anything a third-party tool charges for its "
         "paid tier. Those are paid by you, directly to them."),
        ("The smaller version, if there is one",
         "If a template plus setup would do the same job for less, we will say so and point "
         "you at it instead of quoting you for a custom build you do not need."),
     ], "list"),
     ("Other ways we help", "", "", [
        ("Shopify templates", "/templates/"),
        ("Template setup and launch", "/services/setup/"),
        ("Business tools", "/services/tools/"),
        ("Ask a question", "/support/#support-message"),
     ], "links"),
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
     # Named products, same as Everyday Tools. The two lines that used to sit
     # here and were not products -- photo guidance, and an argument for
     # buying a website -- are gone: the first folded into the profile setup,
     # the second was a sales line in a list of prices.
     ("Get found and reviewed", "Most local customers decide.",
      "before they ever reach your website.", [
        ("Google Business Profile Setup",
         "The hours, the phone number, the address and the category, correct and saying the "
         "same thing everywhere somebody might look, plus a list of the photos of the real "
         "place worth taking.", "$75–$150"),
        ("Google Review NFC Card",
         "One branded card a customer taps with their phone to land straight on your Google "
         "review box. A QR code on the back for phones that will not tap, programmed and "
         "tested before it reaches you. No app, no typing, no finding you on a map first.",
         "$50–$75"),
        ("Review Starter Pack",
         "The same card, two or three of them, so there is one at the till, one where people "
         "wait and one by the door — plus a printable QR sign for the counter. The whole "
         "place set up to collect reviews rather than one spot in it.", "$100–$150"),
     ], "cards"),
     ("Everyday Tools", "", "One link, one tap, one page that does its job.", [
        ("Link-in-Bio Site",
         "One page holding your menu, your booking, your number and your socials, for the "
         "bio field that only allows a single link.", "$100–$200"),
        ("Digital NFC Business Card",
         "A card somebody taps with their phone to get your details, your booking page or "
         "your socials. You can change where it points later without reprinting anything.",
         "$50–$100"),
        ("Booking Page",
         "Pick a slot, leave a number, done — on a phone, without ringing anybody.",
         "$100–$250"),
        ("QR Menu",
         "Your menu or price list on a page you can edit yourself, behind a code people scan "
         "at the table. Changing a price should not mean asking somebody and waiting a week.",
         "$75–$150"),
     ], "cards"),
     ("Email & automation", "Most small businesses do not lose customers to competitors.",
      "They lose them to nobody answering.", [
        ("Automatic Reply",
         "The moment somebody contacts you they get an answer saying you have it and when a "
         "person will come back to them. It stops them ringing the next business on the "
         "list while they wait.", "$50–$75"),
        ("Post-Job Follow-Up",
         "A thank-you and a review ask, sent a few days after the job without you "
         "remembering to send it. Wired to whatever marks a job finished, which is where "
         "most reviews actually come from.", "$150–$250"),
        ("Email Template",
         "A branded shell you reuse for an offer, a change of hours, a quiet month or a "
         "regular newsletter. You add the words; it already looks like you.", "$100–$150"),
        ("Marketing Email",
         "One email designed and built for a particular send, so it arrives looking right "
         "in Gmail, Outlook and on a phone instead of falling apart in half of them.",
         "$125–$200"),
     ], "cards"),
     _PRICE_COVER,
     ("Other ways we help", "", "", [
        ("Shopify templates", "/templates/"),
        ("Template setup and launch", "/services/setup/"),
        ("Custom website", "/services/custom/"),
        ("Ask a question", "/support/#support-message"),
     ], "links"),
   ],
   "panel2": _P2,
 },
}
