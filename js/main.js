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
