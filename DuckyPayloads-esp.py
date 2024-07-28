import tkinter as tk
from tkinter import filedialog
import os

us_to_es_map = {
    '"':'@',
    '#':'·',
    '^':'{',
    '&':'^',
    '*':'\\',
    '(':'*',
    ')':'(',
    '=':')',
    '_':'§',
    '|': '!',
    ';':'<',
    ':':'>',
    '/':'&',
    '-':"/",
    "'":'-',
    '?':'_',
    '§':'?',
    '}':"""
DELAY 300
GUI r
DELAY 100
STRING charmap
DELAY 100
ENTER
DELAY 600
TAB
TAB
DELAY 100
RIGHTARROW
REPEAT 91
DELAY 100
TAB
TAB
DELAY 100
ENTER
DELAY 100
ALT F4
DELAY 300
CTRL V
DELAY 100
STRING """,
    '{':"""
DELAY 300
GUI r
DELAY 100
STRING charmap
DELAY 100
ENTER
DELAY 600
TAB
TAB
DELAY 100
RIGHTARROW
REPEAT 89
DELAY 100
TAB
TAB
DELAY 100
ENTER
DELAY 100
ALT F4
DELAY 300
CTRL V
DELAY 100
STRING """,
    '[':"""
DELAY 300
GUI r
DELAY 100
STRING charmap
DELAY 100
ENTER
DELAY 600
TAB
TAB
DELAY 100
RIGHTARROW
REPEAT 57
DELAY 100
TAB
TAB
DELAY 100
ENTER
DELAY 100
ALT F4
DELAY 300
CTRL V
DELAY 100
STRING """,
    ']': """
DELAY 300
GUI r
DELAY 100
STRING charmap
DELAY 100
ENTER
DELAY 600
TAB
TAB
DELAY 100
RIGHTARROW
REPEAT 59
DELAY 100
TAB
TAB
DELAY 100
ENTER
DELAY 100
ALT F4
DELAY 300
CTRL V
DELAY 100
STRING """,
    '+':']',
    '`':'['
}

def replace(content):
    for us_char, es_char in us_to_es_map.items():
        content = content.replace(us_char, es_char)
    return content

def replace_chars(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        modified_content = replace(content)

        base, ext = os.path.splitext(input_file)
        output_file = f"{base}-esp{ext}"

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Archivo procesado y guardado como {output_file}")

    except FileNotFoundError:
        print(f"El archivo {input_file} no se encontró.")
    except IOError:
        print("Ocurrió un error al leer o escribir el archivo.")

def main():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(title="Selecciona el payload.")
    if not input_file:
        print("No se seleccionó ningún archivo.")
        return

    replace_chars(input_file)

if __name__ == "__main__":
    main()
