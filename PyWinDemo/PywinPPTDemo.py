import win32com.client

def CreatePresentationFile(filePath):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    powerpoint.Visible = True

    presentation = powerpoint.Presentations.Add()

    slide = presentation.Slides.Add(1,1)
    slide.Shapes[0].TextFrame.TextRange.Text = "Automating Powerpoint"
    slide.Shapes[1].TextFrame.TextRange.Text = "Using pywin32 for automation"
    
    powerpoint.SaveAs(filePath)
    powerpoint.Quit()

CreatePresentationFile(r"D:\Training\259398_PythonTraining\PyWinDemo\PPTSample.pptx")
