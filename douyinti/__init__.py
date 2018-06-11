import argparse
from douyinti.converter import text_to_img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="text to add effect", dest="text")
    parser.add_argument("--out", help="path of output image, default to ./out.jpeg", dest="out")
    args = parser.parse_args()

    if args.text is None:
        parser.error("please specify --text")

    out = args.out if args.out is not None else "out.jpeg"
    text_to_img(args.text, out)
