import win32com.client

def CreateWordDocument(filePath):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True

    doc = word.Documents.Add()

    selection = word.Selection
    selection.TypeText("Hello word document")
    selection.TypeParagraph()
    selection.TypeText("Automation in fun!!")
    selection.TypeParagraph()
    selection.TypeText("This is a auto generated doc file")

    # Saving the document
    doc.SaveAs(filePath)
    word.Quit()

CreateWordDocument(r"D:\Training\259398_PythonTraining\PyWinDemo\DemDoc.docx")
