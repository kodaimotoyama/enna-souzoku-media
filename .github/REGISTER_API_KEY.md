# Claude APIキー登録ガイド（提供済み）

提供いただいたClaude APIキーをGitHub Secretsに登録する手順です。

## 🔐 セキュリティ上の注意

⚠️ **このAPIキーはチャットに表示されているため、以下の手順で登録後に Anthropic Console で新しいキーに変更してください。**

---

## 📝 GitHub Secrets へ登録する手順

### ステップ1: GitHubにログイン

1. [GitHub](https://github.com) を開く
2. ログイン（未ログインの場合）

### ステップ2: リポジトリ設定を開く

1. `https://github.com/[your-username]/enna-souzoku-media` を開く
2. **Settings** タブをクリック

### ステップ 3: Secrets メニューを開く

左サイドバーから：
- **Security** → **Secrets and variables** → **Actions**

（または直接: `https://github.com/[your-username]/enna-souzoku-media/settings/secrets/actions`）

### ステップ4: 新しいシークレットを作成

**New repository secret** ボタンをクリック

### ステップ5: シークレット情報を入力

以下の情報を入力：

```
Name: CLAUDE_API_KEY

Secret: YOUR_CLAUDE_API_KEY_HERE
```

### ステップ6: 保存

**Add secret** ボタンをクリック

---

## ✅ 動作確認

シークレットが登録されたら、ワークフローが自動実行開始します：

**実行スケジュール**: 毎時 00 分（UTC）

または、手動実行：
1. **Actions** タブをクリック
2. **Generate Souzoku Titles Hourly** ワークフローを選択
3. **Run workflow** → **Run workflow** をクリック

ワークフロー実行後、 `articles/` フォルダに新しい記事HTMLが生成されます。

---

## 🔄 セキュリティ: APIキーの更新（推奨）

このチャットにキーが表示されているため、以下の手順で新しいキーに変更してください：

### 1. Anthropic Console で新しいキーを生成

1. [Anthropic Console](https://console.anthropic.com/) を開く
2. **API Keys** セクションを開く
3. 古いキーを「Delete」または「Deactivate」
4. **Create Key** で新しいキーを生成
5. 新しいキーをコピー

### 2. GitHub Secretsを更新

1. GitHub リポジトリ → **Settings** → **Secrets and variables** → **Actions**
2. **CLAUDE_API_KEY** をクリック
3. **Update secret** をクリック
4. 新しいAPIキーを貼り付け
5. **Update secret** をクリック

---

## 📞 サポート

**ワークフロー実行に問題があった場合:**

1. GitHub → **Actions** タブ
2. **Generate Souzoku Titles Hourly** の最新実行結果をクリック
3. ログを確認（赤いエラーメッセージが表示されている場合）

一般的なエラー：
- `401 Unauthorized` → APIキーが無効（新しいキーを登録）
- `403 Forbidden` → API呼び出し制限（Anthropic console で使用量を確認）
- `Rate limit exceeded` → 一時的な制限（数分待機後、再実行）

---

**登録完了したら、毎時5本の記事が自動生成・公開されます！🚀**
