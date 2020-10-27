import PyPDF2

pdf = input("Enter the name of the PDF")

if pdf == "":
    
    print("If you do not have a PDF now, we provide you a sample pdf.")
    print("Type sample_pdf to use the sample pdf") 
    pdf = input() 

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

def roatate_pdf_single_page(page):
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

total_pages()
is_encrypted()

while(True):

    print("what more you like to do with the pdf?")
    print("1. See more details of the PDF 2. Extract data from a single page 3. Extract data from multiple pages 4. Rotate a page. 5. Exit the program")
    print("Enter your choice")

    choiceEntry = int(input())

    if(choiceEntry == 1):
        details_of_the_pdf()

    elif(choiceEntry == 2):
        print("Enter the page number from which you want to extract the data")
        print("If the PDF contains only a single page type 1")

        page = input()

        ext_page_data(page)

    elif(choiceEntry == 3):

        print("Enter the range in which you want to extract the data")

        startRange = input("Enter the starting range")
        endRange = input("Enter the ending range")
        ext_page_data_of_many_pages(startRange, endRange)

    elif(choiceEntry == 4):

        print("Enter the page which you want to rotate")
        print("If the PDF contains only a single page type 1")

        pageRotate = input()
        roatate_pdf_single_page(pageRotate + 1) 

    elif(choiceEntry == 5):
        print("Thanks for using my application....")
        exit()

    else:
        print("Please enter a correct choice")                   
    