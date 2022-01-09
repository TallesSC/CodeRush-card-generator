import textwrap
from PIL import Image, ImageFont, ImageDraw


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
        spacing=16,
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
        text=str(difficulty),
        fill="black",
        stroke_fill="black",
        stroke_width=1,
        font=difficulty_font,
        align="center"
    )


def drawOptions(draw, a, b, c, d, e):
    options_font = ImageFont.truetype('assets/fonts/Consolas.ttf', 36)
    draw.text(xy=(70, 860), text="A) " + str(a), fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(70, 935), text="B) " + str(b), fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(70, 1010), text="C) " + str(c), fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(470, 860), text="D) " + str(d), fill="black", font=options_font, stroke_fill="black", stroke_width=1)
    draw.text(xy=(470, 935), text="E) " + str(e), fill="black", font=options_font, stroke_fill="black", stroke_width=1)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def drawCardBack(answer):
    card_width = 827
    card_height = 1122
    card_back = Image.new(mode="RGB", size=(card_width, card_height), color="black")
    draw = ImageDraw.Draw(card_back)
    draw.rounded_rectangle(
        xy=(370, 870, 457, 957),
        radius=100,
        fill="white"
    )
    answer_font = ImageFont.truetype('assets/fonts/Typori-Regular.ttf', 64)
    draw.text(
        text=answer.capitalize(),
        xy=(397, 873),
        fill="black",
        font=answer_font
    )
    logo = Image.open("assets/images/CodeRush_logo.png")
    card_back.paste(im=logo, box=(int(card_width/2 - logo.width/2), 250), mask=logo)
    return card_back


def generateIndividualCardsJPEG(cards, background_color, path):
    card_width = 827
    card_height = 1122

    images = []
    back_images = []
    index = 1
    for card in cards:
        img = Image.new(
            mode="RGB",
            size=(card_width, card_height),
            color=hex_to_rgb(background_color)
        )

        draw = ImageDraw.Draw(img)
        drawBackground(draw, card_width, card_height)
        drawTitle(draw, card_width, card["baralho"])
        drawBody(draw, card["enunciado"])
        drawDifficulty(draw, card["dificuldade"], background_color)
        drawOptions(draw, card["alternativa_a"], card["alternativa_b"], card["alternativa_c"], card["alternativa_d"],
                    card["alternativa_e"])
        back_images.append(drawCardBack(card["resposta"]))

        img.save(path + "/" + str(card["baralho"]) + str(index) + ".jpg")
        images.append(img)
        index += 1

    return {
        "front_cards": images,
        "back_cards": back_images
    }


def drawMargins(page):
    draw = ImageDraw.Draw(page)
    draw.line(xy=[(293, 263), (293, 4699)], width=1, fill="black")
    draw.line(xy=[(1048, 263), (1048, 4699)], width=1, fill="black")
    draw.line(xy=[(1377, 263), (1377, 4699)], width=1, fill="black")
    draw.line(xy=[(2132, 263), (2132, 4699)], width=1, fill="black")
    draw.line(xy=[(2461, 263), (2461, 4699)], width=1, fill="black")
    draw.line(xy=[(3216, 263), (3216, 4699)], width=1, fill="black")
    draw.line(xy=[(221, 435), (3288, 435)], width=1, fill="black")
    draw.line(xy=[(221, 1485), (3288, 1485)], width=1, fill="black")
    draw.line(xy=[(221, 1956), (3288, 1956)], width=1, fill="black")
    draw.line(xy=[(221, 3006), (3288, 3006)], width=1, fill="black")
    draw.line(xy=[(221, 3477), (3288, 3477)], width=1, fill="black")
    draw.line(xy=[(221, 4527), (3288, 4527)], width=1, fill="black")


def generatePrintablePDFs(cards, path):
    page_width = 3508
    page_height = 4961

    cont = 0
    pages = []
    while cont < len(cards["front_cards"]):
        page = Image.new(mode="RGB", size=(page_width, page_height), color="white")
        back_page = Image.new(mode="RGB", size=(page_width, page_height), color="white")
        drawMargins(page)
        drawMargins(back_page)

        for i in range(9):
            if cont >= len(cards["front_cards"]):
                break

            page.paste(
                im=cards["front_cards"][cont],
                box=((i % 3 + 1) * 257 + (i % 3) * 827, (i // 3 + 1) * 399 + (i // 3) * 1122)
            )
            back_page.paste(
                im=cards["back_cards"][cont],
                box=((3 - (i % 3)) * 257 + (2 - (i % 3)) * 827, (i // 3 + 1) * 399 + (i // 3) * 1122)
            )

            cont += 1
        pages.append(page)
        pages.append(back_page)

    printable = pages[0]
    pages.pop(0)
    printable.save(
        fp=path + "/printable.pdf",
        save_all=True,
        append_images=pages
    )
