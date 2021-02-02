from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import argparse as ap

image_size = 1025

header_size = 95
header_position = (60, 45)


def main():
    pr = ap.ArgumentParser(description='Image generator for the SCP-CS Instagram')
    pr.add_argument('-s', '--scp', help='Item number', required=True)
    pr.add_argument('-c', '--class', help='Object Class', required=True)
    pr.add_argument('-d', '--description', help='Description (duh)', required=True)
    pr.add_argument('-o', '--output', help='The output file', required=True)

    args = pr.parse_args()

    img = Image.open('media/bg_text.png')
    draw = ImageDraw.Draw(img)

    header_font = ImageFont.truetype('JetBrainsMono-Bold.ttf', header_size)

    # Draw header
    draw.text(header_position, args.scp, (0, 0, 0), font=header_font)
    img.save(args.output)


if __name__ == '__main__':
    main()
