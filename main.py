import PyPDF2

pdf = "sample_pdf"
pdf = pdf + ".pdf"

a = PyPDF2.PdfFileReader(pdf)

print("Some basic imformation from the pdf are")

# funtion to see the total number of pages in the pdf

def total_pages():
    print("The total number of pages in the pdf are")
    print(a.numPages)

# function to see whether the pdf is encrypted or not

def is_encrypted():
    
    enc = a.isEncrypted
    if enc == True:
        print("The book is Encripted")
    else:
        print("The book is not Encrypted")

# function to see extract data from a single page        

def ext_page_data(page_num):
    extracted_data = a.getPage(page_num).extractText()
    f_name = input("Enter the name of the file where you want to store the texts.")
    f_name = f_name + ".txt"
    with open(f_name, "w", encoding='utf-8') as f:
        f.write(extracted_data)

    f.close()     

#function for extracting data from multiple pages of the pdf

def ext_page_data_of_many_pages(starting_page, ending_page):
    f_name = input("Enter the name of the file where you want to store the texts.")
    f_name = f_name + ".txt"
    for i in range(starting_page, ending_page + 1):
        str = str + a.getPage(i).extractText()

    with open(f_name, "w", encoding='utf-8') as f:
        f.write(str) 

    f.close()  

# function to see the details of the pdf       

def details_of_the_pdf():

    print("Do you want to see the details of the pdf? Y/N")
    inp = input()

    if(inp == 'Y' or inp == 'y'):
        print(a.documentInfo)
    else:
        print("Ok, Let's proceed")  

# function to rotate a page         

def roatate_pdf_single_page():
    page = a.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    inp = input("Enter the name of the file where you want to store the pdf ")
    inp = inp + ".pdf"

    print("Rotating page....")

    output = open(inp, 'bw')
    writer.write(output)

    output.close()  

    print("The page has been rotated") 

# function to rotate multiple pages         

def roatate_pdf_multiple_pages(start_page, end_page):
    inp = input("Enter the name of the file where you want to store the pdf ")
    inp = inp + ".pdf"

    print("Rotating all the pages....")
    output = open(inp, 'ab+')

    for i in range(start_page, end_page):
        page = a.getPage(i)
        page.rotateClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)

        writer.write(output)
    output.close()

    print("All the pages are rotated sucessfully")


roatate_pdf_multiple_pages(16, 28)     
              

# ext_page_data_of_many_pages(16,18)           
# print(a.numPages)
# print(a.getPage(24).extractText())
# print(a.getPageNumber('Constructors'))
# print(a.isEncrypted)
# print(a.getNamedDestinations)
