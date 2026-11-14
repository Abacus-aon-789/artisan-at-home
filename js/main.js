// Artisan at Home — shared interactions

// Clear any leftover service worker / cache from the old website, so returning
// visitors (and saved bookmarks) always load the current site, not a stale copy.
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.getRegistrations().then(function (regs) {
    regs.forEach(function (r) { r.unregister(); });
  }).catch(function () {});
}
if (window.caches && caches.keys) {
  caches.keys().then(function (keys) {
    keys.forEach(function (k) { caches.delete(k); });
  }).catch(function () {});
}

// Mobile navigation
const navToggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".nav");
if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
}

// FAQ accordion
document.querySelectorAll(".faq-q").forEach((btn) => {
  btn.addEventListener("click", () => {
    const item = btn.closest(".faq-item");
    const open = item.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
});

// Menu tabs (any .tabs group controls sibling .panel elements)
document.querySelectorAll(".tabs").forEach((tablist) => {
  const tabs = tablist.querySelectorAll(".tab");
  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      tabs.forEach((t) => t.setAttribute("aria-selected", "false"));
      tab.setAttribute("aria-selected", "true");
      const scope = tablist.parentElement;
      scope.querySelectorAll(":scope > .panel").forEach((p) => (p.hidden = true));
      const target = scope.querySelector("#" + tab.dataset.panel);
      if (target) target.hidden = false;
    });
  });
});

// Floating "Text us" button + popup (site-wide)
(function () {
  var TEXT_NUMBER = "+64275723373";
  var wrap = document.createElement("div");
  wrap.className = "textus";
  wrap.innerHTML =
    '<div class="textus-pop" role="dialog" aria-label="Text us">' +
      '<button class="textus-x" id="textusX" aria-label="Close">&times;</button>' +
      '<p class="textus-msg">Need a quick response?</p>' +
      '<p class="textus-sub">Flick us a text. If we\'re not out on a job, we\'ll get straight back to you.</p>' +
      '<a class="textus-btn" href="sms:' + TEXT_NUMBER + '">Text us &rarr;</a>' +
    '</div>' +
    '<button class="textus-fab" id="textusFab" aria-label="Text us">Text us</button>';
  document.body.appendChild(wrap);
  document.getElementById("textusFab").addEventListener("click", function () { wrap.classList.toggle("open"); });
  document.getElementById("textusX").addEventListener("click", function () { wrap.classList.remove("open"); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") wrap.classList.remove("open"); });
})();

/* Submit Formspree forms in the background, then redirect to our OWN branded thank-you
   page (free — avoids Formspree's paid custom-redirect). Uses the path from _next on the
   current domain, so it works on the preview AND the live site with no changes. */
document.querySelectorAll('form.form[action*="formspree.io"]').forEach(function (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = form.querySelector('[type="submit"]');
    var nextInput = form.querySelector('input[name="_next"]');
    var dest = '/';
    if (nextInput && nextInput.value) {
      try { dest = new URL(nextInput.value).pathname; } catch (err) { dest = nextInput.value; }
    }
    var original = btn ? btn.textContent : '';
    if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
      .then(function (r) {
        if (r.ok) {
          var ord = form.querySelector('[name="order"]'), tot = form.querySelector('[name="order_total"]');
          if (ord && ord.value) { try { sessionStorage.setItem('aah_order', ord.value); sessionStorage.setItem('aah_order_total', tot ? (tot.value || '') : ''); } catch (se) {} }
          window.location.assign(dest); return;
        }
        throw new Error('submit failed');
      })
      .catch(function () {
        window.alert("Sorry, that didn't send. Please try again, or email hello@artisanathome.nz.");
        if (btn) { btn.disabled = false; btn.textContent = original; }
      });
  });
});

/* First-year announcement — shows up to twice per visitor, then never again */
(function () {
  var KEY = "aah_notice_delivered";
  var count = 0;
  try { count = parseInt(localStorage.getItem(KEY) || "0", 10) || 0; } catch (e) { return; }
  if (count >= 2) return;
  try { localStorage.setItem(KEY, String(count + 1)); } catch (e) {}

  function showNotice() {
    if (document.getElementById("aah-notice")) return;
    var overlay = document.createElement("div");
    overlay.id = "aah-notice";
    overlay.className = "aah-notice-overlay";
    overlay.innerHTML =
      '<div class="aah-notice" role="dialog" aria-modal="true" aria-labelledby="aah-notice-title">' +
        '<button class="aah-notice-x" aria-label="Close">&times;</button>' +
        '<p class="aah-notice-eyebrow">A note from us</p>' +
        '<h2 class="aah-notice-title" id="aah-notice-title">Thank you</h2>' +
        '<p class="aah-notice-body">Thank you for all your support through our first year in business. ' +
        'Due to ongoing demand, we&rsquo;ve made the decision to step back from our delivered catering, so we can pour our energy into what we love most &mdash; ' +
        'private dining, events and weddings. That said, if you&rsquo;ve a special event you&rsquo;d love us to cater, do still reach out &mdash; if we can make it work, we shall!</p>' +
        '<p class="aah-notice-sign">Abi &amp; Jake</p>' +
      '</div>';
    document.body.appendChild(overlay);
    function close() { if (overlay && overlay.parentNode) overlay.parentNode.removeChild(overlay); }
    overlay.querySelector(".aah-notice-x").addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.addEventListener("keydown", function esc(e) { if (e.key === "Escape") { close(); document.removeEventListener("keydown", esc); } });
    requestAnimationFrame(function () { overlay.classList.add("open"); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { setTimeout(showNotice, 900); });
  } else {
    setTimeout(showNotice, 900);
  }
})();
