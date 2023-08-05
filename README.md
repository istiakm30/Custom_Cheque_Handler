# Receipt Generator

This is a Python script that generates a receipt image with custom values.

## Usage

The script prompts the user for the following inputs:

- Name
- Amount 
- Date (optional, will use today's date if left blank)
- Purpose of the amount

It then generates a receipt image with the provided values and prints it to the default printer.

The image contains:

- Name
- Date
- Amount in digits
- Amount in words 
- Purpose

## Requirements

- Python 3
- PIL 
- num2words
- CUPS 

The script uses PIL to generate the image, num2words to convert the numeric amount to words, and CUPS to print the file.

## Installation

```
pip install pillow num2words
```

## Running

```
python main.py
```

Follow the prompts to provide the required inputs. The generated image will be saved as `new_image.png` and printed automatically.

## Credits

Font used in the image is Arial.

Let me know if you would like me to expand or modify the README in any way!
