import PyPDF2
input_file = PyPDF2.PdfFileReader(open("261852'rb'))
watermark_file = PyPDF2.PdfFileReader(open("wtr.pdf",'rb'))
Output_file = PyPDF2.PdfFileWriter()
for i in range(input_file.getNumPages()):
    page = input_file.getPage(i)
    wtr =watermark_file.getPage(0)
    page.mergePage(wtr)
    Output_file.addPage(page)

with open("Yoyo.pdf",'wb') as output :
    Output_file.write(output)

