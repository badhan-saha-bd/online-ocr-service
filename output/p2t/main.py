import PyPDF2 as p2
def extract(path):
    PDFfile = open(path,"rb")
    pdfread = p2.PdfFileReader(PDFfile)
    i=0
    var =''
    while i<pdfread.getNumPages():
        pageinfo = pdfread.getPage(i)
        var=var+pageinfo.extractText()
        i=i+1
    return var

#print(extract("pdfs/test.pdf"))
