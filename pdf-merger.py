import PyPDF2

def merge_pdfs(pdfs, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        pdf_merger.append(PyPDF2.PdfReader(pdf))

    with open(output_file, 'wb') as f:
        pdf_merger.write(f)

if __name__ == '__main__':
    pdfs = ['1.pdf', '2.pdf', '3.pdf']
    output_file = 'merged_file.pdf'
    merge_pdfs(pdfs, output_file)
