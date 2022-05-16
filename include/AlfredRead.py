from include import AlfredTranslate as AT


def traducirtexto( lenguaEn, lenguaAfuera, textoEn):
    try:

        sTranslateTxt = AT.AlfredEstBilingue(lenguaEn, textoEn, lenguaAfuera)

        return sTranslateTxt

    except(Exception)as e:
        print("une exeption de type " + str(e) + " est survenu")




        #sPath = "docs/"
        #if not checkFileExistance(sPath):
        #    print('probleme lors de la recherche du dossier')
        #    pass

        #readDoc = os.listdir('docs')
        #mime = magic.Magic(mime=True)

        #sPathDocTranslate = "docTranslate/"
        #if not checkFileExistance("docTranslate"):
        #    print('probleme lors de la recherche du dossier')

        #for file in readDoc:
        #    sPathFile = sPath + file
        #    sMine = mime.from_file(sPathFile)

        #    if str(sMine) == "text/plain":
        #        lang = 'ES'
        #        fichier = open(sPathDocTranslate + 'translate_' + lang + '_' + file, "a")
        #        #sDocTxt = open(sPathFile, "r")
        #        sDocTxt = textoEn
        #        sTranslateTxt = AlfredEstBilingue(sDocTxt, lenguaAfuera, lenguaEn)
        #        sFile = file.split()
        #        fichier.write(str(sTranslateTxt))
        #        fichier.close()