/* PSForever site behavior. Runs on every page load, including instant
   navigation. Apart from the header links, it only acts on the landing page. */

(function () {
  "use strict";

  var ROTATE_MS = 8000;
  var timer = null;

  /* Show the weekly Sunday 12:00 (New York) session in the visitor's time zone. */
  function showNextSession() {
    var el = document.querySelector("[data-psf-session]");
    if (!el || typeof Intl === "undefined") return;
    var tz = "America/New_York";
    var offset = function (ts) {
      var parts = {};
      new Intl.DateTimeFormat("en-US", {
        timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit",
        day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit"
      }).formatToParts(ts).forEach(function (p) { parts[p.type] = p.value; });
      return Date.UTC(+parts.year, +parts.month - 1, +parts.day, +parts.hour, +parts.minute, +parts.second) - ts;
    };
    var now = Date.now();
    for (var i = 0; i < 8; i++) {
      var day = {};
      new Intl.DateTimeFormat("en-US", {
        timeZone: tz, weekday: "short", year: "numeric", month: "numeric", day: "numeric"
      }).formatToParts(new Date(now + i * 864e5)).forEach(function (p) { day[p.type] = p.value; });
      if (day.weekday !== "Sun") continue;
      var noon = Date.UTC(+day.year, +day.month - 1, +day.day, 12);
      var start = noon - offset(noon);
      if (start < now - 3 * 36e5) continue; // still "next" until 3 hours after start
      el.textContent = new Intl.DateTimeFormat(undefined, {
        weekday: "long", hour: "numeric", minute: "2-digit", timeZoneName: "short"
      }).format(start);
      return;
    }
  }

  /* Rotate hero backgrounds. ?hero=N (1-based) pins one image for previewing. */
  function rotateHero() {
    if (timer) { clearInterval(timer); timer = null; }
    var layers = Array.prototype.slice.call(document.querySelectorAll(".psf-hero__bg"));
    if (!layers.length) return;

    var load = function (layer) {
      var src = layer.getAttribute("data-psf-bg");
      if (src) {
        layer.style.backgroundImage = "url(\"" + src + "\")";
        layer.removeAttribute("data-psf-bg");
      }
    };
    var show = function (index) {
      layers.forEach(function (layer, i) { layer.classList.toggle("is-active", i === index); });
    };

    var pinned = parseInt(new URLSearchParams(location.search).get("hero"), 10);
    if (pinned >= 1 && pinned <= layers.length) {
      load(layers[pinned - 1]);
      show(pinned - 1);
      return;
    }

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (layers.length < 2 || reduceMotion) return;

    var current = 0;
    timer = setInterval(function () {
      if (document.hidden) return;
      var next = (current + 1) % layers.length;
      var src = layers[next].getAttribute("data-psf-bg");
      var advance = function () { load(layers[next]); show(next); current = next; };
      if (!src) { advance(); return; }
      var img = new Image();
      img.onload = advance; // fade only once the image is ready
      img.src = src;
    }, ROTATE_MS);
  }

  /* Keep the Home/Wiki highlight (header and menu drawer) right after instant navigation,
     which swaps the page content but not the header. Links use paths from
     the site root ("/", "/wiki/"). */
  function markHeaderLinks() {
    var path = location.pathname;
    Array.prototype.forEach.call(document.querySelectorAll("[data-psf-section]"), function (link) {
      var section = link.getAttribute("data-psf-section");
      var home = path === "/" || path === "/index.html";
      var active = section === "/" ? home
        : link.hasAttribute("data-psf-everywhere-else") ? !home
        : path.indexOf(section) === 0;
      link.classList.toggle("is-active", active);
      if (active) link.setAttribute("aria-current", "page"); else link.removeAttribute("aria-current");
    });
  }

  function init() {
    markHeaderLinks();
    showNextSession();
    rotateHero();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
