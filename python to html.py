from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import tkinter as tk
from tkinter import filedialog

def convert_to_html():
    root = tk.Tk()
    root.withdraw()

    py_file = filedialog.askopenfilename()
    html_file = filedialog.asksaveasfilename(defaultextension=".html")

    with open(py_file, 'r') as f:
        code = f.read()

    html_code = highlight(code, PythonLexer(), HtmlFormatter(full=True))

    with open(html_file, 'w') as f:
        f.write(html_code)

# Usage
convert_to_html()
