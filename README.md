# Artisan at Home — Static Site (WordPress → Vercel migration)

A faithful static rebuild of artisanathome.nz. All page content, menus, FAQs and pricing were transcribed from the live WordPress site (June 2026). No WordPress, no Elementor, no plugins — just fast HTML/CSS/JS.

## Site structure

```
/                                  Home
/services/                         Services overview
/services/private-chef/            Private Chef Experience (degustation + banquet menus)
/services/event-catering/          Event & Wedding Catering (full menus)
/services/corporate-catering/      Corporate Catering (menus, packages, order form)
/our-story/                        Our Story
/faqs/                             FAQs
/contact-us/                       Contact (enquiry form)
404.html                           Not-found page
```

URLs match the old WordPress site exactly, so Google rankings and existing links keep working. `vercel.json` also redirects old/legacy paths (e.g. `/private-chef` → `/services/private-chef/`).

## Before you deploy — 3 manual steps

### 1. Download the images (do this FIRST, while WordPress is still online)

The HTML references local images in `/images/`, but I couldn't download them for you. On your computer, open a terminal in this folder and run:

```bash
bash download-images.sh
```

This pulls all 14 images + the corporate menu PDF from the live site. **Do this before you switch DNS away from WordPress**, or the images will become unreachable.

### 2. Set up the contact forms

WordPress handled your form submissions; a static site needs a form service. The easiest free option is Formspree:

1. Sign up at https://formspree.io (free tier: 50 submissions/month)
2. Create a form, set the email to hello@artisanathome.nz
3. Copy your form ID (looks like `xqkrwzyz`)
4. Replace `YOUR_FORM_ID` in **two files**:
   - `contact-us/index.html` (contact form)
   - `services/corporate-catering/index.html` (order form — you can create a second Formspree form for this so orders are labelled separately)

Until you do this, the forms won't deliver — but the Email Us / Call buttons work regardless.

### 3. Deploy to Vercel

**Option A — Vercel CLI (quickest, no GitHub needed):**
```bash
npm install -g vercel
cd <this folder>
vercel login          # log in with your email or GitHub
vercel --prod         # answer the prompts; accept defaults
```

**Option B — GitHub (better long-term: every push auto-deploys):**
1. Create a repo on GitHub and push this folder to it
2. Go to https://vercel.com/new → Import the repo
3. Framework preset: **Other**. No build command, no output directory. Deploy.

Either way you'll get a `something.vercel.app` preview URL. Check every page there before touching DNS.

### 4. Point your domain at Vercel

1. In Vercel: Project → Settings → Domains → add `artisanathome.nz` and `www.artisanathome.nz`
2. Vercel will show you the DNS records to set. At your domain registrar (wherever artisanathome.nz is registered — likely the same place you bought WordPress hosting, or a NZ registrar):
   - `A` record for `artisanathome.nz` → `76.76.21.21`
   - `CNAME` for `www` → `cname.vercel-dns.com`
   (Use the exact values Vercel shows you — they can vary.)
3. DNS can take up to 24–48h to propagate, usually much faster. HTTPS certificates are automatic.

### 5. After go-live

- Keep your WordPress hosting alive for a week or two as a safety net, then cancel it.
- **Email check:** if your hello@artisanathome.nz email is hosted with the same provider as WordPress, do NOT delete the MX records when changing DNS — only change the A/CNAME records. If unsure, screenshot your current DNS records before touching anything.
- In Google Search Console, verify the site (the verification meta tag from WordPress was Site Kit's; re-verify via DNS) and submit `https://artisanathome.nz/sitemap.xml`.
- Optionally compress images (favicon.png is 2048px — 512px is plenty) at https://squoosh.app.

## Editing the site later

The HTML pages are hand-editable. If you prefer, the `build.py` / `pages_content.py` / `service_pages.py` files regenerate all pages from one place (run `python3 build.py`) — handy when updating the header, footer, or menus seasonally. These build files are excluded from deployment via `.vercelignore`.

## What changed vs WordPress

- Same content, same URLs, same brand (green/cream, serif italics, the "· eyebrow ·" labels)
- Rebuilt without Elementor — pages are a fraction of the size and load much faster
- Fixed a few broken footer links that existed on the old site (e.g. `/services//event-catering`)
- Forms now use Formspree instead of WordPress
- The "Kitchen Hero" footer link pointed to a page that didn't exist; `/kitchen-hero` now redirects to the contact page (change in vercel.json if you add that page later)
