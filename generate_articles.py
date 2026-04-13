#!/usr/bin/env python3
"""
Generate article content from SEO titles using Claude API
Reads latest keywords-titles CSV and generates full article HTML
"""

import os
import sys
import csv
import json
import re
from pathlib import Path
from datetime import datetime
import anthropic

class ArticleGenerator:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('CLAUDE_API_KEY')
        if not self.api_key:
            raise ValueError("CLAUDE_API_KEY environment variable not set")
        
        try:
            self.client = anthropic.Anthropic(api_key=self.api_key)
            # Test the API key with a simple request
            self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=10,
                messages=[{"role": "user", "content": "test"}]
            )
            print("✓ API key validated successfully")
        except Exception as e:
            print(f"❌ API key validation failed: {str(e)}")
            raise ValueError(f"Invalid Claude API key: {str(e)}")
        
        self.base_path = Path(__file__).parent
        self.output_dir = self.base_path / 'articles'
    
    def get_latest_csv(self) -> Path:
        """Find the most recent keywords-titles CSV file"""
        csv_dir = self.base_path / 'output'
        if not csv_dir.exists():
            raise FileNotFoundError(f"Output directory not found: {csv_dir}")
        
        csv_files = sorted(csv_dir.glob('keywords-titles-*.csv'), reverse=True)
        if not csv_files:
            raise FileNotFoundError("No keywords-titles CSV files found")
        
        return csv_files[0]
    
    def read_csv_rows(self, csv_path: Path, limit: int = 5) -> list:
        """Read first N rows from CSV"""
        rows = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= limit:
                    break
                rows.append(row)
        return rows
    
    def generate_article_content(self, h1_title: str, h2_headings: str, context: str, filename: str) -> str:
        """Generate article content using Claude API"""
        
        # Parse H2 headings from pipe-separated format
        h2_list = [h.strip() for h in h2_headings.split('|') if h.strip()]
        
        prompt = f"""あなたはSEOに特化した相続メディアのライターです。以下の構成で4000文字以上の記事本文を日本語で生成してください。

**記事ファイル名**: {filename}
**H1タイトル**: {h1_title}
**コンテキスト**: {context}
**H2見出し**: {', '.join(h2_list)}

**生成ルール**:
1. イントロダクション（150-200文字）
2. 各H2セクション（300-500文字）
3. よくある質問セクション（FAQ 3-5項目）
4. 結論（100-150文字）
5. 合計4000文字以上

**スタイル**:
- 日本の相続法（民法改正対応）を踏まえた正確な情報
- 読みやすい構成（短い段落、リスト化）
- 広島市ローカルコンテキスト（地域特性の記述）
- 相談CTAを最後に含める（「無料相談へ」への誘導）

**出力形式**:
以下のHTMLマークアップで返してください（classは含めない、内容のみ）:

<article>
<p>イントロダクション...</p>

<h2>H2見出し1</h2>
<p>本文...</p>
<h3>H3サブ見出し（必要に応じて）</h3>
<p>...")

<h2>H2見出し2</h2>
...

<h2>よくある質問（FAQ）</h2>
<h3>Q1: ...</h3>
<p>A: ...</p>
...

<h2>結論</h2>
<p>...)

</article>

生成開始してください。
"""
        
        # Try different models in case some aren't available
        models_to_try = [
            "claude-3-5-sonnet-20241022",  # Try the latest first
            "claude-3-5-sonnet-20240620",  # Original 3.5 Sonnet
            "claude-3-sonnet-20240229",    # Claude 3 Sonnet
            "claude-3-haiku-20240307",     # Claude 3 Haiku
            "claude-3-opus-20240229",      # Claude 3 Opus
            "claude-2.1",                  # Claude 2.1
            "claude-2.0"                   # Claude 2.0
        ]
        
        last_error = None
        for model in models_to_try:
            try:
                print(f"Trying model: {model}")
                message = self.client.messages.create(
                    model=model,
                    max_tokens=4096,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                print(f"✓ Successfully used model: {model}")
                return message.content[0].text
            except Exception as e:
                error_msg = str(e)
                print(f"✗ Model {model} failed: {error_msg}")
                last_error = e
                # Continue to next model
                continue
        
        # If all models failed, raise the last error
        print(f"❌ All models failed. Last error: {last_error}")
        raise last_error
    
    def wrap_html_template(self, h1_title: str, lead: str, article_content: str, filename: str, description: str) -> str:
        """Wrap article content in HTML template"""
        
        # Extract internal links from article content if present
        internal_links = ""
        if "内部リンク" in article_content or "関連記事" in article_content:
            internal_links = "<!-- Internal links extracted from article -->"
        
        html = f"""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{h1_title} | 相継ぎの相談室 by ENNA</title>
    <meta name="description" content="{description}" />
    <link rel="stylesheet" href="../styles.css" />
  </head>
  <body>
    <div class="site-shell">
      <header class="page-hero">
        <nav class="topbar">
          <a class="brand" href="../index.html"><span class="brand-mark">ENNA</span><span>相続の相談室</span></a>
          <div class="topbar-links">
            <a href="./category-real-estate.html">相続不動産</a>
            <a class="cta-link" href="https://enna-protect.com/" target="_blank" rel="noopener noreferrer">無料相談へ</a>
          </div>
        </nav>
        <div class="page-hero-grid">
          <div>
            <p class="eyebrow">Article</p>
            <h1>{h1_title}</h1>
            <p class="lead">{lead}</p>
          </div>
          <aside class="panel-card subtle">
            <p class="panel-label">この記事で分かること</p>
            <ul class="compact-list">
              <li>相続の基礎知識と実務的なポイント</li>
              <li>相談前に確認すべき事項</li>
              <li>次のステップと相談の進め方</li>
            </ul>
          </aside>
        </div>
      </header>

      <main class="page-layout section">
        <article class="article-content">
{article_content}
          <div class="article-actions">
            <a class="button button-primary" href="https://enna-protect.com/" target="_blank" rel="noopener noreferrer">ENNAに無料相談する</a>
          </div>
        </article>
      </main>
    </div>
  </body>
</html>
"""
        return html
    
    def save_article(self, filename: str, html_content: str):
        """Save article HTML file"""
        output_path = self.output_dir / filename
        output_path.write_text(html_content, encoding='utf-8')
        print(f"✓ Saved: {output_path}")
    
    def process_batch(self, limit: int = 5):
        """Process CSV and generate articles"""
        csv_path = self.get_latest_csv()
        print(f"📄 Reading CSV: {csv_path}")
        
        rows = self.read_csv_rows(csv_path, limit=limit)
        print(f"📝 Processing {len(rows)} articles...\n")
        
        article_metadata = {
            'neighborhood': {
                'aita-souzoku': ('相田', '安佐南区', '相田で相続不動産と保険を整理する方法'),
                'akebono-souzoku': ('曙', '東区', '曙の相続相談'),
                'aozaki-souzoku': ('青崎', '西区', '青崎で相続相談するなら何から始める'),
            },
            'category': {
                'category-insurance': ('相続保険', 'カテゴリ', '相続保険まとめ'),
                'category-real-estate': ('相続不動産', 'カテゴリ', '相続不動産まとめ'),
            }
        }
        
        results = []
        
        for idx, row in enumerate(rows, 1):
            filename = row['filename'].replace('.html', '')
            h1_title = row['h1_title'].strip() if row.get('h1_title') else ''
            h2_headings = row['h2_headings'].strip() if row.get('h2_headings') else ''
            context = row['context'].strip() if row.get('context') else ''
            
            if not h1_title or not h2_headings:
                print(f"⊘ Skipped {idx}: Missing title or headings")
                continue
            
            print(f"\n[{idx}/{len(rows)}] Generating: {filename}")
            print(f"    Title: {h1_title}")
            
            # Get metadata
            meta_info = None
            for category_type, items in article_metadata.items():
                if filename in items:
                    meta_info = items[filename]
                    break
            
            if not meta_info:
                # Fallback to context
                lead = f"{context}に関する記事です。"
                description = f"{h1_title}について、初心者から実務的なポイントまで解説しています。"
            else:
                location, region, title = meta_info
                lead = f"{region}{location}で相続を考える方へ、実務的なポイントをまとめた記事です。"
                description = f"{location}{region}で相続を考えるための記事。{h1_title}について解説しています。"
            
            try:
                # Generate article content
                article_html = self.generate_article_content(h1_title, h2_headings, context, filename)
                
                # Wrap in template
                full_html = self.wrap_html_template(h1_title, lead, article_html, filename, description)
                
                # Save file
                self.save_article(f"{filename}.html", full_html)
                results.append({'filename': filename, 'status': 'success', 'title': h1_title})
                
            except Exception as e:
                print(f"✗ Error generating {filename}: {str(e)}")
                results.append({'filename': filename, 'status': 'error', 'error': str(e)})
        
        # Summary
        print(f"\n{'='*60}")
        print(f"記事生成完了")
        print(f"成功: {sum(1 for r in results if r['status'] == 'success')}/{len(results)}")
        print(f"{'='*60}")
        
        return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate article content from CSV')
    parser.add_argument('--limit', type=int, default=5, help='Number of articles to generate per batch')
    parser.add_argument('--api-key', help='Claude API key (or use CLAUDE_API_KEY env var)')
    
    args = parser.parse_args()
    
    try:
        generator = ArticleGenerator(api_key=args.api_key)
        results = generator.process_batch(limit=args.limit)
        
        # Exit with error if any failed
        if any(r['status'] == 'error' for r in results):
            sys.exit(1)
    
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
