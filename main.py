from docxcompose.composer import Composer
from docx import Document
import os
todo = os.listdir(os.path.abspath("")+"\docxfiles")

todo.sort()

master = Document()
composer = Composer(master)

for file in todo:
    path = os.path.abspath("")+"\docxfiles\\"+file
    docfile = Document(path)
    composer.append(docfile)

composer.save(os.path.abspath("")+"\docxfiles\combined.docx")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/