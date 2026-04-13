# Souzoku Title Generator - Hourly Automation

## Overview

毎時オートメーション・システムで、キーワード候補（`keyword-candidates-*.md`）から SEO 最適化されたタイトルと見出しを自動生成します。

**実行頻度**: 毎時間 00 分（UTC）  
**実行環境**: GitHub Actions（クラウド）  
**出力形式**: CSV（`output/keywords-titles-YYYY-MM-DD_HHmmss.csv`）  
**出力内容**: ファイル名、タイプ、文脈、H1 タイトル、H2 見出し（パイプ区切り）

---

## How It Works

### 1. GitHub Actions ワークフロー
**ファイル**: `.github/workflows/generate-titles-hourly.yml`

毎時 00 分に自動実行：
1. リポジトリをチェックアウト
2. Python 環境をセットアップ
3. `generate_titles.py --output-format csv --output-dir output` を実行
4. 生成結果（CSV）を Git にコミット・プッシュ

### 2. Python スクリプト
**ファイル**: `generate_titles.py`

#### CLI オプション
```bash
# CSV 形式で全記事タイトルを生成 (GitHub Actions 用)
python generate_titles.py --output-format csv --output-dir output

# 特定バッチをバッチ処理 (手動実行)
python generate_titles.py --batch 1

# ヘルプ
python generate_titles.py --help
```

#### 機能

- **`generate_all_titles_csv()`**
  - `articles/` 内のすべての HTML ファイルをスキャン
  - 各ファイルに対して H1 タイトルと H2 見出しを自動生成
  - 結果を CSV ファイル（`output/keywords-titles-YYYY-MM-DD_HHmmss.csv`）に出力

- **タイプ判定**
  - **neighborhood** (`*-souzoku.html`) → 町名 + 区の文脈を含める
  - **topic** (その他) → キーワード1 / キーワード2 を含める

- **出力フィールド**
  - `filename`: HTML ファイル名
  - `type`: neighborhood / topic / error
  - `context`: 町名（区名）またはキーワード
  - `h1_title`: 生成された H1 タイトル
  - `h2_headings`: H2 見出しをパイプ（`|`）で区切った形式
  - `generated_at`: タイムスタンプ（ISO 8601）

---

## Output Examples

### CSV 形式

```csv
filename,type,context,h1_title,h2_headings,generated_at
aita-souzoku.html,neighborhood,相田（安佐南区）,相田で相続相談するなら何から始める？安佐南区での不動産・保険整理ガイド,相田で相続相談を考えるときの確認事項 | 不動産と保険の整理で最初に見るポイント | 相田での相続相談前に準備したい資料 | 相続相談の進め方と次のステップ,2026-04-13T15:00:00.123456
inheritance-empty-house.html,topic,空き家 / 相続不動産,空き家になった相続不動産は放置でいい？管理・売却・活用の判断基準,空き家放置で起きやすい問題と負担 | 売却か保有か | 判断の軸を整理する | 相談前に確認・準備しておくこと | よくある質問と次のステップ,2026-04-13T15:00:00.234567
```

---

## Integration 

### Souzoku Title Generator Skill に連携

このオートメーション結果は、**Souzoku Title Generator Skill** （`.github/skills/souzoku-title-generator/SKILL.md`）の基盤として機能します。

**スキル使用フロー**:
1. GitHub Actions が毎時 CSV を生成
2. ユーザーが Skill を手動呼び出し（`/souzoku title`）
3. Skill は最新の CSV から参照 → インタラクティブにタイトル・見出しを最適化

### 他のエージェントへの引き継ぎ

生成されたタイトルと見出し構成を：
1. **Souzoku SEO Specialist** → SEO 最適化チェック
2. **Souzoku AIO Writer** → 完全な記事本文生成

---

## Manual Execution

### ローカル実行

```bash
# CSV 形式で出力
python generate_titles.py --output-format csv --output-dir output

# 特定バッチをバッチ処理して HTML を更新
python generate_titles.py --batch 1
```

### GitHub UI から手動実行

1. GitHub リポジトリ　→　**Actions** タブ
2. **"Generate Souzoku Titles Hourly"** ワークフロー選択
3. **Run workflow** → **Run workflow** クリック
4. ～1 分で実行完了、`output/` に CSV が生成

---

## Scheduled Execution History

**最新の実行結果**:
- 出力ファイル: `output/keywords-titles-*.csv`
- 更新サイクル: 毎時近 00 分（UTC）
- ファイル保有期間: 無制限（Git で管理）

CSV ファイルの履歴閲覧：
```bash
# 最新の 10 個を表示
ls -lt output/keywords-titles-*.csv | head -10

# 特定日付の結果を確認
ls output/keywords-titles-2026-04-13*.csv
```

---

## Configuration

### 実行スケジュール変更

`.github/workflows/generate-titles-hourly.yml` の `cron` 値を編集：

```yaml
on:
  schedule:
    # デフォルト: 毎時 00 分
    - cron: '0 * * * *'
    
    # 例: 毎日午前 9 時（JST = UTC+9）
    # - cron: '0 0 * * *'  # UTC 00:00
    
    # 例: 1 日 3 回（UTC）
    # - cron: '0 0,8,16 * * *'
```

**cron フォーマット**: `分 時 日 月 曜日`
- `*` = あらゆる値
- `0 * * * *` = 毎時 00 分
- `0 9 * * *` = 毎日 09:00

---

## Troubleshooting

### CSV が生成されていない

確認項目：
1. GitHub Actions が有効か確認 → Settings > Actions
2. ワークフローファイルが正しく配置されているか → `.github/workflows/`
3. Python スクリプトに構文エラーがないか
   ```bash
   python -m py_compile generate_titles.py
   ```
4. `articles/` ディレクトリが存在するか
   ```bash
   ls articles/ | head
   ```

### CSV の内容が古い

- GitHub Actions は UTC 時刻で実行します（日本時間＋9 時間）
- 手動実行で最新内容を生成：
  ```
  GitHub → Actions → "Generate Souzoku Titles Hourly" → Run workflow
  ```

---

## Files Reference

| ファイル | 役割 | 更新頻度 |
|---------|------|-------|
| `.github/workflows/generate-titles-hourly.yml` | スケジュール実行定義 | 手動（config 変更時） |
| `generate_titles.py` | タイトル生成ロジック | 手動（新機能追加時） |
| `output/keywords-titles-*.csv` | 生成結果（自動出力） | 毎時 00 分 × UTC |
| `.github/skills/souzoku-title-generator/SKILL.md` | インタラクティブ Skill | 手動（改良時） |
| `keyword-candidates-2026-04-13.md` | キーワード候補リスト | 手動（更新時） |

---

## Next Steps

- [ ] API から外部ツール（Notion、Slack）に結果を通知
- [ ] CSV 結果を HTML レポートに変換
- [ ] タイトル品質スコア（SEO スコア）を CSV に追加
- [ ] 定期的な見出し A/B テストの自動実施
