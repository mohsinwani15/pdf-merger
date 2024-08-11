import PyPDF2

import sys

input_files = sys.argv[1:]

# merger_file func is used to merge multiple pdfs
def merger_file (pdf_files):
    merger = PyPDF2.PdfWriter()
    
    for pdf in pdf_files:
        merger.append(pdf)
    
    merger.write("merged_file.pdf")
    merger.close()


# merger_file(input_files)


# watermark adder
def watermark_adder(pdf,watermark):
    template = PyPDF2.PdfReader(open(pdf, 'rb'))
    watermark = PyPDF2.PdfReader(open(watermark, 'rb'))
    output = PyPDF2.PdfWriter()

    for i in range(len(template.pages)):
        page = template.pages[i]
        page.merge_page(watermark.pages[0])
        output.add_page(page)
        
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)

watermark_adder("merged_file.pdf","wtr.pdf")