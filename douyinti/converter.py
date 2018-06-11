from PIL import Image, ImageDraw, ImageFont
import numpy as np

def text_to_img(txt, outpath):
    fnt = ImageFont.truetype('/Library/Fonts/Tahoma Bold.ttf', 100)
    width = len(txt) * 65
    text1 = Image.new("RGB", (width, 180), color=(0, 0, 0))
    text2 = Image.new("RGB", (width, 180), color=(0, 0, 0))
    textdraw1 = ImageDraw.ImageDraw(text1, "RGB")
    textdraw2 = ImageDraw.ImageDraw(text2, "RGB")
    textdraw1.text((23, 23), txt, font=fnt, fill=(255, 0, 0))
    textdraw2.text((18, 18), txt, font=fnt, fill=(0, 255, 255))
    array1 = np.array(text1)
    array2 = np.array(text2)
    result_array = array1 + array2
    result = Image.fromarray(result_array)
    result.save(outpath)
