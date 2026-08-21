// Secure Stripe Checkout for the corporate catering order form.
// Recomputes/validates every line price against the real menu (menu-data.js)
// so the amount charged can't be tampered with from the browser.
// Requires a Vercel Environment Variable: STRIPE_SECRET_KEY

const Stripe = require('stripe');
const { MENU } = require('../menu-data.js');

// Build the set of every legitimate "label||price" the menu can produce
function buildValidSet() {
  const set = new Set();
  const add = (label, price) => set.add(label + '||' + Number(price).toFixed(2));
  (MENU || []).forEach((cat) => (cat.groups || []).forEach((group) => (group.options || []).forEach((opt) => {
    const base = opt.name || group.name || 'Item';
    if (opt.variants) {
      opt.variants.forEach((v) => add(base + ' — ' + v.label, v.price));
    } else if (opt.addons) {
      const n = opt.addons.length;
      for (let m = 0; m < (1 << n); m++) {
        const names = []; let price = opt.price;
        for (let k = 0; k < n; k++) { if (m & (1 << k)) { names.push(opt.addons[k].label); price += opt.addons[k].price; } }
        add(names.length ? base + ' (+ ' + names.join(', ') + ')' : base, price);
      }
    } else {
      add(base, opt.price);
    }
  })));
  return set;
}
const VALID = buildValidSet();

module.exports = async (req, res) => {
  if (req.method !== 'POST') { res.status(405).json({ error: 'Method not allowed' }); return; }
  if (!process.env.STRIPE_SECRET_KEY) { res.status(500).json({ error: 'Payments are not configured yet.' }); return; }

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
    const items = Array.isArray(body.items) ? body.items : [];
    const details = body.details || {};
    if (!items.length) { res.status(400).json({ error: 'Your order is empty.' }); return; }

    const line_items = [];
    for (const it of items) {
      const price = Number(it.price);
      const qty = parseInt(it.qty, 10);
      if (!it.label || !(price >= 0) || !(qty >= 1)) { res.status(400).json({ error: 'Invalid item in order.' }); return; }
      if (!VALID.has(String(it.label) + '||' + price.toFixed(2))) {
        res.status(400).json({ error: 'Item not recognised: ' + it.label }); return;
      }
      line_items.push({
        price_data: { currency: 'nzd', product_data: { name: String(it.label).slice(0, 250) }, unit_amount: Math.round(price * 100) },
        quantity: qty
      });
    }

    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
    const origin = req.headers.origin || ('https://' + req.headers.host);
    const md = {};
    ['contact_name', 'company', 'email', 'phone', 'delivery_address', 'date_required', 'delivery_time', 'headcount', 'dietary', 'notes']
      .forEach((k) => { if (details[k]) md[k] = String(details[k]).slice(0, 480); });

    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      line_items,
      customer_email: details.email || undefined,
      success_url: origin + '/order-received/?paid=1',
      cancel_url: origin + '/services/corporate-catering/',
      metadata: md
    });
    res.status(200).json({ url: session.url });
  } catch (err) {
    res.status(500).json({ error: 'Sorry, we could not start checkout.', detail: String((err && err.message) || err) });
  }
};
