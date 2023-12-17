from docxcompose.composer import Composer
from docx import Document
from natsort import natsorted
import os

todo = os.listdir(os.path.abspath("")+"\docxfiles")

todo = natsorted(todo)

master = Document()
composer = Composer(master)

for file in todo:
    path = os.path.abspath("")+"\docxfiles\\"+file
    try:
        docfile = Document(path)
    except:
        print("error reading the document at " + path)
        exit(2)
    try:
        composer.append(docfile)
    except:
        print("error appending the document at " + path)
        exit(1)

composer.save(os.path.abspath("")+"\docxfiles\combined.docx")
