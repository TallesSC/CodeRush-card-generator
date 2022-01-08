import textwrap
from PIL import Image, ImageFont, ImageDraw


def drawMargins(draw, card_width, card_height):
    draw.rectangle(
        xy=(36, 36, card_width - 36, card_height - 36),
        fill='cyan'
    )


def drawBackground(draw, card_width, card_height):
    draw.rectangle(
        xy=(0, 170, card_width, card_height - 300),
        fill='black',
    )


def drawTitle(draw, card_width, title):
    title_font = ImageFont.truetype('assets/fonts/Typori-Regular.ttf', 90)
    title_width, title_height = draw.textsize(
        text=title,
        font=title_font
    )
    draw.text(
        xy=((card_width - title_width) / 2, 55),
        text=title.capitalize(),
        fill="black",
        stroke_fill="black",
        stroke_width=1,
        font=title_font,
        align="center"
    )


def drawBody(draw, text):
    body_font = ImageFont.truetype('assets/fonts/Consolas.ttf', 40)
    paragraphs = text.splitlines()
    wrapped_paragraphs = []
    for p in paragraphs:
        wrapped_paragraphs.append(textwrap.fill(
            text=p,
            width=32,
            replace_whitespace=False,
            drop_whitespace=False,
            break_long_words=True,
            expand_tabs=False,
            tabsize=4
        ))
    draw.text(
        xy=(60, 195),
        text="\n".join(wrapped_paragraphs),
        fill="white",
        font=body_font,
        align="left",
    )


def drawDifficulty(draw, difficulty, color):
    draw.rounded_rectangle(
        xy=(680, 710, 770, 800),
        fill=hex_to_rgb(color),
        radius=10
    )
    difficulty_font = ImageFont.truetype('assets/fonts/Typori-Regular.ttf', 80)
    draw.text(
        xy=(702, 708),
        text=difficulty,
        fill="black",
        stroke_fill="black",
        stroke_width=1,
        font=difficulty_font,
        align="center"
    )


def drawOptions(draw, a, b, c, d, e):
    options_font = ImageFont.truetype('assets/fonts/Consolas.ttf', 36)
    draw.text(xy=(70, 860), text="A) " + a, fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(70, 935), text="B) " + b, fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(70, 1010), text="C) " + c, fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(470, 860), text="D) " + d, fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(470, 935), text="E) " + e, fill="black", font=options_font, stroke_fill="black", stroke_width=1)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def generateIndividualCardsJPEG(cards, background_color):
    print("Gerando arquivos...")
    card_width = 827
    card_height = 1122

    # for card in cards:
    img = Image.new(
        mode="RGB",
        size=(card_width, card_height),
        color=hex_to_rgb(background_color)
    )

    draw = ImageDraw.Draw(img)
    drawMargins(draw, card_width, card_height)
    drawBackground(draw, card_width, card_height)
    drawTitle(draw, card_width, cards[0]["baralho"])
    drawBody(draw, cards[0]["enunciado"])
    drawDifficulty(draw, cards[0]["dificuldade"], background_color)
    drawOptions(draw, cards[0]["alternativa_a"], cards[0]["alternativa_b"], cards[0]["alternativa_c"],
                cards[0]["alternativa_d"], cards[0]["alternativa_e"])

    img.show()
