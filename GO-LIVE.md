# Artisan at Home — Go-Live Checklist

The site is built and QA'd. These are the steps to switch `artisanathome.nz` over from WordPress to the new site.

## The switch-over (in order)

1. **Publish the latest site to Vercel** (your usual Publish step / git push). This deploys everything you see now.

2. **Add the domain in Vercel** — in the Vercel project, add `artisanathome.nz` (and `www.artisanathome.nz`) as custom domains. Vercel will show you the DNS records it needs.

3. **Point the DNS at Vercel** — at your domain host (1st Domains), update the records to the ones Vercel gives you (usually an A record and/or CNAME).
   - **⚠️ KEEP your existing MX records** (and any TXT/SPF records) exactly as they are, so email to **@artisanathome.nz keeps working.** Only change the web records.

4. **Wait for DNS to propagate** (minutes to a few hours). Once `artisanathome.nz` shows the new site, you're live.

5. **Test the forms on the live domain** — send a test through the Contact, Wedding, Event and Order forms and confirm the email arrives and you land on the branded thank-you page. (The forms now redirect to your own thank-you page automatically on whatever domain they're on — no redirect changes needed.)

## Already done
- All forms tested and working (redirects point to the Vercel preview for now — flip to the live domain at go-live)
- Every page on the new header/footer/nav
- Links, images and responsive layouts checked

## Work-in-progress (safe to add after launch — not blockers)
- Menus page: banner image, Walk 'n Fork menu content, section photos
- Corporate order page: item thumbnails (data is preserved; toggled off until photos are ready)
- Old `/faqs/` page can be deleted (FAQs now live on the service pages)

## SEO polish (after launch)
- Submit `sitemap.xml` in Google Search Console
- Suburb targeting (Devonport, Takapuna, Matakana, etc.)

## Post-launch backlog
- **Website security check** — confirm HTTPS is enforced (http → https redirect), review security headers, and check form spam protection.
- **Decommission the old website** — once the new site is confirmed live and stable, cancel/turn off the old WordPress web hosting at 1st Domains (keep the domain + email; only remove the old hosting).
