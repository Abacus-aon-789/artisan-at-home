// Artisan at Home — shared interactions

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
