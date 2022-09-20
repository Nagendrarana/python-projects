# Writing to an excel 
# sheet using Python
from xlwt import Workbook
def toExcel(page_no,name,type):


  
    # Workbook is created
    wb = Workbook()
  
    # add_sheet is used to create sheet.

    sheet1 = wb.add_sheet('Sheet 1')
    text1 = "asjals"
    text2 = "skajsla"
    
  
    
    sheet1.write(0, 1, 'Page_No')
    sheet1.write(0, 2, 'Name')
    sheet1.write(0, 3, 'Type')
    
   
    
    wb.save('example.xls')
if __name__=="__main__":
    toExcel("demo","demo","demo")
