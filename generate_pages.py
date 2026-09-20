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
  <header class="global-header" id="global-header" style="background: rgba(242, 239, 231, 0.95);">
    <a href="index.html" class="header-logo en-serif">SAN-IN HIDDEN JAPAN</a>
    <nav class="header-nav">
      <a href="index.html">HOME</a>
      <a href="about.html">ABOUT</a>
      <a href="shop.html">SHOP</a>
      <a href="secret-box.html">SECRET BOX</a>
      <a href="stories.html">STORIES</a>
      <a href="vision.html">OUR VISION</a>
      <a href="investors.html">FOR INVESTORS</a>
    </nav>
  </header>

  <div class="interior-hero">
    <h1>{HERO_TITLE}</h1>
    <p>{HERO_SUB}</p>
  </div>

  <main class="container page-section fade-in">
    {CONTENT}
  </main>

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
  </script>
</body>
</html>
"""

pages = {
    "about.html": {
        "title": "ABOUT", "hero_title": "ABOUT", "hero_sub": "ブランドについて",
        "content": """
        <h2 class="section-title"><span class="en-serif">PHILOSOPHY</span>なぜ山陰なのか</h2>
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <p class="lead-copy">メディアではなく、<br>「商品を届けるブランド」であること。</p>
            <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">私たちは、鳥取・島根を中心とした山陰地方に眠る、まだ広く知られていない日本の伝統・文化・地域資源を発掘し、その価値を現代の商品として再編集し、全国・世界へ届けていくブランドです。</p>
            <p style="margin-bottom: 2rem; line-height: 2; text-align: left;">その出発点となったのが、希少な地犬「山陰柴犬」です。彼らは単なる犬種ではなく、この土地の人々の暮らしの中で静かに受け継がれてきた「生きた文化」そのものでした。山陰には、このような「まだ知られていない日本」が数多く存在します。</p>
            <p style="line-height: 2; text-align: left;">土地の恵み、受け継がれる技術、人々の物語。<br>私たちはそれらを確かな「商品」という形にして、あなたの手元へお届けします。</p>
        </div>
        """
    },
    "shop.html": {
        "title": "SHOP", "hero_title": "SHOP", "hero_sub": "カテゴリ一覧",
        "content": """
        <div class="category-grid">
            <a href="category-shiba.html" class="category-card">
              <img src="assets/images/shiba_product.jpg" alt="山陰柴犬">
              <div class="category-info">
                <h3 class="category-title">山陰柴犬グッズ</h3>
                <p class="text-content" style="font-size: 0.85rem;">ブランドの象徴。日常に寄り添うアイテム。</p>
              </div>
            </a>
            <a href="category-craft.html" class="category-card">
              <img src="assets/images/prod_craft_pottery_mug.png" alt="工芸品">
              <div class="category-info">
                <h3 class="category-title">伝統工芸品</h3>
                <p class="text-content" style="font-size: 0.85rem;">山陰の手仕事。日々の暮らしを豊かに。</p>
              </div>
            </a>
            <a href="category-food.html" class="category-card">
              <img src="assets/images/prod_food_pear.png" alt="食品">
              <div class="category-info">
                <h3 class="category-title">食品・特産品</h3>
                <p class="text-content" style="font-size: 0.85rem;">季節ごとの極上の味覚。</p>
              </div>
            </a>
            <a href="secret-box.html" class="category-card">
              <img src="assets/images/secret_box_washi.jpg" alt="SECRET BOX">
              <div class="category-info">
                <h3 class="category-title">SECRET BOX</h3>
                <p class="text-content" style="font-size: 0.85rem;">何が届くかはお楽しみ。</p>
              </div>
            </a>
        </div>
        """
    },
    "category-shiba.html": {
        "title": "山陰柴犬プロダクト", "hero_title": "SHIBA INU", "hero_sub": "山陰柴犬プロダクト",
        "content": """
        <p style="text-align:center; margin-bottom: 3rem;">ブランドの象徴である山陰柴犬。知られざる物語を日常に寄り添う形でお届けします。</p>
        <div class="product-grid">
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_s.png"></div><h3>山陰柴犬 ミニぬいぐるみ</h3><p class="price">¥2,200</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_m.png"></div><h3>山陰柴犬 ぬいぐるみ M</h3><p class="price">¥3,300</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_l.png"></div><h3>山陰柴犬 ぬいぐるみ L</h3><p class="price">¥4,400</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_plush_big.png"></div><h3>山陰柴犬 BIGぬいぐるみ</h3><p class="price">¥6,600</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_keyholder.png"></div><h3>山陰柴犬 キーホルダー</h3><p class="price">¥1,100</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_cap.png"></div><h3>山陰柴犬 刺繍キャップ</h3><p class="price">¥3,300</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_tshirt.png"></div><h3>山陰柴犬 Tシャツ</h3><p class="price">¥3,800</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_totebag.png"></div><h3>山陰柴犬 トートバッグ</h3><p class="price">¥2,200</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_sticker.png"></div><h3>山陰柴犬 ステッカーセット</h3><p class="price">¥880</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_shiba_mug.png"></div><h3>山陰柴犬 マグカップ</h3><p class="price">¥2,200</p></a>
        </div>
        """
    },
    "category-craft.html": {
        "title": "伝統工芸品", "hero_title": "CRAFTS", "hero_sub": "山陰に息づく手仕事",
        "content": """
        <p style="text-align:center; margin-bottom: 3rem;">山陰の職人や工房が生み出す逸品。日々の暮らしを豊かにする本物の手仕事。</p>
        <div class="product-grid">
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_washi_letter.png"></div><h3>因州和紙レターセット</h3><p class="price">¥1,800</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_pottery_mug.png"></div><h3>民藝陶器マグ</h3><p class="price">¥3,500</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_stole.png"></div><h3>弓浜絣のストール</h3><p class="price">¥7,500</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_washi_lantern.png"></div><h3>和紙ランタン</h3><p class="price">¥6,000</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_craft_abacus.png"></div><h3>木製そろばん</h3><p class="price">¥5,000</p></a>
        </div>
        """
    },
    "category-food.html": {
        "title": "食品・特産品", "hero_title": "FOOD", "hero_sub": "季節の極上味覚",
        "content": """
        <p style="text-align:center; margin-bottom: 3rem;">鳥取・島根から届く、旬の豊かさ。個別商品やおすすめ便でお届けします。</p>
        <div class="product-grid">
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_pear.png"></div><h3>二十世紀梨ギフト(秋便)</h3><p class="price">¥3,980</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_squid.png"></div><h3>日本海の白いか(夏便)</h3><p class="price">¥4,980</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_rakkyo.png"></div><h3>砂丘らっきょう</h3><p class="price">¥1,480</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_chikuwa.png"></div><h3>とうふちくわセット</h3><p class="price">¥1,680</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_soba.png"></div><h3>出雲そばギフト</h3><p class="price">¥2,480</p></a>
            <a href="product-detail.html" class="product-card"><div class="img-wrap"><img src="assets/images/prod_food_shijimi.png"></div><h3>宍道湖しじみ</h3><p class="price">¥2,980</p></a>
        </div>
        """
    },
    "secret-box.html": {
        "title": "SECRET BOX", "hero_title": "SECRET BOX", "hero_sub": "開けるまで分からない、山陰からの一箱。",
        "content": """
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <p class="lead-copy">あなたへ、山陰の「旬」を厳選。</p>
            <p style="margin-bottom: 2rem; text-align: left;">※本サービスは定期便（サブスクリプション）ではなく、<b>都度購入型</b>のギフトボックスです。<br>ご注文いただいた時期にもっとも美味しい食品や、季節に合わせた工芸品を厳選してお届けします。<br>中身は届くまでのお楽しみです。</p>
            
            <h2 class="section-title" style="margin-top:4rem;"><span class="en-serif">PRICE</span>3つの価格帯</h2>
            <div class="tier-grid">
                <div class="tier-card">
                    <h3>STANDARD</h3>
                    <p class="price">¥2,980</p>
                    <ul>
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
                        <li>季節の極上特産品 2〜3品</li>
                        <li>山陰柴犬プチグッズ</li>
                        <li>山陰の物語ジャーナル</li>
                        <li>送料無料</li>
                    </ul>
                    <a href="how-it-works.html" class="btn" style="width: 100%;">選択する</a>
                </div>
                <div class="tier-card">
                    <h3>LUXURY</h3>
                    <p class="price">¥6,980</p>
                    <ul>
                        <li>最高級特産品・工芸品</li>
                        <li>山陰柴犬グッズ</li>
                        <li>山陰の物語ジャーナル</li>
                        <li>送料無料</li>
                    </ul>
                    <a href="how-it-works.html" class="btn" style="width: 100%;">選択する</a>
                </div>
            </div>
        </div>
        """
    },
    "how-it-works.html": {
        "title": "HOW IT WORKS", "hero_title": "HOW IT WORKS", "hero_sub": "お買い物の流れ",
        "content": """
        <div style="max-width: 800px; margin: 0 auto;">
            <ul style="list-style: none; padding: 0;">
                <li style="position: relative; padding-left: 4rem; margin-bottom: 4rem;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 2.5rem; color: var(--color-accent-gold); font-family: var(--font-en); font-weight: bold; line-height: 1;">01</span>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">商品、または SECRET BOX を選ぶ</h3>
                    <p style="color: var(--color-text-sub); line-height: 1.8;">カタログからお好きな商品をご自身で選ぶか、価格帯別の「SECRET BOX（おまかせ箱）」を選択します。</p>
                </li>
                <li style="position: relative; padding-left: 4rem; margin-bottom: 4rem;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 2.5rem; color: var(--color-accent-gold); font-family: var(--font-en); font-weight: bold; line-height: 1;">02</span>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">注文する</h3>
                    <p style="color: var(--color-text-sub); line-height: 1.8;">お届け先や決済情報を入力し、ご注文を確定します。<br>※SECRET BOXは定期便ではなく「都度購入」ですので、お好きなタイミングで気軽にご利用いただけます。</p>
                </li>
                <li style="position: relative; padding-left: 4rem; margin-bottom: 4rem;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 2.5rem; color: var(--color-accent-gold); font-family: var(--font-en); font-weight: bold; line-height: 1;">03</span>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">山陰から届く・開けて楽しむ</h3>
                    <p style="color: var(--color-text-sub); line-height: 1.8;">現地の空気とともに、商品と「物語を記したジャーナル」が手元に届きます。生産者の思いや背景を知りながら、上質な体験をお楽しみください。</p>
                </li>
            </ul>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="shop.html" class="btn">買い物を始める</a>
            </div>
        </div>
        """
    },
    "vision.html": {
        "title": "OUR VISION", "hero_title": "OUR VISION", "hero_sub": "ブランドの未来図",
        "content": """
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <p class="lead-copy">知られざる日本を、世界へ。</p>
            <p style="margin-bottom: 4rem; text-align: left; line-height: 2;">SAN-IN HIDDEN JAPAN は、単なるECサイトではありません。<br>地域の価値を再定義し、新しい循環を生み出すためのロードマップを描いています。</p>
            
            <div style="display: flex; flex-direction: column; gap: 2rem; text-align: left;">
                <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                    <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">STEP 1 : DISCOVER</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">山陰柴犬という象徴からの発見</p>
                    <p style="color: var(--color-text-sub); font-size: 0.95rem;">ブランドの起点として山陰柴犬をアイコン化し、まだ知られていない魅力への入り口を作ります。</p>
                </div>
                <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid var(--color-accent-gold);">
                    <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">STEP 2 : DELIVER</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">シークレット通販 / 工芸品・食品の販売</p>
                    <p style="color: var(--color-text-sub); font-size: 0.95rem;">厳選された逸品を、驚き（SECRET BOX）と選択（カタログ）の両軸で全国へ届けます。</p>
                </div>
                <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                    <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">STEP 3 : CONNECT</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">生産者との直接購入・繋がり</p>
                    <p style="color: #999; font-size: 0.95rem;">将来的に、消費者が気に入った生産者から直接継続購入できるプラットフォームへと進化します。</p>
                </div>
                <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                    <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">STEP 4 : CREATE</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">自社商品・共同開発</p>
                    <p style="color: #999; font-size: 0.95rem;">伝統技術を活かしたオリジナルプロダクトを現地の職人と共に生み出します。</p>
                </div>
                <div style="background: #fff; padding: 2rem 3rem; border-left: 4px solid #ccc;">
                    <h3 style="font-family: var(--font-en); font-size: 1.5rem; color: #999; margin-bottom: 0.5rem; letter-spacing: 0.1em;">STEP 5 : GLOBAL</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 0.5rem; font-weight: bold;">越境EC・海外販売</p>
                    <p style="color: #999; font-size: 0.95rem;">「HIDDEN JAPAN」のコンセプトのもと、山陰の価値を世界の市場へ直接届けます。</p>
                </div>
            </div>
        </div>
        """
    },
    "investors.html": {
        "title": "FOR INVESTORS", "hero_title": "FOR INVESTORS", "hero_sub": "投資家・協業先の皆様へ",
        "content": """
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 class="section-title"><span class="en-serif">BUSINESS MODEL</span>事業コンセプト</h2>
            <p style="margin-bottom: 4rem; line-height: 2;">
                「SAN-IN HIDDEN JAPAN」は、地方に眠る高付加価値な未利用資源（文化・技術・産品）を再編集し、高感度層へダイレクトに届けるD2Cプラットフォームです。<br>
                既存の「ふるさと納税」や「総合お土産EC」が陥りがちな価格競争・スペック競争から脱却し、<strong>「物語と神秘性」</strong>を付加価値とした高単価なブランド構築を目指します。
            </p>
            
            <h2 class="section-title"><span class="en-serif">TARGET & VALUE</span>想定顧客と提供価値</h2>
            <ul style="margin-bottom: 4rem; line-height: 2.2; padding-left: 1.5rem; list-style-type: disc;">
                <li><strong>ターゲット層：</strong> 地域の深い文化や手仕事に価値を感じる30〜50代の高所得者層、本物志向のギフト購入者。</li>
                <li><strong>提供価値：</strong> 単なるモノの消費ではなく、「知られざる日本を発見する」という体験価値と、生産者の背景を知る情緒的価値。</li>
                <li><strong>地域資源の優位性：</strong> 未発掘であるからこそ、ブランドとしての「余白」と「神秘性」が保たれています。</li>
            </ul>
            
            <h2 class="section-title"><span class="en-serif">GROWTH</span>今後のブランドの伸びしろ</h2>
            <p style="line-height: 2;">
                山陰柴犬というキャッチーかつ希少なアイコンを起点に集客を図りつつ、最終的にはLTV（顧客生涯価値）の高い「食」や「工芸品」の定期・リピート購買へと繋げる導線を設計しています。<br>
                また、「HIDDEN JAPAN」というコンセプトは拡張性が高く、将来的なインバウンド・越境ECにおいて強力な競争優位性を発揮します。
            </p>
            
            <div style="text-align: center; margin-top: 4rem; padding-top: 4rem; border-top: 1px solid #ddd;">
                <p style="margin-bottom: 2rem;">事業詳細・協業に関するお問い合わせはこちら</p>
                <a href="#" class="btn btn-outline">お問い合わせ（デモ）</a>
            </div>
        </div>
        """
    },
    "stories.html": {
        "title": "STORIES", "hero_title": "STORIES", "hero_sub": "土地の物語",
        "content": """
        <div style="text-align:center; margin-bottom:4rem;">
            <p class="lead-copy">商品に込められた、<br>人々と土地の記憶。</p>
        </div>
        <div class="category-grid">
            <div class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff;">
                <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">海と生きる。白いか漁師の夜</h3>
                <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">真っ暗な日本海に浮かぶ漁火。極上の甘みを持つ白いかが私たちの食卓に届くまでの、ある漁師の物語。</p>
                <a href="#" style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</a>
            </div>
            <div class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff;">
                <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">因州和紙。千年の手仕事</h3>
                <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">鳥取に伝わる伝統工芸。水と植物、そして職人の手のひらから生まれる、強くて美しい和紙の秘密。</p>
                <a href="#" style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</a>
            </div>
            <div class="category-card" style="padding: 2rem; border: 1px solid #ddd; background: #fff;">
                <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">山陰柴犬を守り抜く</h3>
                <p style="font-size: 0.9rem; color: #666; margin-bottom: 1.5rem; line-height: 1.8;">絶滅の危機を乗り越え、地元の人々の愛情によって血脈を繋いできた地犬たちの歴史と現在。</p>
                <a href="#" style="color: var(--color-accent-gold); font-size: 0.85rem; font-family: var(--font-en); letter-spacing: 0.1em;">READ MORE →</a>
            </div>
        </div>
        """
    },
    "product-detail.html": {
        "title": "商品詳細（デモ）", "hero_title": "PRODUCT", "hero_sub": "商品詳細",
        "content": """
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 4rem; max-width: 1000px; margin: 0 auto;">
            <div style="aspect-ratio: 1/1; background: #fff; padding: 2rem; display: flex; align-items:center; justify-content:center;">
                <img src="assets/images/prod_shiba_plush_m.png" alt="山陰柴犬 ぬいぐるみ M" style="width: 100%; object-fit: cover;">
            </div>
            <div>
                <div style="color: var(--color-accent-gold); font-family: var(--font-en); letter-spacing: 0.1em; margin-bottom: 1rem;">PHASE 1 / ORIGIN</div>
                <h1 style="font-size: 2rem; margin-bottom: 1rem;">山陰柴犬 ぬいぐるみ M</h1>
                <p style="font-size: 1.5rem; margin-bottom: 2rem; font-family: var(--font-ja-sans);">¥3,300 <span style="font-size: 0.9rem; color:#999;">(税込)</span></p>
                
                <p style="line-height: 2; margin-bottom: 2rem;">
                    ブランドの象徴である山陰柴犬の愛らしい姿を、手触りの良いぬいぐるみで再現しました。<br>
                    ピンと立った耳、くるりと巻いた尻尾など、山陰柴犬特有のシルエットにこだわっています。
                </p>
                
                <div style="background: rgba(0,0,0,0.03); padding: 2rem; margin-bottom: 2rem; border-left: 2px solid var(--color-indigo);">
                    <h4 style="font-family: var(--font-en); color: var(--color-indigo); margin-bottom: 0.5rem; letter-spacing: 0.1em;">WHY WE FOUND IT</h4>
                    <p style="font-size: 0.9rem; line-height: 1.8;">「この犬の存在と物語を、まずは全国の人に知ってもらいたい。」そんな思いから、もっとも身近に置いていただけるプロダクトとして開発しました。</p>
                </div>
                
                <ul style="font-size: 0.9rem; color: var(--color-text-sub); line-height: 2; margin-bottom: 3rem; padding-left: 0;">
                    <li><strong>サイズ：</strong> 約25cm × 15cm</li>
                    <li><strong>素材：</strong> ポリエステル100%</li>
                    <li><strong>発送方法：</strong> 常温便</li>
                </ul>
                
                <button class="btn" style="width: 100%;">カートに入れる</button>
            </div>
        </div>
        """
    }
}

for filename, data in pages.items():
    with open(filename, "w") as f:
        f.write(TEMPLATE.format(
            TITLE=data["title"],
            HERO_TITLE=data["hero_title"],
            HERO_SUB=data["hero_sub"],
            CONTENT=data["content"]
        ))

print("Generated all pages successfully!")
