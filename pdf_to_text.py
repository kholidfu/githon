#!/usr/bin/python
# @sopier

import sys
import re
import subprocess

class PdfToText(object):
    """Simple PDF to Text Module

    Usage:
        python pdf_to_text.py file_name.pdf
    Output:
        file_name.pdf.txt"""

    PDF_FILE = 'pdf.pdf'
    TXT_FILE = 'pdf.txt'

    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        subprocess.call(["mv", sys.argv[1], self.PDF_FILE])

    def pdf_to_text(self):
        # calling pdftotext, output => .txt
        subprocess.call(["pdftotext", self.PDF_FILE])

    def read_txt_n_clean_them(self):
        f = open(self.TXT_FILE, 'r')
        data = f.read()
        f.close()

        clean_dot = data.replace('.', '')
        clean_new_line = clean_dot.replace('\n', ' ')
        clean_double_space = re.sub(re.compile(r"\s{2,}"), ' ', clean_new_line)
        return clean_double_space

    def save_to_txt_file(self):
        txt_file = sys.argv[1] + '.txt'
        new_file = open(txt_file, 'w')
        new_file.write(self.read_txt_n_clean_them())
        new_file.close()


if __name__ == '__main__':
    pdf = PdfToText(sys.argv[1])
    pdf.pdf_to_text()
    pdf.read_txt_n_clean_them()
    pdf.save_to_txt_file()
