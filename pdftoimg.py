import fitz
pdffile = "Name.pdf"
with fitz.open(pdffile) as doc:
	for page in doc:
		print("page %i" % page.number)
		Page = doc.loadPage(page.number)  # number of page
		pix = Page.getPixmap()
		output = "Name"
		output = output+str(page.number)+str('.png')
		pix.writePNG(output)