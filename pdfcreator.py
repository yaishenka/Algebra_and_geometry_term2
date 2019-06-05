from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import os
from io import BytesIO

main_dir = '/Users/daniilgagarinov/GitReps/Algebra_and_geometry_term2/'
sources_dir = '/Users/daniilgagarinov/GitReps/Algebra_and_geometry_term2/sources'
list = os.listdir(sources_dir)

for file in list:
    if '.' in file:
        list.remove(file)

for task_number in list:
    sources = os.listdir(sources_dir + '/' + task_number)
    sources.sort()
    new_task_file = PdfFileWriter()
    for source_file_name in sources:
        if 'DS_Store' in source_file_name:
            continue
        buf = BytesIO()
        img = Image.open(sources_dir + '/' + task_number + '/' + source_file_name)
        img.convert("RGB").save(buf, format="pdf")
        # once image is PDF, it can be appended
        new_task_file.addPage(PdfFileReader(buf).getPage(0))
    folder = 'pdfs/'
    outputStream = open(main_dir + folder + task_number  + ' билет'+ '.pdf', "wb")
    new_task_file.write(outputStream)
    outputStream.close()






