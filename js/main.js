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
