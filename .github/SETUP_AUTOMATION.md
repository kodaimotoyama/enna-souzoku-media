# GitHub Secretsへの登録手順

毎時5本の記事を自動生成するために、Claude APIキーをGitHub Secretsに登録してください。

## 手順

### 1. Claude APIキーの取得

1. [Anthropic Claude Console](https://console.anthropic.com/) にアクセス
2. ログインして、`API Keys` 或は `Keys` メニューで新しいAPIキーを生成
3. キーをコピー（後で使用）

### 2. GitHub Secretsへの登録

1. GitHub リポジトリを開く
   - `enna-souzoku-media` リポジトリ
   
2. **Settings** → **Secrets and variables** → **Actions** をクリック

3. **New repository secret** ボタンをクリック

4. 以下を入力：
   - **Name**: `CLAUDE_API_KEY`
   - **Secret**: 上記でコピーしたAPIキーを貼り付け

5. **Add secret** をクリックして保存

### 3. 動作確認

- ワークフロー: `.github/workflows/generate-titles-hourly.yml`
- 毎時実行: 毎時 00 分（UTC）
- または、GitHub UI → **Actions** → **Generate Souzoku Titles Hourly** → **Run workflow** で手動実行

## 自動実行内容

```
毎時 00 分 (UTC):
1. generate_titles.py → タイトル・見出しをCSV生成
2. generate_articles.py → Claude APIで記事本文生成（5本）
3. articles/ へHTML保存
4. Git にコミット・プッシュ
```

## コスト

- Claude API呼び出し: 記事1本あたり約 3,000～5,000トークン
- 毎時5本 × 約4,000トークン = 20,000トークン/時
- 月間: 約 480,000トークン

Claude Sonnet 3.5 の価格（2026年4月時点）:
- Input: $3 / 100万トークン
- Output: $15 / 100万トークン

毎月の推定コスト: 約 $10～20

## トラブルシューティング

**APIキーが無効というエラーが出た場合:**
1. Anthropic Console で有効なAPIキーを確認
2. Secret を再度登録

**記事生成が失敗する場合:**
1. GitHub Actions のログで詳細を確認
2. Anthropic コンソールでAPI使用量を確認

---

**登録後、ワークフローは毎時自動実行されます！**
