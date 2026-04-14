# ENNA デザインガイド

このファイルは `/Users/admin/sumai-navi/css/style.css` を参照元として、ENNA 相続メディアで使うデザインルールを整理したものです。今後の改修では、抽象的な雰囲気指定ではなく、このファイルのトークンとコンポーネント方針を優先します。

## 参照元

- CSSソース: `/Users/admin/sumai-navi/css/style.css`
- 参照スキル:
  - `media-builder`
  - `fudosan-media`

## デザイン方針

- ベースは「住まいナビ」準拠の不動産メディアUI
- 印象は `信頼感 > 可読性 > CTAの明確さ`
- レイアウトは軽量な静的HTML前提
- 記事ページは AIO 対応の `summary-box` と `FAQ` を必須にする
- CTA は「通常問い合わせ」だけでなく、強い導線色を分けて使う

## デザイントークン

```css
:root {
  --color-primary:        #0066CC;
  --color-primary-dark:   #00449E;
  --color-primary-deep:   #003580;
  --color-primary-grad:   linear-gradient(135deg, #216CCE 0%, #00449E 100%);
  --color-primary-light:  #EFF7FF;
  --color-primary-mid:    #EBF5FF;

  --color-accent:         #FF4678;
  --color-accent-dark:    #DE0044;
  --color-line:           #06C655;
  --color-line-dark:      #00AF48;
  --color-orange:         #FF7321;

  --color-bg:             #F1F4F8;
  --color-bg-soft:        #F8F8F9;
  --color-white:          #FFFFFF;

  --color-text:           #111111;
  --color-text-sub:       #4A4A4A;
  --color-text-muted:     #8B8B8B;

  --color-border:         #DBE1E8;
  --color-border-mid:     #BBBFC7;

  --font-base: "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Noto Sans JP",
               "Yu Gothic", "Meiryo", sans-serif;

  --radius-sm:   6px;
  --radius-md:   10px;
  --radius-lg:   16px;
  --radius-pill: 999px;

  --shadow-sm:  0 1px 4px rgba(0,0,0,0.08);
  --shadow-md:  0 4px 16px rgba(0,0,0,0.10);
  --shadow-lg:  0 8px 32px rgba(0,0,0,0.12);

  --max-width:  1140px;
  --content-width: 800px;

  --transition: 0.22s ease;
}
```

## カラー運用ルール

- `--color-primary`
  メインブランド色。見出しの強調、主要リンク、タブ、セクション見出しに使う
- `--color-primary-grad`
  ヒーロー、重要CTA、カテゴリーヒーロー、記事CTAの面背景に使う
- `--color-accent`
  通常の問い合わせCTAや補助的な強調に使う
- `--color-line`
  LINE相談や即時連絡導線専用
- `--color-bg`
  サイト全体の背景
- `--color-bg-soft`
  TOC、リスト、入力UI、補助カードの背景

## レイアウト基準

- 最大幅は `1140px`
- 記事本文の読み幅は `800px`
- セクション余白は基本 `64px`
- 強い区切りが必要なセクションは `96px`
- カード、記事、FAQ、サイドバーは `white + border + shadow-sm` を基本にする

## タイポグラフィ

- 本文サイズは `16px`
- 本文行間は `1.8` から `1.9`
- 見出しは太めで、情報の階層が一目で分かることを優先
- `h2` は淡いブルー背景 + 左ボーダー
- `h3` は下線 + 左に短いブルーバー

推奨階層:

- `h1`: `clamp(1.8rem, 5vw, 3.2rem)` 前後
- `h2`: `1.45rem`
- `h3`: `1.15rem`
- 本文: `1rem`
- 補助文: `0.85rem` から `0.95rem`

## 主要コンポーネント

### ボタン

- `.btn--primary`
  メインブルーのグラデーション
- `.btn--contact`
  ピンク系の相談導線
- `.btn--line`
  LINE導線専用
- `.btn--outline`
  補助ボタン

ルール:

- 角丸は基本 `pill`
- hover では `translateY(-1px〜-2px)` を使う
- 影で押しやすさを出す

### ヒーロー

- 背景は `--color-primary-grad`
- 薄いドットパターンを重ねる
- 中央寄せ
- `eyebrow` は白半透明のカプセル
- CTA を2つまで並べる
- 検索ボックスや条件導線を内包できる構造にする

### カード

- 白背景
- `radius-md`
- `border: 1.5px solid var(--color-border)` または `shadow-sm`
- hover 時に浮かせる
- タイトルの hover で `primary` に寄せる

### FAQ

- `.faq-item` を単位にする
- `.faq-question` はボタン要素
- `Q` マークは青の円形
- 展開時は `.faq-item.is-open`
- 回答は `100〜180文字` を目安に簡潔にする

### summary-box

- 記事冒頭に必須
- `background: var(--color-primary-light)`
- 左に `4px` の primary ボーダー
- 角丸は右側だけ丸める
- タイトルは青字

### TOC

- 淡い背景と細いボーダー
- 項目番号は青い丸で表示
- 記事本文前に置く

### callout

- `.callout--info`
  ブルー系の補足
- `.callout--warn`
  オレンジ系の注意喚起

## 記事ページ構成

`sumai-navi` ベースでは次の順番を標準とします。

1. `.breadcrumb`
2. `.article-header`
3. `.summary-box`
4. `.toc`
5. `.article-body`
6. `.article-faq`
7. `.article-cta`
8. `.author-box`
9. `.sidebar`

ENNA 側でも、この順番を基本形として扱います。

## 記事本文ルール

- `h2` ごとに論点を明確に分ける
- 箇条書きはグレー背景のボックスリスト化
- 番号リストは丸番号付き
- 表は `th` を primary 背景にする
- 本文色は `--color-text-sub` を基本にして、真っ黒を避ける

## CTAルール

- サイト全体CTAはブルーグラデーションを基本にする
- LINE系CTAだけ緑に分離する
- 記事末CTAは `title + desc + 2 actions` の構造にする
- CTA文言は短く、行動が明確なものにする

例:

- `無料相談する`
- `LINEで相談する`
- `関連記事を見る`
- `カテゴリ一覧へ`

## サイドバー

- `sticky`
- 上端オフセットは `88px`
- ウィジェット見出しは primary gradient
- リンクリストは hover で `primary-light`

## モバイルルール

- ハンバーガーメニューあり
- ヒーロー内 CTA は縦積み可
- 3カラムは 1カラムまたは 2カラムへ落とす
- 検索ボックスは横並び固定にしない
- 角丸の大きいカードでも、横余白を削りすぎない

## ENNAへの適用ルール

- 現在の ENNA は相続メディアだが、UI は `sumai-navi` の不動産メディアCSSをベースにしてよい
- ただし文脈上、暖色や相続向け表現を少し混ぜるのは許容
- それでも、色設計・カード密度・CTAの強さ・FAQ/summary の構造は `sumai-navi` を優先する
- 新しいページや改修では、この `design.md` を参照して判断する

## 実装時の優先順位

1. `sumai-navi` の CSS トークンを維持する
2. AIO 必須要素 `summary-box` と `FAQ` を崩さない
3. 記事の可読性を優先する
4. CTA は色で役割を分ける
5. 既存 ENNA ページでも、順次このガイドに寄せていく
