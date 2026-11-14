// Self-destructing service worker.
// If a visitor's browser still has a service worker from the old website, this
// replaces it, clears its cached (old) pages, unregisters itself, and reloads
// so they land on the current site.
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (event) {
  event.waitUntil((async function () {
    try {
      var keys = await caches.keys();
      await Promise.all(keys.map(function (k) { return caches.delete(k); }));
    } catch (e) {}
    try { await self.registration.unregister(); } catch (e) {}
    try {
      var clients = await self.clients.matchAll();
      clients.forEach(function (c) { if (c.url && "navigate" in c) { c.navigate(c.url); } });
    } catch (e) {}
  })());
});
