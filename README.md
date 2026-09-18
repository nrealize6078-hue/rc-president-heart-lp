# 社長向けLP「社員を想う、その先へ。」編集用コピー

元サイト: https://realize-president-heart.uminchu-t0422.chatgpt.site/
（ChatGPTのサイト公開機能でホスティングされているページ。2026年9月17日時点の内容を取得）

## ファイル構成

| ファイル | 中身 |
|---|---|
| `index.html` | 本文（全7セクション＋フッター＋固定ボトムバー）。整形済みで直接編集できる |
| `style.css` | デザイン。セクションごとに `/* ==== HERO ==== */` のコメントで区切ってある |
| `script.js` | 固定ボトムバーの出し入れとLINE画像のフォールバック（下記「補ったもの」参照） |
| `assets/hero.jpg` | ファーストビューの写真（187KB） |
| `assets/ogp.jpg` | 1200×630。SNS・LINEでURLを送ったときのサムネイル |
| `tools/build_ogp.py` | 上のOGP画像を作り直すスクリプト（`python tools/build_ogp.py`） |

ビルド不要。`index.html` をそのまま置けば動く静的サイト。

## セクションの順番（index.html の上から）

1. `.hero` — DEAR PRESIDENT / その想いは、まだ、もっと届く。
2. `#letter` — 「この会社に入って、よかった。」
3. `.belief` — 社員を想う気持ちを、届けられる仕組みへ
4. `.outside` — 社員には、会社から見えない人生がある
5. `.system` — 3つの機能（学ぶ／考える／相談する）＋REALIZEマーケット
6. `.ripple` — 社長の想い → 社員の人生 → 家族の未来 → 地域の明日
7. `#journey` — PRESIDENT JOURNEY ＋ ご案内カード
8. 固定ボトムバー `#ctabar` — ヒーローを抜けたら出る（金色ボタン）

## LINE導線

問い合わせはLINE公式に一本化。リンクは `https://lin.ee/8jf4Da7`（**index.html内4か所**）。

| 場所 | 見た目 |
|---|---|
| ファーストビュー | 白いボタン「LINEで相談する」（金ボタンの下） |
| 最終CTA（`.invitation`） | 金ボタン「旅のはじめ方を見る」＋LINE公式の友だち追加ボタン |
| 固定ボトムバー | 金色ボタン「LINEで相談する」 |

- 友だち追加ボタンはLINE公式配布画像。読み込めない時は `script.js` が緑のテキストボタンに差し替える
- 固定バーの高さ分の余白は `--bar-h`（70px）で footer の `padding-bottom` に確保。**PC・スマホ両方のfooterルールに入れること**
- `hidden` 属性はCSSの `display` に負けるため、CSS冒頭に `[hidden]{display:none!important}` を置いてある。消さない
- 担当者経由の案内モーダル（旧 `<dialog id="guide">`）は廃止済み

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
- **`script.js` を新規追加**。元サイトにはJSが1本も無く、案内ボタンが無反応だった。
  当初はモーダルを補完していたが、LINE登録リンクが用意できたため**LINE導線に一本化**し、
  現在は固定ボトムバーの制御とLINE画像のフォールバックだけを担う。

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

### OGP画像

`assets/ogp.jpg`（1200×630）。ヒーロー写真に同じ紺のベールを重ね、
游明朝で「その想いは、まだ／もっと届く。」を置いた構図。

文言や配色を変えるときは `tools/build_ogp.py` を直して作り直す。

```bash
python tools/build_ogp.py
```

**URLを変えたら `index.html` の `og:url` / `og:image` / `canonical` も直すこと。**
OGPは絶対URLで書く必要があるため、相対パスにできない。

FacebookやLINEは一度読んだOGPをキャッシュするので、差し替え直後に古い画像が出る場合は
[Facebookシェアデバッガー](https://developers.facebook.com/tools/debug/)で再取得する。

### まだ入れていないもの

- 独自ドメイン（`realizeclub.net` 配下に置きたい場合はCNAME設定が必要）

## デザイン刷新（2026年9月18日）

- 刷新は **`theme.css` に集約**（`style.css` の後に読む）。アイボリー＋紺金、ピル型ボタン、角丸カード
- **AI的な装飾は使わない**：矢印（↓↗→）・文章前の短い横線・二重枠・「SCROLL」表示は入れない
- ファーストビューは**写真に影を重ねない**。PCは紺地の左に文字＋右に角丸写真、スマホ・タブレットは写真が上・文字が下
- ヘッダー・フッターのロゴ左に **Bマーク**（`assets/bmark-96.png` / `-192.png`）。430px以下はヘッダーのナビを省く（固定バーが同じ役目）
- CSSを変えたら `index.html` の `theme.css?v=3` の数字を上げる（上げないとキャッシュで届かない）

## 改行の固定（どのスマホでも同じ位置で改行）

- 本文は文節タグ `<w-b>` で包んである。760px以下で `inline-block` になり、**文節の途中で折り返さない**
- `<br>` 区切りの各行は、320px幅で1行に収まる大きさを実測し、要素に `data-fit` と `style="--fit:Nvw;--fit-cap:Cpx"` で持たせている。
  520px以下で `font-size:min(--fit-cap, --fit)`。vw比例なので320pxで収まれば全機種で収まる
- 長すぎる行は文節の切れ目に `<br class="sp">`（520px以下だけ改行）を入れてある（8か所）
- **文章を変えたら測り直す**：ローカルで開いたページのコンソールで `_measure.js` を読み込み、
  `await __fit(320,430,{all:true,useCap:true})` の結果で `--fit` を更新。`await __measure(幅)` で違反0を確認する
  （`_measure.js` `_apply_bunsetsu.py` `_bunsetsu.py` はローカル専用。`_` で始まるファイルは公開しない）
