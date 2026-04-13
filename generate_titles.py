#!/usr/bin/env python3
"""
ENNA Souzoku Media - SEO Title & Heading Generator
Automatically generates SEO-optimized Japanese titles and H2/H3 headings.
Processes 10 articles per batch.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class SouzokuTitleGenerator:
    """Generate SEO-optimized titles and headings for inheritance media."""
    
    # Keyword mapping for neighborhood names
    NEIGHBORHOOD_WARDS = {
        'aita': ('相田', '安佐南区'),
        'akebono': ('曙', '東区'),
        'aozaki': ('青崎', '西区'),
        'eba': ('江波', '中区'),
        'ebisucho': ('恵比須町', '中区'),
        'fukuda': ('福田', '西区'),
        'gion': ('祇園', '安佐南区'),
        'inokuchi': ('猪口', '安佐北区'),
        'inokuchidai': ('猪口台', '安佐北区'),
        'inokuchimyojin': ('猪口神社前', '安佐北区'),
        'itsukachchuo': ('五日市中央', '佐伯区'),
        'kakomachi': ('加古町', '中区'),
        'kaminoboricho': ('上のぼり町', '東区'),
        'kamiseno': ('上瀬野', '安佐北区'),
        'kawauchi': ('川内', '安佐北区'),
        'midorii': ('緑井', '安佐南区'),
        'motomachi': ('元町', '中区'),
        'nakahirocho': ('中広町', '中区'),
        'nakano': ('中野', '東区'),
        'nukushina': ('抜沢', '安汽北区'),
        'omachi': ('尾町', '東区'),
        'omiya': ('大宮', '中区'),
        'oshiba': ('押部', '安佐南区'),
        'otemachi': ('大手町', '中区'),
        'ujinakaigan': ('宇品海岸', '南区'),
        'ujinakanda': ('宇品神田', '南区'),
        'ujinanishi': ('宇品西', '南区'),
        'ushitaasahi': ('牛田旭', '東区'),
        'ushitahigashi': ('牛田東', '東区'),
        'ushitashinmachi': ('牛田新町', '東区'),
    }
    
    # Topic keywords
    TOPIC_KEYWORDS = {
        'inheritance-empty-house': ('空き家', '相続不動産'),
        'inheritance-real-estate-sale': ('売却', '相続不動産'),
        'inheritance-shared-property': ('共有', '相続不動産'),
        'inheritance-insurance': ('保険', '相続保険'),
        'inheritance-insurance-beneficiary': ('受取人', '相続保険'),
        'inheritance-insurance-strategy': ('活用', '相続保険'),
        'inheritance-insurance-tax': ('税対策', '相続保険'),
        'category-real-estate': ('相続不動産', 'カテゴリ'),
        'category-insurance': ('相続保険', 'カテゴリ'),
    }
    
    def __init__(self, base_path: str = '.'):
        self.base_path = Path(base_path)
        self.articles_dir = self.base_path / 'articles'
        self.log = []
    
    def get_neighborhood_info(self, filename: str) -> Tuple[str, str]:
        """Extract neighborhood name and ward from filename."""
        base = filename.replace('-souzoku.html', '').replace('.html', '')
        
        for key, (name, ward) in self.NEIGHBORHOOD_WARDS.items():
            if base == key:
                return name, ward
        return '', ''
    
    def get_topic_info(self, filename: str) -> Tuple[str, str]:
        """Extract topic keywords from filename."""
        base = filename.replace('.html', '')
        
        for key, (keyword1, keyword2) in self.TOPIC_KEYWORDS.items():
            if base == key:
                return keyword1, keyword2
        return '', ''
    
    def extract_content_preview(self, html_content: str) -> str:
        """Extract text content for analysis."""
        # Remove script and style tags
        html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', html_content)
        # Clean up whitespace
        text = ' '.join(text.split())
        return text[:500]
    
    def generate_title_for_neighborhood(self, filename: str, html_content: str) -> str:
        """Generate SEO title for neighborhood article."""
        neighborhood, ward = self.get_neighborhood_info(filename)
        
        if not neighborhood:
            return ""
        
        # Neighborhood articles: "[neighborhood]で相続を考えたら - [ward]で【資産・保険】の整理ポイント"
        templates = [
            f"{neighborhood}で相続相談するなら何から始める？{ward}での不動産・保険整理ガイド",
            f"{neighborhood}の相続相談 | {ward}で理想の資産継承を実現する方法",
            f"{neighborhood}で相続対策をスタート｜{ward}での無料相談サポート",
            f"{neighborhood}で相続不動産と保険を整理する方法 | {ward}の相続相談室",
        ]
        return templates[hash(filename) % len(templates)]
    
    def generate_title_for_topic(self, filename: str, html_content: str) -> str:
        """Generate SEO title for topic article."""
        keyword1, keyword2 = self.get_topic_info(filename)
        
        if not keyword1:
            return ""
        
        # Topic articles with strong intent keywords
        base = filename.replace('.html', '')
        
        if 'empty-house' in base:
            return "空き家になった相続不動産は放置でいい？管理・売却・活用の判断基準"
        elif 'real-estate-sale' in base:
            return "相続不動産を売却するなら | 売却前の登記・タイトル・査定確認リスト"
        elif 'shared-property' in base:
            return "共有名義の相続不動産を売却する方法 | 共有持分の判断と意思決定"
        elif 'beneficiary' in base:
            return "受取人が亡くなっていた場合の生命保険対応 | 契約変更・相続手続きの流れ"
        elif 'insurance-strategy' in base:
            return "相続対策に活用する生命保険の活用法 | 資金計画と保険設計"
        elif 'insurance-tax' in base:
            return "相続保険の税務対策 | 控除の仕組みと節税プランニング"
        elif 'category-real-estate' in base:
            return "相続不動産まとめ | 売却・共有・空き家の整理ポイント"
        elif 'category-insurance' in base:
            return "相続保険まとめ | 受取人・活用・税務対策の完全ガイド"
        
        return f"{keyword1}で{keyword2}の悩みを整理する方法"
    
    def generate_headings_for_neighborhood(self, filename: str) -> List[str]:
        """Generate H2 headings for neighborhood articles."""
        neighborhood, _ = self.get_neighborhood_info(filename)
        
        if not neighborhood:
            return []
        
        return [
            f"{neighborhood}で相続相談を考えるときの確認事項",
            f"不動産と保険の整理で最初に見るポイント",
            f"{neighborhood}での相続相談前に準備したい資料",
            f"相続相談の進め方と次のステップ"
        ]
    
    def generate_headings_for_topic(self, filename: str) -> List[str]:
        """Generate H2 headings for topic articles."""
        base = filename.replace('.html', '')
        
        heading_maps = {
            'empty-house': [
                '空き家放置で起きやすい問題と負担',
                '売却か保有か | 判断の軸を整理する',
                '相談前に確認・準備しておくこと',
                'よくある質問と次のステップ'
            ],
            'real-estate-sale': [
                '相続登記と家系図の確認が最初',
                '売却に向けた不動産査定と準備',
                '共有者との話し合いと意思決定',
                '最後の確認と売却手続きの進め方'
            ],
            'shared-property': [
                '共有名義とは | 権利と課題の基礎知識',
                '共有不動産を動かすための意思決定',
                '分割か売却か | 選択肢の整理',
                '相談で話す重要なポイント'
            ],
            'beneficiary': [
                '受取人確認が重要な理由',
                '見直しが必要になりやすい場面',
                '相談前に見る書類と確認項目',
                '受取人変更の手続きと次のステップ'
            ],
            'insurance-strategy': [
                '相続対策に保険が活躍する場面',
                '保険を使った資金計画の組み立て方',
                '相続税対策と保険の関係',
                '相談で確認すべき保険の活用方針'
            ],
            'insurance-tax': [
                '相続保険の税務控除の仕組み',
                '保険金受け取りと税の関係',
                '保険を使った相続税対策',
                '税務相談と保険相談の連携ポイント'
            ],
        }
        
        for key, headings in heading_maps.items():
            if key in base:
                return headings
        
        return [
            'テーマの基礎知識',
            '相続での活用シーン',
            '相談前の確認項目',
            '次のステップ'
        ]
    
    def generate_headings(self, filename: str, html_content: str) -> List[str]:
        """Generate appropriate headings based on article type."""
        if '-souzoku.html' in filename:
            return self.generate_headings_for_neighborhood(filename)
        else:
            return self.generate_headings_for_topic(filename)
    
    def generate_title(self, filename: str, html_content: str) -> str:
        """Generate appropriate title based on article type."""
        if '-souzoku.html' in filename:
            return self.generate_title_for_neighborhood(filename, html_content)
        else:
            return self.generate_title_for_topic(filename, html_content)
    
    def update_html_title(self, html_content: str, new_title: str) -> str:
        """Update <title> and meta description with new title."""
        # Update <title> tag
        html_content = re.sub(
            r'<title>[^<]*</title>',
            f'<title>{new_title} | 相続の相談室 by ENNA</title>',
            html_content
        )
        
        # Update meta description (keep it shorter, focus on problem + location)
        description = new_title[:120].rstrip('。') + '相続不動産や保険の悩みから無料相談へ。'
        html_content = re.sub(
            r'<meta name="description" content="[^"]*"',
            f'<meta name="description" content="{description}"',
            html_content
        )
        
        # Update h1 in page-hero
        h1_match = re.search(r'<h1>([^<]*)</h1>', html_content)
        if h1_match:
            old_h1 = h1_match.group(1)
            # Keep the first part if it's a question
            if '？' in new_title:
                new_h1 = new_title.split('|')[0].split('｜')[0].strip()
            else:
                new_h1 = new_title[:40]
            html_content = html_content.replace(f'<h1>{old_h1}</h1>', f'<h1>{new_h1}</h1>', 1)
        
        return html_content
    
    def update_html_headings(self, html_content: str, headings: List[str]) -> str:
        """Update h2 tags in the article content with new headings."""
        # Find all h2 tags in article-content
        h2_pattern = r'<h2>([^<]*)</h2>'
        h2_matches = list(re.finditer(h2_pattern, html_content))
        
        if not h2_matches:
            return html_content
        
        # Replace h2 tags with new headings (up to the number we generated)
        for i, match in enumerate(h2_matches):
            if i < len(headings):
                old_h2 = match.group(1)
                new_h2 = headings[i]
                html_content = html_content.replace(f'<h2>{old_h2}</h2>', f'<h2>{new_h2}</h2>', 1)
        
        return html_content
    
    def process_batch(self, batch_num: int = 1, batch_size: int = 10) -> Dict:
        """Process a batch of articles (default 10 at a time)."""
        
        if not self.articles_dir.exists():
            return {'error': f'Articles directory not found: {self.articles_dir}'}
        
        # Get all HTML files
        html_files = sorted([f.name for f in self.articles_dir.glob('*.html')])
        
        # Calculate batch range
        start_idx = (batch_num - 1) * batch_size
        end_idx = start_idx + batch_size
        batch_files = html_files[start_idx:end_idx]
        
        if not batch_files:
            return {
                'error': f'Batch {batch_num} is out of range. Total articles: {len(html_files)}',
                'total_articles': len(html_files),
                'max_batch': (len(html_files) - 1) // batch_size + 1
            }
        
        results = {
            'batch': batch_num,
            'processed': 0,
            'updated_files': [],
            'timestamp': datetime.now().isoformat(),
            'total_batches': (len(html_files) - 1) // batch_size + 1,
        }
        
        for filename in batch_files:
            filepath = self.articles_dir / filename
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Generate new title and headings
                new_title = self.generate_title(filename, html_content)
                new_headings = self.generate_headings(filename, html_content)
                
                if not new_title:
                    continue
                
                # Update HTML
                updated_html = self.update_html_title(html_content, new_title)
                updated_html = self.update_html_headings(updated_html, new_headings)
                
                # Write back
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_html)
                
                results['updated_files'].append({
                    'file': filename,
                    'title': new_title,
                    'headings': new_headings
                })
                results['processed'] += 1
                
                self.log.append(f'✓ {filename}: {new_title}')
                
            except Exception as e:
                self.log.append(f'✗ {filename}: {str(e)}')
        
        return results
    
    def save_log(self, log_file: str = 'generate_titles.log'):
        """Save processing log."""
        log_path = self.base_path / log_file
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.log))
        return str(log_path)


def generate_all_titles_csv(base_path: str = '.', output_dir: str = 'output') -> str:
    """Generate titles for all articles and save as CSV."""
    import csv
    from datetime import datetime
    
    generator = SouzokuTitleGenerator(base_path=base_path)
    
    if not generator.articles_dir.exists():
        raise FileNotFoundError(f'Articles directory not found: {generator.articles_dir}')
    
    # Get all HTML files
    html_files = sorted([f.name for f in generator.articles_dir.glob('*.html')])
    
    # Prepare output
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    csv_file = output_path / f'keywords-titles-{timestamp}.csv'
    
    # Collect all titles and headings
    records = []
    for filename in html_files:
        filepath = generator.articles_dir / filename
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            title = generator.generate_title(filename, html_content)
            headings = generator.generate_headings(filename, html_content)
            
            # Neighborhood or topic type
            if '-souzoku.html' in filename:
                article_type = 'neighborhood'
                neighborhood, ward = generator.get_neighborhood_info(filename)
                context = f'{neighborhood}（{ward}）'
            else:
                article_type = 'topic'
                keyword1, keyword2 = generator.get_topic_info(filename)
                context = f'{keyword1} / {keyword2}'
            
            records.append({
                'filename': filename,
                'type': article_type,
                'context': context,
                'h1_title': title,
                'h2_headings': ' | '.join(headings),
                'generated_at': datetime.now().isoformat()
            })
            
        except Exception as e:
            records.append({
                'filename': filename,
                'type': 'error',
                'context': str(e),
                'h1_title': '',
                'h2_headings': '',
                'generated_at': datetime.now().isoformat()
            })
    
    # Write CSV
    if records:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['filename', 'type', 'context', 'h1_title', 'h2_headings', 'generated_at']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
    
    return str(csv_file)


def main():
    """Main entry point."""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='ENNA Souzoku Title Generator')
    parser.add_argument('--batch', type=int, default=1, help='Batch number to process (default: 1)')
    parser.add_argument('--output-format', choices=['csv', 'json'], default='json', help='Output format')
    parser.add_argument('--output-dir', type=str, default='output', help='Output directory')
    
    args = parser.parse_args()
    
    # If CSV format is requested, generate for all articles
    if args.output_format == 'csv':
        csv_file = generate_all_titles_csv(base_path='.', output_dir=args.output_dir)
        print(f'✓ CSV file generated: {csv_file}')
        return {'output_file': csv_file, 'format': 'csv'}
    
    # Default: Process batch
    generator = SouzokuTitleGenerator(base_path='.')
    result = generator.process_batch(batch_num=args.batch, batch_size=10)
    
    # Print results
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # Save log
    log_file = generator.save_log()
    print(f'\nLog saved to: {log_file}')
    
    return result


if __name__ == '__main__':
    main()
