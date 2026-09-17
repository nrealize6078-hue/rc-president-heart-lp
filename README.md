# 社長向けLP「社員を想う、その先へ。」編集用コピー

元サイト: https://realize-president-heart.uminchu-t0422.chatgpt.site/
（ChatGPTのサイト公開機能でホスティングされているページ。2026年9月17日時点の内容を取得）

## ファイル構成

| ファイル | 中身 |
|---|---|
| `index.html` | 本文（全7セクション＋フッター＋案内モーダル）。整形済みで直接編集できる |
| `style.css` | デザイン。セクションごとに `/* ==== HERO ==== */` のコメントで区切ってある |
| `script.js` | 「旅のはじめ方を見る」モーダルの開閉とコピー処理（下記「補ったもの」参照） |
| `assets/hero.jpg` | ファーストビューの写真（186KB） |

ビルド不要。`index.html` をそのまま置けば動く静的サイト。

## セクションの順番（index.html の上から）

1. `.hero` — DEAR PRESIDENT / その想いは、まだ、もっと届く。
2. `#letter` — 「この会社に入って、よかった。」
3. `.belief` — 社員を想う気持ちを、届けられる仕組みへ
4. `.outside` — 社員には、会社から見えない人生がある
5. `.system` — 3つの機能（学ぶ／考える／相談する）＋REALIZEマーケット
6. `.ripple` — 社長の想い → 社員の人生 → 家族の未来 → 地域の明日
7. `#journey` — PRESIDENT JOURNEY ＋ ご案内カード
8. `<dialog id="guide">` — 「旅のはじめ方を見る」で開く案内モーダル

## プレビュー

`.claude/launch.json` に `lp-president-heart`（ポート8956）として登録済み。
手動で見る場合:

```bash
python -m http.server 8956 --directory "C:/Users/realize5/Documents/Claude/rc-president-heart-lp"
```

## 元サイトから変えたところ

- Cloudflareが自動挿入していた計測スクリプトを削除
- 1行に圧縮されていたHTML/CSSを整形（見た目は変えていない）
- 画像を `assets/` へ移動し、CSSの参照先を `assets/hero.jpg` に変更
- **`script.js` を新規追加**。元サイトにはモーダルを開閉するJSが含まれておらず、
  「旅のはじめ方を見る」「文章をコピー」ボタンが無反応だった。最小構成で補完してある。
  コピーされる定型文は `script.js` の `MESSAGE` で変更できる。

## 公開先（2026年9月17日 公開済み）

```
https://nrealize6078-hue.github.io/rc-president-heart-lp/
```

| | |
|---|---|
| リポジトリ | [nrealize6078-hue/rc-president-heart-lp](https://github.com/nrealize6078-hue/rc-president-heart-lp)（public） |
| 公開方法 | GitHub Pages（main / ルート） |
| 検索エンジン | **掲載する**（noindexは入れていない） |

### 直したあとの反映

このフォルダがそのままリポジトリなので、コミットしてpushすれば1〜2分で本番に出る。

```bash
cd "C:/Users/realize5/Documents/Claude/rc-president-heart-lp" && git add -A && git commit -m "文言修正" && git push
```

### 元サイトとの関係

元の `...chatgpt.site` のページは別物として残っている。
**こちらを直しても元サイトは変わらない。** 今後はGitHub Pages側を正とし、
元サイトは使わない（または案内リンクをこちらへ差し替える）のが分かりやすい。

### まだ入れていないもの

- OGP画像（LINEやSNSでURLを送ったときのサムネイル）。必要なら1200×630を作って
  `<meta property="og:image">` を足す
- 独自ドメイン（`realizeclub.net` 配下に置きたい場合はCNAME設定が必要）
