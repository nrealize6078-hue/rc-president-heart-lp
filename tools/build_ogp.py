# -*- coding: utf-8 -*-
"""OGP画像(1200x630)を assets/ogp.jpg として書き出す。
   ファーストビュー(assets/hero.jpg)と同じ写真・同じ配色で、
   縦書きLPのヒーローをそのまま横1200×630に収めた構図。
   python tools/build_ogp.py で再生成できる。"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BASE = os.path.join(os.path.dirname(__file__), '..')
HERO = os.path.join(BASE, 'assets', 'hero.jpg')
OUT = os.path.join(BASE, 'assets', 'ogp.jpg')

GOLD = (222, 189, 128)
WHITE = (255, 255, 255)
NAVY = (7, 23, 34)

MINCHO = 'C:/Windows/Fonts/yumin.ttf'        # 游明朝（見出し＝サイトのh1と同系）
MINCHO_B = 'C:/Windows/Fonts/yumindb.ttf'
GOTHIC = 'C:/Windows/Fonts/YuGothM.ttc'      # 游ゴシック（本文）
GOTHIC_B = 'C:/Windows/Fonts/YuGothB.ttc'
GEORGIA = 'C:/Windows/Fonts/georgia.ttf'     # ロゴ（サイトのbrandと同じ）


def font(path, size):
    return ImageFont.truetype(path, size)


def tracked(draw, xy, text, f, fill, tracking=0):
    """letter-spacing付きで1行描く。描いた幅を返す。"""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x - tracking - xy[0]


# --- 背景：写真をcoverで敷き、左から紺のグラデーションを重ねる ---
img = Image.open(HERO).convert('RGB')
scale = max(W / img.width, H / img.height)
img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
# 人物が右に来るよう、横は中央から少し右寄りで切る
left = min(img.width - W, max(0, (img.width - W) // 2 + 60))
top = max(0, (img.height - H) // 2)
canvas = img.crop((left, top, left + W, top + H))

# 左86%→右5%の紺ベール（サイトのhero-imgと同じ値）
veil = Image.new('L', (W, 1))
for x in range(W):
    t = x / (W - 1)
    a = 0.90 - (0.90 - 0.30) * min(t / 0.60, 1.0) if t < 0.60 else 0.30 - (0.30 - 0.06) * ((t - 0.60) / 0.40)
    veil.putpixel((x, 0), int(a * 255))
veil = veil.resize((W, H))
canvas = Image.composite(Image.new('RGB', (W, H), NAVY), canvas, veil)

d = ImageDraw.Draw(canvas)

# --- 上：ロゴ ---
x = 72
x += tracked(d, (x, 56), 'REALIZE ', font(GEORGIA, 30), WHITE, 4)
tracked(d, (x, 56), 'CLUB', font(GEORGIA, 30), WHITE, 4)
tracked(d, (72, 100), '人生支援経営という、新しい選択。', font(GOTHIC, 14), (206, 214, 218), 1.6)

# --- 中：eyebrow＋見出し ---
tracked(d, (72, 196), 'DEAR PRESIDENT', font(GOTHIC_B, 17), GOLD, 3.4)

f_h1 = font(MINCHO, 76)
tracked(d, (72, 250), 'その想いは、まだ、', f_h1, WHITE, 6)
tracked(d, (72, 356), 'もっと届く。', f_h1, GOLD, 6)

# --- 下：リード文 ---
tracked(d, (72, 492), '社員を大切にしたい。その気持ちを、', font(GOTHIC, 22), WHITE, 1.4)
tracked(d, (72, 530), '社員と家族の人生を支える仕組みへ。', font(GOTHIC, 22), WHITE, 1.4)

# 金の罫線
d.rectangle([72, 466, 72 + 56, 468], fill=GOLD)

canvas.save(OUT, 'JPEG', quality=88, optimize=True, progressive=True)
print('wrote', OUT, os.path.getsize(OUT), 'bytes', canvas.size)
