import pdfrw


pdf = pdfrw.PdfReader("5E_CharacterSheet_Fillable_1.pdf")
pdf123 = pdf.Root.StructTreeRoot.ClassMap

# print(pdf.Root.keys())
# print(pdf.Root.StructTreeRoot.ClassMap.keys())
# pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true'))) 
if str(pdf123.values()).find("fsdfnsdjk") == -1:
    print(pdf123.values())
else:
    print(str(pdf.Root.values()).find("fsdfnsdjk"))