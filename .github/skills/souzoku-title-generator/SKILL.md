---
name: souzoku-title-generator
description: "Use when creating SEO-optimized Japanese titles and H2/H3 headings from inheritance (相続) keywords. Generates article titles, section headings, and content outlines for Hiroshima local inheritance media. Type `/` and search for 'souzoku title' or 'キーワードから見出し' to invoke."
---

# Souzoku Title & Heading Generator Skill

**Purpose**: Generate SEO-optimized Japanese titles, meta descriptions, and heading hierarchies (H2/H3) from a list of inheritance keywords and topic phrases.

**Use When**:
- Creating new article titles from keyword lists
- Generating H2/H3 heading structures for inheritance content
- Building article outlines with nested headings
- Optimizing existing titles for Hiroshima local inheritance search
- Batch-generating meta descriptions for multiple articles
- Planning content hierarchies for category pages

---

## Workflow

### Step 1: Prepare Keywords
Provide keywords or topic phrases. Format options:
- **List format**: Comma-separated or newline-separated keywords
- **Keyword file**: Reference `keyword-candidates-2026-04-13.md` or custom keyword list
- **Topic clusters**: Category + keywords (e.g., "real-estate: 不動産, 売却, 相続不動産")

Example input:
```
相続税, 相続手続き, 広島市, 空き家, 不動産売却
```

### Step 2: Select Title Type
Choose output format:

| Type | Description | Example |
|------|-------------|---------|
| **Article Title** | H1 for main article page | 広島市での相続税申告手続き｜必要書類と期限 |
| **Heading Structure** | Full H2/H3 outline | Main topic → 3-5 subtopics → 2-3 details each |
| **Meta Description** | 120-160 character search snippet | 広島市の相続税申告について... |
| **Category Title** | H1 for category landing page | 相続不動産｜広島市の売却・活用ガイド |
| **Neighborhood Titles** | Location + topic variations | 広島市○○町での相続... |

### Step 3: Specify Context (Optional)
- **Target audience**: 相続初心者, 相続人, 税理士
- **Content type**: 解説記事, 手続きガイド, 事例紹介
- **Content length**: ショート(800語), ミディアム(2000語), ロング(4000語+)
- **Local angle**: 広島市全体 / 特定の区や町名

### Step 4: Generate & Review
Agent generates 3-5 heading variations per topic. You select or refine based on:
- ✓ Keyword inclusion (primary + secondary keywords present)
- ✓ Readability (natural Japanese, scannable)
- ✓ Local relevance (Hiroshima place names when appropriate)
- ✓ Search intent match ("相続とは" = informational, "相続手続き" = how-to)

### Step 5: Output & Implementation
Receives formatted output ready for:
- HTML `<h1>`, `<h2>`, `<h3>` tags
- JSON structure for content management
- Markdown for documentation
- CSV for bulk article metadata

---

## Quick Commands

Use these examples to invoke the skill:

1. **Single article title from keywords**:
   - "キーワード「相続不動産, 売却, 広島市」からH1タイトルを3つ作成して"
   - "Create 3 H1 titles from keywords: inheritance, real estate, Hiroshima"

2. **Full heading structure**:
   - "「相続税」のトピックで、H2 見出しと H3 サブ見出しの構成を作成して"
   - "Build complete H2/H3 Structure for topic: inheritance tax procedures"

3. **Batch meta descriptions**:
   - "これらの記事タイトルのメタ説明文を生成: [リスト]"
   - "Generate 160-character meta descriptions for these 5 article titles"

4. **Neighborhood-specific titles**:
   - "「祇園」「福田」「川内」など広島市内の町名を含む見出しを作成"
   - "Generate headings incorporating Hiroshima neighborhood names: Gion, Fukuda, Kawauchi..."

5. **Category page structure**:
   - "相続保険のカテゴリーページ用にH1とサブカテゴリーを構成"
   - "Create H1 + subcategory structure for Insurance category landing page"

---

## Context & Constraints

**Keyword Sources**:
- Primary: `keyword-candidates-2026-04-13.md` (50+ legal + local terms)
- Secondary: Neighborhood ward mapping (30+ Hiroshima locations)
- Optional: Custom keyword lists

**SEO Guidelines**:
- Include target keyword in H1, typically in first 60 characters
- Use modifiers (2024年, 初心者向け, ガイド, etc.) for freshness & intent clarity
- Secondary keywords recommended in H2/H3 structure
- Local qualifier (広島市/市区町村) for local intent keywords

**Language Constraints**:
- Japanese (自然な日本語)
- Formal business tone (ビジネス文体)
- Natural sentence flow (理解しやすい構成)
- Avoid SPAM phrases (危険, 秘訣, 裏技 overuse)

**Output Formats**:
- **Plain text**: Simple list of titles/headings
- **Markdown**: Hierarchical with `#`, `##`, `###`
- **HTML**: Ready-to-use tags
- **JSON**: Structured for CMS integration
- **CSV**: Bulk title + metadata

---

## Example Scenarios

### Scenario A: Article on Inheritance Real Estate Sales
**Input keywords**: 相続不動産, 売却, 手続き, 広島市, 相談  
**Request**: "相続不動産売却記事のH1と見出し構成を作成"

**Output**:
```markdown
# 相続不動産を広島市で売却する全手続きガイド｜相続税対策も解説

## 相続不動産売却の流れ（全6ステップ）
### ステップ1: 遺産分割と名義変更
### ステップ2: 不動産査定と売却活動
### ステップ3: 売買契約から決済まで

## 相続不動産売却にかかる税金
### 譲渡所得税
### 相続税との重複課税を避けるには

## 広島市で相続不動産売却の相談先
### 税理士への相談
### 不動産業者の選び方
```

### Scenario B: Neighborhood-Specific Title
**Input**: Neighborhood name "祇園" + keyword "相続"  
**Request**: "祇園での相続関連タイトルを3つ作成"

**Output**:
```
1. 広島市安佐南区祇園での相続手続き｜地域密着の支援ガイド
2. 祇園で相続を進めるなら｜不動産売却・相続税相談まで
3. 祇園地区での相続相談｜空き家活用・相続登記完全ガイド
```

### Scenario C: Meta Description Generation
**Input**: Article titles  
**Request**: "以下のタイトル5つのメタ説明文を生成:"

**Output**: 120-160文字のメタ説明リスト

---

## Integration Notes

**Compatible with**:
- [Souzoku SEO Specialist Agent](../souzoku-seo-specialist) — for detailed SEO research & content optimization
- [Souzoku AIO Writer Agent](../souzoku-aio-writer) — for full article body generation from titles/outlines
- `generate_titles.py` — for batch automation of title generation

**Next Steps After Title Generation**:
1. Use titles as H1 for new article files
2. Pass heading structure to AIO Writer for article body
3. Generate meta descriptions from final titles
4. Add internal linking between related heading topics
5. Create category pages with grouped titles

---

## Keywords & Phrases Covered

**Domain Topics**:
- 相続, 相続手続き, 相続人, 相続放棄, 相続登記
- 相続税, 相続税申告, 相続税評価, 基礎控除
- 遺産分割, 遺言, 遺留分, 代襲相続
- 相続不動産, 相続保険, 負債相続

**Hiroshima Neighborhoods** (30+):
- Central: 中区 (元町, 大手町, 中広町, etc.)
- East: 東区 (牛田, 中野, 穴吹, etc.)
- West: 西区 (福田, 青崎, etc.)
- South: 南区 (宇品, etc.)
- North: 安佐北区, 安佐南区, 佐伯区

---

## Tips for Best Results

✓ **Be specific**: "見出し構成を作成" is OK, but "4つの主要な見出しと各3つのサブ見出し" is better  
✓ **Provide context**: Mention audience level, article length, or content intent  
✓ **List keywords clearly**: Use consistent formatting (comma or newline-separated)  
✓ **Check local accuracy**: Verify neighborhood names/wards before finalizing  
✓ **Review for naturalness**: Japanese headings should read naturally, not forced  
✓ **SEO coherence**: Ensure keywords flow logically H1 → H2 → H3  

---

## Alternative Inputs

If you don't have a pre-made keyword list, you can:
- "相続税手続きについて、初心者向けの見出し構成を作成"
- "空き家の相続と売却のための3段階の見出しを作成"
- "「相続とは」について説明する記事の見出し5つを作成"

The agent will generate appropriate keywords and titles automatically.
