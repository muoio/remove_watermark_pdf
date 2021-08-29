import fitz  # this is pymupdf


def replace_text(pdf_path, text):
	with fitz.open(pdf_path) as doc:
		for page in doc:
		    areas = page.searchFor("TAILIEUONTHI.NET") 
		    [page.addRedactAnnot(area) for area in areas] 
		    page.apply_redactions() 
		doc.save(pdf_path[:-4]+'_out.pdf')




if __name__ == "__main__":
   replace_text("TEST.pdf","TAILIEUONTHI.NET")
