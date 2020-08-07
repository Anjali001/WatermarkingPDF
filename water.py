import PyPDF2
input_file = PyPDF2.PdfFileReader(open("261852'rb')) #Write the input_file here
watermark_file = PyPDF2.PdfFileReader(open("wtr.pdf",'rb')) # This is the file that has wateramrk
Output_file = PyPDF2.PdfFileWriter() 
for i in range(input_file.getNumPages()): # Looping over all pages of input file
    page = input_file.getPage(i) #getting a page of input file
    wtr =watermark_file.getPage(0) # Getting watermark page
    page.mergePage(wtr) # Putting watermark on input file page
    Output_file.addPage(page) # added merged page to new pdf

with open("Yoyo.pdf",'wb') as output :
    Output_file.write(output) 

