import os
import datetime
import time
from PIL import Image, ImageDraw, ImageFont
import subprocess
from num2words import num2words


def select_printer():
    try:
        output = subprocess.check_output("lpstat -p", shell=True).decode()
    except subprocess.CalledProcessError:
        raise Exception("No printers found or there's a problem with your CUPS setup")

    lines = [line for line in output.split('\n') if line.startswith('printer')]

    if not lines:
        raise Exception("No printers found")

    if len(lines) == 1:
        return lines[0].split(' ')[1]

    print("Multiple printers found. Please choose one:")
    for i, line in enumerate(lines):
        print(f"{i + 1}. {line.split(' ')[1]}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return lines[choice].split(' ')[1]


def print_file(filename):
    try:
        printer = select_printer()
        os.system(f"lpr -P {printer} {filename}")
    except Exception as e:
        print(str(e))


def add_value(name, date, amount, amount_word, for_):
    img = Image.new('RGBA', (1228, 462), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((190, 155), name, (0, 0, 0), font=font)
    draw.text((870, 135), date, (0, 0, 0), font=ImageFont.truetype("arial.ttf", 25))
    draw.text((1050, 185), amount, (0, 0, 0), font=ImageFont.truetype("arial.ttf", 30))
    draw.text((188, 220), amount_word, (0, 0, 0), font=font)
    draw.text((104, 350), for_, (0, 0, 0), font=ImageFont.truetype("arial.ttf", 30))
    img.save('new_image.png')


def main():
    name = input("Enter your name: ")
    amount = input("Enter the amount: ")
    date = input("Enter the date (leave blank for today's date): ")
    for_ = input("Enter the purpose of the amount: ")

    amount_words = amount.split(".")
    amount_word = ''
    if len(amount_words) == 1:
        amount_word = num2words(amount, lang='en_IN') + " and zero cents"
    elif len(amount_words) == 2:
        amount_word = num2words(amount_words[0], lang='en_IN') + " and "
        amount_word += num2words(amount_words[1], lang='en_IN') + " cents"
    amount_word = amount_word.replace(",", "")
    amount_word = amount_word[0].upper() + amount_word[1:]

    if date == '':
        date = datetime.datetime.now().strftime("%m/%d/%Y")

    add_value(name, date, amount, amount_word, for_)

    # Use the function to print a file
    print_file("gen_img.png")


if __name__ == "__main__":
    main()
