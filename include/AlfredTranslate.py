from translate import Translator

def AlfredEstBilingue(lenguaEn, textoEn, lenguaAfuera):
    translator = Translator(from_lang = lenguaEn ,to_lang = lenguaAfuera)
    translation = translator.translate(str(textoEn))

    return translation

