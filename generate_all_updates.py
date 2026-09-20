import os

TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE} | SAN-IN HIDDEN JAPAN</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <header class="global-header" id="global-header" style="{HEADER_STYLE}">
    <a href="index.html" class="header-logo en-serif" style="{LOGO_STYLE}">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav" style="{NAV_STYLE}">
      <a href="index.html">HOME</a>
      <a href="about.html">ABOUT</a>
      <a href="shop.html">SHOP</a>
      <a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a>
      <a href="vision.html">OUR VISION</a>
      <a href="investors.html">FOR INVESTORS</a>
    </nav>
  </header>

  {HERO_SECTION}

  {CONTENT}

  <footer style="margin-top:0; padding: 4rem 2rem; background: #EBE7DD; color: var(--color-text-main);">
    <div class="container">
      <p class="en-serif" style="font-size: 1.5rem; margin-bottom: 1rem;">SAN-IN HIDDEN JAPAN</p>
      <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">
        <a href="vision.html">OUR VISION</a>
        <a href="investors.html">FOR INVESTORS</a>
        <a href="how-it-works.html">HOW IT WORKS</a>
      </div>
      <p>※本サービスはプロトタイプです。</p>
    </div>
  </footer>
  <script>
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{ entry.target.classList.add('visible'); }}
      }});
    }});
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    
    const header = document.getElementById('global-header');
    if(!header.style.background.includes('transparent')) {{
        window.addEventListener('scroll', () => {{
          if (window.scrollY > 100) {{ header.style.background = 'rgba(242, 239, 231, 0.95)'; header.style.color = '#1B1B19'; }}
        }});
    }}
  </script>
</body>
</html>
"""

def write_html(filename, title, content, hero_section="", header_style="background: rgba(242, 239, 231, 0.95);", logo_style="", nav_style=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(
            TITLE=title,
            HEADER_STYLE=header_style,
            LOGO_STYLE=logo_style,
            NAV_STYLE=nav_style,
            HERO_SECTION=hero_section,
            CONTENT=content
        ))

# ================================
# 1. index.html (TOP)
# ================================
index_hero = """
  <section class="hero">
    <img src="assets/images/hero_bg_moon.png" alt="静かな日本海" class="hero-bg">
    <div class="hero-logo fade-in">
      <div class="main en-serif">SAN-IN</div>
      <div class="sub en-serif">HIDDEN JAPAN</div>
      <div class="copy">まだ知らない山陰が、届く。</div>
    </div>
  </section>
"""
index_content = """
  <!-- イントロダクション -->
  <section class="container fade-in" style="text-align: center; max-width: 800px; padding-top: 8rem; padding-bottom: 4rem;">
    <h2 class="section-title"><span class="en-serif">ABOUT</span>SAN-IN HIDDEN JAPANとは</h2>
    <p class="lead-copy">鳥取と島根に眠る、<br>知られざる逸品を物語とともに。</p>
    <p class="text-content" style="margin-bottom: 2rem;">
      一度は姿を消しかけた希少な地犬「山陰柴犬」から始まった、私たちのブランド。<br>
      山陰には、全国的にはもちろん、地元の人でさえ十分に知らない文化や産品が数多く存在します。<br>
      私たちはそれらを見つけ、磨き、本物の価値としてあなたへお届けします。
    </p>
    <a href="about.html" class="btn btn-outline">ブランドストーリーを読む</a>
  </section>

  <!-- 2つの体験導線 -->
  <section class="container fade-in" style="padding-top: 4rem;">
    <h2 class="section-title"><span class="en-serif">EXPERIENCE</span>2つの出会い方</h2>
    <div class="dual-path">
      <a href="shop.html" class="path-card">
        <img src="assets/images/catalog_selection.jpg" alt="自分で選ぶ">
        <div class="path-content">
          <h3>自分で選ぶ</h3>
          <p>山陰に眠る知られざる伝統、文化、味覚の中から、あなたが最も惹かれる物語を選んでください。山陰に息づく職人の手仕事や、極上の季節の味覚をご用意しています。</p>
          <span class="btn">カタログを見る</span>
        </div>
      </a>
      <a href="secret-box.html" class="path-card">
        <img src="assets/images/secret_box_washi.jpg" alt="SECRET BOX">
        <div class="path-content">
          <h3>おまかせで楽しむ</h3>
          <p>何が届くかは、開けてからのお楽しみ。<br>私たちが現地で見つけ、心を動かされたその時期一番の価値あるものを、美しい和紙と木箱に包んで都度お届けします。</p>
          <span class="btn">SECRET BOXを見る</span>
        </div>
      </a>
    </div>
  </section>

  <!-- STORIES FROM SAN-IN -->
  <section class="top-story-section fade-in">
    <div class="container">
      <h2 class="section-title"><span class="en-serif">STORIES FROM SAN-IN</span>山陰で見つけた、3つの物語。</h2>
      
      <!-- STORY 01 -->
      <div class="story-row">
        <div class="story-img-wrap"><img src="assets/images/shiba_product.jpg" alt="山陰柴犬"></div>
        <div class="story-text-wrap">
          <span class="story-number">STORY 01</span>
          <div class="story-meta">山陰柴犬</div>
          <h3>消えかけた犬を、地域で守る。</h3>
          <p>何度も絶滅の危機を経験した山陰柴犬。<br>地域の人々による保存と繁殖の取り組みによって、その血統はいまも山陰で受け継がれています。<br>SAN-IN HIDDEN JAPANが最初に見つめたのも、この土地で守られてきた小さな日本犬でした。</p>
          <a href="story-shibainu.html" class="story-link">山陰柴犬の物語を読む →</a>
        </div>
      </div>

      <!-- STORY 02 -->
      <div class="story-row reverse">
        <div class="story-img-wrap"><img src="assets/images/story_ushinotoyaki_somewake.jpg" alt="牛ノ戸焼"></div>
        <div class="story-text-wrap">
          <span class="story-number">STORY 02</span>
          <div class="story-meta">工芸・牛ノ戸焼</div>
          <h3>100年前、鳥取にはすでに<br>「地域の商品を世に出す人」がいた。</h3>
          <p>江戸時代末期から続く鳥取の牛ノ戸焼。<br>1931年、民藝運動家・吉田璋也はこの窯の技術に着目し、地域の素材と職人の技を生かした新しい器づくりを始めました。<br>地域のいいものを商品として磨き、外へ届ける。その思想は今にもつながっています。</p>
          <a href="story-ushinotoyaki.html" class="story-link">牛ノ戸焼の物語を読む →</a>
        </div>
      </div>

      <!-- STORY 03 -->
      <div class="story-row">
        <div class="story-img-wrap"><img src="assets/images/hero_bg_starry.jpeg" alt="日本海の夜・漁火"></div>
        <div class="story-text-wrap">
          <span class="story-number">STORY 03</span>
          <div class="story-meta">食品・白いか</div>
          <h3>夏の夜、海に灯りが浮かぶ。</h3>
          <p>初夏から秋、鳥取の日本海には白いか漁の漁火が並びます。<br>地元で「白いか」と呼ばれるケンサキイカは、透き通る身と上品な甘みが魅力の、山陰を代表する夏の味覚。<br>味だけでなく、その海の風景まで山陰の物語です。</p>
          <a href="story-shiroika.html" class="story-link">白いかの物語を読む →</a>
        </div>
      </div>

    </div>
  </section>

  <!-- カテゴリ一覧 -->
  <section style="background-color: #EBE7DD;">
    <div class="container fade-in">
      <h2 class="section-title"><span class="en-serif">CATEGORIES</span>箱に詰まる、山陰の物語。</h2>
      <div class="category-grid">
        <a href="category-shiba.html" class="category-card">
          <img src="assets/images/shiba_product.jpg" alt="山陰柴犬グッズ">
          <div class="category-info">
            <div class="category-meta">ORIGIN</div>
            <h3 class="category-title">山陰柴犬グッズ</h3>
            <p class="text-content" style="font-size: 0.85rem;">ブランドの象徴。日常に寄り添うアイテム。</p>
          </div>
        </a>
        <a href="category-craft.html" class="category-card">
          <img src="assets/images/traditional_craft.jpg" alt="伝統工芸品">
          <div class="category-info">
            <div class="category-meta">CRAFT</div>
            <h3 class="category-title">伝統工芸品</h3>
            <p class="text-content" style="font-size: 0.85rem;">山陰に息づく職人の手仕事。</p>
          </div>
        </a>
        <a href="category-food.html" class="category-card">
          <img src="assets/images/prod_food_pear.png" alt="食品・特産品">
          <div class="category-info">
            <div class="category-meta">FOOD</div>
            <h3 class="category-title">食品・特産品</h3>
            <p class="text-content" style="font-size: 0.85rem;">季節ごとの極上の味覚。</p>
          </div>
        </a>
        <a href="secret-box.html" class="category-card">
          <img src="assets/images/secret_box_washi.jpg" alt="SECRET BOX">
          <div class="category-info">
            <div class="category-meta">SECRET</div>
            <h3 class="category-title">SECRET BOX</h3>
            <p class="text-content" style="font-size: 0.85rem;">何が届くかはお楽しみ。都度購入のギフト箱。</p>
          </div>
        </a>
      </div>
    </div>
  </section>

  <div style="text-align:center; padding: 4rem 0;">
    <a href="vision.html" class="btn btn-outline" style="margin: 1rem;">OUR VISION</a>
    <a href="investors.html" class="btn btn-outline" style="margin: 1rem; border-color:transparent; color:#999; text-decoration:underline;">FOR INVESTORS</a>
  </div>
"""
write_html("index.html", "SAN-IN HIDDEN JAPAN | まだ知らない山陰が、届く。", index_content, hero_section=index_hero, header_style="background:transparent; color:#fff;", logo_style="color:#fff;", nav_style="color:#fff;")

# ================================
# 2. about.html
# ================================
about_hero = """
  <div class="interior-hero" style="background-image: url('assets/images/shiba_epic.jpeg'); background-size: cover; background-position: center; min-height: 500px;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5);"></div>
    <div style="position:relative; z-index:1;">
      <h1>ABOUT BRAND</h1>
      <p>SAN-IN HIDDEN JAPANについて</p>
    </div>
  </div>
"""
about_content = """
  <main class="container page-section fade-in">
    <h2 class="section-title"><span class="en-serif">PHILOSOPHY</span>なぜ山陰なのか</h2>
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
        <p class="lead-copy">メディアではなく、<br>「商品を届けるブランド」であること。</p>
        <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">
            私たちは、鳥取・島根を中心とした山陰地方に眠る、まだ広く知られていない日本の伝統・文化・地域資源を発掘し、その価値を現代の商品として再編集し、全国・世界へ届けていくブランドです。
        </p>
        <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">
            このブランドの出発点として私たちが着目したのが、山陰柴犬でした。彼らは単なる犬種ではなく、この土地の人々の暮らしの中で静かに受け継がれてきた「生きた文化」そのものでした。知られざる歴史や、それを守る人々の温かさに触れたとき、山陰にはこのような「まだ知られていない日本」が数多く存在することに気づきました。
        </p>
        <p style="margin-bottom: 3rem; line-height: 2; text-align: left;">
            土地の恵み、受け継がれる技術、人々の物語。<br>
            私たちは単なる情報を発信するメディアではなく、それらを確かな「商品」という手触りのある形にして、あなたの手元へお届けします。
        </p>
        <a href="story-shibainu.html" class="btn btn-outline">ブランドの原点・山陰柴犬の物語を読む</a>
    </div>
  </main>
"""
write_html("about.html", "ABOUT", about_content, hero_section=about_hero, header_style="background:transparent; color:#fff;", logo_style="color:#fff;", nav_style="color:#fff;")


# ================================
# 3. stories.html
# ================================
stories_hero = """
  <div class="interior-hero">
    <h1>STORIES</h1>
    <p>土地の物語</p>
  </div>
"""
stories_content = """
  <main class="container page-section fade-in">
    <div style="text-align:center; margin-bottom:4rem;">
        <p class="lead-copy">商品に込められた、<br>人々と土地の記憶。</p>
    </div>
    <div class="category-grid">
        <a href="story-shibainu.html" class="category-card" style="border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <img src="assets/images/shiba_epic.jpeg" alt="山陰柴犬" style="aspect-ratio:16/9; object-fit:cover;">
            <div style="padding: 2rem;">
              <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">消えかけた犬を、地域で守る。</h3>
              <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">かつて絶滅の危機にあった山陰柴犬。地域の人々による長年の保存活動の物語。</p>
              <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
            </div>
        </a>
        <a href="story-ushinotoyaki.html" class="category-card" style="border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <img src="assets/images/story_ushinotoyaki_somewake.jpg" alt="牛ノ戸焼" style="aspect-ratio:16/9; object-fit:cover;">
            <div style="padding: 2rem;">
              <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">100年前から続く、地域の商品づくり。</h3>
              <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">吉田璋也が約100年前に牛ノ戸焼にもたらした、工芸のデザインとプロデュースの歴史。</p>
              <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
            </div>
        </a>
        <a href="story-shiroika.html" class="category-card" style="border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <img src="assets/images/hero_bg_starry.jpeg" alt="白いか漁火" style="aspect-ratio:16/9; object-fit:cover;">
            <div style="padding: 2rem;">
              <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">夏の夜、海に灯りが浮かぶ。</h3>
              <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">極上の甘みを持つ白いかが私たちの食卓に届くまでの風景と、人々を魅了する力。</p>
              <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
            </div>
        </a>
    </div>
  </main>
"""
write_html("stories.html", "STORIES", stories_content, hero_section=stories_hero)


# ================================
# 4. story-shibainu.html
# ================================
shiba_story_hero = """
  <div class="interior-hero" style="background-image: url('assets/images/shiba_epic.jpeg'); background-size: cover; background-position: center; min-height: 400px; position:relative;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:0;"></div>
    <div style="position:relative; z-index:1;">
      <h1>STORY 01</h1>
      <p>消えかけた犬を、地域で守る。山陰柴犬の物語</p>
    </div>
  </div>
"""
shiba_story_content = """
  <main class="container page-section fade-in">
    <div class="story-article">
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">SAN-IN HIDDEN JAPANの<br>ブランドの起点は、一匹の地犬でした。</p>
        
        <h2>山陰柴犬とは</h2>
        <p>山陰柴犬は、鳥取・島根を中心とする山陰地方固有の柴犬です。一般的な柴犬に比べて、四肢が長くスリムで引き締まった体型が特徴とされています。毛色については、保存活動に関わる資料でも「赤」と表現されるように、美しい赤みを帯びた被毛を持っています。</p>
        <p>その系統は、鳥取県東部で飼育されていた「因幡犬（いなばけん）」と、島根県西部で飼育されていた「石州犬（せきしゅうけん）」に由来します。時代の変遷とともに純粋な地犬が減っていく中、生き残った因幡犬を基礎として石州犬を交配し、現在の系統が残されました。</p>

        <h2>絶滅の危機</h2>
        <p>かつては猟犬や番犬として人々の暮らしのすぐそばにいた彼らですが、戦争や伝染病などの影響で、戦時中には一時約20頭まで減少したとも伝えられています。</p>
        <p>この「絶滅の危機」を救ったのは、他でもない地域の人々でした。有志らが血統の保存に尽力し、生き残ったわずかな個体から少しずつ命を繋いできました。（なお、この過程で1947年に生まれた「太刀号」という個体が、現在の系統を残す上で重要な役割を果たしたと言われています）</p>

        <h2>山陰柴犬育成会と、守る人々</h2>
        <p>その後、平成6年ごろには約100頭まで回復したものの、高齢化などによって再び飼育者が減少する危機が訪れます。そこで2004年、地元有志によって「山陰柴犬育成会」が結成されました。</p>
        <img src="assets/images/shiba_kentaro.png" alt="山陰柴犬と人" style="margin:2rem 0; width:100%;">
        <p>現在では鑑賞会や品評会が定期的に開催され、繁殖や飼育者支援など、地道な保存活動が続けられています。この物語の主役は、犬そのものはもちろん、この小さな命を何代にもわたって「守っている人々」でもあります。彼らの情熱的な取り組みによって、近年の報道では約400〜500頭規模まで回復していると伝えられています。</p>

        <h2>なぜSAN-IN HIDDEN JAPANなのか</h2>
        <p>私たちが「山陰柴犬」に着目したのは、単に希少だからではありません。この犬が、地域の人々の並々ならぬ愛情と執念によって「現代に奇跡的に受け継がれている文化」そのものだからです。</p>
        <p>山陰には、この犬のように「地元の人々に愛されながらも、外からは見えていない宝物」がたくさん眠っています。私たちは山陰柴犬をブランドの起点とし、彼らが生きる山陰の他の素晴らしい資源（工芸・食）を全国に届けていきます。</p>
        
        <div class="story-article-footer">
          <a href="category-shiba.html" class="btn">山陰柴犬グッズを見る</a>
        </div>
    </div>
  </main>
"""
write_html("story-shibainu.html", "山陰柴犬の物語", shiba_story_content, hero_section=shiba_story_hero, header_style="background:transparent; color:#fff;", logo_style="color:#fff;", nav_style="color:#fff;")

# ================================
# 5. story-ushinotoyaki.html
# ================================
ushi_hero = """
  <div class="interior-hero" style="background-image: url('assets/images/story_ushinotoyaki_somewake.jpg'); background-size: cover; background-position: center; min-height: 400px; position:relative;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:0;"></div>
    <div style="position:relative; z-index:1;">
      <h1>STORY 02</h1>
      <p>100年前から続く、地域の商品づくり</p>
    </div>
  </div>
"""
ushi_content = """
  <main class="container page-section fade-in">
    <div class="story-article">
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">民藝の火を灯した先人と、<br>現在に息づく手仕事。</p>
        
        <h2>鳥取に残る窯元、牛ノ戸焼</h2>
        <p>鳥取市河原町にある「牛ノ戸焼（うしのとやき）」は、江戸時代末期から続く窯元です。地元の土を使い、日々の暮らしの中で使われる素朴で丈夫な日用雑器を作り続けてきました。しかし、現代の牛ノ戸焼を語る上で欠かせないのが、今から約100年前の「ある出会い」です。</p>
        
        <h2>吉田璋也と「緑釉黒釉染分皿」</h2>
        <p>1931年、鳥取に帰郷して医院を開業した医師であり民藝運動家の吉田璋也（よしだしょうや）は、牛ノ戸焼の四代目・小林秀晴と出会います。当時の民藝運動の指導者であった柳宗悦らに共鳴していた吉田は、牛ノ戸焼の窯元に足を運び、新しい生活様式に合った器の制作を提案しました。</p>
        <img src="assets/images/story_ushinotoyaki_somewake.jpg" alt="緑釉黒釉染分皿イメージ" style="margin:2rem 0; width:100%;">
        <p>そこで生まれたのが、現在も牛ノ戸焼の象徴となっている「緑釉黒釉染分皿（りょくゆうこくゆうそめわけざら）」です。緑と黒がくっきりと半分ずつ染め分けられたモダンなデザインは、瞬く間に全国の民藝ファンを魅了しました。</p>
        
        <h2>先駆的な「プロデューサー」としての姿</h2>
        <p>吉田璋也の凄さは、ただデザインを指導しただけではありませんでした。吉田自身が「民藝のプロデューサー」として活動し、商品開発から販売、流通に至るまで深く関わったのです。1932年には「たくみ工芸店」を鳥取市内に開き、作られた器を流通・販売する仕組みまでを自らの手で作り上げました。</p>
        <p>「昔からある工芸をそのまま保存する」のではなく、「時代の生活に合わせた商品として再編集し、外の世界へ届ける」。このデザインから流通に至る一連のシステム構築は、現代の商品開発の先駆けと言えます。</p>
        
        <h2>現在の作り手と、SAN-IN HIDDEN JAPAN</h2>
        <img src="assets/images/traditional_craft.jpg" alt="作陶イメージ" style="margin:2rem 0; width:100%;">
        <p>現在の作り手は、六代目・小林孝男氏と七代目・小林遼司氏。彼らは伝統を守りながら、現代の暮らしに合う器やインテリアにも積極的に取り組んでいます。</p>
        <p>吉田璋也が約100年前に行った「地域の技術を商品として再編集し、外へ届ける」という行為は、まさにSAN-IN HIDDEN JAPANが目指す事業思想と完全に一致しています。私たちは、この土地が持つ「手仕事のDNA」を、現代の価値として改めて全国へ提案します。</p>
        
        <div class="story-article-footer">
          <a href="category-craft.html" class="btn">工芸品を見る</a>
        </div>
    </div>
  </main>
"""
write_html("story-ushinotoyaki.html", "牛ノ戸焼の物語", ushi_content, hero_section=ushi_hero, header_style="background:transparent; color:#fff;", logo_style="color:#fff;", nav_style="color:#fff;")


# ================================
# 6. story-shiroika.html
# ================================
shiroika_hero = """
  <div class="interior-hero" style="background-image: url('assets/images/hero_bg_starry.jpeg'); background-size: cover; background-position: center; min-height: 400px; position:relative;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:0;"></div>
    <div style="position:relative; z-index:1;">
      <h1>STORY 03</h1>
      <p>夏の夜、海に灯りが浮かぶ</p>
    </div>
  </div>
"""
shiroika_content = """
  <main class="container page-section fade-in">
    <div class="story-article">
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">夜の日本海を彩る漁火と、<br>極上の上品な甘み。</p>
        
        <h2>夜の海に浮かぶ「漁火（いさりび）」</h2>
        <p>漆黒の日本海の水平線に、何十隻もの一本釣り漁船が点灯する「集魚灯」が等間隔に並びます。この「漁火」は、まるで海の上に光の道ができたかのように幻想的で、夏の鳥取の夜を象徴する風物詩として多くの人々を魅了しています。</p>
        <img src="assets/images/squid_fisherman.png" alt="イカ漁" style="margin:2rem 0; width:100%;">

        <h2>山陰の夏の主役、白いか</h2>
        <p>一般的には「ケンサキイカ」と呼ばれるこのイカは、山陰地方（特に鳥取県周辺）では親しみを込めて「白いか」と呼ばれています。初夏から秋にかけて旬を迎え、透き通るような美しい身を持っています。</p>
        <img src="assets/images/squid_raw.png" alt="新鮮な白いか" style="margin:2rem 0; width:100%;">
        
        <p>その最大の特徴は、柔らかく、濃厚で、上品な甘みを持つことです。刺身はもちろん、天ぷらや煮付け、地元ならではの一夜干しなど、様々な味わい方で食卓を彩ります。</p>
        <img src="assets/images/squid_sashimi.png" alt="白いかの刺身" style="margin:2rem 0; width:100%;">

        <h2>食と風景が繋ぐ、山陰への想い</h2>
        <p>この極上の味と風景は、地元の人々だけのものに留まりません。「本場の白いかを食べたい」「あの漁火の風景を見たい」と、毎年夏になると遠方から多くの観光客が鳥取を訪れます。</p>
        <p>近年では白いかを食べるだけでなく、夜の白いか釣りそのものを体験する観光も行われています。食と風景をきっかけに、山陰との新しい関係が始まります。SAN-IN HIDDEN JAPANは、ただ食品を箱に詰めるのではなく、このような「風景」や「土地の空気感」ごと、あなたにお届けしたいと考えています。</p>
        
        <div class="story-article-footer">
          <a href="category-food.html" class="btn">山陰の食品を見る</a>
        </div>
    </div>
  </main>
"""
write_html("story-shiroika.html", "白いかの物語", shiroika_content, hero_section=shiroika_hero, header_style="background:transparent; color:#fff;", logo_style="color:#fff;", nav_style="color:#fff;")

# ================================
# 7. Category Pages (Craft fix & Links fix)
# ================================
cat_hero_template = """<div class="interior-hero"><h1>{T1}</h1><p>{T2}</p></div>"""
cat_shiba = """
  <main class="container page-section fade-in">
    <p style="text-align:center; margin-bottom: 3rem;">ブランドの象徴である山陰柴犬。知られざる物語を日常に寄り添う形でお届けします。</p>
    <div class="product-grid">
        <a href="product-shiba-plush.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_s.png"></div><h3>山陰柴犬 ミニぬいぐるみ</h3><p class="price">¥2,200</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_m.png"></div><h3>山陰柴犬 ぬいぐるみ M</h3><p class="price">¥3,300</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_l.png"></div><h3>山陰柴犬 ぬいぐるみ L</h3><p class="price">¥4,400</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_big.png"></div><h3>山陰柴犬 BIGぬいぐるみ</h3><p class="price">¥6,600</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_keyholder.png"></div><h3>山陰柴犬 キーホルダー</h3><p class="price">¥1,100</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_cap.png"></div><h3>山陰柴犬 刺繍キャップ</h3><p class="price">¥3,300</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_tshirt.png"></div><h3>山陰柴犬 Tシャツ</h3><p class="price">¥3,800</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_totebag.png"></div><h3>山陰柴犬 トートバッグ</h3><p class="price">¥2,200</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_sticker.png"></div><h3>山陰柴犬 ステッカーセット</h3><p class="price">¥880</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_mug.png"></div><h3>山陰柴犬 マグカップ</h3><p class="price">¥2,200</p></a>
    </div>
  </main>
"""
write_html("category-shiba.html", "山陰柴犬プロダクト", cat_shiba, hero_section=cat_hero_template.format(T1="SHIBA INU", T2="山陰柴犬プロダクト"))

cat_craft = """
  <main class="container page-section fade-in">
    <p style="text-align:center; margin-bottom: 3rem;">山陰の職人や工房が生み出す逸品。日々の暮らしを豊かにする本物の手仕事。</p>
    <div class="product-grid">
        <a href="product-craft-washi.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_washi_letter.png"></div><h3>因州和紙レターセット</h3><p class="price">¥1,800</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_pottery_mug.png"></div><h3>民藝陶器マグ</h3><p class="price">¥3,500</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_stole.png"></div><h3>弓浜絣風ストール</h3><p class="price">¥7,500</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_washi_lantern.png"></div><h3>和紙ランタン</h3><p class="price">¥6,000</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_abacus.png"></div><h3>木製そろばん</h3><p class="price">¥5,000</p></a>
    </div>
  </main>
"""
write_html("category-craft.html", "伝統工芸品", cat_craft, hero_section=cat_hero_template.format(T1="CRAFTS", T2="山陰に息づく手仕事"))

cat_food = """
  <main class="container page-section fade-in">
    <p style="text-align:center; margin-bottom: 3rem;">鳥取・島根から届く、旬の豊かさ。個別商品やおすすめ便でお届けします。</p>
    <div class="product-grid">
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_pear.png"></div><h3>二十世紀梨ギフト(秋便)</h3><p class="price">¥3,980</p></a>
        <a href="product-food-shiroika.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_squid.png"></div><h3>日本海の白いか(夏便)</h3><p class="price">¥4,980</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_rakkyo.png"></div><h3>砂丘らっきょう</h3><p class="price">¥1,480</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_chikuwa.png"></div><h3>とうふちくわセット</h3><p class="price">¥1,680</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_soba.png"></div><h3>出雲そばギフト</h3><p class="price">¥2,480</p></a>
        <a href="javascript:void(0)" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_shijimi.png"></div><h3>宍道湖しじみ</h3><p class="price">¥2,980</p></a>
    </div>
  </main>
"""
write_html("category-food.html", "食品・特産品", cat_food, hero_section=cat_hero_template.format(T1="FOOD", T2="季節の極上味覚"))


# ================================
# 8. Product Detail Pages
# ================================
prod_temp = """
  <div class="interior-hero"><h1>PRODUCT</h1><p>商品詳細</p></div>
  <main class="container page-section fade-in">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; max-width: 1000px; margin: 0 auto;">
        <div style="background: #fff; padding: 2rem; display: flex; align-items:center; justify-content:center; aspect-ratio: 1/1;">
            <img src="{IMG}" alt="{NAME}" style="width: 100%; object-fit: cover;">
        </div>
        <div>
            <div style="color: var(--color-accent-gold); font-family: var(--font-en); letter-spacing: 0.1em; margin-bottom: 1rem;">{CAT}</div>
            <h1 style="font-size: 2rem; margin-bottom: 1rem;">{NAME}</h1>
            <p style="font-size: 1.5rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">{PRICE} <span style="font-size: 0.9rem; color:#999;">(税込)</span></p>
            <p style="line-height: 2; margin-bottom: 2rem;">{DESC}</p>
            <div style="background: rgba(0,0,0,0.03); padding: 2rem; margin-bottom: 2rem; border-left: 2px solid var(--color-indigo);">
                <h4 style="font-family: var(--font-en); color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">WHY WE FOUND IT</h4>
                <p style="font-size: 0.9rem; line-height: 1.8;">{WHY}</p>
            </div>
            <button class="btn" style="width: 100%;">カートに入れる</button>
        </div>
    </div>
  </main>
"""
p1 = prod_temp.format(IMG="assets/images/prod_shiba_plush_s.png", NAME="山陰柴犬 ミニぬいぐるみ", CAT="PHASE 1 / ORIGIN", PRICE="¥2,200", DESC="ブランドの象徴である山陰柴犬の愛らしい姿を、手触りの良いぬいぐるみで再現しました。", WHY="この犬の存在と物語を、まずは全国の人に知ってもらいたい。そんな思いから開発しました。")
write_html("product-shiba-plush.html", "山陰柴犬 ミニぬいぐるみ", p1)

p2 = prod_temp.format(IMG="assets/images/prod_craft_washi_letter.png", NAME="因州和紙レターセット", CAT="CRAFT", PRICE="¥1,800", DESC="鳥取に伝わる因州和紙を使用した美しいレターセット。手すきの温もりが伝わります。", WHY="1000年以上の歴史を持つ因州和紙。今の生活で一番使いやすい「手紙」という形でお届けします。")
write_html("product-craft-washi.html", "因州和紙レターセット", p2)

p3 = prod_temp.format(IMG="assets/images/prod_food_squid.png", NAME="日本海の白いか(夏便)", CAT="FOOD", PRICE="¥4,980", DESC="上品な甘みと柔らかさを持つ山陰の夏の主役「白いか」。とれたての鮮度をそのままにお届けします。", WHY="夏の夜の日本海に浮かぶ漁火の風景ごと、この極上の味覚を味わっていただきたいです。")
write_html("product-food-shiroika.html", "日本海の白いか", p3)


# ================================
# 9. shop.html
# ================================
shop_content = """
  <main class="container page-section fade-in">
    <div class="category-grid">
        <a href="category-shiba.html" class="category-card">
          <img src="assets/images/shiba_product.jpg" alt="山陰柴犬">
          <div class="category-info"><h3 class="category-title">山陰柴犬グッズ</h3><p class="text-content" style="font-size: 0.85rem;">ブランドの象徴。日常に寄り添うアイテム。</p></div>
        </a>
        <a href="category-craft.html" class="category-card">
          <img src="assets/images/traditional_craft.jpg" alt="工芸品">
          <div class="category-info"><h3 class="category-title">伝統工芸品</h3><p class="text-content" style="font-size: 0.85rem;">山陰の手仕事。日々の暮らしを豊かに。</p></div>
        </a>
        <a href="category-food.html" class="category-card">
          <img src="assets/images/prod_food_pear.png" alt="食品">
          <div class="category-info"><h3 class="category-title">食品・特産品</h3><p class="text-content" style="font-size: 0.85rem;">季節ごとの極上の味覚。</p></div>
        </a>
        <a href="secret-box.html" class="category-card">
          <img src="assets/images/secret_box_washi.jpg" alt="SECRET BOX">
          <div class="category-info"><h3 class="category-title">SECRET BOX</h3><p class="text-content" style="font-size: 0.85rem;">何が届くかはお楽しみ。</p></div>
        </a>
    </div>
  </main>
"""
write_html("shop.html", "SHOP", shop_content, hero_section=cat_hero_template.format(T1="SHOP", T2="カテゴリ一覧"))


# ================================
# 10. secret-box.html
# ================================
secret_content = """
  <main class="container page-section fade-in">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
        <p class="lead-copy">あなたへ、山陰の「旬」を厳選。</p>
        <p style="margin-bottom: 2rem; text-align: left;">※本サービスは定期便（サブスクリプション）ではなく、<b>都度購入型</b>のギフトボックスです。<br>ご注文いただいた時期（発送時点）にもっとも旬を迎えている美味しい食品や名産品を厳選してお届けします。<br>何が届くかは開けてからのお楽しみです。</p>
        
        <h2 class="section-title" style="margin-top:4rem;"><span class="en-serif">PRICE</span>3つの価格帯</h2>
        <div class="tier-grid">
            <div class="tier-card">
                <h3>STANDARD</h3>
                <p class="price">¥2,980</p>
                <ul>
                    <li>小さな出会い</li>
                    <li>季節の特産品 1〜2品</li>
                    <li>山陰の物語ジャーナル</li>
                    <li>送料別</li>
                </ul>
                <a href="how-it-works.html" class="btn" style="width: 100%;">選択する</a>
            </div>
            <div class="tier-card" style="border-width: 2px; transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.05);">
                <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--color-accent-gold); color: #fff; font-size: 0.75rem; padding: 4px 12px; letter-spacing: 0.1em; font-family: var(--font-en);">RECOMMEND</div>
                <h3>PREMIUM</h3>
                <p class="price">¥4,980</p>
                <ul>
                    <li>山陰の旬をしっかり楽しむ</li>
                    <li>季節の特産品 2〜4品</li>
                    <li>山陰の物語ジャーナル</li>
                    <li>送料無料</li>
                </ul>
                <a href="how-it-works.html" class="btn" style="width: 100%;">選択する</a>
            </div>
            <div class="tier-card">
                <h3>LUXURY</h3>
                <p class="price">¥6,980</p>
                <ul>
                    <li>希少・高付加価値商品を含む特別な箱</li>
                    <li>最高級特産品（※特別企画で工芸品を含む場合あり）</li>
                    <li>山陰の物語ジャーナル</li>
                    <li>送料無料</li>
                </ul>
                <a href="how-it-works.html" class="btn" style="width: 100%;">選択する</a>
            </div>
        </div>

        <h2 class="section-title" style="margin-top:6rem;"><span class="en-serif">WHAT MAY COME</span>届くかもしれない山陰の旬</h2>
        <p style="text-align:left; margin-bottom: 2rem;">※以下の商品は一例です。必ず入る商品ではなく、季節や水揚げ、収穫状況によって内容は毎回変わります。</p>
        <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap:2rem;">
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_pear.png"></div><h3 style="font-size:0.95rem;">二十世紀梨</h3></div>
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_squid.png"></div><h3 style="font-size:0.95rem;">白いか</h3></div>
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_rakkyo.png"></div><h3 style="font-size:0.95rem;">砂丘らっきょう</h3></div>
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_chikuwa.png"></div><h3 style="font-size:0.95rem;">とうふちくわ</h3></div>
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_soba.png"></div><h3 style="font-size:0.95rem;">出雲そば</h3></div>
            <div class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_shijimi.png"></div><h3 style="font-size:0.95rem;">宍道湖しじみ</h3></div>
        </div>
    </div>
  </main>
"""
write_html("secret-box.html", "SECRET BOX", secret_content, hero_section=cat_hero_template.format(T1="SECRET BOX", T2="開けるまで分からない、山陰からの一箱。"))


# ================================
# 11. vision.html
# ================================
vision_content = """
  <main class="container page-section fade-in">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
        <p class="lead-copy">知られざる日本を、世界へ。</p>
        <p style="margin-bottom: 4rem; text-align: left; line-height: 2;">SAN-IN HIDDEN JAPAN は、単なるECサイトではありません。<br>地域の価値を再定義し、新しい循環を生み出すためのロードマップを描いています。</p>
        
        <div style="display: flex; flex-direction: column; gap: 2rem; text-align: left;">
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">01 ORIGIN</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">山陰柴犬</p>
                <p style="color: var(--color-text-sub); font-size: 0.95rem;">ブランドの起点として山陰柴犬をアイコン化し、まだ知られていない魅力への入り口を作ります。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">02 DISCOVER</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">SECRET BOX（おまかせ箱）</p>
                <p style="color: var(--color-text-sub); font-size: 0.95rem;">厳選された旬の逸品を、驚きとともに全国へ届けます。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">03 CRAFT</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">工芸品</p>
                <p style="color: var(--color-text-sub); font-size: 0.95rem;">山陰の職人の手仕事を、現代の暮らしに合う形で提案します。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">04 TASTE</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">食品</p>
                <p style="color: var(--color-text-sub); font-size: 0.95rem;">季節ごとの極上の味覚を、物語とともに届けます。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">05 CONNECT</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">生産者との直接購入</p>
                <p style="color: #999; font-size: 0.95rem;">将来的に、消費者が気に入った生産者から直接継続購入できるプラットフォームへと進化します。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">06 CREATE</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">自社商品・共同開発</p>
                <p style="color: #999; font-size: 0.95rem;">伝統技術を活かしたオリジナルプロダクトを現地の職人と共に生み出します。</p>
            </div>
            <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">07 GLOBAL</h3>
                <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">海外販売</p>
                <p style="color: #999; font-size: 0.95rem;">「HIDDEN JAPAN」のコンセプトのもと、山陰の価値を世界の市場へ直接届けます。</p>
            </div>
        </div>
    </div>
  </main>
"""
write_html("vision.html", "OUR VISION", vision_content, hero_section=cat_hero_template.format(T1="OUR VISION", T2="ブランドの未来図"))


# ================================
# 12. investors.html
# ================================
investors_content = """
  <main class="container page-section fade-in">
    <div style="max-width: 800px; margin: 0 auto;">
        
        <h2 class="section-title"><span class="en-serif">PROBLEM</span>課題</h2>
        <p style="margin-bottom: 3rem; line-height: 2;">
            山陰には優れた地域資源（工芸、食、文化）が多数存在しますが、アクセスや発信力の課題から、全国的にはその価値が十分に認知されていません。
        </p>

        <h2 class="section-title"><span class="en-serif">WHY SAN-IN</span>なぜ山陰なのか</h2>
        <p style="margin-bottom: 3rem; line-height: 2;">
            鳥取・島根は豊かな自然を背景に、食・手仕事の工芸・特有の文化が集積しています。未発掘であるからこそ、ブランドとしての「余白」と「神秘性」が保たれている強力な強みがあります。
        </p>

        <h2 class="section-title"><span class="en-serif">WHY NOW</span>なぜ今か</h2>
        <p style="margin-bottom: 3rem; line-height: 2;">
            地方EC、背景を重視するストーリー消費、プレミアムな体験を求めるギフト需要、そしてインバウンド観光の分散化など、地方のリアルな文化に対する関心がかつてなく高まっています。
        </p>

        <h2 class="section-title"><span class="en-serif">TARGET</span>想定顧客</h2>
        <ul style="margin-bottom: 3rem; line-height: 2.2; padding-left: 1.5rem; list-style-type: disc;">
            <li>地域の食・文化・手仕事に深い価値を感じる購入者</li>
            <li>本物志向のギフト購入者</li>
        </ul>
        
        <h2 class="section-title"><span class="en-serif">VALUE</span>提供価値</h2>
        <p style="margin-bottom: 3rem; line-height: 2;">
            単なるモノの消費ではなく、「知られざる日本を発見する」という体験価値（商品＋物語＋発見体験）と、生産者の背景を知る情緒的価値を提供します。
        </p>

        <h2 class="section-title"><span class="en-serif">REVENUE</span>収益モデル</h2>
        <ul style="margin-bottom: 3rem; line-height: 2.2; padding-left: 1.5rem; list-style-type: disc;">
            <li>商品販売（工芸品、食品、山陰柴犬グッズ）</li>
            <li>SECRET BOX（都度購入型おまかせ箱）</li>
            <li>将来的な共同開発商品</li>
            <li>将来的な海外販売</li>
        </ul>

        <h2 class="section-title"><span class="en-serif">ROADMAP</span>今後の伸びしろ</h2>
        <p style="line-height: 2;">
            山陰柴犬というキャッチーかつ希少なアイコンを起点に集客を図りつつ、最終的にはLTV（顧客生涯価値）の高い「食」や「工芸品」のリピート購買へと繋げる導線を設計しています。（ロードマップの詳細は<a href="vision.html" style="color:var(--color-accent-gold); text-decoration:underline;">OUR VISION</a>をご覧ください）
        </p>
        
        <div style="text-align: center; margin-top: 4rem; padding-top: 4rem; border-top: 1px solid #ddd;">
            <p style="margin-bottom: 2rem;">事業詳細・協業に関するお問い合わせはこちら</p>
            <a href="#" class="btn btn-outline">お問い合わせ（デモ）</a>
        </div>
    </div>
  </main>
"""
write_html("investors.html", "FOR INVESTORS", investors_content, hero_section=cat_hero_template.format(T1="FOR INVESTORS", T2="投資家・協業先の皆様へ"))


# Remove unused old product-detail if exists
if os.path.exists("product-detail.html"):
    os.remove("product-detail.html")

print("All HTML pages generated successfully.")
