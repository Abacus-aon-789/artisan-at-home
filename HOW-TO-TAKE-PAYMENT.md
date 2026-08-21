# How to take payment for catering orders 💳

Your corporate catering page lets customers **build an order and send it to you**.
No money is taken on the website — you confirm the order, then collect payment
through **Stripe**. Here's the simple routine.

---

## When an order comes in

1. You'll get an **email** (subject: "New catering order from website") with:
   - The customer's contact + delivery details
   - The full itemised order and subtotal
2. Check your **date and availability**, and reply to the customer to confirm.

## Collecting payment with Stripe

The easiest way (no website code, no developer needed):

**Option A — Stripe Invoice (recommended for catering)**
1. Log in to your Stripe Dashboard → **Invoices** → **Create invoice**
2. Add the customer's email
3. Add line items (or one line "Catering order — [date]") for the agreed total
4. Add delivery as a separate line if it applies
5. Send — Stripe emails the customer a secure pay link and chases it for you

**Option B — Stripe Payment Link**
1. Stripe Dashboard → **Payment links** → **Create**
2. Set the amount, create the link, and paste it into your reply email
3. Customer clicks and pays by card

Either way, Stripe handles the card details securely — nothing sensitive ever
touches your website. You get paid into your bank as normal.

## Tips

- Keep a simple deposit policy if you like (e.g. 50% to confirm, balance before
  delivery) — just create two invoices/links.
- Stripe charges a small fee per transaction (a percentage + a few cents); check
  current NZ rates in your Stripe dashboard.
- Save a reusable invoice template in Stripe to make repeat orders faster.

---

## Later upgrade (optional)

If you ever want customers to **pay instantly on the website** at checkout
(instead of you sending a link), that can be added — it connects the site
directly to Stripe Checkout. Just ask Claude when you're ready. For now,
"confirm then send a payment link" keeps you in control of availability.

---

*Made with Claude. Keep this in your ArtisanWebsite folder for reference.*
