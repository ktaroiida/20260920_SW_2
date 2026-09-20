import os
import re

BASE = '/Users/kentaroiida/Desktop/20260919_sw鳥取'

# ============================================================
# 1. RESPONSIVE CSS
# ============================================================
RESPONSIVE_CSS = """

/* ============================================================
   HAMBURGER MENU & MOBILE NAV
============================================================ */
.menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 44px; height: 44px;
  background: transparent;
  border: none;
  cursor: pointer;
  gap: 5px;
  padding: 0;
  z-index: 2001;
}
.menu-toggle span {
  display: block;
  width: 24px; height: 2px;
  background: currentColor;
  transition: transform 0.3s, opacity 0.3s;
  transform-origin: center;
}
.menu-toggle[aria-expanded="true"] span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.menu-toggle[aria-expanded="true"] span:nth-child(2) { opacity: 0; }
.menu-toggle[aria-expanded="true"] span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

.mobile-menu {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: #111820;
  z-index: 2000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s ease;
}
.mobile-menu.is-open {
  opacity: 1;
  pointer-events: auto;
}
.mobile-menu-brand {
  font-family: var(--font-en);
  font-size: 1rem;
  letter-spacing: 0.2em;
  color: var(--color-accent-gold);
  margin-bottom: 3rem;
}
.mobile-menu a {
  font-family: var(--font-en);
  font-size: clamp(1.8rem, 6vw, 2.5rem);
  color: #F2EFE7;
  letter-spacing: 0.1em;
  padding: 0.8rem 0;
  min-height: 44px;
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: color 0.2s;
}
.mobile-menu a:hover { color: var(--color-accent-gold); }
.mobile-menu-close {
  position: absolute;
  top: 1.5rem; right: 1.5rem;
  background: transparent;
  border: none;
  color: #F2EFE7;
  font-size: 2rem;
  width: 44px; height: 44px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ============================================================
   GLOBAL OVERRIDES (all sizes)
============================================================ */
body { overflow-x: hidden; }
* { overflow-wrap: anywhere; }
.container { padding: 0 clamp(1.25rem, 4vw, 2rem); }
img { max-width: 100%; height: auto; display: block; }

/* Footer link flex → wrap */
footer .footer-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
}

/* prefers-reduced-motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* ============================================================
   TABLET  768px ~ 1199px
============================================================ */
@media (max-width: 1199px) {
  .header-nav { gap: 1.2rem; }
  .header-nav a { font-size: 0.8rem; }
  header.global-header { padding: 0 2rem; }

  .hero-logo .main { font-size: 3rem; }
  .hero-logo .sub { font-size: 1.2rem; }

  .product-grid { grid-template-columns: repeat(2, 1fr); gap: 2.5rem 1.5rem; }
  .category-grid { grid-template-columns: repeat(2, 1fr); }

  .story-text-wrap { padding: 0 2.5rem !important; }
  .story-row.reverse .story-text-wrap { padding: 0 2.5rem 0 0 !important; }
  .story-text-wrap h3 { font-size: 1.6rem; }

  .tier-grid { grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
  .tier-card { padding: 2rem 1.25rem; }
}

/* ============================================================
   MOBILE  ~ 767px
============================================================ */
@media (max-width: 767px) {

  /* Header */
  header.global-header {
    padding: 0 1.25rem;
    height: 60px;
    --header-height: 60px;
  }
  .header-nav { display: none; }
  .menu-toggle { display: flex; }
  .header-logo { font-size: 1rem; }

  /* Hero */
  .hero {
    height: 80vh;
    min-height: 480px;
  }
  .hero-bg { object-position: center center; }
  .hero-logo .main { font-size: clamp(2.2rem, 10vw, 3.5rem); }
  .hero-logo .sub { font-size: clamp(0.9rem, 4vw, 1.3rem); margin-bottom: 2rem; }
  .hero-logo .copy { font-size: clamp(1.1rem, 4.5vw, 1.6rem); }

  /* Section spacing */
  section { padding: 4rem 0; }
  .page-section { padding: 3rem 0; }
  .container { padding: 0 1.25rem; }

  /* Interior hero */
  .interior-hero {
    height: auto;
    min-height: 260px;
    padding: 80px 1.25rem 3rem;
  }
  .interior-hero h1 { font-size: clamp(2rem, 8vw, 3rem); }
  .interior-hero p { font-size: 0.9rem; }

  /* Typography */
  .section-title .en-serif { font-size: clamp(1.8rem, 6vw, 2.5rem); }
  .lead-copy { font-size: clamp(1.3rem, 5vw, 1.8rem); }

  /* BTN */
  .btn { padding: 0.9rem 2rem; font-size: 0.9rem; }

  /* EXPERIENCE — dual path */
  .dual-path { grid-template-columns: 1fr; gap: 1.5rem; }
  .path-card { aspect-ratio: 4/3; padding: 2rem 1.5rem; }
  .path-content h3 { font-size: 1.5rem; }
  .path-content p { font-size: 0.9rem; margin-bottom: 1.5rem; }

  /* STORIES — always column */
  .story-row,
  .story-row.reverse {
    flex-direction: column !important;
    gap: 2rem;
  }
  .story-img-wrap, .story-text-wrap { width: 100% !important; }
  .story-text-wrap { padding: 0 !important; }
  .story-text-wrap h3 { font-size: 1.5rem; }
  .story-img-wrap { aspect-ratio: 4/3; }

  /* Category grid — 1 col on mobile */
  .category-grid { grid-template-columns: 1fr; gap: 1.5rem; }
  .category-card img { aspect-ratio: 16/9; }

  /* Product grid — 1 col */
  .product-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .product-card .img-wrap { aspect-ratio: 1/1; }

  /* Tier grid (Secret Box) — 1 col */
  .tier-grid { grid-template-columns: 1fr; gap: 1.5rem; }
  .tier-card { padding: 2rem 1.5rem; }
  .tier-card h3 { font-size: 1.3rem; }
  .tier-card .price { font-size: 1.8rem; }

  /* Story article */
  .story-article { padding: 0 0 3rem; }
  .story-article h2 { font-size: 1.4rem; }
  .story-article p { font-size: 1rem; line-height: 1.9; }
  .story-article img { margin: 1.5rem -1.25rem; width: calc(100% + 2.5rem); max-width: calc(100% + 2.5rem); }

  /* Footer */
  footer .footer-nav-wrap {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  /* Carousel prevent x-overflow */
  .secret-carousel-wrap {
    margin: 0 -1.25rem;
    padding: 0 1.25rem;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  .secret-carousel {
    display: flex;
    gap: 1rem;
    scroll-snap-type: x mandatory;
    overflow-x: auto;
    padding-bottom: 1rem;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  .secret-carousel::-webkit-scrollbar { display: none; }
  .secret-carousel-item {
    flex: 0 0 78%;
    scroll-snap-align: start;
    background: #fff;
    text-align: center;
  }
  .secret-carousel-item img {
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
  }
  .secret-carousel-item h3 {
    font-size: 0.95rem;
    padding: 0.75rem 0.5rem;
  }
  .swipe-hint {
    font-family: var(--font-en);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: #999;
    text-align: right;
    margin-bottom: 0.5rem;
  }

  /* Vision roadmap — 1 col */
  .vision-roadmap { flex-direction: column; }

  /* CTA full width on mobile */
  .btn-full-mobile { width: 100%; text-align: center; }
  .product-detail-cta .btn { width: 100%; }

  /* Overflow safety */
  .hero, section, footer, main { max-width: 100vw; }
}

/* ============================================================
   SMALL MOBILE  ~ 374px
============================================================ */
@media (max-width: 374px) {
  .hero-logo .main { font-size: 2rem; }
  .section-title .en-serif { font-size: 1.6rem; }
  .path-card { aspect-ratio: 3/4; }
  .secret-carousel-item { flex-basis: 88%; }
}
"""

with open(os.path.join(BASE, 'assets/css/style.css'), 'a', encoding='utf-8') as f:
    f.write(RESPONSIVE_CSS)
print("✓ style.css updated")


# ============================================================
# 2. MAIN JS
# ============================================================
MAIN_JS = """/* ============================================================
   SAN-IN HIDDEN JAPAN — main.js
============================================================ */

(function () {

  // ──────────────────────────────
  // Fade-in (IntersectionObserver)
  // ──────────────────────────────
  const fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) e.target.classList.add('visible');
      });
    }, { threshold: 0.08 });
    fadeEls.forEach(el => io.observe(el));
  }

  // ──────────────────────────────
  // Header scroll effect
  // ──────────────────────────────
  const header = document.getElementById('global-header');
  if (header) {
    const isTransparent = header.dataset.transparent === 'true';
    if (isTransparent) {
      const onScroll = () => {
        if (window.scrollY > 60) {
          header.style.background = 'rgba(242, 239, 231, 0.97)';
          header.style.color = '#1B1B19';
          header.querySelectorAll('a').forEach(a => a.style.color = '');
        } else {
          header.style.background = 'transparent';
          header.style.color = '#fff';
          header.querySelectorAll('a').forEach(a => a.style.color = '#fff');
        }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
    }
  }

  // ──────────────────────────────
  // Hamburger menu
  // ──────────────────────────────
  const toggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  const closeBtn = document.querySelector('.mobile-menu-close');

  function openMenu() {
    mobileMenu.classList.add('is-open');
    mobileMenu.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    closeBtn && closeBtn.focus();
  }

  function closeMenu() {
    mobileMenu.classList.remove('is-open');
    mobileMenu.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    toggle && toggle.focus();
  }

  if (toggle && mobileMenu) {
    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      isOpen ? closeMenu() : openMenu();
    });

    closeBtn && closeBtn.addEventListener('click', closeMenu);

    // Close on nav link click
    mobileMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', closeMenu);
    });

    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) closeMenu();
    });
  }

})();
"""

js_path = os.path.join(BASE, 'assets/js/main.js')
os.makedirs(os.path.dirname(js_path), exist_ok=True)
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(MAIN_JS)
print("✓ main.js created")


# ============================================================
# 3. HTML HEADER SNIPPET (hamburger + mobile menu)
# ============================================================

HEADER_SNIPPET_TRANSPARENT = '''  <header class="global-header" id="global-header" data-transparent="true" style="background:transparent; color:#fff;">
    <a href="{HOME}" class="header-logo en-serif" style="color:#fff;">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav" style="color:#fff;">
      <a href="{HOME}">HOME</a>
      <a href="about.html">ABOUT</a>
      <a href="shop.html">SHOP</a>
      <a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a>
      <a href="vision.html">OUR VISION</a>
      <a href="investors.html">FOR INVESTORS</a>
    </nav>
    <button class="menu-toggle" aria-label="メニューを開く" aria-expanded="false" style="color:#fff;">
      <span></span><span></span><span></span>
    </button>
  </header>
  <nav class="mobile-menu" aria-hidden="true" aria-label="モバイルメニュー">
    <button class="mobile-menu-close" aria-label="メニューを閉じる">&#x2715;</button>
    <div class="mobile-menu-brand">SAN-IN HIDDEN JAPAN</div>
    <a href="{HOME}">HOME</a>
    <a href="about.html">ABOUT</a>
    <a href="shop.html">SHOP</a>
    <a href="secret-box.html">SECRET BOX</a>
    <a href="stories.html">STORIES</a>
    <a href="vision.html">OUR VISION</a>
    <a href="investors.html">FOR INVESTORS</a>
  </nav>'''

HEADER_SNIPPET_SOLID = '''  <header class="global-header" id="global-header" style="background: rgba(242, 239, 231, 0.95);">
    <a href="{HOME}" class="header-logo en-serif">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav">
      <a href="{HOME}">HOME</a>
      <a href="about.html">ABOUT</a>
      <a href="shop.html">SHOP</a>
      <a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a>
      <a href="vision.html">OUR VISION</a>
      <a href="investors.html">FOR INVESTORS</a>
    </nav>
    <button class="menu-toggle" aria-label="メニューを開く" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </header>
  <nav class="mobile-menu" aria-hidden="true" aria-label="モバイルメニュー">
    <button class="mobile-menu-close" aria-label="メニューを閉じる">&#x2715;</button>
    <div class="mobile-menu-brand">SAN-IN HIDDEN JAPAN</div>
    <a href="{HOME}">HOME</a>
    <a href="about.html">ABOUT</a>
    <a href="shop.html">SHOP</a>
    <a href="secret-box.html">SECRET BOX</a>
    <a href="stories.html">STORIES</a>
    <a href="vision.html">OUR VISION</a>
    <a href="investors.html">FOR INVESTORS</a>
  </nav>'''

SCRIPT_TAG = '  <script src="assets/js/main.js"></script>\n</body>'

# Pages that use transparent header (hero image behind)
TRANSPARENT_PAGES = {'index.html', 'about.html', 'story-shibainu.html', 'story-ushinotoyaki.html', 'story-shiroika.html'}

HTML_FILES = [
    'index.html', 'about.html', 'shop.html',
    'category-shiba.html', 'category-craft.html', 'category-food.html',
    'secret-box.html', 'stories.html',
    'story-shibainu.html', 'story-ushinotoyaki.html', 'story-shiroika.html',
    'product-shiba-plush.html', 'product-craft-washi.html', 'product-food-shiroika.html',
    'how-it-works.html', 'vision.html', 'investors.html',
]

def process_html(filename):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {filename}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    home = 'index.html'
    is_transparent = filename in TRANSPARENT_PAGES
    snippet = (HEADER_SNIPPET_TRANSPARENT if is_transparent else HEADER_SNIPPET_SOLID).replace('{HOME}', home)

    # Replace existing <header ... </header> block (and any existing .mobile-menu)
    # Remove existing header block
    html = re.sub(r'<header class="global-header".*?</header>', '', html, flags=re.DOTALL)
    # Remove existing mobile-menu if present
    html = re.sub(r'<nav class="mobile-menu".*?</nav>', '', html, flags=re.DOTALL)

    # Insert new header + mobile-menu right after <body>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + snippet, html)

    # Add lazy loading to non-hero images
    # First mark hero images (those in .hero or .interior-hero) — we skip them
    # Simple approach: add loading="lazy" to all <img> except hero-bg
    def add_lazy(m):
        tag = m.group(0)
        if 'hero-bg' in tag or 'loading=' in tag:
            return tag
        return tag.replace('<img ', '<img loading="lazy" ')
    html = re.sub(r'<img [^>]+>', add_lazy, html)

    # Replace old inline script with src reference
    html = re.sub(r'<script>\s*const observer[\s\S]*?</script>', '', html)

    # Inject main.js before </body>
    if 'assets/js/main.js' not in html:
        html = html.replace('</body>', SCRIPT_TAG)

    # Add footer-nav-wrap class to footer div containing links
    html = re.sub(
        r'(<div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var\(--font-ja-sans\);">)',
        r'<div class="footer-links" style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ {filename}")


# ============================================================
# 4. SECRET BOX — add carousel markup
# ============================================================
def patch_secret_box():
    path = os.path.join(BASE, 'secret-box.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the static product-grid inside secret box with carousel-aware markup
    old_grid_pattern = r'(<div class="product-grid"[^>]*>)(.*?)(</div>)'
    
    CAROUSEL_HTML = '''<p class="swipe-hint">SWIPE →</p>
        <div class="secret-carousel-wrap">
          <div class="secret-carousel">
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_pear.png" alt="二十世紀梨"></div>
              <h3>二十世紀梨</h3>
            </div>
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_squid.png" alt="白いか"></div>
              <h3>白いか</h3>
            </div>
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_rakkyo.png" alt="砂丘らっきょう"></div>
              <h3>砂丘らっきょう</h3>
            </div>
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_chikuwa.png" alt="とうふちくわ"></div>
              <h3>とうふちくわ</h3>
            </div>
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_soba.png" alt="出雲そば"></div>
              <h3>出雲そば</h3>
            </div>
            <div class="secret-carousel-item product-card">
              <div class="img-wrap"><img loading="lazy" src="assets/images/prod_food_shijimi.png" alt="宍道湖しじみ"></div>
              <h3>宍道湖しじみ</h3>
            </div>
          </div>
        </div>'''

    # Find and replace the product-grid section in secret-box
    if 'secret-carousel' not in html:
        html = re.sub(
            r'<div class="product-grid"[^>]*>.*?</div>\s*</div>\s*</main>',
            CAROUSEL_HTML + '\n  </main>',
            html,
            flags=re.DOTALL,
            count=1
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("  ✓ secret-box.html (carousel patched)")


print("\n[HTML FILES]")
for f in HTML_FILES:
    process_html(f)

print("\n[SECRET BOX CAROUSEL]")
patch_secret_box()

print("\n✅ All done!")
