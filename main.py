import PyPDF2

input_path = "./img/sample_image.pdf"
output_path = "./img/output.pdf"

trim_x = 50
trim_y = 50
trim_width = 500
trim_height = 500

with open (input_path, "rb") as input_f:
    input_pdf = PyPDF2.PdfFileReader(input_f)
    output_pdf = PyPDF2.PdfFileWriter()

    page = input_pdf.getPage(0)

    print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())

    page.cropBox.lowerLeft = (trim_x, trim_y)
    page.cropBox.upperRight = (trim_x + trim_width, trim_width + trim_y)

    output_pdf.addPage(page)

    with open(output_path, "wb") as out_f:
        output_pdf.write(out_f)
