import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    output = "merged.pdf"
    merger.write(output)
    merger.close()
    print(f"Merged PDFs into {output}")

def select_pdfs():
    root = tk.Tk()
    root.withdraw()  # Preventing the tk dialog window from appearing
    pdf_list = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])  # Returns a tuple of selected files
    return pdf_list

def main():
    pdf_list = select_pdfs()
    if pdf_list:
        merge_pdfs(pdf_list)
    else:
        print("No PDFs selected.")

if __name__ == "__main__":
    main()
