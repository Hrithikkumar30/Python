import PyPDF2  as P

file   = open("Data Sciencee/Noise reduction.pdf" , "rb")

pd = P.PdfFileReader(file)
x= pd.getPage(0)
y=pd.getPage(1)
print(y.extractText())
