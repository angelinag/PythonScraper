import win32com.client
worksheetname = 'americanAirlinesReviews'
filename = 'american_airlines_reviews_scraped'
filepath = 'D:\\'

class Export:
    def __init__(self):
        self.xl = win32com.client.Dispatch("Excel.Application")
        self.workBook = self.xl.Workbooks.Add()
        #self.xl.Visible = True
        self.workSheet = self.workBook.ActiveSheet
        self.workSheet.Name = worksheetname

    columnpointer = 'A'
    def movecolumnpointer(self):
        self.columnpointer = chr(ord(self.columnpointer) + 1)
    rowpointer = 1
    def moverowpointer(self):
        self.rowpointer = self.rowpointer + 1

    def populatecolumn(self, data):
        for cell in data:
            range = self.columnpointer + str(self.rowpointer)
            rangeObj = self.workSheet.Range(range)
            rangeObj.Value = cell
            self.moverowpointer()

        self.movecolumnpointer()
        self.rowpointer = 1

    def endexport(self):
        self.workSheet.Columns.AutoFit()
        self.workBook.SaveAs(filepath + filename + '.xls')
        #self.workBook.Close(savechanges=1)
        self.xl.Quit()

