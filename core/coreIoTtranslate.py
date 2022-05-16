import os

import PyPDF2

import PyPDF2 as pyPdf
from PyPDF2 import PdfFileReader


def checkFileExistance(sPath):
    if not os.path.exists(sPath):
        os.makedirs(sPath)
    return True


def nbpagespdf(fichierpdf):
    with open(fichierpdf, "rb") as f:
        nbrPage = pyPdf.PdfFileReader(f).getNumPages()
        return nbrPage


def getPDFContent(path):
    fichier = open("1.txt", "a")
    pdftext = ""
    pdf = open(path, 'rb')
    pdfreader = PdfFileReader(pdf)
    nbrPage = nbpagespdf(path)
    txt ="Ławrynowicz and Tresp / Introduction to Machine Learning"
    for i in range(nbrPage):
        pageObj = pdfreader.getPage(i)

        pdftext = pageObj.extractText().encode("utf-8")
        lignedeTexteBrut = str(pdftext) + "\n"
        lignedetext = lignedeTexteBrut.replace(str(txt),"")
        fichier.write(lignedetext)

    fichier.close()




