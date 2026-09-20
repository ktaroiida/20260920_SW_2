import os
import re

# ==========================================
# 1. Update index.html
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

story_section = """
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
          <p>かつて絶滅の危機にあった山陰柴犬。<br>地域の人々による長年の保存活動によって、その血統は今も山陰で受け継がれています。<br>SAN-IN HIDDEN JAPANの物語は、この小さな日本犬との出会いから始まりました。</p>
          <a href="story-shibainu.html" class="story-link">山陰柴犬の物語を読む →</a>
        </div>
      </div>

      <!-- STORY 02 -->
      <div class="story-row reverse">
        <div class="story-img-wrap"><img src="assets/images/prod_craft_pottery_mug.png" alt="牛ノ戸焼"></div>
        <div class="story-text-wrap">
          <span class="story-number">STORY 02</span>
          <div class="story-meta">工芸品・牛ノ戸焼</div>
          <h3>100年前から続く、<br>地域の商品づくり。</h3>
          <p>鳥取に残る民藝、牛ノ戸焼。<br>約100年前、吉田璋也は地域の素材と職人の技を生かし、暮らしの中で使われる新しい器を生み出しました。<br>その考え方は、今の山陰の商品づくりにもつながっています。</p>
          <a href="story-ushinotoyaki.html" class="story-link">牛ノ戸焼の物語を読む →</a>
        </div>
      </div>

      <!-- STORY 03 -->
      <div class="story-row">
        <div class="story-img-wrap"><img src="assets/images/hero_bg_moon.png" alt="日本海の夜・漁火"></div>
        <div class="story-text-wrap">
          <span class="story-number">STORY 03</span>
          <div class="story-meta">食品・白いか</div>
          <h3>夏の夜、海に灯りが浮かぶ。</h3>
          <p>夏の山陰を代表する味覚、白いか。<br>夜の日本海にはイカ釣り漁船の漁火が並び、その風景そのものが山陰の夏をつくっています。<br>土地を訪れたくなるほどの味と風景を、山陰から届けます。</p>
          <a href="story-shiroika.html" class="story-link">白いかの物語を読む →</a>
        </div>
      </div>

    </div>
  </section>
"""

# Insert right after the dual-path section
index_html = re.sub(
    r'(<section class="container fade-in"[^>]*>.*?<div class="dual-path">.*?</section>)',
    r'\1\n' + story_section,
    index_html,
    flags=re.DOTALL
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# ==========================================
# 2. Update about.html
# ==========================================
about_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ABOUT | SAN-IN HIDDEN JAPAN</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <header class="global-header" id="global-header" style="background: transparent;">
    <a href="index.html" class="header-logo en-serif" style="color:#fff;">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav" style="color:#fff;">
      <a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="shop.html">SHOP</a><a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a><a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a>
    </nav>
  </header>

  <div class="interior-hero" style="background-image: url('assets/images/shiba_product.jpg'); background-size: cover; background-position: center; min-height: 500px;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5);"></div>
    <div style="position:relative; z-index:1;">
      <h1>ABOUT BRAND</h1>
      <p>SAN-IN HIDDEN JAPANについて</p>
    </div>
  </div>

  <main class="container page-section fade-in">
    <h2 class="section-title"><span class="en-serif">PHILOSOPHY</span>なぜ山陰なのか</h2>
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
        <p class="lead-copy">メディアではなく、<br>「商品を届けるブランド」であること。</p>
        <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">
            私たちは、鳥取・島根を中心とした山陰地方に眠る、まだ広く知られていない日本の伝統・文化・地域資源を発掘し、その価値を現代の商品として再編集し、全国・世界へ届けていくブランドです。
        </p>
        <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">
            その出発点となったのが、一枚の写真に写る「山陰柴犬」でした。彼らは単なる犬種ではなく、この土地の人々の暮らしの中で静かに受け継がれてきた「生きた文化」そのものでした。知られざる歴史や、それを守る人々の温かさに触れたとき、山陰にはこのような「まだ知られていない日本」が数多く存在することに気づきました。
        </p>
        <p style="margin-bottom: 3rem; line-height: 2; text-align: left;">
            土地の恵み、受け継がれる技術、人々の物語。<br>
            私たちは単なる情報を発信するメディアではなく、それらを確かな「商品」という手触りのある形にして、あなたの手元へお届けします。
        </p>
        <a href="story-shibainu.html" class="btn btn-outline">ブランドの原点・山陰柴犬の物語を読む</a>
    </div>
  </main>

  <footer style="margin-top:0; padding: 4rem 2rem; background: #EBE7DD; color: var(--color-text-main);">
    <div class="container">
      <p class="en-serif" style="font-size: 1.5rem; margin-bottom: 1rem;">SAN-IN HIDDEN JAPAN</p>
      <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">
        <a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a><a href="how-it-works.html">HOW IT WORKS</a>
      </div>
      <p>※本サービスはプロトタイプです。</p>
    </div>
  </footer>
</body>
</html>
"""
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)


# ==========================================
# 3. Create Story Detail Pages
# ==========================================

STORY_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE} | SAN-IN HIDDEN JAPAN</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <header class="global-header" id="global-header" style="background: rgba(242, 239, 231, 0.95);">
    <a href="index.html" class="header-logo en-serif">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav">
      <a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="shop.html">SHOP</a><a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a><a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a>
    </nav>
  </header>

  <div class="interior-hero" style="background-image: url('{HERO_IMG}'); background-size: cover; background-position: center; min-height: 400px; position:relative;">
    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:0;"></div>
    <div style="position:relative; z-index:1;">
      <h1>{HERO_TITLE}</h1>
      <p>{HERO_SUB}</p>
    </div>
  </div>

  <main class="container page-section fade-in">
    <div class="story-article">
      {CONTENT}
      <div class="story-article-footer">
        <a href="{SHOP_LINK}" class="btn">{SHOP_BTN_TEXT}</a>
      </div>
    </div>
  </main>

  <footer style="margin-top:0; padding: 4rem 2rem; background: #EBE7DD; color: var(--color-text-main);">
    <div class="container">
      <p class="en-serif" style="font-size: 1.5rem; margin-bottom: 1rem;">SAN-IN HIDDEN JAPAN</p>
      <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">
        <a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a><a href="how-it-works.html">HOW IT WORKS</a>
      </div>
      <p>※本サービスはプロトタイプです。</p>
    </div>
  </footer>
</body>
</html>
"""

stories = {
    "story-shibainu.html": {
        "title": "山陰柴犬の物語",
        "hero_img": "assets/images/shiba_product.jpg",
        "hero_title": "STORY 01",
        "hero_sub": "消えかけた犬を、地域で守る。山陰柴犬の物語",
        "shop_link": "category-shiba.html",
        "shop_btn_text": "山陰柴犬グッズを見る",
        "content": """
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">SAN-IN HIDDEN JAPANの<br>ブランドの起点は、一匹の地犬でした。</p>
        
        <h2>山陰柴犬とは何か</h2>
        <p>山陰柴犬は、鳥取・島根を中心とする山陰地方に古くから根付いていた地犬をルーツに持つ日本犬です。鳥取県東部で飼育されていた「因幡犬（いなばけん）」と、島根県西部で飼育されていた「石州犬（せきしゅうけん）」の長所を組み合わせる形で改良され、誕生しました。</p>
        <p>一般的な柴犬に比べて、四肢が長くスラリとした体型、赤みのある被毛（赤胡麻）、そして温和で従順な性格が特徴とされています。</p>

        <h2>絶滅の危機と、地域の人々の奮闘</h2>
        <p>かつては猟犬や番犬として人々の暮らしのすぐそばにいた山陰柴犬ですが、昭和に入り、戦時中の混乱やジステンパーなどの感染症の流行により、その数は激減。終戦直後には、純粋な血統を残す個体はわずか20頭ほどにまで追い込まれました。</p>
        <p>この「絶滅の危機」を救ったのは、他でもない地域の人々でした。鳥取の名士らが立ち上がり、血統の保存に尽力しました。1947年に生まれた「太刀号」という一匹のオス犬が、現在のすべての山陰柴犬の祖先となっています。</p>

        <h2>山陰柴犬育成会の誕生と現在</h2>
        <p>さらに時代が下り、高齢化などによって再び飼育者が減少する危機が訪れました。そこで2004年、地元の有志らが集まり「山陰柴犬育成会」が結成されます。現在では、品評会や鑑賞会が定期的に開催され、育成会を中心とした地道な保護・繁殖活動により、個体数はおおよそ500頭前後にまで回復しています。</p>

        <h2>なぜSAN-IN HIDDEN JAPANなのか</h2>
        <p>私たちが「山陰柴犬」に惹かれたのは、単に希少だからではありません。この犬が、地域の人々の並々ならぬ愛情と、血統を残そうとする執念のような行動によって「現代に奇跡的に受け継がれている文化」そのものだからです。</p>
        <p>山陰には、この犬のように「地元の人々に愛されながらも、外からは見えていない宝物」がたくさん眠っています。私たちは山陰柴犬をブランドの起点・象徴とし、その魅力と、彼らが生きる山陰の他の素晴らしい資源（工芸・食）を全国に届けていきます。</p>
        """
    },
    "story-ushinotoyaki.html": {
        "title": "牛ノ戸焼の物語",
        "hero_img": "assets/images/prod_craft_pottery_mug.png",
        "hero_title": "STORY 02",
        "hero_sub": "100年前から続く、地域の商品づくり",
        "shop_link": "category-craft.html",
        "shop_btn_text": "工芸品を見る",
        "content": """
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">民藝の火を灯した先人と、<br>現在に息づく手仕事。</p>
        
        <h2>鳥取に残る民藝、牛ノ戸焼</h2>
        <p>鳥取市河原町にある「牛ノ戸焼（うしのとやき）」は、江戸時代末期から続く窯元です。地元の土を使い、日々の暮らしの中で使われる素朴で丈夫な器を作り続けてきました。しかし、現代の牛ノ戸焼を語る上で欠かせないのが、今から約100年前の「ある出会い」です。</p>
        
        <h2>吉田璋也と「緑釉黒釉染分皿」</h2>
        <p>1931年、鳥取に帰郷して医院を開業した医師・吉田璋也（よしだしょうや）は、地元の瀬戸物屋で牛ノ戸焼の茶碗に出会い、その美しさに強く心を打たれました。当時の民藝運動の指導者であった柳宗悦らに共鳴していた吉田は、牛ノ戸焼の窯元に足を運び、新しい生活様式に合った器の制作を提案します。</p>
        <p>そこで生まれたのが、現在も牛ノ戸焼の象徴となっている「緑釉黒釉染分皿（りょくゆうこくゆうそめわけざら）」です。緑と黒（または茶）がくっきりと半分ずつ染め分けられたモダンなデザインは、瞬く間に全国の民藝ファンを魅了しました。</p>
        
        <h2>先駆的な「プロデューサー」としての姿</h2>
        <p>吉田璋也の凄さは、ただデザインを指導しただけではありませんでした。「新作民藝」を提唱し、職人を組織して「鳥取民藝協団」を結成。さらに1932年には「たくみ工芸店」を鳥取市内に開き、作られた器を流通・販売する仕組みまでを自らの手で作り上げたのです。</p>
        <p>「昔からある工芸をそのまま保存する」のではなく、「時代の生活に合わせた商品として再編集し、外の世界へ届ける」。このデザインから流通に至る一連のシステム構築は、現代の商品開発の先駆けと言えます。</p>
        
        <h2>SAN-IN HIDDEN JAPANとの共通点</h2>
        <p>吉田璋也が約100年前に行った「地域の技術を商品として再編集し、外へ届ける」という行為は、まさにSAN-IN HIDDEN JAPANが目指す事業思想と完全に一致しています。</p>
        <p>牛ノ戸焼の窯には、今も当時の技術と思想が受け継がれ、新しい作り手たちによって美しい器が生み出されています。私たちは、この土地が持つ「手仕事のDNA」を、現代の価値として改めて全国へ提案します。</p>
        """
    },
    "story-shiroika.html": {
        "title": "白いかの物語",
        "hero_img": "assets/images/hero_bg_moon.png",
        "hero_title": "STORY 03",
        "hero_sub": "夏の夜、海に灯りが浮かぶ",
        "shop_link": "category-food.html",
        "shop_btn_text": "山陰の食品を見る",
        "content": """
        <p class="lead-copy" style="text-align:center; margin-bottom: 4rem;">「イカの女王」と称される味と、<br>夜の日本海を彩る漁火。</p>
        
        <h2>山陰の夏の主役、白いか</h2>
        <p>一般的には「ケンサキイカ」と呼ばれるこのイカは、山陰地方（特に鳥取県周辺）では親しみを込めて「白いか」と呼ばれています。初夏から秋にかけて旬を迎え、その肉厚で柔らかい食感と、噛むほどに口の中に広がる濃厚な甘みから、「イカの女王」「イカの大トロ」と称されるほどの極上の味覚です。</p>
        <p>鮮度の良い白いかは、身が透き通るように美しく、刺身はもちろん、天ぷらや煮付け、地元ならではの一夜干しなど、様々な味わい方で食卓を彩ります。</p>

        <h2>夜の海に浮かぶ「漁火（いさりび）」</h2>
        <p>白いかの美味しさだけでなく、それを獲るための「風景」もまた山陰の夏の重要な一部です。白いかは夜行性で光に集まる習性があるため、漁は夜間に行われます。</p>
        <p>漆黒の日本海の水平線に、何十隻もの一本釣り漁船が点灯する「集魚灯」が等間隔に並びます。この「漁火」は、まるで海の上に光の道ができたかのように幻想的で、夏の鳥取の夜を象徴する風物詩として多くの人々を魅了しています。</p>

        <h2>食が繋ぐ、山陰への想い</h2>
        <p>この極上の味と風景は、地元の人々だけのものに留まりません。「本場の白いかを食べたい」「あの漁火の風景を見たい」と、毎年夏になると遠方から多くの観光客や釣り人が鳥取を訪れます。</p>
        <p>中には、旅行で訪れて食べた白いかのあまりの美味しさに感動し、それがきっかけで鳥取へ移住を決め、自ら地域資源を広める活動に関わるようになったという話もあるほど、この土地の食には「人の人生を動かす力」が秘められています。</p>
        <p>SAN-IN HIDDEN JAPANは、ただ食品を箱に詰めるのではなく、このような「風景」や「土地の空気感」ごと、あなたにお届けしたいと考えています。</p>
        """
    }
}

for filename, data in stories.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(STORY_TEMPLATE.format(
            TITLE=data["title"],
            HERO_IMG=data["hero_img"],
            HERO_TITLE=data["hero_title"],
            HERO_SUB=data["hero_sub"],
            CONTENT=data["content"],
            SHOP_LINK=data["shop_link"],
            SHOP_BTN_TEXT=data["shop_btn_text"]
        ))
        
# ==========================================
# 4. Ensure stories.html index points correctly
# ==========================================
stories_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>STORIES | SAN-IN HIDDEN JAPAN</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <header class="global-header" id="global-header" style="background: rgba(242, 239, 231, 0.95);">
    <a href="index.html" class="header-logo en-serif">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav">
      <a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="shop.html">SHOP</a><a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a><a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a>
    </nav>
  </header>

  <div class="interior-hero">
    <h1>STORIES</h1>
    <p>土地の物語</p>
  </div>

  <main class="container page-section fade-in">
    <div style="text-align:center; margin-bottom:4rem;">
        <p class="lead-copy">商品に込められた、<br>人々と土地の記憶。</p>
    </div>
    <div class="category-grid">
        <a href="story-shibainu.html" class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">消えかけた犬を、地域で守る。</h3>
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">かつて絶滅の危機にあった山陰柴犬。地域の人々による長年の保存活動の物語。</p>
            <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
        </a>
        <a href="story-ushinotoyaki.html" class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">100年前から続く、地域の商品づくり。</h3>
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">吉田璋也が約100年前に牛ノ戸焼にもたらした、工芸のデザインとプロデュースの歴史。</p>
            <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
        </a>
        <a href="story-shiroika.html" class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff; text-decoration: none; color: inherit; display: block;">
            <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">夏の夜、海に灯りが浮かぶ。</h3>
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">極上の甘みを持つ白いかが私たちの食卓に届くまでの風景と、人々を魅了する力。</p>
            <span style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</span>
        </a>
    </div>
  </main>

  <footer style="margin-top:0; padding: 4rem 2rem; background: #EBE7DD; color: var(--color-text-main);">
    <div class="container">
      <p class="en-serif" style="font-size: 1.5rem; margin-bottom: 1rem;">SAN-IN HIDDEN JAPAN</p>
      <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">
        <a href="vision.html">OUR VISION</a><a href="investors.html">FOR INVESTORS</a><a href="how-it-works.html">HOW IT WORKS</a>
      </div>
      <p>※本サービスはプロトタイプです。</p>
    </div>
  </footer>
</body>
</html>
"""
with open('stories.html', 'w', encoding='utf-8') as f:
    f.write(stories_html)

print("Generated Story details and updated Top/About successfully.")
