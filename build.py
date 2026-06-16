#!/usr/bin/env python3
"""Generate all pages for artisanathome.nz static site."""
import os

ROOT = "/home/claude/artisanathome"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://artisanathome.nz{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://artisanathome.nz{path}">
<meta property="og:image" content="https://artisanathome.nz/images/og-image.png">
<meta property="og:site_name" content="Artisan at Home">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>
<a class="skip-link" href="#content">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Artisan at Home — home">
      <img src="/images/logo-mark.png" alt="Artisan at Home logo" width="120" height="56">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <a href="/" {c_home}>Home</a>
      <div class="has-sub">
        <a href="/services/" {c_services}>Services</a>
        <div class="sub">
          <a href="/services/private-chef/">Private Chef Experience</a>
          <a href="/services/event-catering/">Event Catering</a>
          <a href="/services/corporate-catering/">Corporate Catering</a>
        </div>
      </div>
      <a href="/our-story/" {c_story}>Our Story</a>
      <a href="/faqs/" {c_faqs}>FAQs</a>
      <a href="/contact-us/" {c_contact}>Contact Us</a>
      <a class="book-btn" href="/contact-us/">Book</a>
    </nav>
  </div>
</header>
<main id="content">
"""

FOOTER = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="/images/logo-green.png" alt="Artisan at Home logomark">
      </div>
      <div>
        <h4>Explore</h4>
        <div class="footer-links">
          <a href="/services/private-chef/">Private Chef Experience</a>
          <a href="/services/event-catering/">Wedding Catering</a>
          <a href="/services/corporate-catering/">Corporate Catering</a>
          <a href="/services/event-catering/">Event Catering</a>
        </div>
      </div>
      <div class="footer-contact">
        <h4>Connect</h4>
        <p><strong>M:</strong> <a href="tel:0275723373">027 572 3373</a></p>
        <p><strong>E:</strong> <a href="mailto:hello@artisanathome.nz">hello@artisanathome.nz</a></p>
        <p><strong>L:</strong> Auckland, NZ</p>
        <div class="footer-social">
          <a href="https://www.instagram.com/artisanathome.nz" rel="noopener" target="_blank">Instagram</a>
          <a href="https://www.facebook.com/profile.php?id=61585152107425" rel="noopener" target="_blank">Facebook</a>
        </div>
      </div>
    </div>
    <div class="footer-base">Website made with love, sweat &amp; tears by Abi. &copy; 2026 Artisan at Home.</div>
  </div>
</footer>
<script src="/js/main.js"></script>
</body>
</html>
"""

def write_page(relpath, title, desc, canonical, body, active):
    keys = {"c_home": "", "c_services": "", "c_story": "", "c_faqs": "", "c_contact": ""}
    if active:
        keys["c_" + active] = 'aria-current="page"'
    html = HEAD.format(title=title, desc=desc, path=canonical, **keys) + body + FOOTER
    out = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)
    print("wrote", relpath)

# Page bodies are defined in pages_content.py
from pages_content import PAGES

for p in PAGES:
    write_page(**p)
