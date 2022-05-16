import coreIA

def Bonjour():
    sp = coreIA.Speech()
    sp.engine.say('Bonjour !!!!     Comment ça va ?')
    sp.engine.runAndWait()

Bonjour()