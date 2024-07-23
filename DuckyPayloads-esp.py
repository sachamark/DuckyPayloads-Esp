import tkinter as tk
from tkinter import filedialog
import os

us_to_es_map = {
    '@': '"',
    '#': '·',
    '^': '&',
    '&': '/',
    '*': '(',
    '(': ')',
    ')': '=',
    '-': "'",
    '=': '¡',
    '_': '?',
    '{': '^',
    '}': '*',
    '|': 'Ç',
    ';': 'ñ',
    ':': 'Ñ',
    "'": '´',
    '"': '¨',
    '<': ';',
    '>': ':',
    '/': '-',
    '?': '_'
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

    input_file = filedialog.askopenfilename(title="Selecciona el archivo de entrada")
    if not input_file:
        print("No se seleccionó ningún archivo.")
        return

    replace_chars(input_file)

if __name__ == "__main__":
    main()

